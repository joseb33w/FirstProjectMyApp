import streamlit as st

# Ensure st.set_page_config is called only once at the top
st.set_page_config(page_title="Explore Investments", layout="wide")

import importlib.util
import os

# Function to dynamically import modules
def dynamic_import(module_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Dynamically resolve the base directory
base_dir = os.path.abspath(os.path.dirname(__file__))  
modules_dir = os.path.join(base_dir, "modules")

# Resolve the actual paths of the modules
for_you_path = os.path.join(modules_dir, "2_For_you.py")
current_retirement_path = os.path.join(modules_dir, "3_Current_Retirement.py")
growth_preservation_path = os.path.join(modules_dir, "4_Growth_&_Preservation.py")

# Dynamically import the modules (Ensure they don't call st.set_page_config)
try:
    for_you_module = dynamic_import(for_you_path, "for_you")
    current_retirement_module = dynamic_import(current_retirement_path, "current_retirement")
    growth_preservation_module = dynamic_import(growth_preservation_path, "growth_preservation")
except FileNotFoundError as e:
    st.error(f"Module not found: {e}")
    st.stop()

# Function to display the login page
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()  # Ensure proper page refresh after login
        else:
            st.error("Invalid username or password.")

# Function to display the main app after login
def main_app():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["For You", "Current Retirement", "Growth & Preservation"])

    # Navigate between modules
    if page == "For You":
        for_you_module.main()
    elif page == "Current Retirement":
        current_retirement_module.main()
    elif page == "Growth & Preservation":
        growth_preservation_module.main()

# Main function to control the entire app flow
def main():
    # Ensure the login and main app do not overlap
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main_app()  # Show the main app
    else:
        login()  # Show the login page

if __name__ == "__main__":
    main()
