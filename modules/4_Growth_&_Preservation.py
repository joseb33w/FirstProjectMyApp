import streamlit as st
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Initialize the session state for user data and login state if not already present
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_age" not in st.session_state:
    st.session_state.user_age = 30
if "savings_amount" not in st.session_state:
    st.session_state.savings_amount = 100000
if "retirement_age" not in st.session_state:
    st.session_state.retirement_age = 65
if "monthly_expenses" not in st.session_state:
    st.session_state.monthly_expenses = 3000
if "inflation_rate" not in st.session_state:
    st.session_state.inflation_rate = 3
if "annual_return" not in st.session_state:
    st.session_state.annual_return = 6

# Function to display the login page
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Simple login logic for demonstration purposes
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password. Please try again.")

# Calculate projected retirement income and savings longevity
def calculate_retirement_insights():
    years_until_retirement = st.session_state.retirement_age - st.session_state.user_age
    future_value = st.session_state.savings_amount * ((1 + st.session_state.annual_return / 100) ** years_until_retirement)
    monthly_income = future_value * (st.session_state.annual_return / 100) / 12

    # Adjusting expenses for inflation
    adjusted_monthly_expenses = st.session_state.monthly_expenses * ((1 + st.session_state.inflation_rate / 100) ** years_until_retirement)
    annual_expenses = adjusted_monthly_expenses * 12
    years_covered = future_value / annual_expenses

    return future_value, monthly_income, adjusted_monthly_expenses, years_covered

# Function to display the retirement tracker
def retirement_tracker():
    st.title("Current Retirement Savings Tracker")

    st.subheader("Enter Your Retirement Information")
    st.session_state.user_age = st.number_input("Enter your current age:", min_value=18, max_value=100, value=30)
    st.session_state.retirement_age = st.number_input("Enter your retirement age:", min_value=50, max_value=100, value=65)
    st.session_state.savings_amount = st.number_input("Current Savings Amount ($):", min_value=0, value=100000)
    st.session_state.monthly_expenses = st.number_input("Expected Monthly Retirement Expenses ($):", min_value=0, value=3000)
    st.session_state.inflation_rate = st.number_input("Inflation Rate (%):", min_value=0.0, max_value=10.0, value=3.0)
    st.session_state.annual_return = st.number_input("Annual Return Rate (%):", min_value=0.0, max_value=20.0, value=6.0)

    # Display insights
    future_value, monthly_income, adjusted_monthly_expenses, years_covered = calculate_retirement_insights()

    st.subheader("Retirement Insights")
    st.metric(label="Projected Retirement Savings", value=f"${future_value:,.2f}")
    st.metric(label="Estimated Monthly Income from Savings", value=f"${monthly_income:,.2f}")
    st.metric(label="Adjusted Monthly Expenses (Inflation Adjusted)", value=f"${adjusted_monthly_expenses:,.2f}")
    st.metric(label="Years Savings Will Last After Retirement", value=f"{years_covered:.1f} years")

    # Retirement Readiness Indicator
    if years_covered >= 35:
        st.success("✅ You're on track for a comfortable retirement!")
    elif years_covered >= 20:
        st.warning("⚠️ You might need to adjust your savings strategy.")
    else:
        st.error("❌ Your current savings may not be sufficient for a comfortable retirement.")

    # Interactive Chart
    years = np.arange(st.session_state.retirement_age, 101)
    savings_projection = [future_value - (adjusted_monthly_expenses * 12 * (year - st.session_state.retirement_age)) for year in years]
    savings_projection = [max(0, value) for value in savings_projection]

    fig, ax = plt.subplots()
    ax.plot(years, savings_projection, color='green')
    ax.set_title("Projected Savings Over Time")
    ax.set_xlabel("Age")
    ax.set_ylabel("Savings ($)")
    ax.axhline(0, color='red', linestyle='--')
    st.pyplot(fig)

# Main function to control login and app flow
def main():
    if not st.session_state.logged_in:
        login()
    else:
        retirement_tracker()

if __name__ == "__main__":
    main()
