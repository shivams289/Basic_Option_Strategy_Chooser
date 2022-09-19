import streamlit as st
from Model.model import Strategy
import pandas as pd
import numpy as np


st.title("Options Strategy Payoff Analyzer")

st.sidebar.subheader("What's Your Sentiment")
sentiment = ["Bullish", "Bearish", "Market Neutral", "Range Bound"]
sentiment_option = st.sidebar.selectbox("Sentiment", sentiment)

strats_list = {
    "call_ratio_back_spread": "This Strategy requires you to: Buy 2 OTM CE, Sell ITM CE",
    "bull_put_spread": "This Strategy requires you to: Buy OTM PE, Sell ITM PE",
    "bull_call_spread": "This Strategy requires you to: Buy ITM CE, Sell OTM CE",
    "put_ratio_back_spread": "This Strategy requires you to: Buy 2 OTM PE, Sell an ITM PE",
    "bear_put_spread": "This Strategy requires you to: Buy ITM PE, Sell OTM PE",
    "bear_call_spread": "This Strategy requires you to: Buy OTM CE, Sell ITM CE",
    "long_straddle": "This Strategy requires you to: Sell ATM CE, Sell ATM PE",
    "long_strangle": "This Strategy requires you to: Sell OTM CE, Sell OTM PE",
    "short_straddle": "This Strategy requires you to: Buy ATM CE, Buy ATM PE",
    "short_strangle": "This Strategy requires you to: Buy OTM CE, Buy OTM PE",
}

st.subheader("Select Strategy")
if sentiment_option == "Bullish":
    strat = list(strats_list.keys())[0:3]

elif sentiment_option == "Bearish":
    strat = list(strats_list.keys())[3:6]

elif sentiment_option == "Market Neutral":
    strat = list(strats_list.keys())[6:8]

else:
    strat = list(strats_list.keys())[8:10]

opt = st.selectbox("Strategy", strat)
st.subheader(strats_list[opt])

st.write("### Input Strategy Parameters")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    spot = st.number_input("Spot Price", min_value=1)

with col2:
    LS = st.number_input("Lower Strike", min_value=1)

with col3:
    HS = st.number_input("Higher Strike", min_value=1)

with col4:
    hsp = st.number_input("High Strike Premium", min_value=1)

with col5:
    lsp = st.number_input("Low Strike Premium", min_value=1)

crbs = Strategy(LS, spot, HS, hsp, lsp)
st.subheader("Payoff Chart And OutPut Parameters")
crbs.call_ratio_back_spread()
