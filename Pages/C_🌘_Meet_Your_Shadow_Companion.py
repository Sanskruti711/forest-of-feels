import streamlit as st
import random

st.set_page_config(page_title="🌘 Meet Your Shadow Companion")

st.markdown("<h2 style='text-align: center;'>🌘 Meet Your Shadow Companion</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>They've been waiting... patiently.</p>", unsafe_allow_html=True)

# Moods to choose
mood = st.radio("How are you feeling today?", ["Anxious", "Lonely", "Heartbroken", "Hopeful", "Lost"])

companion_names = {
    "Anxious": "Whisp",
    "Lonely": "Luma",
    "Heartbroken": "Ash",
    "Hopeful": "Sol",
    "Lost": "Umbra"
}

companion_traits = {
    "Whisp": "a quiet, soft-spoken being made of fog",
    "Luma": "a gentle creature that glows in the dark, always nearby",
    "Ash": "a shadowy figure with fire in their eyes, tender but fierce",
    "Sol": "a radiant, warm guide who hums soft songs to calm your heart",
    "Umbra": "a mysterious figure who never leaves your side, even in silence"
}

if st.button("Summon My Shadow Companion"):
    name = companion_names[mood]
    trait = companion_traits[name]

    st.success(f"✨ {name} has arrived.")
    st.markdown(f"""
    <div style='background-color:#1e1e1e;padding:15px;border-radius:10px;color:#ffffff'>
        <h4 style='text-align:center;'>{name}</h4>
        <p style='text-align:center;'>They are {trait}.</p>
        <p style='text-align:center;'>"{name}" looks at you and nods, understanding your feelings without words.</p>
    </div>
    """, unsafe_allow_html=True)
