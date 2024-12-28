import streamlit as st
import json
import time

def read_shared_data():
    """
    Reads the shared data from the JSON file.
    """
    try:
        with open("shared_data.json", "r") as file:
            data = json.load(file)
            return data.get("final_savings", 0)
    except FileNotFoundError:
        return 0

def display_savings(savings):
    """
    Displays "Savings" dynamically in the visual interface.
    """
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 0.3rem;">
            <div style="font-size: 1.5rem; font-weight: bold;">Savings:</div>
            <div style="font-size: 2rem; font-weight: bold;">${savings:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_color_bar(savings):
    """
    Displays a color bar with a dynamically positioned arrow based on savings between $0 and $300 million.
    """
    # Map savings to a position on the color bar (0 to 300 million)
    max_savings = 300_000_000  # 300 million
    position_percentage = min(savings / max_savings, 1) * 100  # Cap at 100%
    
    st.markdown(
        f"""
        <div style="position: relative; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; margin-top: -5px;">
            <!-- Color Bar -->
            <div style="height: 8px; width: 100%; background: linear-gradient(to right, #FCE2E1, #F8B6B4, #F28783, #E85A50, #D12014); position: relative;">
                <!-- Arrow -->
                <div style="position: absolute; top: -15px; left: {position_percentage}%; transform: translateX(-50%); font-size: 1.2rem; color: white;">
                    ▼
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    # Replace title with "For you"
    st.markdown(
        """
        <h1 style="text-align: left; font-weight: bold; margin-bottom: 2rem;">For you</h1>
        """,
        unsafe_allow_html=True
    )
    
    placeholder = st.empty()
    while True:
        # Read the dynamic savings value from the shared JSON file
        final_savings = read_shared_data()
        
        with placeholder.container():
            display_savings(final_savings)
            display_color_bar(final_savings)
        
        # Refresh every 2 seconds
        time.sleep(2)

if __name__ == "__main__":
    main()
