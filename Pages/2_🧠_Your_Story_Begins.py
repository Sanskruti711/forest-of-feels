import streamlit as st

st.set_page_config(page_title="Your Story Begins", layout="centered")

# Background + narration
st.markdown("""
    <style>
    .forest-bg {
        background-color: #0b1d26;
        padding: 20px;
        border-radius: 10px;
        color: #ffffff;
        font-family: 'Georgia', serif;
        line-height: 1.6;
    }
    .emotion {
        color: #FFD1DC;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='forest-bg'>", unsafe_allow_html=True)

st.markdown("## 🌌 The Forest Responds...")

st.markdown("""
As you take your first steps, the leaves whisper your name.  
Your chosen emotion... it begins to shape the path ahead.  

A soft mist coils at your feet. In the distance, you hear:

*“What you feel... becomes the world you walk in.”*

The forest guide turns to you, cloak shimmering with stardust.
""")

# Retrieve selected emotion from session (if we want to later)
emotion = st.radio(
    "What emotion did you pick in the forest?",
    ["💔 Heartache", "🌪️ Overwhelmed", "🌫️ Numb", "🔥 Angry", "😞 Hopeless", "✨ Curious"],
    index=0
)

# Begin first path scene
if st.button("🚪 Step Deeper"):
    if emotion == "💔 Heartache":
        st.markdown("The trees seem to sigh with you. A red scarf flutters from a broken branch. Someone was here once... and left pieces behind.")
    elif emotion == "🌪️ Overwhelmed":
        st.markdown("Branches swirl, paths twist, everything feels *too much*. But then — a single bluebird lands on your shoulder, steady and calm.")
    elif emotion == "🌫️ Numb":
        st.markdown("It’s quiet. Too quiet. You can’t even hear your own thoughts. But the guide simply offers you a lantern. *“Light comes when you carry it.”*")
    elif emotion == "🔥 Angry":
        st.markdown("The air crackles. Flames flicker across the bark. The guide doesn’t flinch. *“Let’s walk until it burns itself out.”*")
    elif emotion == "😞 Hopeless":
        st.markdown("You collapse onto a mossy rock. The guide kneels beside you, eyes soft. *“If you don’t walk, I’ll wait here with you.”*")
    else:
        st.markdown("The trees part slightly. You glimpse a glowing path. Something is calling you forward, curious and wild. A new story...")

    st.markdown("[➡️ Go to the Next Chapter](./3_🎭_Meet_Your_Inner_Shadows)")

st.markdown("</div>", unsafe_allow_html=True)
