from __future__ import annotations
from typing import ForwardRef
from pydantic import BaseModel


Point = ForwardRef('Point')
Edge = ForwardRef('Edge')

class EdgeBase(BaseModel):
    lower_id: int
    higher_id: int
    class Config:
        orm_mode = True
    # lower_node
    # higher_node

class EdgeCreate(EdgeBase):
    pass

class Edge(EdgeBase):
    lower_node: PointNeighbour 
    higher_node: PointNeighbour
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
    lower_edges: list[Edge]

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
