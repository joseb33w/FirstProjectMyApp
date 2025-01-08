import streamlit as st
import pandas as pd
import altair as alt
import json
from datetime import datetime
from dateutil import parser

# Custom CSS for better font and aesthetics
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        font-size: 36px !important;
        font-weight: bold;
    }
    .stMetric, h2, h3, h4, h5, h6, p {
        font-size: 24px !important;
        font-weight: normal;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to read historical savings data
@st.cache_data
def read_savings_data():
    try:
        with open("savings_history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"ages": [], "savings": []}  # Return an empty structure if no file exists

# Function to write updated savings data
def write_savings_data(data):
    with open("savings_history.json", "w") as file:
        json.dump(data, file)

# Function to display the line chart
def display_savings_chart(data):
    # Create a DataFrame for the chart
    df = pd.DataFrame(data)

    # Ensure the date is correctly parsed and formatted
    df["Date"] = pd.to_datetime(df["Date"])

    # Create the Altair line chart with grid lines and red dots on each savings point
    line_chart = alt.Chart(df).mark_line().encode(
        x=alt.X("Date:T", title="Date", axis=alt.Axis(format="%m/%d", grid=True)),
        y=alt.Y("Savings:Q", title="Savings ($)", axis=alt.Axis(grid=True)),
        tooltip=[
            alt.Tooltip("Date:T", title="Date", format="%m/%d/%Y"),
            alt.Tooltip("Savings:Q", title="Savings", format="$.2f")
        ]
    ) + alt.Chart(df).mark_circle(color='red', size=80).encode(
        x="Date:T",
        y="Savings:Q"
    )

    # Display the chart
    st.altair_chart(line_chart, use_container_width=True)

    # Display savings at the beginning and end of the year with requested format
    st.subheader("Savings Summary")
    st.markdown("<h3 style='font-size:28px;'>Savings Amount</h3>", unsafe_allow_html=True)
    for year in sorted(set(df["Date"].dt.year)):
        yearly_data = df[df["Date"].dt.year == year]
        start_savings = yearly_data.iloc[0]["Savings"]
        end_savings = yearly_data.iloc[-1]["Savings"]
        st.markdown(f"**Start:** ${start_savings:,.2f}")
        st.markdown(f"**End:** ${end_savings:,.2f}")

    # Display yearly contributions summary
    st.markdown("<h3 style='font-size:28px;'>Year's Contribution</h3>", unsafe_allow_html=True)
    for year in sorted(set(df["Date"].dt.year)):
        yearly_data = df[df["Date"].dt.year == year]
        contribution = yearly_data.iloc[-1]["Savings"] - yearly_data.iloc[0]["Savings"]
        st.markdown(f"**Contributions Made:** ${contribution:,.2f}")

    # Display investment returns summary with dollar and percentage vertically stacked
    st.markdown("<h3 style='font-size:28px;'>Investment's Return</h3>", unsafe_allow_html=True)
    for year in sorted(set(df["Date"].dt.year)):
        yearly_data = df[df["Date"].dt.year == year]
        start_savings = yearly_data.iloc[0]["Savings"]
        end_savings = yearly_data.iloc[-1]["Savings"]
        contribution = yearly_data.iloc[-1]["Savings"] - yearly_data.iloc[0]["Savings"]
        investment_return = end_savings - start_savings - contribution
        investment_return_percentage = (investment_return / start_savings) * 100 if start_savings > 0 else 0
        st.markdown(f"**Return on Investment:**\n${investment_return:,.2f}\n{investment_return_percentage:.2f}%")

    # Display current investments summary with individual returns
    st.markdown("<h3 style='font-size:28px;'>Current Investments</h3>", unsafe_allow_html=True)
    investments = [
        {"name": "Stocks", "return": 1500, "percentage": 5.0},
        {"name": "Bonds", "return": 500, "percentage": 2.0},
        {"name": "Real Estate", "return": 3000, "percentage": 8.0}
    ]
    for investment in investments:
        st.markdown(f"**{investment['name']}:**\n${investment['return']:,.2f}\n{investment['percentage']:.2f}%")

# Main function
def main():
    st.title("Current Retirement")

    # Load historical savings data
    data = read_savings_data()

    # Get the current savings and dates from the shared data
    try:
        with open("shared_data.json", "r") as file:
            shared_data = json.load(file)
            current_savings = shared_data.get("final_savings", 0)
            dates = shared_data.get("dates", [])
            savings = shared_data.get("savings", [])

            # Ensure both lists are of the same length
            min_length = min(len(dates), len(savings))
            dates = dates[:min_length]
            savings = savings[:min_length]

    except FileNotFoundError:
        st.error("No shared data found. Please use the app in For_you.py to generate savings data.")
        current_savings = None
        dates = []
        savings = []

    if current_savings is not None and dates:
        # Prepare the data for visualization using dates
        filtered_data = {
            "Date": dates,
            "Savings": savings
        }

        # Allow user to type a year instead of selecting
        years = sorted(set([parser.parse(date).year for date in dates]))

        selected_year = st.text_input("Enter Year (YYYY)")

        if selected_year:
            try:
                selected_year = int(selected_year)
                if selected_year not in years:
                    st.error("The year you entered is not in the data.")
                else:
                    # Filter data for the selected year
                    filtered_dates = [date for date in dates if parser.parse(date).year == selected_year]
                    filtered_savings = [savings[i] for i, date in enumerate(dates) if parser.parse(date).year == selected_year]

                    # Display the filtered chart
                    display_savings_chart({"Date": filtered_dates, "Savings": filtered_savings})
            except ValueError:
                st.error("Please enter a valid year.")

if __name__ == "__main__":
    main()
