import streamlit as st
import json

# Function to read shared data (optional)
@st.cache_data
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
    max_savings = 300_000_000  # Example max value for the bar
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

# Main function for the "For You" page
def main():
    st.title("For You")
    st.write("Welcome to the personalized 'For You' page!")

    # Load shared data (if applicable)
    final_savings = read_shared_data()
    
    # Display user's savings
    st.subheader("Your Financial Overview")
    display_savings(final_savings)
    display_color_bar(final_savings)

    # Example additional content
    st.subheader("Recommendations for You")
    st.write("""
    - **Increase your monthly contributions:** Small changes can make a big difference!
    - **Diversify your investments:** Consider different asset classes for better returns.
    - **Set new goals:** Keep revisiting your financial goals to stay on track.
    """)

    st.subheader("Quick Actions")
    if st.button("Update Profile"):
        st.info("Profile update feature coming soon!")
    if st.button("View Reports"):
        st.info("Reports feature coming soon!")

if __name__ == "__main__":
    main()
