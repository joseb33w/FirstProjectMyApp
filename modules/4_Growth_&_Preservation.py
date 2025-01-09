import streamlit as st

# Ensure this module does not call set_page_config again if imported
def main():
    st.title("Growth & Preservation")
    st.subheader("Investments")
    st.write("Here are your individual investments and their returns since purchase:")

    # Example investment categories from 'Current Retirement'
    investment_options = {
        "401(k)": "A retirement savings plan sponsored by an employer with tax advantages.",
        "IRA": "Individual Retirement Account offering tax benefits for retirement savings.",
        "Stocks": "Invest in publicly traded companies for growth.",
        "Bonds": "Fixed-income investments for preservation.",
        "Mutual Funds": "Pooled investments managed professionally.",
        "Savings Accounts": "Low-risk accounts for preserving capital."
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
