import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: #87CEFA;'>🌌 The Memory Pool</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #E6E6FA;'>You reach a quiet lagoon. In its mirrored surface, flickers of the past ripple — moments you forgot, but they never forgot you.</p>",
    unsafe_allow_html=True
)

st.image("https://media.giphy.com/media/8vQSQ3cNXuDGo/giphy.gif", width=400)

# Reflective prompts
st.markdown("### 🫧 Which memory surfaced first?")
st.text_area("Write the one memory that keeps floating back...", placeholder="Even if it stings a little...")

st.markdown("### 📸 If this memory had a color, what would it be?")
color = st.selectbox("Pick a color:", ["Grey", "Red", "Blue", "Gold", "Black", "Lavender", "Other"])

st.markdown("### 🌙 How old were you?")
st.number_input("Your age in that memory:", min_value=1, max_value=99, step=1)

st.markdown("---")
st.markdown("🕯️ _“You don’t have to erase the memory. Just let it rest differently inside you.”_")

if st.button("🌊 Let it drift"):
    st.success("You watch it ripple... then disappear into calm.")

# Navigation
if st.button("➡️ Continue to the Lantern"):
    st.switch_page("pages/18_🕯️_The_Woundkeepers_Lantern.py")
