import streamlit as st

# Configure the page layout and title
st.set_page_config(page_title="Multipage Streamlit App", page_icon=":house:", layout="wide")

# Sidebar message for navigation
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
