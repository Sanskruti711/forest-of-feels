import streamlit as st

st.set_page_config(page_title="Enter the Forest", layout="centered")

st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
        color: #FFFFFF;
        text-align: center;
    }
    .subtle {
        color: #BBBBBB;
        text-align: center;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='big-font'>🌲 You Step Into the Forest... 🌲</p>", unsafe_allow_html=True)
st.markdown("<p class='subtle'>The air shimmers with memories. Choose a feeling to guide you.</p>", unsafe_allow_html=True)

# Character introduction
st.markdown("---")
st.image("https://i.imgur.com/I3neU6U.gif", width=300)  # mysterious forest guide gif
st.markdown("#### 🧝‍♂️ A forest guide appears from the mist...")
st.markdown("*“You look like you’ve been carrying too much... Which emotion is loudest today?”*")

# Emotion choices
emotion = st.radio(
    "Choose your current feeling:",
    ["💔 Heartache", "🌪️ Overwhelmed", "🌫️ Numb", "🔥 Angry", "😞 Hopeless", "✨ Curious"],
    index=5
)

# Button to next page
if st.button("🌌 Begin Your Path"):
    st.switch_page("Pages/B_🫧_Your_Story_Begins.py")
    import streamlit as st

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login Page")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    st.switch_page("Pages/B_🫧_Your_Story_Begins.py")
    if st.button("Login"):
        if email == "user@example.com" and password == "password123":
            st.session_state.logged_in = True
            st.success("Logged in!")
            st.switch_page("Pages/B_🫧_Your_Story_Begins.py")  # <-- next page
        else:
            st.error("Wrong email or password!")

if not st.session_state.logged_in:
    login()
else:
    st.switch_page("Pages/B_🫧_Your_Story_Begins.py")

    st.success(f"Ah... '{emotion}' it is. Let’s walk together.")
    st.markdown("[➡️ Continue Your Journey](./B_🧠_Your_Story_Begins)")

