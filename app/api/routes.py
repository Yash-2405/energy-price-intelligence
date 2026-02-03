from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.ingestion_service import ingest_prices
from app.services.analytics_service import detect_price_spikes
from app.models.energy_price import EnergyPrice

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Energy Price Intelligence Platform Running"}

@router.post("/ingest")
def ingest(db: Session = Depends(get_db)):
    return ingest_prices(db)

@router.get("/prices")
def get_all_prices(db: Session = Depends(get_db)):
    return db.query(EnergyPrice).all()

@router.get("/alerts")
def alerts(db: Session = Depends(get_db)):
    return detect_price_spikes(db)
