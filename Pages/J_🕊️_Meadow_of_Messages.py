import streamlit as st
import json
import os
import random

MESSAGES_FILE = "messages.json"

# Load or initialize messages
def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, "r") as f:
            return json.load(f)
    return []

def save_message(new_message):
    messages = load_messages()
    messages.append(new_message)
    with open(MESSAGES_FILE, "w") as f:
        json.dump(messages, f)

# UI
st.set_page_config(page_title="🕊️ Meadow of Messages", layout="centered")

st.markdown("""
    <style>
        .meadow {
            background: #f0fdf4;
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 0 15px rgba(100, 200, 150, 0.2);
        }
        .note-box {
            background: #d1fae5;
            padding: 1em;
            margin: 1em 0;
            border-left: 5px solid #34d399;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='meadow'>", unsafe_allow_html=True)

st.markdown("## 🕊️ Meadow of Messages")
st.markdown("Leave behind a whisper of kindness, truth, or strength. And receive one from someone else in return.")

user_message = st.text_area("🌼 Leave your message here:", placeholder="What would you tell someone who's lost, like you once were?")

if st.button("🌱 Send & Receive"):
    if user_message.strip():
        save_message(user_message.strip())
        st.success("Your message was planted in the meadow.")
        all_messages = load_messages()
        if len(all_messages) > 1:
            other_messages = [m for m in all_messages if m != user_message.strip()]
            received = random.choice(other_messages)
            st.markdown(f"<div class='note-box'><b>🌬️ A message found in the wind:</b><br>{received}</div>", unsafe_allow_html=True)
        else:
            st.info("You're the first to leave a note. Come back soon to see what others say.")
    else:
        st.warning("Whisper something soft before you send.")

st.markdown("</div>", unsafe_allow_html=True)
