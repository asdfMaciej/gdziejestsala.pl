from fastapi import FastAPI


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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/path/{start_point}/{end_point}")
def get_route(start_point: int, end_point: int):
    return {"start_point": start_point, "end_point": end_point}