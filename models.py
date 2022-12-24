from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

    def adjacencies(self):
        all_nodes = [x.lower_node for x in self.higher_edges]
        all_nodes.extend([x.higher_node for x in self.lower_edges])
        return all_nodes



class Edge(Base):  # ? point - point
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

    def __init__(self, n1, n2):
        if n1.id < n2.id:
            self.lower_node = n1
            self.higher_node = n2
        else:
            self.lower_node = n2
            self.higher_node = n1
