from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    is_classroom = Column(Boolean, nullable=False)

    floors = relationship("FloorPoint", back_populates="point")

    def __str__(self):
        return f"<{self.id}> {self.name}"


class Edge(Base):
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

    points = relationship("FloorPoint", back_populates="floor")

    def __str__(self):
        return f"<{self.id}> {self.name}"


class FloorPoint(Base):
    __tablename__ = "floor_points"
    id = Column(Integer, primary_key=True, index=True)
    floor_id = Column(Integer, ForeignKey("floors.id"))
    floor = relationship(
        Floor, primaryjoin=floor_id == Floor.id, back_populates="points"
    )
    point_id = Column(Integer, ForeignKey("points.id"))
    point = relationship(
        Point, primaryjoin=point_id == Point.id, back_populates="floors"
    )
    x = Column(Integer, nullable=True)
    y = Column(Integer, nullable=True)

    __table_args__ = (UniqueConstraint("floor_id", "point_id"),)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    login = Column(String(80), unique=True)
    email = Column(String(120))
    password = Column(String(128))

    # Flask-Login integration
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username
