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

# Main function for the "For You" page
def main():
    st.title("For You")

    # Load shared data (if applicable)
    final_savings = read_shared_data()
    
    # Display user's savings
    display_savings(final_savings)

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
