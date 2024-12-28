import streamlit as st

# Configure the main page
st.set_page_config(page_title="Multipage App", page_icon=":house:", layout="wide")

# Sidebar success message
st.sidebar.success("Select a page above.")

# Main page content
st.title("Welcome to the Multipage Streamlit App")
st.write(
    """
    Use the sidebar to navigate between pages:
    - **Savings Visualization**: View the updated savings display.
    - **Retirement Calculator**: Calculate your retirement savings.
    """
)
