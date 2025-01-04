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
        st.image("https://www.investopedia.com/thmb/x7K8k3vK4A3BxUPO1J7U9I0i9-8=/1500x1000/filters:fill(auto,1)/risk-return-graph-57c47c9d5f9b5855e5c0a1b6.png", caption="High Risk, High Return Investment in Stocks")
        st.image("https://via.placeholder.com/150", caption="Post 2")

    with col2:
        st.image("https://via.placeholder.com/150", caption="Post 3")
        st.image("https://via.placeholder.com/150", caption="Post 4")

    with col3:
        st.image("https://via.placeholder.com/150", caption="Post 5")
        st.image("https://via.placeholder.com/150", caption="Post 6")

if __name__ == "__main__":
    main()
