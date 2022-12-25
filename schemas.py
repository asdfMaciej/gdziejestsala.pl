from __future__ import annotations
from typing import ForwardRef
from pydantic import BaseModel


Point = ForwardRef('Point')
Edge = ForwardRef('Edge')

class EdgeBase(BaseModel):
    from_point_id: int
    to_point_id: int
    class Config:
        orm_mode = True

class EdgeCreate(EdgeBase):
    pass

class Edge(EdgeBase):
    from_point: PointNeighbour 
    to_point: PointNeighbour
    pass

class PointBase(BaseModel):
    name: str
    description: str | None
    class Config:
        orm_mode = True

class PointCreate(PointBase):
    pass

class PointNeighbour(PointBase):
    id: int

class Point(PointNeighbour):
    connected_from: list[Edge]
    connected_to: list[Edge]

"""
As classes are referenced in type hints before their declaration,
  Point and Edge are both defined using ForwardRef,
  so type hints work properly and schema can be generated

After schemas are defined, it is important to call update_forward_refs
  to change the type hint from ForwardRef to the actual class
"""
EdgeBase.update_forward_refs()
Edge.update_forward_refs()
EdgeCreate.update_forward_refs()
Point.update_forward_refs()

class Floor(BaseModel):
    id: int
    name: str 

class Path(BaseModel):
    path: list[PointNeighbour]
    floors: list[Floor]



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

