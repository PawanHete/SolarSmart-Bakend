from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud, database

router = APIRouter(
    prefix="/metrics",
    tags=["metrics"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MetricResponse)
def create_metric(metric: schemas.MetricCreate, db: Session = Depends(get_db)):
    return crud.create_metric(db, metric)

@router.get("/", response_model=List[schemas.MetricResponse])
def read_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_metrics(db, skip=skip, limit=limit)