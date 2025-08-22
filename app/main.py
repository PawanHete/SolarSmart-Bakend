from fastapi import FastAPI
from . import models, database
from .routers import metrics

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ESP32 Metrics API")

app.include_router(metrics.router)