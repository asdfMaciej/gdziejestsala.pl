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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get("/points", response_model=list[schemas.PointNeighbour])
def get_points(db: Session = Depends(get_db)):
    return crud.get_points(db)


@app.get("/route/{start_point_id}/{destination_point_id}", 
    response_model=schemas.Path, 
    responses={
        404: {"description": "Path not found"},
        400: {"description": "Invalid arguments"}
    })
def get_route(start_point_id: int, destination_point_id: int, db: Session = Depends(get_db)):
    all_edges = crud.get_edges(db)

    
    try:
        path_point_ids = graph.get_path(all_edges, start_point_id, destination_point_id)
    except AssertionError:
        raise HTTPException(status_code=400, detail="Start and destination must be different")

    if not path_point_ids:
        raise HTTPException(status_code=404, detail="Path not found")
    path_points = crud.get_points_by_ids(db, path_point_ids)

    path = schemas.Path(
        path = path_points,
        floors = []
    )
    return path


flask_app = Flask(__name__)
flask_app.secret_key = "SUPER SECRET KEY!!!"  # TODO: read from .env

flask_admin = Admin(flask_app, name='USOS', template_mode='bootstrap4')
flask_admin.add_view(ModelView(models.Point, SessionLocal()))
flask_admin.add_view(ModelView(models.Edge, SessionLocal()))

app.mount("/v1", WSGIMiddleware(flask_app))