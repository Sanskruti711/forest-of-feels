import streamlit as st
from PIL import Image
import datetime

st.set_page_config(page_title="🕯️ Shadow Confession Temple", layout="centered")

# Page style
st.markdown("""
    <style>
        .temple-bg {
            background-color: #0f0a0a;
            color: #f4f0ec;
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 0 40px #a68f7c50;
        }
        .candle-box {
            background-color: #1e1616;
            padding: 1em;
            margin-top: 1.2em;
            border-left: 5px solid #d4af37;
            border-radius: 10px;
            font-style: italic;
        }
    </style>
""", unsafe_allow_html=True)

# Container
st.markdown("<div class='temple-bg'>", unsafe_allow_html=True)

st.markdown("## 🕯️ Shadow Confession Temple")
st.markdown("This is a sacred space. No names. No judgement. Just truth, whispered into the candlelight.")

# Input area
confession = st.text_area("🖤 What’s something you've never admitted before?")

if st.button("Release it into the shadows"):
    if confession.strip():
        st.success("Your shadow has been heard by the flame.")
        st.markdown(
            f"<div class='candle-box'>🕯️ {confession}<br><span style='font-size: 12px; color: #aaa;'>— {datetime.datetime.now().strftime('%B %d, %Y • %H:%M')}</span></div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Speak your shadow before releasing it.")

# Image visual
try:
    img = Image.open("assets/confession-temple.gif")
    st.image(img, use_column_width=True)
except:
    st.info("Confession temple gif will appear here when assets are added.")

st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>You may return to this temple anytime. The shadows will always listen.</div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
