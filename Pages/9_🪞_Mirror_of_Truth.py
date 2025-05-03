import streamlit as st
import datetime

st.set_page_config(page_title="🪞 Mirror of Truth", layout="centered")

st.markdown("""
    <style>
        .mirror-container {
            background-color: #111111;
            color: #e0e0e0;
            padding: 2em;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }
        .truth-box {
            background-color: #1d1d1d;
            padding: 1em;
            margin-top: 1em;
            border-left: 4px solid #7dd3fc;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='mirror-container'>", unsafe_allow_html=True)

st.markdown("## 🪞 Mirror of Truth")
st.markdown("Look into this space as if you’re looking at yourself. These reflections are for your eyes only.")

questions = [
    "✨ What part of yourself have you been avoiding?",
    "🌑 What emotion keeps returning no matter how much you ignore it?",
    "🌀 If your shadow could speak, what would it beg you to feel?",
    "🔥 What truth scares you, but also frees you?"
]

responses = {}

for i, q in enumerate(questions):
    response = st.text_area(f"**{q}**", key=f"q{i}")
    if response.strip():
        responses[q] = response.strip()

if st.button("🌫️ Reflect into the mirror"):
    if responses:
        st.success("Reflections accepted.")
        for q, a in responses.items():
            st.markdown(f"<div class='truth-box'><b>{q}</b><br>{a}</div>", unsafe_allow_html=True)
    else:
        st.warning("Gently answer at least one question before reflecting.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #999;'>You can return to this mirror whenever you feel ready to see more.</div>",
    unsafe_allow_html=True
)
