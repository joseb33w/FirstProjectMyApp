import streamlit as st
import json

def format_number_with_commas(value):
    """
    Format a number with commas as thousands separators.
    """
    if value:
        try:
            # Remove any existing commas, convert to float, then reformat
            formatted_value = f"{float(value.replace(',', '')):,.0f}"
            return formatted_value
        except ValueError:
            return value  # If the value is invalid, return it as-is
    return ""

def calculate_retirement_savings(current_savings,
                                 monthly_contribution,
                                 annual_return_rate,
                                 years_to_invest):
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

def main():
    st.title("Retirement Calculator")
    
    # User inputs with automatic comma formatting
    current_age = st.text_input("Current Age:")
    retirement_age = st.text_input("Desired Retirement Age:")
    
    # Current Savings with automatic formatting
    current_savings = st.text_input("Current Retirement Savings ($):")
    current_savings = format_number_with_commas(current_savings)  # Apply formatting dynamically
    
    # Monthly Contribution with automatic formatting
    monthly_contribution = st.text_input("Monthly Contribution ($):")
    monthly_contribution = format_number_with_commas(monthly_contribution)  # Apply formatting dynamically
    
    # Annual return rate starts blank
    annual_return_rate_percent = st.text_input("Annual Return Rate (%)")
    
    # Handle inputs and calculations when the button is clicked
    if st.button("Calculate"):
        try:
            # Convert inputs to appropriate types
            current_age = int(current_age) if current_age else 0
            retirement_age = int(retirement_age) if retirement_age else 0
            current_savings = float(current_savings.replace(",", "")) if current_savings else 0.0
            monthly_contribution = float(monthly_contribution.replace(",", "")) if monthly_contribution else 0.0
            annual_return_rate_percent = float(annual_return_rate_percent) if annual_return_rate_percent else 0.0
            annual_return_rate = annual_return_rate_percent / 100.0
            years_to_invest = retirement_age - current_age
            
            # Calculate retirement savings
            final_savings = calculate_retirement_savings(
                current_savings, 
                monthly_contribution, 
                annual_return_rate, 
                years_to_invest
            )
            
            # Save the result to a shared JSON file
            data = {"final_savings": final_savings}
            with open("shared_data.json", "w") as file:
                json.dump(data, file)
            
            # Format monetary values with commas
            st.write(f"Projected Savings: ${final_savings:,.2f}")
        except ValueError:
            st.error("Please ensure all inputs are numeric.")

if __name__ == "__main__":
    main()
