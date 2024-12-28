import streamlit as st

# Set page configuration
st.set_page_config(page_title="Streamlit App", page_icon=":house:", layout="wide")

# Sidebar navigation message
st.sidebar.title("Navigation")
st.sidebar.success("Select a page to navigate.")

# Main page content
st.title("Welcome to the Multipage Streamlit App")
st.write(
    """
    Use the sidebar to navigate between pages:
    - **Savings Visualization**: View the updated savings display.
    - **Retirement Calculator**: Calculate your retirement savings.
    """
)
