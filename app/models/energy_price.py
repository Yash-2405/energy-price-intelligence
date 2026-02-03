from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class EnergyPrice(Base):
    __tablename__ = "energy_prices"

    id = Column(Integer, primary_key=True, index=True)
    commodity = Column(String, index=True)
    price = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
