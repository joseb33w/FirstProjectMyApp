import streamlit as st

# Ensure st.set_page_config is called only once as the first Streamlit command
st.set_page_config(page_title="Tani", layout="wide")

import importlib.util
import os

# Function to dynamically import modules without calling set_page_config again
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

# Dynamically import the modules
try:
    for_you_module = dynamic_import(for_you_path, "for_you")
    current_retirement_module = dynamic_import(current_retirement_path, "current_retirement")
    growth_preservation_module = dynamic_import(growth_preservation_path, "growth_preservation")
except FileNotFoundError as e:
    st.error(f"Module not found: {e}")
    st.stop()

# ✅ Updated Login Page with Correct Rerun Handling
def login():
    st.title("Login Page")
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.success("Login successful!")
            # ✅ Removed experimental rerun, replaced with a clearer state update
        else:
            st.error("Invalid credentials. Please try again.")

# ✅ Main App Functionality
def main_app():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["For You", "Current Retirement", "Growth & Preservation"])

    if page == "For You":
        for_you_module.main()
    elif page == "Current Retirement":
        current_retirement_module.main()
    elif page == "Growth & Preservation":
        growth_preservation_module.main()

# ✅ Main Function to Control App Flow
def main():
    # Ensures state control between login and the main app
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main_app()
    else:
        login()

if __name__ == "__main__":
    main()

