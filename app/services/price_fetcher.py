import requests

# Free commodity symbols from Stooq
SYMBOLS = {
    "Crude Oil": "cl.f",
    "Natural Gas": "ng.f"
}

def fetch_real_price(commodity: str) -> float:
    symbol = SYMBOLS.get(commodity)

    if not symbol:
        raise ValueError("Unsupported commodity")

    url = f"https://stooq.com/q/l/?s={symbol}&f=sd2t2ohlcv&h&e=csv"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch market data")

    lines = response.text.strip().split("\n")

    # CSV format: Symbol,Date,Time,Open,High,Low,Close,Volume
    if len(lines) < 2:
        raise Exception("No market data available")

    latest = lines[1].split(",")

    close_price = float(latest[6])  # Close column
    return close_price
