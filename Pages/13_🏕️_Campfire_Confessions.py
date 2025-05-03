import streamlit as st
import random

st.set_page_config(page_title="🏕️ Campfire Confessions", layout="centered")

st.markdown("""
    <style>
        .campfire {
            background: radial-gradient(ellipse at center, #2e1d10, #1b0c05);
            color: #ffd9b3;
            padding: 2em;
            border-radius: 20px;
            font-family: 'Georgia', serif;
        }
        .glow {
            animation: flicker 2s infinite;
            color: #ff9966;
        }
        @keyframes flicker {
            0% { opacity: 1; }
            50% { opacity: 0.6; }
            100% { opacity: 1; }
        }
        .story {
            margin-top: 1.5em;
            padding: 1em;
            background-color: rgba(255, 255, 255, 0.05);
            border-left: 4px solid #ffcc99;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='campfire'>", unsafe_allow_html=True)
st.markdown("## 🔥 Campfire Confessions")
st.markdown("<p class='glow'>The fire crackles. One by one, they begin to speak — the characters you've met, the parts of you you’ve hidden.</p>", unsafe_allow_html=True)

confessions = [
    "🌒 *'I still dream about the one who left without a goodbye. Sometimes I wake up angry. Sometimes I don’t want to wake up at all.'*",
    "🌘 *'When I laugh too hard, it feels like I’m borrowing joy from a future I don’t trust.'*",
    "🌗 *'I used to believe love could save anyone. Now I just hope it doesn’t ruin me.'*",
    "🌑 *'I hide my softness under sarcasm. But every joke is a scar.'*",
    "🌓 *'I once told someone I was fine. I haven’t stopped pretending since.'*"
]

st.markdown("**Tonight, someone leans in and shares...**")
st.markdown(f"<div class='story'>{random.choice(confessions)}</div>", unsafe_allow_html=True)

st.markdown("---")
user_confession = st.text_area("💬 Your turn. Whisper into the flames. What’s a truth you rarely say out loud?")

if st.button("🔥 Send it to the night"):
    st.success("Thank you. The fire holds your secret now. You’re lighter already.")

st.markdown("</div>", unsafe_allow_html=True)
