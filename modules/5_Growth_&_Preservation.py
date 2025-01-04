import streamlit as st

def main():
    st.title("Growth & Preservation Investments")

    st.header("Investment Options")
    st.markdown("""
    - **Stocks**: Higher risk, higher potential returns
    - **Bonds**: Lower risk, stable returns
    - **Mutual Funds**: Professionally managed diversified portfolios
    - **Real Estate**: Tangible assets with long-term growth
    - **Certificates of Deposit (CDs)**: Safe, fixed interest returns
    - **Index Funds**: Broad market exposure with lower fees
    - **Savings Account**: Secure, low-interest option for liquidity
    """)

    # Explore Page Layout
    st.header("Explore Page")
    col1, col2, col3 = st.columns(3)

    # Mockup content for the explore page (You can replace with dynamic content)
    with col1:
        st.image("https://via.placeholder.com/150", caption="Post 1")
        st.image("https://via.placeholder.com/150", caption="Post 2")

    with col2:
        st.image("https://via.placeholder.com/150", caption="Post 3")
        st.image("https://via.placeholder.com/150", caption="Post 4")

    with col3:
        st.image("https://via.placeholder.com/150", caption="Post 5")
        st.image("https://via.placeholder.com/150", caption="Post 6")

if __name__ == "__main__":
    main()
