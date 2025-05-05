import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: #D4AF37;'>🎭 The Mask Tree</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #F0E68C;'>You find a towering tree draped in masks — wooden, porcelain, glittering, broken. Each one once belonged to someone trying to be 'enough'.</p>",
    unsafe_allow_html=True
)

st.image("https://media.giphy.com/media/JTjSlqiz63j4VTHMUA/giphy.gif", width=350)

# Emotional prompt
st.markdown("### 🕊️ Which mask have you worn the longest?")
mask_type = st.selectbox(
    "Choose the mask that feels most familiar...",
    [
        "The Achiever – 'I’m only worthy if I succeed.'",
        "The Caretaker – 'If I fix others, I matter.'",
        "The Clown – 'If I keep it light, no one sees my pain.'",
        "The Rebel – 'If I push back, no one controls me.'",
        "The Perfect One – 'Flaws aren’t allowed.'",
        "The Ghost – 'If I disappear, I won’t get hurt.'"
    ]
)

st.text_area("Where did you learn to wear this mask?", placeholder="Write freely...")

st.markdown("### 🔥 Are you ready to burn this mask?")
if st.button("🔥 Yes. Let it burn."):
    st.success("The flames dance — but you feel lighter. More *you*.")

st.markdown("---")
st.markdown("🕯️ **A whisper from the tree:** _“Every time you hid, you were just trying to survive. But now... maybe you’re ready to be seen.”_")

# Navigation
if st.button("🍃 Walk away, unmasked"):
    st.success("Bare-faced and brave, you walk into the wind.")
