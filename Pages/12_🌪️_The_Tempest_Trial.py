import streamlit as st
import random

st.set_page_config(page_title="🌪️ The Tempest Trial", layout="centered")

st.markdown("""
    <style>
        .storm {
            background: linear-gradient(to top, #1c1c1c, #3a3a3a);
            color: white;
            padding: 2em;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }
        .outcome {
            background-color: #444;
            padding: 1em;
            border-radius: 10px;
            margin-top: 1em;
            color: #d0f0ff;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='storm'>", unsafe_allow_html=True)
st.markdown("## 🌪️ The Tempest Trial")
st.markdown("You stand at the center of a storm. Voices rise, shadows swirl. You're not sure if it’s thunder or your thoughts.")

st.markdown("---")

# Trigger scenarios
scenarios = {
    "Someone you love is withdrawing from you.": [
        "You confront them directly, voice shaking.",
        "You write it down, but never send it.",
        "You pretend you're fine, hoping it passes."
    ],
    "You failed at something you cared deeply about.": [
        "You vent in your journal until the ink bleeds.",
        "You sign up again, determined to try.",
        "You disappear for a while."
    ],
    "You feel invisible in a room full of people.": [
        "You make a joke. Loud. Too loud.",
        "You slip outside to breathe under the sky.",
        "You imagine a version of you they *would* see."
    ]
}

chosen_trigger = random.choice(list(scenarios.keys()))
st.markdown(f"**🌩️ Scenario:** *{chosen_trigger}*")

options = scenarios[chosen_trigger]
choice = st.radio("How do you respond?", options)

# After making a choice
if st.button("🌫️ Face It"):
    outcomes = {
        0: "🖤 That took courage. Even if it wasn’t graceful, it was *honest*.",
        1: "⚡ That was growth. Silent, perhaps, but fierce.",
        2: "🌑 That was survival. And sometimes, that’s more than enough."
    }
    index = options.index(choice)
    st.markdown(f"<div class='outcome'>{outcomes[index]}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
