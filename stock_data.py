import yfinance as yf
import streamlit as st

st.write("""
## Complete Stock Info on Google
Shown are the Stock Details of google
""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Info Of Google
resp = tickerData.info
st.write("""## Stock Info : \n Push Down to See stock info of google: """)
st.write(resp)

#get the historical prices for this ticker
# Open	High	Low	Close	Volume	Dividends	Stock Splits
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""## Closing Price of Stock Chart :""")
st.line_chart(tickerDf.Close)
st.write("""## Volume of Stock Sold Chart :""")
st.line_chart(tickerDf.Volume)
