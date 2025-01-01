import streamlit as st
import importlib.util
import os

# Set the page configuration
st.set_page_config(page_title="My App", page_icon="", layout="wide")

# Function to dynamically import modules
def dynamic_import(module_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Dynamically resolve the base directory
base_dir = os.path.abspath(os.path.dirname(__file__))  # Directory of App.py
modules_dir = os.path.join(base_dir, "modules")  # Point to the "modules" directory relative to App.py

# Resolve the actual paths of the modules
for_you_path = os.path.join(modules_dir, "2_For_you.py")
retirement_path = os.path.join(modules_dir, "3_Retirement.py")

# Dynamically import the "For You" and "Retirement" pages
try:
    for_you_module = dynamic_import(for_you_path, "for_you")
    retirement_module = dynamic_import(retirement_path, "retirement")
except FileNotFoundError as e:
    st.error(f"Module not found: {e}")
    st.stop()

# Function to hide the sidebar (on login page)
def hide_sidebar():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to display the login page
def login():
    hide_sidebar()  # Hide the sidebar during login
    st.title("Login Page")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Login button logic
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.success("Login successful! You can now access the app.")
        else:
            st.error("Invalid username or password. Please try again.")

# Function to display the main app after login
def main_app():
    # Unhide the sidebar
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: block;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["For You", "Retirement"])

    # Navigate to the selected page dynamically
    if page == "For You":
        for_you_module.main()  # Call the "For You" page's main function
    elif page == "Retirement":
        retirement_module.main()  # Call the "Retirement" page's main function

# Main function
def main():
    # Check login state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main_app()  # Show the main app
    else:
        login()  # Show the login page

if __name__ == "__main__":
    main()