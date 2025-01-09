import streamlit as st
import importlib.util
import os

# Define investment categories
types_of_investments = {
    "Stocks": "Invest in publicly traded companies with growth potential.",
    "Bonds": "Fixed-income investments offering regular interest payments.",
    "Real Estate": "Invest in physical properties for rental income and capital gains.",
    "Mutual Funds": "Pooled investment managed by professionals.",
    "ETFs": "Exchange-Traded Funds combining multiple assets for diversified exposure.",
    "Cryptocurrency": "Digital assets with high volatility and growth potential.",
    "Commodities": "Invest in physical goods like gold, oil, and agricultural products.",
    "Savings Accounts": "Low-risk, interest-bearing bank accounts.",
    "Index Funds": "Passive investment funds tracking market indices.",
    "Startups & Private Equity": "Invest in early-stage companies and private businesses."
}

# Streamlit app layout
st.title("Explore Investment Opportunities")
st.write("Browse different types of investment options to grow and preserve your wealth.")

# Display investment categories in a grid
cols = st.columns(3)
for i, (investment, description) in enumerate(types_of_investments.items()):
    with cols[i % 3]:
        st.subheader(investment)
        st.write(description)
        st.button(f"Explore {investment}")

# Footer
st.write("---")
st.write("Select an investment type to learn more about how you can start building wealth!")
