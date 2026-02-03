from datetime import date
from sqlalchemy.orm import Session

from app.models.energy_price import EnergyPrice
from app.services.price_fetcher import fetch_real_price

COMMODITIES = ["Crude Oil", "Natural Gas"]

def ingest_prices(db: Session):
    today = date.today()
    inserted = 0
    updated = 0

    for commodity in COMMODITIES:
        # Fetch real market price
        try:
            new_price = fetch_real_price(commodity)
        except Exception:
            continue

        existing = db.query(EnergyPrice).filter(
            EnergyPrice.commodity == commodity,
            EnergyPrice.date == today
        ).first()

        if existing:
            existing.price = new_price
            updated += 1
        else:
            record = EnergyPrice(
                commodity=commodity,
                price=new_price,
                date=today
            )
            db.add(record)
            inserted += 1

    db.commit()

    return {
        "status": "Real market ingestion completed",
        "inserted": inserted,
        "updated": updated,
        "date": str(today)
    }
