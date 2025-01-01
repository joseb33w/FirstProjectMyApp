import streamlit as st
import pandas as pd
import altair as alt
import json
from datetime import datetime

# Function to read historical savings data
@st.cache_data
def read_savings_data():
    try:
        with open("savings_history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"dates": [], "savings": []}  # Return an empty structure if no file exists

# Function to write updated savings data
def write_savings_data(data):
    with open("savings_history.json", "w") as file:
        json.dump(data, file)

# Function to display the line chart
def display_savings_chart(data):
    # Create a DataFrame for the chart
    df = pd.DataFrame({
        "Date": pd.to_datetime(data["dates"]),
        "Savings": data["savings"]
    })

    # Create the Altair line chart
    line_chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y(
            "Savings:Q",
            title="Savings ($)",
            axis=alt.Axis(labelExpr="datum.value >= 1000000 ? datum.value / 1000000 + 'M' : datum.value >= 1000 ? datum.value / 1000 + 'k' : datum.value"),
        ),
        tooltip=[
            alt.Tooltip("Date:T", title="Date"),
            alt.Tooltip("Savings:Q", title="Savings", format="$.2f")
        ]
    ).properties(
        width=800,
        height=400,
        title="Savings History"
    )

    # Display the chart
    st.altair_chart(line_chart, use_container_width=True)

# Main function
def main():
    st.title("Current Retirement Savings Tracker")

    # Load historical savings data
    data = read_savings_data()

    # Get the current savings from the shared data in For_you.py
    try:
        with open("shared_data.json", "r") as file:
            shared_data = json.load(file)
            current_savings = shared_data.get("final_savings", 0)
    except FileNotFoundError:
        st.error("No shared data found. Please use the app in For_you.py to generate savings data.")
        current_savings = None

    if current_savings is not None:
        # Add the current savings to the history if it's new
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if current_date not in data["dates"]:  # Avoid duplicate entries for the same date
            data["dates"].append(current_date)
            data["savings"].append(current_savings)
            write_savings_data(data)

        # Display the line chart
        display_savings_chart(data)

        # Show the most recent savings
        st.success(f"Your most recent savings: ${current_savings:,.2f}")

if __name__ == "__main__":
    main()