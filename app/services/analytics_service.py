from sqlalchemy.orm import Session
from app.models.energy_price import EnergyPrice

def detect_price_spikes(db: Session, threshold=8):
    alerts = []

    commodities = db.query(EnergyPrice.commodity).distinct().all()

    for (commodity,) in commodities:
        records = (
            db.query(EnergyPrice)
            .filter(EnergyPrice.commodity == commodity)
            .order_by(EnergyPrice.date.desc())
            .limit(2)
            .all()
        )

        if len(records) == 2:
            diff = abs(records[0].price - records[1].price)

            if diff > threshold:
                alerts.append({
                    "commodity": commodity,
                    "change": diff,
                    "message": "Volatility spike detected"
                })

    return alerts
