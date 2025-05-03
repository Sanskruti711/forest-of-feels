import streamlit as st
from PIL import Image

st.set_page_config(page_title="🌌 Nostalgia Lantern Field", layout="centered")

# Page aesthetics
st.markdown("""
    <style>
        .lantern-bg {
            background-color: #1a132f;
            color: #e8d6ff;
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 0 25px #6f42c1;
        }
        .lantern {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 1.2em;
            margin-top: 1.2em;
            border-radius: 12px;
            border: 1px solid #ffffff10;
        }
    </style>
""", unsafe_allow_html=True)

# Container
st.markdown("<div class='lantern-bg'>", unsafe_allow_html=True)

st.markdown("## 🌌 Nostalgia Lantern Field")
st.markdown("Write a memory into the lantern. Let it float. This field keeps your stories glowing in silence.")

# User input
memory = st.text_area("🎈 What memory do you want to release into the night sky?")

if st.button("✨ Release the Lantern"):
    if memory.strip():
        st.success("Your memory lantern has been released into the stars ✨")
        st.markdown(
            f"<div class='lantern'>🕯️ <i>{memory}</i></div>",
            unsafe_allow_html=True
        )
        st.snow()
    else:
        st.warning("Your lantern needs a memory to float.")

# Optional: calming prompt
st.markdown("---")
st.markdown("#### 🌙 Close your eyes for a moment...")
st.markdown(
    """
    <div style='text-align: center; font-size: 20px;'>
        Imagine your lantern floating into the sky...<br>
        Slowly rising with all the warmth you gave it.<br>
        Your memory is safe here.
    </div>
    """,
    unsafe_allow_html=True
)

# Visual
try:
    img = Image.open("assets/lantern.gif")
    st.image(img, use_column_width=True)
except:
    st.info("Lantern field gif will appear here when assets are added.")

st.markdown("</div>", unsafe_allow_html=True)
