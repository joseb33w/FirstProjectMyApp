import streamlit as st

# Main function to display investment options
def main():
    st.title("Growth & Preservation Investments")

    st.write(
        "Explore simple investment options to grow and preserve your savings. Diversify your portfolio for a balanced financial future."
    )

    # Investment options
    investment_options = [
        "Stocks - Higher risk, higher potential returns",
        "Bonds - Lower risk, stable returns",
        "Mutual Funds - Professionally managed diversified portfolios",
        "Real Estate - Tangible assets with long-term growth",
        "Certificates of Deposit (CDs) - Safe, fixed interest returns",
        "Index Funds - Broad market exposure with lower fees",
        "Savings Account - Secure, low-interest option for liquidity"
    ]

    st.subheader("Investment Options")
    for option in investment_options:
        st.markdown(f"- **{option}**")

    # Informative section
    st.subheader("Investment Principles")
    st.write(
        "- **Diversification:** Spread your investments to reduce risk.\n"
        "- **Risk Management:** Choose investments based on your financial goals and risk tolerance.\n"
        "- **Long-Term Growth:** Consider compounding returns and consistent contributions."
    )

    st.success("Remember: A balanced approach can help you secure your financial future.")

if __name__ == "__main__":
    main()
