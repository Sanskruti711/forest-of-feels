import streamlit as st
import random

st.set_page_config(page_title="🌌 Night of Memory Stars", layout="centered")

# Styling for star sky
st.markdown("""
    <style>
        .sky {
            background: radial-gradient(ellipse at bottom, #0d1b2a 0%, #000000 100%);
            color: white;
            padding: 2em;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 0 20px rgba(255,255,255,0.1);
        }
        .message {
            font-size: 18px;
            color: #d0f0ff;
            padding-top: 1em;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='sky'>", unsafe_allow_html=True)

st.markdown("## 🌌 Night of Memory Stars")
st.markdown("Pick a memory you’re ready to release — one that’s weighed heavy, or bloomed deep. Let it rise like a star.")

# Memory selection
memory_type = st.radio("What kind of memory is it?", ["🌧️ A painful one", "🌸 A beautiful one", "🌗 A mix of both"])
memory_text = st.text_area("Write about your memory here...", placeholder="It still lingers because...")

if st.button("✨ Release to the stars"):
    if memory_text.strip():
        st.balloons()
        st.success("Your memory is now part of the night sky.")
        
        messages = [
            "✨ It was real. It mattered. And now, it can float freely.",
            "🌟 You carry the lesson. The weight can stay behind.",
            "💫 It shaped you. But it no longer defines you.",
            "🌠 The stars have heard you. Now exhale."
        ]
        st.markdown(f"<div class='message'>{random.choice(messages)}</div>", unsafe_allow_html=True)
    else:
        st.warning("Write something before you release it.")

st.markdown("</div>", unsafe_allow_html=True)
