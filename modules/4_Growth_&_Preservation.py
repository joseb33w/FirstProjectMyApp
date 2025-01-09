import streamlit as st

# Ensure this module does not call set_page_config again if imported
def main():
    st.subheader("Investments")
    st.write("Here are your individual investments and their returns since purchase:")

    # Example investment categories for growth and preservation
    investment_options = {
        "Stocks": "Invest in publicly traded companies for growth.",
        "Bonds": "Fixed-income investments for preservation.",
        "Real Estate": "Invest in properties for both growth and preservation.",
        "Mutual Funds": "Pooled investments managed professionally.",
        "ETFs": "Diversified funds for balanced growth and preservation.",
        "Cryptocurrency": "High-risk, high-reward digital assets.",
        "Commodities": "Physical goods like gold and oil for stability.",
        "Savings Accounts": "Low-risk accounts for preserving capital.",
        "Index Funds": "Passive investment strategies for long-term growth.",
        "Startups & Private Equity": "Invest in early-stage companies."
    }

    # Display investment categories in a grid with better alignment
    cols = st.columns(2)
    for i, (investment, description) in enumerate(investment_options.items()):
        with cols[i % 2]:
            st.subheader(investment)
            st.write(description)
            st.button(f"Learn More about {investment}")

    st.write("---")

# ✅ Guard clause to prevent accidental execution when imported
if __name__ == "__main__":
    st.warning("This module is intended to be imported and not run directly.")
