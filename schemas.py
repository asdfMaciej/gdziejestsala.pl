from __future__ import annotations
from pydantic import BaseModel


class EdgeBase(BaseModel):
    lower_node: Point 
    higher_node: Point
    class Config:
        orm_mode = True
    # lower_node
    # higher_node

class EdgeCreate(EdgeBase):
    pass

class Edge(EdgeBase):
    pass

class PointBase(BaseModel):
    name: str
    description: str | None
    class Config:
        orm_mode = True

class PointCreate(PointBase):
    pass

class Point(PointBase):
    id: int
    lower_edges: list[Edge]
