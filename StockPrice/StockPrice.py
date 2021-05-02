import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-1')

st.write("""
## Google
""")

st.write("""
### Closing Price History
""")
st.line_chart(tickerDf.Close)

st.write("""
### Stock Volume
""")
st.line_chart(tickerDf.Volume)