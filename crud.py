from sqlalchemy.orm import Session

import models
import schemas


def create_point(db: Session, point: schemas.PointBase):
    db_point = models.Point(**point.dict())
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point


def create_edge(db: Session, edge: schemas.EdgeBase):
    db_edge = models.Edge(**edge.dict())
    db.add(db_edge)
    db.commit()
    db.refresh(db_edge)
    return db_edge


def get_point(db: Session, point_id: int):
    return db.query(models.Point).filter(models.Point.id == point_id).first()


def get_points(db: Session):
    return db.query(models.Point).all()


def get_edges(db: Session) -> list[models.Edge]:
    return db.query(models.Edge).all()


def get_point_max_id(db: Session):
    return db.query(models.Point.id).order_by(models.Point.id.desc()).first().id


def get_points_by_ids(db: Session, points_id: list[int]) -> list[models.Point]:
    points = db.query(models.Point).filter(models.Point.id.in_(points_id)).all()
    return points


def get_floors_by_ids(db: Session, floors_id: list[int]) -> list[models.Floor]:
    floors = db.query(models.Floor).filter(models.Floor.id.in_(floors_id)).all()
    return floors


def get_floors_by_id_for_points(
    db: Session, points_list: list[models.Point]
) -> dict[int, models.Floor]:
    # Get unique floor IDs
    floor_ids = set()
    for point in points_list:
        for floor in point.floors:
            floor_ids.add(floor.floor_id)

    # Fetch their data
    floors = get_floors_by_ids(db, list(floor_ids))

    # Convert them to ID -> floor
    floors_by_id = {}
    for floor in floors:
        floors_by_id[floor.id] = floor

    return floors_by_id
