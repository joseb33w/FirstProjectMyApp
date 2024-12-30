import streamlit as st
import importlib.util
import os

# Set the page configuration
st.set_page_config(page_title="My App", page_icon="🔒", layout="wide")

# Debugging current working directory and files
st.write("Current working directory:", os.getcwd())
st.write("Files and folders in current directory:")
for root, dirs, files in os.walk("."):
    st.write(root, dirs, files)

# Function to dynamically import modules
def dynamic_import(module_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Update paths to match the actual directory structure
for_you_module = dynamic_import("project/modules/2_For_you.py", "for_you")  # Updated path
retirement_calculator_module = dynamic_import("project/modules/3_Retirement_Calculator.py", "retirement_calculator")  # Updated path

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
    page = st.sidebar.radio("Go to", ["For You", "Retirement Calculator"])

    # Navigate to the selected page dynamically
    if page == "For You":
        for_you_module.main()  # Call the "For You" page's main function
    elif page == "Retirement Calculator":
        retirement_calculator_module.main()  # Call the "Retirement Calculator" page's main function

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
