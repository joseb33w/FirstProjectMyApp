import streamlit as st
import json
import time

# Set page configuration
st.set_page_config(page_title="Savings Visualization", page_icon="💰", layout="wide")

# Sidebar navigation message
st.sidebar.success("Select a page above.")

# Function to read shared data
def read_shared_data():
    try:
        with open("shared_data.json", "r") as file:
            data = json.load(file)
            return data.get("final_savings", 0)
    except FileNotFoundError:
        return 0

# Function to display savings
def display_savings(savings):
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 0.3rem;">
            <div style="font-size: 1.5rem; font-weight: bold;">Savings:</div>
            <div style="font-size: 2rem; font-weight: bold;">${savings:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main function
def main():
    st.title("Savings Visualization")

    placeholder = st.empty()
    while True:
        final_savings = read_shared_data()
        
        with placeholder.container():
            display_savings(final_savings)
        
        time.sleep(2)

if __name__ == "__main__":
    main()
