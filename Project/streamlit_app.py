import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", page_icon=":house:", layout="wide")

# Sidebar message
st.sidebar.success("Select a page above to navigate.")

# Main page content
st.title("Welcome to the Multipage Streamlit App")
st.write(
    """
    Use the sidebar to navigate between pages:
    - **Savings Visualization**: View the updated savings display.
    - **Retirement Calculator**: Calculate your retirement savings.
    """
)
