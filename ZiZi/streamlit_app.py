import streamlit as st

st.set_page_config(page_title="Multipage Streamlit App", page_icon=":house:", layout="wide")

st.sidebar.success("Select a page above")
st.title("Multipage Streamlit App")
st.write(
    """
    Welcome to the multipage Streamlit app! Use the sidebar to navigate between pages:
    - **Savings Visualization**: View the updated savings display.
    - **Retirement Calculator**: Calculate your retirement savings.
    """
)
