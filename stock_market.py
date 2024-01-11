import pandas as pd 
import streamlit as st 
import yfinance as yf 

st.title("Stock Market App")
st.write('This presents stock market data')
# enter user stock symbol
user_stock_symbol = st.text_input("Enter stock ticker symbol","AAPL")
ticker_symbol = user_stock_symbol
ticker_data = yf.Ticker(ticker_symbol)
starting_date = st.date_input("Enter starting date",value=pd.to_datetime("2021-01-01"))
ending_date = st.date_input("Enter ending date",value=pd.to_datetime("today"))
hist = ticker_data.history(start=starting_date,end=ending_date)
st.write(hist)
col1,col2 = st.columns(2)
with col1:
    st.write("This plot is for volume of stock")
    st.line_chart(hist.Volume)
with col2:
    st.write("This plot is for closing price of stock")
    st.line_chart(hist.Close)