import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: #E6E6FA;'>🌼 The Meadow of Mercy</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #F8F8FF;'>The path opens into a field glowing with wildflowers. Each bloom is a truth you finally forgave yourself for.</p>",
    unsafe_allow_html=True
)

st.image("https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif", width=400)

st.markdown("### 🌸 What guilt or regret are you planting here?")
st.text_area("Let it turn into flowers — no judgment.", placeholder="Write it honestly... then watch it grow.")

st.markdown("### 💛 What would you say to your past self, right now?")
st.text_area("Mercy is a voice. Speak it to them...", placeholder="‘I forgive you for not knowing better.’")

if st.button("🌼 Let it grow"):
    st.success("You feel petals against your fingertips. A bloom opens with your name on it.")

st.markdown("---")
st.markdown("🌤️ _“Even shadows soften when held in love.”_")

if st.button("🚪 Walk toward the return gate..."):
    st.switch_page("pages/20_🚪_The_Return_Gate.py")
