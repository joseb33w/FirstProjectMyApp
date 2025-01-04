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
        return {"ages": [], "savings": []}  # Return an empty structure if no file exists

# Function to write updated savings data
def write_savings_data(data):
    with open("savings_history.json", "w") as file:
        json.dump(data, file)

# Function to display the line chart
def display_savings_chart(data, current_age, retirement_age):
    # Filter the data to show only ages within the desired range
    filtered_data = {
        "Age": [age for age, _ in zip(data["ages"], data["savings"]) if current_age <= age <= retirement_age],
        "Savings": [saving for age, saving in zip(data["ages"], data["savings"]) if current_age <= age <= retirement_age],
    }

    # Create a DataFrame for the chart
    df = pd.DataFrame(filtered_data)

    # Create the Altair line chart
    line_chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("Age:Q", title="Age"),
        y=alt.Y(
            "Savings:Q",
            title="Savings ($)",
            scale=alt.Scale(domain=[0, max(data["savings"], default=1)]),  # Set y-axis to include all savings
            axis=alt.Axis(labelExpr="datum.value >= 1000000 ? datum.value / 1000000 + 'M' : datum.value >= 1000 ? datum.value / 1000 + 'k' : datum.value"),
        ),
        tooltip=[
            alt.Tooltip("Age:Q", title="Age"),
            alt.Tooltip("Savings:Q", title="Savings", format="$.2f")
        ]
    ).properties(
        width=800,
        height=400,
        title="Savings Over Time (Age)"
    )

    # Display the chart
    st.altair_chart(line_chart, use_container_width=True)

# Main function
def main():
    st.title("Current Retirement Savings Tracker")

    # Input fields for age and desired retirement age
    current_age = st.number_input("Enter your current age:", min_value=0, max_value=120, step=1, value=25)
    retirement_age = st.number_input("Enter your desired retirement age:", min_value=current_age, max_value=120, step=1, value=65)

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
        # Add the current savings and age to the history if it's new
        if current_age not in data["ages"]:  # Avoid duplicate entries for the same age
            data["ages"].append(current_age)
            data["savings"].append(current_savings)
            write_savings_data(data)

        # Display the line chart
        display_savings_chart(data, current_age, retirement_age)

if __name__ == "__main__":
    main()
