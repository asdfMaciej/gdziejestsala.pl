from sqlalchemy.orm import Session

import models
import schemas

def create_point(db: Session, point: schemas.PointCreate):
    db_point = models.Point(**point.dict())
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

def create_edge(db: Session, edge: schemas.EdgeCreate):
    db_edge = models.Edge(**edge.dict())
    db.add(db_edge)
    db.commit()
    db.refresh(db_edge)
    return db_edge

def get_point(db: Session, point_id: int):
    return db.query(models.Point).filter(models.Point.id == point_id).first()