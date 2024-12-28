import streamlit as st
import json

# Set page configuration
st.set_page_config(page_title="Retirement Calculator", page_icon="📈", layout="wide")

# Sidebar custom label
st.sidebar.title("Retirement Calculator")

# Function to calculate retirement savings
def calculate_retirement_savings(current_savings, monthly_contribution, annual_return_rate, years_to_invest):
    annual_contribution = monthly_contribution * 12
    future_value_current_savings = current_savings * ((1 + annual_return_rate) ** years_to_invest)
    
    if annual_return_rate != 0:
        future_value_contributions = (
            annual_contribution *
            (((1 + annual_return_rate) ** years_to_invest - 1) / annual_return_rate)
        )
    else:
        future_value_contributions = annual_contribution * years_to_invest

    total_future_value = future_value_current_savings + future_value_contributions
    return total_future_value

# Main function
def main():
    st.title("Retirement Calculator")
    
    # Inputs
    current_age = st.number_input("Current Age:", min_value=0, max_value=120, step=1)
    retirement_age = st.number_input("Desired Retirement Age:", min_value=0, max_value=120, step=1)
    current_savings = st.number_input("Current Retirement Savings ($):", min_value=0.0, step=1000.0, format="%0.2f")
    monthly_contribution = st.number_input("Monthly Contribution ($):", min_value=0.0, step=100.0, format="%0.2f")
    annual_return_rate = st.number_input("Annual Return Rate (%):", min_value=0.0, step=0.1, format="%0.2f") / 100

    if st.button("Calculate"):
        years_to_invest = retirement_age - current_age
        if years_to_invest > 0:
            final_savings = calculate_retirement_savings(
                current_savings,
                monthly_contribution,
                annual_return_rate,
                years_to_invest,
            )

            # Save final savings to JSON
            with open("shared_data.json", "w") as f:
                json.dump({"final_savings": final_savings}, f)

            st.success(f"Projected Savings: ${final_savings:,.2f}")
        else:
            st.error("Retirement age must be greater than current age.")

if __name__ == "__main__":
    main()
