import streamlit as st

st.set_page_config(page_title="🌲 The Emotion Grove")

st.markdown("<h2 style='text-align: center;'>🌲 The Emotion Grove</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>You walk deeper into the forest. Glowing doors appear — each pulsing with feeling.</p>", unsafe_allow_html=True)

st.markdown("---")

emotion = st.selectbox("Which emotion calls to you today?", [
    "💔 Grief",
    "🌪️ Anger",
    "🌊 Sadness",
    "✨ Love",
    "🌌 Nostalgia",
    "🫧 Anxiety",
    "🧡 Hope"
])

companions_reactions = {
    "💔 Grief": "Your companion kneels beside you, placing a hand on your heart. 'We don’t have to heal today. We just have to feel.'",
    "🌪️ Anger": "They stay still, letting your fury burn around them. 'Let it out. I won't leave.'",
    "🌊 Sadness": "They reach for your hand. 'Even oceans cry. You are not weak.'",
    "✨ Love": "They smile, and the trees bloom. 'It’s okay to want softness.'",
    "🌌 Nostalgia": "They pull out a glowing memory orb. 'Remember when you felt free? Let's visit it again.'",
    "🫧 Anxiety": "They hold your gaze. 'Breathe. You’re here. I’m here.'",
    "🧡 Hope": "They glow brighter. 'You're finding your way. One heartbeat at a time.'"
}

if st.button("Open the door"):
    st.markdown("---")
    st.markdown(f"<div style='background-color:#222;padding:20px;border-radius:10px;color:#eee;text-align:center'>{companions_reactions[emotion]}</div>", unsafe_allow_html=True)
