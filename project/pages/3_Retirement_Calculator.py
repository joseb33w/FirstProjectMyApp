import streamlit as st

# Set page configuration
st.set_page_config(page_title="Retirement Calculator", page_icon="📈", layout="wide")

# Function to calculate retirement savings
def calculate_retirement_savings(current_savings, monthly_contribution, annual_return_rate, years_to_invest):
    annual_contribution = monthly_contribution * 12
    future_value_current_savings = current_savings * ((1 + annual_return_rate) ** years_to_invest)
    future_value_contributions = (
        (annual_contribution * (((1 + annual_return_rate) ** years_to_invest - 1) / annual_return_rate))
        if annual_return_rate != 0
        else annual_contribution * years_to_invest
    )
    return future_value_current_savings + future_value_contributions

# Main function
def main():
    st.title("Retirement Calculator")
    
    # Inputs
    current_age = st.text_input("Current Age (Years):", "")
    retirement_age = st.text_input("Desired Retirement Age (Years):", "")
    current_savings = st.text_input("Current Retirement Savings ($):", "")
    monthly_contribution = st.text_input("Monthly Contribution ($):", "")
    annual_return_rate = st.text_input("Annual Return Rate (%):", "")

    if st.button("Calculate"):
        try:
            # Convert inputs
            current_age = int(current_age)
            retirement_age = int(retirement_age)
            current_savings = float(current_savings.replace(",", ""))
            monthly_contribution = float(monthly_contribution.replace(",", ""))
            annual_return_rate = float(annual_return_rate) / 100.0

            # Validate inputs
            if current_age < 0 or retirement_age < 0 or current_age >= retirement_age:
                st.error("Invalid age range. Current age must be less than retirement age.")
                return
            if current_savings < 0 or monthly_contribution < 0 or annual_return_rate < 0:
                st.error("Inputs must be non-negative.")
                return

            years_to_invest = retirement_age - current_age
            final_savings = calculate_retirement_savings(current_savings, monthly_contribution, annual_return_rate, years_to_invest)
            st.success(f"Projected Savings: ${final_savings:,.2f}")
        except ValueError:
            st.error("Please enter valid numerical inputs.")

if __name__ == "__main__":
    main()
