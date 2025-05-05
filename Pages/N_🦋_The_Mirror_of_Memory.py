import streamlit as st

st.set_page_config(page_title="🦋 The Mirror of Memory", layout="centered")

st.markdown("""
    <style>
        .mirror {
            background: linear-gradient(to bottom, #1d1f20, #0e0f10);
            color: #e0e0e0;
            padding: 2em;
            border-radius: 20px;
            font-family: 'Palatino Linotype', serif;
            text-align: center;
        }
        .reflection {
            margin-top: 1.5em;
            padding: 1em;
            border-left: 4px solid #88c0d0;
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
        .blueglow {
            color: #88c0d0;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='mirror'>", unsafe_allow_html=True)
st.markdown("## 🦋 The Mirror of Memory")
st.markdown("<p class='blueglow'>You step into a silver-lit clearing. A tall mirror shimmers, showing not your face — but a memory. An old version of you.</p>", unsafe_allow_html=True)

age_reflection = st.selectbox(
    "🔍 Choose the version of yourself you wish to speak to:",
    ["Your 8-year-old self", "Your 13-year-old self", "Your 16-year-old self", "Last year's you", "The you from your hardest day"]
)

st.markdown(f"<div class='reflection'><em>You see them — {age_reflection}. Their eyes search yours.</em><br><br>💭 What do you want to say to them?</div>", unsafe_allow_html=True)

msg_to_past = st.text_area("Write your message here...")

if st.button("📨 Send the message"):
    st.success(f"Your words have reached {age_reflection}. Maybe they’ve changed something in you too.")

st.markdown("</div>", unsafe_allow_html=True)
