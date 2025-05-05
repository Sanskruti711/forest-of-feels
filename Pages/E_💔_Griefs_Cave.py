import streamlit as st

st.set_page_config(page_title="💔 Grief's Cave")

st.markdown("<h2 style='text-align: center;'>💔 Grief's Cave</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>You enter a quiet cave. The air is still. Memories echo off the walls like wind.</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("Your companion sits beside you, their lantern casting soft light.")

# Prompt for journaling
st.text_area("What does your grief want to say today?", placeholder="Write freely. You are not being judged.")

if st.button("Let it Echo"):
    st.success("The cave holds your words in silence. Your grief is safe here.")

st.markdown("---")
st.markdown("<p style='text-align: center; color:#999'>Grief doesn’t ask to be solved. It asks to be heard.</p>", unsafe_allow_html=True)
