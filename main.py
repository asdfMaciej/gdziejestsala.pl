from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
import models, crud, schemas

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

@app.get("/point/{point_id}", response_model=schemas.Point)
def get_point(point_id: int, db: Session = Depends(get_db)):
    return crud.get_point(db, point_id)


@app.post("/point", response_model=schemas.Point)
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    return crud.create_point(db, point)


@app.post("/edge", response_model=schemas.Edge)
def create_edge(edge: schemas.EdgeCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_edge(db, edge)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Edge already exists")

flask_app = Flask(__name__)
flask_admin = Admin(flask_app, name='USOS', template_mode='bootstrap4')
flask_admin.add_view(ModelView(models.Point, SessionLocal()))
flask_admin.add_view(ModelView(models.Edge, SessionLocal()))

app.mount("/v1", WSGIMiddleware(flask_app))