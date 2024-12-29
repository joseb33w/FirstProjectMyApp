import streamlit as st
import json

# Set page configuration
st.set_page_config(page_title="Retirement Calculator", page_icon="📈", layout="wide")

# Sidebar navigation message
st.sidebar.success("Select a page above.")

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
    current_age = st.text_input("Current Age (Years):", "")
    retirement_age = st.text_input("Desired Retirement Age (Years):", "")
    current_savings = st.text_input("Current Retirement Savings ($):", "")
    monthly_contribution = st.text_input("Monthly Contribution ($):", "")
    annual_return_rate = st.text_input("Annual Return Rate (%):", "")
    
    if st.button("Calculate"):
        try:
            # Convert inputs to appropriate types
            current_age = int(current_age)
            retirement_age = int(retirement_age)
            current_savings = float(current_savings.replace(",", ""))
            monthly_contribution = float(monthly_contribution.replace(",", ""))
            annual_return_rate = float(annual_return_rate) / 100.0
            
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
        except ValueError:
            st.error("Please enter valid numerical inputs.")

if __name__ == "__main__":
    main()
