import streamlit as st
import random

st.markdown(
    "<h1 style='text-align: center; color: #FFAE42;'>🦊 The Trickster’s Trail</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #FFFFFF;'>You've stumbled upon a winding trail where reality bends, riddles hide truths, and the only way forward is to play.</p>",
    unsafe_allow_html=True
)

st.image("https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif", width=300)

# Trickster greeting
trickster_quotes = [
    "“Truth? A charming myth.”",
    "“You’re not stuck. You’re just dancing with your own shadow.”",
    "“Who were you before the world told you who to be?”",
    "“I’m not here to solve — I’m here to stir.”"
]
st.info(random.choice(trickster_quotes))

# Riddle challenge
riddle, answer = random.choice([
    ("I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?", "Echo"),
    ("The more you take, the more you leave behind. What am I?", "Footsteps"),
    ("What disappears as soon as you say its name?", "Silence")
])

with st.expander("🧠 Riddle me this..."):
    st.markdown(f"**{riddle}**")
    user_guess = st.text_input("Your guess?")
    if user_guess:
        if user_guess.strip().lower() == answer.lower():
            st.success("🧩 Clever one, you got it right.")
        else:
            st.error("❌ Not quite — but the trickster is pleased by your effort.")

# Reflection prompt
st.markdown("---")
st.markdown("🪞 **A trick question for your heart:**")
st.text_area(
    "What’s something you once believed about yourself that turned out to be untrue?",
    placeholder="Maybe I believed I had to be the strong one all the time..."
)

# Navigation
st.markdown("---")
if st.button("🍂 Follow the fox deeper into the forest"):
    st.success("The trail fades... but something new glows ahead.")
