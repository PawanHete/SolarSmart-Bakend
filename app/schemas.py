from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MetricBase(BaseModel):
    voltage: Optional[float] = None
    current: Optional[float] = None
    power: Optional[float] = None
    energy: Optional[float] = None
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None

# Used when ESP32 sends data
class MetricCreate(MetricBase):
    pass

# Used when API sends data back
class MetricResponse(MetricBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True