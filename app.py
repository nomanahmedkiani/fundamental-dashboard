import streamlit as st

# Page config
st.set_page_config(page_title="Trading Dashboard", layout="wide")

# Header
st.title("📊 Fundamental Trading Dashboard")
st.subheader("User: Noman Ahmed")

# Layout
left, main = st.columns([1, 3])

# LEFT SIDE – Market Structure
with left:
    st.markdown("### 🧱 Market Structure")

    st.write("*Weekly Candle:* 🟢 Bullish")
    st.write("*Daily Candle:* 🔴 Bearish")
    st.write("*Daily Structure:* Range")
    st.write("*H4 Structure:* 🟢 Bullish")

# MAIN SECTION – Top 7 Pairs
with main:
    st.markdown("### 💱 Top 7 Currency Pairs")

    pairs = [
        "EURUSD", "GBPUSD", "USDJPY",
        "AUDUSD", "USDCAD", "USDCHF", "XAUUSD"
    ]

    cols = st.columns(4)
    for i, pair in enumerate(pairs):
        with cols[i % 4]:
            st.metric(
                label=pair,
                value="Neutral",
                delta="Session: London / NY"
            )

st.markdown("---")
st.caption("⚠️ Basic live version — backend & real-time data coming next")
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
