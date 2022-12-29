from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models, crud, schemas, graph, admin

from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


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
    floors_by_id = crud.get_floors_by_id_for_points(db, points)
    response = schemas.PointsResponse(points=points, floors=floors_by_id)
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
    except AssertionError:
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
    floors_by_id = crud.get_floors_by_id_for_points(db, path_points)

    # Return the results
    path = schemas.Path(path=path_points, floors=floors_by_id)
    return path


app.mount("/api/v1/admin", WSGIMiddleware(admin.flask_app))
app.mount("/", StaticFiles(directory="dist", html=True), name="dist")
