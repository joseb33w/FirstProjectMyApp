import streamlit as st
import pandas as pd
import altair as alt

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

# Function to calculate yearly savings for graph
def calculate_yearly_savings(current_savings, monthly_contribution, annual_return_rate, years_to_invest, start_age):
    yearly_savings = []
    savings = current_savings
    for year in range(1, years_to_invest + 1):
        savings = savings * (1 + annual_return_rate) + (monthly_contribution * 12)
        yearly_savings.append({"Age": start_age + year, "Savings": savings})
    return yearly_savings

# Main function for the Retirement Calculator page
def main():
    st.title("Retirement")

    # Input fields for user financial details
    current_age = st.number_input("Current Age (Years):", min_value=0, max_value=100, step=1, key="current_age")
    retirement_age = st.number_input("Desired Retirement Age (Years):", min_value=0, max_value=100, step=1, key="retirement_age")
    current_savings = st.number_input("Current Savings ($):", min_value=0.0, step=100.0, key="current_savings")
    monthly_contribution = st.number_input("Monthly Contribution ($):", min_value=0.0, step=50.0, key="monthly_contribution")
    annual_return_rate = st.number_input("Annual Return Rate (%):", min_value=0.0, step=0.1, key="annual_return_rate") / 100.0

    # Calculate button
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
            st.success(f"Your projected retirement savings at age {retirement_age}: ${final_savings:,.2f}")
            
            # Calculate yearly savings for the graph
            yearly_savings = calculate_yearly_savings(current_savings, monthly_contribution, annual_return_rate, years_to_invest, current_age)
            
            # Fill missing ages with $0 savings for visualization purposes
            all_ages = pd.DataFrame({"Age": range(0, 111), "Savings": 0})
            savings_df = pd.DataFrame(yearly_savings)
            combined_data = pd.concat([all_ages, savings_df]).drop_duplicates(subset="Age", keep="last").sort_values("Age")
            
            # Create Altair chart with fixed axes
            chart = alt.Chart(combined_data).mark_line().encode(
                x=alt.X("Age:Q", scale=alt.Scale(domain=[0, 110]), title="Age"),
                y=alt.Y("Savings:Q", scale=alt.Scale(domain=[0, 150_000_000]), title="Savings ($)"),
            ).properties(
                width=800,
                height=400,
                title="Projected Savings Over Time"
            )

            # Display the line graph
            st.altair_chart(chart, use_container_width=True)

    # Optional additional content
    st.subheader("Tips for Retirement Planning")
    st.write("""
    - Start saving as early as possible to take advantage of compound interest.
    - Increase contributions as your income grows.
    - Diversify your investments to reduce risk.
    - Consult a financial advisor for personalized advice.
    """)

if __name__ == "__main__":
    main()