
import streamlit as st
import random

st.set_page_config(
    page_title="67 BRAINROT",
    page_icon="🗿",
    layout="centered"
)

# CSS styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1a0033, #330066, #000033);
    color: white;
}
h1 {
    text-align: center;
    color: #FFD700 !important;
    font-size: 55px !important;
}
.big67 {
    text-align: center;
    font-size: 100px;
    font-weight: bold;
    color: #ff00ff;
    text-shadow: 0 0 20px cyan;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🗿 67 BRAINROT 🗿")
st.markdown("<div class='big67'>67</div>", unsafe_allow_html=True)

st.subheader("Welcome to the 67 Dimension 💀")
st.write("⚠️ Warning: This app may cause permanent brain damage.")

# Session state
if "count" not in st.session_state:
    st.session_state.count = 0

quotes = [
    "67 IS NOT A NUMBER. IT'S A LIFESTYLE 🗿",
    "Bro is NOT escaping the 67 allegations 💀",
    "SIX SEVENNNNN 🗣️🔥",
    "67% brain cells remaining...",
    "When life gives you lemons, calculate 67.",
    "You are not ready for this level of 67.",
    "67 RIZZ UNLOCKED 😭",
    "WHO LET BRO COOK 💀",
    "67 SIGMA MODE ACTIVATED 🗿"
]

# Random quote
if st.button("🎲 RELEASE THE 67"):
    st.session_state.count += 1
    st.success(random.choice(quotes))
    st.balloons()

# Counter
st.divider()
st.subheader("📈 67 POWER COUNTER")

st.metric("Total 67 Energy", st.session_state.count * 67)

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ MORE 67"):
        st.session_state.count += 1

with col2:
    if st.button("💀 RESET"):
        st.session_state.count = 0

st.write(f"### Current Level: {st.session_state.count}")

# Challenge
st.divider()
st.subheader("🔥 THE ULTIMATE 67 TEST")

answer = st.text_input("What is 6 + 7?")

if st.button("SUBMIT ANSWER"):
    if answer == "13":
        st.error("WRONG. THE ANSWER IS 67. 🗿")
        st.balloons()
    elif answer == "67":
        st.success("YOU ARE THE CHOSEN ONE. 🗣️🔥")
        st.snow()
    else:
        st.warning("Bro failed the 67 test 💀")

# Final boss
st.divider()

if st.button("☢️ SUMMON THE FINAL BOSS"):
    st.markdown("# SIX SEVENNNNNNNNN 🗣️🔥🔥🔥")
    st.balloons()
    st.snow()

st.caption("© 2026 67 University | Powered by Brainrot Technology")
