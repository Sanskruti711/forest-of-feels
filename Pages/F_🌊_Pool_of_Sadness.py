import streamlit as st
from PIL import Image

st.set_page_config(page_title="🌊 Pool of Sadness", layout="centered")

# Background & vibe
st.markdown(
    """
    <style>
        .sad-pool {
            background-color: #0c1a2b;
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 0 20px #4e91c7;
            color: #d6eaff;
        }
        .floating-box {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 1.5em;
            margin-top: 1em;
            border-radius: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page content
st.markdown("<div class='sad-pool'>", unsafe_allow_html=True)

st.markdown("## 🌊 The Pool of Sadness")
st.markdown("Gently step into the cool waters. Let your sadness float here — it's safe, seen, and never judged.")

# Floating sadness journal
st.markdown("#### 🫧 What emotion do you want to release into the water today?")
sadness_entry = st.text_area("Write it out, one ripple at a time...")

if st.button("🌬️ Float it into the water"):
    if sadness_entry.strip():
        st.success("Your sadness has been gently released into the pool.")
        st.balloons()
        st.markdown(
            f"<div class='floating-box'>🌫️ <i>{sadness_entry}</i></div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Let the water hold something — even just a word.")

# Breathing prompt
st.markdown("---")
st.markdown("### 🌫️ Take a moment to breathe")
st.markdown(
    """
    <div style='text-align: center; font-size: 24px; margin-top: 20px;'>
        Inhale slowly... 1... 2... 3... 4...<br>
        Hold...<br>
        Exhale gently... 1... 2... 3... 4...
    </div>
    """,
    unsafe_allow_html=True
)

# Image
try:
    img = Image.open("assets/pool.gif")
    st.image(img, use_column_width=True)
except:
    st.info("Pool gif will appear here when assets are added.")

st.markdown("</div>", unsafe_allow_html=True)
