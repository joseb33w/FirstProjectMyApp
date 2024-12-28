import streamlit as st
import json
import time

# Set page configuration
st.set_page_config(page_title="Savings Visualization", page_icon="💰", layout="wide")

# Sidebar navigation message
st.sidebar.success("You are viewing the Savings Visualization page.")

st.title("Savings Visualization")
st.write("This page displays the savings visualization.")


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

# Function to display a dynamic color bar
def display_color_bar(savings):
    max_savings = 300_000_000  # Max savings value for the bar
    position_percentage = min(savings / max_savings, 1) * 100
    
    st.markdown(
        f"""
        <div style="position: relative; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; margin-top: -5px;">
            <div style="height: 8px; width: 100%; background: linear-gradient(to right, #FCE2E1, #F8B6B4, #F28783, #E85A50, #D12014); position: relative;">
                <div style="position: absolute; top: -15px; left: {position_percentage}%; transform: translateX(-50%); font-size: 1.2rem; color: white;">
                    ▼
                </div>
            </div>
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
            display_color_bar(final_savings)
        
        time.sleep(2)

if __name__ == "__main__":
    main()
