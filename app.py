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
