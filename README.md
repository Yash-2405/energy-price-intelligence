## Energy Price Intelligence Platform

An enterprise-style backend platform that ingests crude oil and natural gas prices, stores historical commodity data in PostgreSQL, and exposes REST APIs for monitoring energy market trends.

This project simulates a real-world commodity market intelligence workflow aligned with energy pricing and analytics use cases.

---

## 🚀 Features

- Daily commodity price ingestion (Crude Oil, Natural Gas)
- PostgreSQL persistence for historical pricing data
- Duplicate-safe ingestion (idempotent updates per trading day)
- Volatility spike detection alerts
- REST APIs built using FastAPI
- Modular clean backend architecture (services, models, routes)

---

## 🛠 Tech Stack

- Backend: FastAPI (Python)
- Database: PostgreSQL
- ORM: SQLAlchemy
- API Documentation: Swagger UI (OpenAPI)
- Server: Uvicorn
- Config Management: python-dotenv

---

## 📌 API Endpoints

| Method | Endpoint   | Description |
|--------|-----------|-------------|
| GET    | `/`       | Health check |
| POST   | `/ingest` | Ingest daily commodity prices |
| GET    | `/prices` | Fetch stored historical prices |
| GET    | `/alerts` | Detect volatility spike alerts |

---

## 📂 Project Architecture

backend/app/

│
├── main.py # FastAPI entry point
├── core/
│ ├── config.py # Environment config
│ └── database.py # DB session + engine
│
├── models/
│ └── energy_price.py # PostgreSQL table schema
│
├── services/
│ ├── ingestion_service.py # Price ingestion logic
│ ├── analytics_service.py # Spike detection engine
│ └── price_fetcher.py # External market price fetch
│
└── api/
└── routes.py # API routes  

---

## ✅ Setup Instructions (Run Locally)

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/energy-price-intelligence.git
cd energy-price-intelligence/backend
```

---

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Configure PostgreSQL
```bash
CREATE DATABASE energydb;
```
### Update the .env file:
```bash
DB_USER=username
DB_PASSWORD=your password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=energydb
```

---

### 5. Start FastAPI Server
```bash
python -m uvicorn app.main:app --reload
```
### Server will start at:
```bash
http://127.0.0.1:8000
```

---

### 6. Swagger API Docs
### Open:
```bash
http://127.0.0.1:8000/docs
```

---

## 🧪 Database Verification

After running POST /ingest, confirm records in PostgreSQL:
```bash
SELECT * FROM energy_prices;
```

---

### 🎥 **[Watch Demo](https://drive.google.com/file/d/1P1pdrKHy41hX_GdLUhorhhx3CgEBTX1M/view?usp=sharing)** 

A short project execution demo is included in the repository:

Swagger UI execution

Price ingestion

PostgreSQL persistence proof

---

### ✅ Key Engineering Highlights

Designed modular enterprise backend architecture

Implemented idempotent ingestion to prevent duplicate entries per day

Integrated PostgreSQL storage using SQLAlchemy ORM

Built commodity-aligned APIs for real-world energy intelligence workflows

---

### 📌 Future Enhancements

Add frontend dashboard for price trend visualization

Deploy backend on AWS/Render with CI/CD pipeline

Expand ingestion pipeline for additional commodity instruments

---

## 👤 Author

Yash V - [LinkedIn](https://www.linkedin.com/in/yash-v-/), [GitHub](https://github.com/Yash-2405).
