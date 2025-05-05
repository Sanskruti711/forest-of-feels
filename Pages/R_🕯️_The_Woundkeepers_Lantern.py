import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: #FFD700;'>🕯️ The Woundkeeper’s Lantern</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #FFF8DC;'>An old figure sits near the Memory Pool’s edge. They hold a lantern — it glows brighter the more truth is placed inside it.</p>",
    unsafe_allow_html=True
)

st.image("https://media.giphy.com/media/SwIMZUJE3ZPpHJBp3z/giphy.gif", width=350)

st.markdown("### 🩹 What pain are you finally ready to hand over?")
pain = st.text_area("Whisper it to the lantern...", placeholder="No one else will read this. Let it be raw.")

st.markdown("### 🌾 What did this pain teach you?")
lesson = st.text_area("Even pain had a message — what was it?", placeholder="Try to name one thing.")

if st.button("🕯️ Place it inside the lantern"):
    st.success("The lantern glows warmer. The keeper nods. You don’t feel so alone.")

st.markdown("---")
st.markdown("🕊️ _“You don’t have to carry this in the dark anymore.”_")

if st.button("🍂 Walk into the soft night..."):
    st.success("Lantern in hand, you walk lighter.")
