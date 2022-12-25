from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

    def __str__(self):
        return f"<{self.id}> {self.name}"

class Edge(Base):
    __tablename__ = "edges"
    
    from_point_id = Column(
        Integer,
        ForeignKey('points.id'),
        primary_key=True
    )

    to_point_id = Column(
        Integer,
        ForeignKey('points.id'),
        primary_key=True
    )

    from_point = relationship(
        Point,
        primaryjoin = from_point_id == Point.id,
        backref='connected_from'
    )

    to_point = relationship(
        Point, 
        primaryjoin = to_point_id == Point.id,
        backref='connected_to'
    )
