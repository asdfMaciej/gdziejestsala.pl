from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
import models, crud, schemas, graph

from database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

"""Create all models in the database.
Simplified method - typically Alembic would be used for handling migrations"""
models.Base.metadata.create_all(bind=engine)

# This function is required to provide an unique, auto-closed connection per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="USOS")


@app.get(
    "/points",
    response_model=list[schemas.PointNeighbour],
    description="Returns a list of all available points.",
)
def get_points(db: Session = Depends(get_db)):
    return crud.get_points(db)


@app.get(
    "/route/{start_point_id}/{destination_point_id}",
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
    # Fetch all edges from DB and generate route in-memory
    all_edges = crud.get_edges(db)
    try:
        path_point_ids = graph.get_path(all_edges, start_point_id, destination_point_id)
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

    # Returns the results
    path = schemas.Path(path=path_points, floors=[])
    return path


# Include an admin panel for CRUD operations
flask_app = Flask(__name__)
flask_app.secret_key = "SUPER SECRET KEY!!!"  # TODO: read from .env

flask_admin = Admin(flask_app, name="USOS", template_mode="bootstrap4")
flask_admin.add_view(ModelView(models.Point, SessionLocal()))
flask_admin.add_view(ModelView(models.Edge, SessionLocal()))
flask_admin.add_view(ModelView(models.Image, SessionLocal()))
flask_admin.add_view(ModelView(models.Floor, SessionLocal()))

app.mount("/v1", WSGIMiddleware(flask_app))
