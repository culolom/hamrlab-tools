import yfinance as yf
import streamlit as st

@st.cache_data(ttl=3600)  # 1 小時更新一次
def get_available_range(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="max", auto_adjust=True)
    return hist.index.min(), hist.index.max()

@st.cache_data(ttl=3600)
def load_history(symbol, period="max"):
    return yf.Ticker(symbol).history(period=period, auto_adjust=True)
