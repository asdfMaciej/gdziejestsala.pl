from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

class Edge(Base):
    __tablename__ = "edges"
    
    lower_id = Column(
        Integer,
        ForeignKey('points.id'),
        primary_key=True
    )

    higher_id = Column(
        Integer,
        ForeignKey('points.id'),
        primary_key=True
    )

    lower_node = relationship(
        Point,
        primaryjoin = lower_id == Point.id,
        backref='lower_edges'
    )

    higher_node = relationship(
        Point, 
        primaryjoin = higher_id == Point.id,
        backref='higher_edges'
    )
