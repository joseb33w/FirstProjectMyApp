import streamlit as st

# Initialize the session state for selected topic if not already present
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = "All"

def main():
    st.subheader("Topic Channels")
    col_a, col_b, col_c = st.columns([1, 1, 1])

    # Button selection with session state management
    with col_a:
        if st.button("All"):
            st.session_state.selected_topic = "All"
    with col_b:
        if st.button("Stocks"):
            st.session_state.selected_topic = "Stocks"
    with col_c:
        if st.button("Real Estate"):
            st.session_state.selected_topic = "Real Estate"
    col_d, col_e = st.columns([1, 1])
    with col_d:
        if st.button("Bonds"):
            st.session_state.selected_topic = "Bonds"
    with col_e:
        if st.button("Mutual Funds"):
            st.session_state.selected_topic = "Mutual Funds"

    # Dynamic grid layout for posts
    st.header(f"Posts on: {st.session_state.selected_topic if st.session_state.selected_topic != 'All' else 'Explore All'}")
    col1, col2, col3 = st.columns(3)

    # Example posts based on topic
    posts = [
        {"image": "https://via.placeholder.com/150", "caption": "High Risk, High Return Stocks", "topic": "Stocks"},
        {"image": "https://via.placeholder.com/150", "caption": "Real Estate Growth Tips", "topic": "Real Estate"},
        {"image": "https://via.placeholder.com/150", "caption": "Top Bonds Investment Strategies", "topic": "Bonds"},
        {"image": "https://via.placeholder.com/150", "caption": "Why Invest in Mutual Funds", "topic": "Mutual Funds"},
        {"image": "https://via.placeholder.com/150", "caption": "Diversify Your Portfolio", "topic": "Stocks"}
    ]

    # Filter posts by topic
    filtered_posts = [p for p in posts if st.session_state.selected_topic == "All" or p["topic"] == st.session_state.selected_topic]

    # Display posts in grid layout
    for index, post in enumerate(filtered_posts):
        if index % 3 == 0:
            with col1:
                st.image(post["image"], caption=post["caption"])
        elif index % 3 == 1:
            with col2:
                st.image(post["image"], caption=post["caption"])
        else:
            with col3:
                st.image(post["image"], caption=post["caption"])

# Main function setup
if __name__ == "__main__":
    main()
