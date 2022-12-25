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
    # TODO: add a constraint so it's impossible to add an edge with not existing keys
    __tablename__ = "edges"

    from_point_id = Column(Integer, ForeignKey("points.id"), primary_key=True)

    to_point_id = Column(Integer, ForeignKey("points.id"), primary_key=True)

    from_point = relationship(
        Point, primaryjoin=from_point_id == Point.id, backref="connected_from"
    )

    to_point = relationship(
        Point, primaryjoin=to_point_id == Point.id, backref="connected_to"
    )


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(256), nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)


class Floor(Base):
    __tablename__ = "floors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    map_image_id = Column(Integer, ForeignKey("images.id"))
    map_image = relationship(Image, primaryjoin=map_image_id == Image.id)
