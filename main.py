from fastapi import FastAPI, Depends, HTTPException
import models, crud, schemas

from database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
class Floor(Base):
    __tablename__ = "floors"

    id: int
    name: int 
    description: int 
    map_image: int
    map_points: int
    #lat: int
    #long: int - include Building model?

class MapPoint(Base):
    __tablename__ = "floor_map_points"
    x: int
    y: int
    order: int

class Image(Base):
    __tablename__ = "images"

    id: int
    url: int
    width: int 
    height: int
"""

app = FastAPI()

"""
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/path/{start_point}/{end_point}")
def get_route(start_point: int, end_point: int):
    return {"start_point": start_point, "end_point": end_point}

"""

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