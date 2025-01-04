import streamlit as st
import pandas as pd
import altair as alt
import json
from datetime import datetime
from dateutil import parser

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

    # Create the Altair line chart with red dots on each savings point
    line_chart = alt.Chart(df).mark_line().encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y("Savings:Q", title="Savings ($)"),
        tooltip=[
            alt.Tooltip("Date:T", title="Date"),
            alt.Tooltip("Savings:Q", title="Savings", format="$.2f")
        ]
    ) + alt.Chart(df).mark_circle(color='red', size=80).encode(
        x="Date:T",
        y="Savings:Q"
    )

    # Display the chart
    st.altair_chart(line_chart, use_container_width=True)

# Main function
def main():
    st.title("Current Retirement Savings Tracker")

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

        # Allow user to select a year to filter data
        years = sorted(set([parser.parse(date).year for date in dates]))

        selected_year = st.selectbox("Select Year", years)

        # Filter data for the selected year
        filtered_dates = [date for date in dates if parser.parse(date).year == selected_year]
        filtered_savings = [savings[i] for i, date in enumerate(dates) if parser.parse(date).year == selected_year]

        # Display the filtered chart
        display_savings_chart({"Date": filtered_dates, "Savings": filtered_savings})

if __name__ == "__main__":
    main()
