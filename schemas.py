from __future__ import annotations
from typing import ForwardRef
from pydantic import BaseModel


Point = ForwardRef("Point")
Edge = ForwardRef("Edge")
FloorPoint = ForwardRef("FloorPoint")


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
    floors: list[FloorPointWithFloor]


class Point(PointNeighbour):
    connected_from: list[Edge]
    connected_to: list[Edge]


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


class FloorPointBase(BaseModel):
    # In case we decide to use a different display method
    #  than a single point for a map floor,
    # we can always create an extra table - right now this is sufficient
    x: int | None
    y: int | None

    class Config:
        orm_mode = True


class FloorPointWithFloor(FloorPointBase):
    floor_id: int


class FloorPointWithPoint(FloorPointBase):
    point_id: int


class FloorPoint(FloorPointBase):
    floor: Floor
    point: Point
    id: int


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
PointNeighbour.update_forward_refs()

# Non-DB models below
class Path(BaseModel):
    path: list[PointNeighbour]
    floors: dict[int, Floor]


# Order-agnostic response
# Same schema, but different semantics - hence the rename
class PointsResponse(BaseModel):
    points: list[PointNeighbour]
    floors: dict[int, Floor]
