import streamlit as st

# Ensure this module does not call set_page_config again if imported
def main():
    st.title("Growth & Preservation")
    st.subheader("Investments")

    # Display the user's current investments and returns
    st.write("Here are your current investments and their returns since purchase:")
    st.write("**Stocks:** $1,500.00 | 5.00%")
    st.write("**Bonds:** $500.00 | 2.00%")
    st.write("**Real Estate:** $3,000.00 | 8.00%")
    st.write("**Average Return on Investment:** $5,000.00 | 5.00%")

    # Display investment categories in a grid without images
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

    cols = st.columns(3)
    for i, (investment, description) in enumerate(investment_options.items()):
        with cols[i % 3]:
            st.subheader(investment)
            st.write(description)
            st.button(f"Learn More about {investment}")

# ✅ Corrected Login Page Logic
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()  # Ensures a page refresh after login
        else:
            st.error("Invalid credentials, please try again.")

# ✅ State Management for Proper Page Control
def app_control():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main()  # Show the investments page after successful login
    else:
        login()  # Keep showing the login page until authenticated

# ✅ Guard clause to prevent accidental execution when imported
if __name__ == "__main__":
    app_control()
