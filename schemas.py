from __future__ import annotations
from typing import ForwardRef
from pydantic import BaseModel


Point = ForwardRef("Point")
Edge = ForwardRef("Edge")


class EdgeBase(BaseModel):
    from_point_id: int
    to_point_id: int

    class Config:
        orm_mode = True


class Edge(EdgeBase):
    from_point: PointNeighbour
    to_point: PointNeighbour
    pass


class PointBase(BaseModel):
    name: str
    description: str | None

    class Config:
        orm_mode = True


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
Point.update_forward_refs()


class ImageBase(BaseModel):
    url: str
    width: int
    height: int

    class Config:
        orm_mode = True


class Image(ImageBase):
    id: int


class FloorBase(BaseModel):
    name: str
    description: str
    map_image: Image | None
    # lat: int
    # long: int - add Building model?
    class Config:
        orm_mode = True


class Floor(FloorBase):
    id: int


# Non-DB model
class Path(BaseModel):
    path: list[PointNeighbour]
    floors: list[Floor]


"""
class MapPoint(BaseModel):
    id: int
    floor: Floor
    point: Point
    x: int
    y: int
"""
