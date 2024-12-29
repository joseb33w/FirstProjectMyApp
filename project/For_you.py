import streamlit as st

# Set page configuration without sidebar
st.set_page_config(page_title="For You", page_icon="💰", layout="wide")

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "For You"

# Function to switch pages
def set_page(page):
    st.session_state.current_page = page

# Custom CSS for the bottom navigation bar
st.markdown(
    """
    <style>
    .bottom-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8f9fa;
        text-align: center;
        padding: 10px 0;
        border-top: 1px solid #dee2e6;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        z-index: 1000;
    }
    .bottom-bar button {
        margin: 0 15px;
        background: none;
        border: none;
        font-size: 1rem;
        font-weight: bold;
        color: #007bff;
        cursor: pointer;
    }
    .bottom-bar button:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation bar
st.markdown(
    """
    <div class="bottom-bar">
        <button onclick="window.location.reload()" onClick="set_page('For You')">For You</button>
        <button onclick="window.location.reload()" onClick="set_page('Retirement Calculator')">Retirement Calculator</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main content based on the active page
if st.session_state.current_page == "For You":
    st.title("For You")
    st.write("This is the For You page. Display your savings visualization here.")
elif st.session_state.current_page == "Retirement Calculator":
    st.title("Retirement Calculator")
    st.write("This is the Retirement Calculator page. Provide input fields for calculations here.")
