import streamlit as st

# Ensure this module does not call set_page_config again if imported
def main():
    st.title("Growth & Preservation")
    st.subheader("Investments")

    # Display the user's current investments and returns in a structured way
    st.write("Here are your current investments and their returns since purchase:")
    st.write("**Stocks:** $1,500.00 | 5.00%")
    st.write("**Bonds:** $500.00 | 2.00%")
    st.write("**Real Estate:** $3,000.00 | 8.00%")
    st.write("**Average Return on Investment:** $5,000.00 | 5.00%")

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

    # Display investment categories in a grid with aligned columns
    cols = st.columns(2)
    for i, (investment, description) in enumerate(investment_options.items()):
        with cols[i % 2]:
            st.subheader(investment)
            st.write(description)
            st.button(f"Learn More about {investment}")

# ✅ Guard clause to prevent accidental execution when imported
if __name__ == "__main__":
    main()
