import streamlit as st

st.set_page_config(page_title="Enter the Forest", layout="centered")

st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
        color: #FFFFFF;
        text-align: center;
    }
    .subtle {
        color: #BBBBBB;
        text-align: center;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='big-font'>🌲 You Step Into the Forest... 🌲</p>", unsafe_allow_html=True)
st.markdown("<p class='subtle'>The air shimmers with memories. Choose a feeling to guide you.</p>", unsafe_allow_html=True)

# Character introduction
st.markdown("---")
st.image("https://i.imgur.com/I3neU6U.gif", width=300)  # mysterious forest guide gif
st.markdown("#### 🧝‍♂️ A forest guide appears from the mist...")
st.markdown("*“You look like you’ve been carrying too much... Which emotion is loudest today?”*")

# Emotion choices
emotion = st.radio(
    "Choose your current feeling:",
    ["💔 Heartache", "🌪️ Overwhelmed", "🌫️ Numb", "🔥 Angry", "😞 Hopeless", "✨ Curious"],
    index=5
)

# Button to next page
if st.button("🌌 Begin Your Path"):
    st.success(f"Ah... '{emotion}' it is. Let’s walk together.")
    st.markdown("[➡️ Continue Your Journey](./2_🧠_Your_Story_Begins)")

