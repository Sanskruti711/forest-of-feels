import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: #D8BFD8;'>🚪 The Return Gate</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #FAFAD2;'>You find a glowing archway of vines and starlight. This is not the end. It’s a re-entry — softer, slower, surer.</p>",
    unsafe_allow_html=True
)

st.image("https://media.giphy.com/media/f9hnhCPwAAWgn/giphy.gif", width=400)

st.markdown("### 🌿 What are you taking back with you?")
take = st.text_input("A truth, a softness, a strength...")

st.markdown("### 🪶 What are you leaving behind?")
leave = st.text_input("Let it go. You don’t need it where you’re going.")

if st.button("🚪 Step through the return gate"):
    st.success("The air hums. Something inside you feels lighter. Welcome back — not as who you were, but as who you’re becoming.")

st.markdown("---")
st.markdown("🫂 _This forest will always remember your footprints._")
st.markdown("🌙 _And when you're ready — it'll open a new path._")
