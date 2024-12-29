import streamlit as st
import json
import time

# Set page configuration
st.set_page_config(page_title="For You", page_icon="💰", layout="wide")

# Custom CSS for the bottom bar
st.markdown(
    """
    <style>
    .bottom-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8f9fa;
        text-align: center;
        padding: 10px 0;
        border-top: 1px solid #dee2e6;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
    }
    .bottom-bar a {
        margin: 0 15px;
        text-decoration: none;
        color: #007bff;
        font-weight: bold;
    }
    .bottom-bar a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation bar
st.markdown(
    """
    <div class="bottom-bar">
        <a href="/">For You</a>
        <a href="/pages/2_Retirement_Calculator.py">Retirement Calculator</a>
    </div>
    """,
    unsafe_allow_html=True,
)

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
    st.title("For You")

    placeholder = st.empty()
    while True:
        final_savings = read_shared_data()
        
        with placeholder.container():
            display_savings(final_savings)
        
        time.sleep(2)

if __name__ == "__main__":
    main()
