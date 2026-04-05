import yfinance as yf

def get_price(ticker):
    # Türk hisseleri için otomatik .IS ekle
    if not ticker.endswith(".IS"):
        ticker = ticker.upper() + ".IS"

    data = yf.Ticker(ticker)
    hist = data.history(period="1d")

    if hist.empty:
        return None

    return float(hist["Close"].iloc[-1])