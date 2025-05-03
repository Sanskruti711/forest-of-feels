import streamlit as st

def forest_home():
    st.markdown(
        "<h2 style='text-align: center; color: #90EE90;'>🌿 Welcome to the Forest of Feels 🌿</h2>",
        unsafe_allow_html=True
    )

    username = st.session_state.get("logged_in_user", "traveler")
    st.markdown(f"<p style='text-align: center;'>Hello, <strong>{username}</strong>. How are you feeling today?</p>", unsafe_allow_html=True)

    emotions = {
        "Lost 🕊️": "A quiet glade where memories whisper...",
        "Angry 🔥": "A scorched grove full of echoing roars...",
        "Hopeful 🌤️": "A sunlit stream with golden leaves...",
        "Lonely 🌑": "A moonlit clearing with shadows that listen...",
        "Numb 🌫️": "A misty path with gentle silence..."
    }

    choice = st.radio("Choose your emotional path:", list(emotions.keys()))

    if st.button("Enter this path 🌲"):
        st.session_state["emotion"] = choice
        st.session_state["page"] = "story"
        st.success(emotions[choice])

if "page" in st.session_state and st.session_state["page"] == "main":
    forest_home()
