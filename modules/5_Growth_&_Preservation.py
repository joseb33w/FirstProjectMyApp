import streamlit as st

# Simple Instagram-Style Explore Page
def main():
    st.title("Explore Page")

    # Search bar for filtering content
    search_query = st.text_input("Search for posts or topics...")

    # Topic Channels
    st.sidebar.title("Topic Channels")
    topics = ["All", "Stocks", "Real Estate", "Bonds", "Mutual Funds"]
    selected_topic = st.sidebar.radio("Select a topic", topics)

    # Dynamic grid layout for posts
    st.header(f"Posts on: {selected_topic if selected_topic != 'All' else 'Explore All'}")
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
    filtered_posts = [p for p in posts if selected_topic == "All" or p["topic"] == selected_topic]

    # Display posts in grid
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

if __name__ == "__main__":
    main()
