from sqlalchemy.orm import Session
from . import models, schemas

def create_metric(db: Session, metric: schemas.MetricCreate):
    db_metric = models.Metric(**metric.model_dump())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

def get_metrics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Metric).order_by(models.Metric.timestamp.desc()).offset(skip).limit(limit).all()