import streamlit as st

# Function to calculate retirement savings
def calculate_retirement_savings(current_savings, monthly_contribution, annual_return_rate, years_to_invest):
    """
    Calculate future retirement savings based on current savings, 
    monthly contributions, annual return rate, and years to invest.
    """
    annual_contribution = monthly_contribution * 12
    future_value_current_savings = current_savings * ((1 + annual_return_rate) ** years_to_invest)
    future_value_contributions = (
        (annual_contribution * (((1 + annual_return_rate) ** years_to_invest - 1) / annual_return_rate))
        if annual_return_rate != 0
        else annual_contribution * years_to_invest
    )
    return future_value_current_savings + future_value_contributions

# Main function for the Retirement page
def main():
    """Render the Retirement page."""
    st.title("Retirement")

    # Input fields for user financial details
    st.subheader("Enter Your Details:")
    current_age = st.number_input(
        "Current Age (Years):", 
        min_value=0, max_value=100, step=1, 
        key="current_age"
    )
    retirement_age = st.number_input(
        "Desired Retirement Age (Years):", 
        min_value=0, max_value=100, step=1, 
        key="retirement_age"
    )
    current_savings = st.number_input(
        "Current Savings ($):", 
        min_value=0.0, step=100.0, 
        key="current_savings", 
        format="%.2f"
    )
    monthly_contribution = st.number_input(
        "Monthly Contribution ($):", 
        min_value=0.0, step=50.0, 
        key="monthly_contribution", 
        format="%.2f"
    )
    annual_return_rate = st.number_input(
        "Annual Return Rate (%):", 
        min_value=0.0, step=0.1, 
        key="annual_return_rate"
    ) / 100.0  # Convert percentage to decimal

    # Calculate button logic
    if st.button("Calculate Retirement Savings"):
        # Input validation
        if retirement_age <= current_age:
            st.error("Retirement age must be greater than current age.")
        else:
            years_to_invest = retirement_age - current_age
            final_savings = calculate_retirement_savings(
                current_savings,
                monthly_contribution,
                annual_return_rate,
                years_to_invest
            )
            st.success(
                f"Your projected retirement savings at age {retirement_age}: "
                f"${final_savings:,.2f}"
            )

    # Optional additional content
    st.subheader("Tips for Retirement Planning:")
    st.markdown("""
    - **Start Early:** Save as early as possible to maximize compound interest.
    - **Increase Contributions:** Raise contributions as your income grows.
    - **Diversify Investments:** Spread your portfolio across asset classes to minimize risk.
    - **Consult an Expert:** Get advice tailored to your financial situation.
    """)

if __name__ == "__main__":
    main()