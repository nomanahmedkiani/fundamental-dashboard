import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trading Dashboard", layout="wide")

st.title("📊 Fundamental Trading Dashboard")
st.subheader("User: Noman Ahmed")

# -------- FUNCTIONS -------- #

def candle_direction(symbol, interval, period):
    data = yf.download(symbol, interval=interval, period=period, progress=False)
    if data.empty or len(data) < 2:
        return "No Data"

    last = data.iloc[-2]  # previous closed candle
    if last["Close"] > last["Open"]:
        return "🟢 Bullish"
    else:
        return "🔴 Bearish"


def live_price(symbol):
    data = yf.download(symbol, period="1d", interval="1m", progress=False)
    if data.empty:
        return "N/A"
    return round(data["Close"].iloc[-1], 3)

# -------- SYMBOL MAPPING -------- #

symbols = {
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "USDJPY": "JPY=X",
    "AUDUSD": "AUDUSD=X",
    "USDCAD": "CAD=X",
    "USDCHF": "CHF=X",
    "XAUUSD": "GC=F"
}

# -------- LAYOUT -------- #

left, main = st.columns([1, 3])

# LEFT SIDE – MARKET STRUCTURE
with left:
    st.markdown("### 🧱 Market Structure (REAL DATA)")

    weekly = candle_direction("EURUSD=X", "1wk", "3mo")
    daily = candle_direction("EURUSD=X", "1d", "1mo")
    h4 = candle_direction("EURUSD=X", "4h", "15d")

    st.write(f"*Weekly Candle:* {weekly}")
    st.write(f"*Daily Candle:* {daily}")
    st.write(f"*H4 Candle:* {h4}")

# MAIN – TOP 7 PAIRS
with main:
    st.markdown("### 💱 Top 7 Currency Pairs (Live Price)")

    cols = st.columns(4)
    for i, (pair, sym) in enumerate(symbols.items()):
        with cols[i % 4]:
            price = live_price(sym)
            st.metric(
                label=pair,
                value=price,
                delta="London / NY"
            )

st.markdown("---")
st.caption("✅ Real price & real candle data | AI & fundamentals next")
