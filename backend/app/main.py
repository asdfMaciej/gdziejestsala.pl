from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models, crud, schemas, graph, admin
from typing import Tuple
import os

from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session

# Source: https://stackoverflow.com/questions/63069190/how-to-capture-arbitrary-paths-at-one-route-in-fastapi
# Created by Noah Cardoza
# Modified to use regular functions instead of async
class SinglePageApplication(StaticFiles):
    """Acts similar to the bripkens/connect-history-api-fallback
    NPM package."""

    def __init__(self, directory: os.PathLike, index="index.html") -> None:
        self.index = index

        # set html=True to resolve the index even when no
        # the base path is passed in
        super().__init__(directory=directory, packages=None, html=True, check_dir=True)

    def lookup_path(self, path: str) -> Tuple[str, os.stat_result]:
        """Returns the index file when no match is found.

        Args:
            path (str): Resource path.

        Returns:
            [tuple[str, os.stat_result]]: Always retuens a full path and stat result.
        """
        full_path, stat_result = super().lookup_path(path)

        # if a file cannot be found
        if stat_result is None:
            return super().lookup_path(self.index)

        return (full_path, stat_result)


app = FastAPI(
    title="USOS",
    openapi_url="/api/v1/openapi.json",
    redoc_url="/api/v1/redoc",
    docs_url="/api/v1/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/api/v1/points",
    response_model=schemas.PointsResponse,
    description="Returns a list of all available points.",
)
def get_points(db: Session = Depends(get_db)):
    points = crud.get_points(db)
    floors = crud.get_floors_for_points(db, points)
    response = schemas.PointsResponse(points=points, floors=floors)
    return response


@app.get(
    "/api/v1/route/{start_point_id}/{destination_point_id}",
    response_model=schemas.Path,
    responses={
        404: {"description": "Path not found"},
        400: {"description": "Invalid arguments"},
    },
    description="Generate route between two given points.",
)
def get_route(
    start_point_id: int, destination_point_id: int, db: Session = Depends(get_db)
):
    # TODO: Check if start and destination points exist
    # Fetch suitable edges from DB and generate route in-memory
    pathfinding_edges = crud.get_edges_for_pathfinding(db, start_point_id)
    try:
        path_point_ids = graph.get_path(
            pathfinding_edges, start_point_id, destination_point_id
        )
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Start and destination must be different"
        )

    # Get details for each point en route
    if path_point_ids is None:
        raise HTTPException(status_code=404, detail="Path not found")
    path_points = crud.get_points_by_ids(db, path_point_ids)

    # Orders the points according to the generated path
    point_positions = {}
    for position, id in enumerate(path_point_ids):
        point_positions[id] = position

    path_points = sorted(path_points, key=lambda o: point_positions[o.id])

    # Retrieve floor details for present floors
    floors = crud.get_floors_for_points(db, path_points)

    # Return the results
    path = schemas.Path(path=path_points, floors=floors)
    return path


app.mount("/api/v1/admin", WSGIMiddleware(admin.flask_app))
app.mount("/static/", StaticFiles(directory="static"), name="static")
app.mount(path="/", app=SinglePageApplication(directory="dist"), name="SPA")
