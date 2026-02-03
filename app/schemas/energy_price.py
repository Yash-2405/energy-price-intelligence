from pydantic import BaseModel
from datetime import date

class EnergyPriceOut(BaseModel):
    commodity: str
    price: float
    date: date

    class Config:
        orm_mode = True
