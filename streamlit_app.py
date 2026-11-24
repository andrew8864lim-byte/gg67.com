
import streamlit as st
import pandas as pd
import random

# Page Configuration
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Main Title
st.title("🚀 Welcome to My App!")
st.subheader("A Simple Interactive Web Application")
st.write("Explore my application and try out the interactive features!")

st.divider()

# Sidebar
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Choose a page:",
    ["Home", "About Me", "Fun Interaction", "Data Dashboard"]
)

# Home Page
if menu == "Home":

    st.header("🏠 Home Page")
    st.success("Welcome! You have successfully opened my Streamlit App.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Users", "1,250", "+50")

    with col2:
        st.metric("Projects", "15", "+3")

    with col3:
        st.metric("Rating", "4.8 ⭐", "+0.2")

    st.divider()

    st.subheader("👋 Say Hello!")

    name = st.text_input("What is your name?", placeholder="Enter your name here...")

    if st.button("Greet Me! 👋"):
        if name:
            st.success(f"Hello, {name}! Welcome to my application!")
            st.balloons()
        else:
            st.warning("Please enter your name first!")

# About Me Page
elif menu == "About Me":

    st.header("🙋 About Me")

    st.write("""
    Hello! Welcome to my personal application.

    I am a Computer Science student who enjoys:
    """)

    st.markdown("""
    - 💻 Programming
    - 🤖 Artificial Intelligence
    - 🏸 Badminton
    - 🏀 Basketball
    """)

    st.info("This application is developed using Python and Streamlit.")

# Fun Interaction Page
elif menu == "Fun Interaction":

    st.header("🎮 Fun Interaction")

    st.write("Let's try some interactive features!")

    # Button
    if st.button("Click Me! 🎉"):
        st.success("Hello, my app! 6767676767")
        st.balloons()

    st.divider()

    # Slider
    age = st.slider("Select your age:", 1, 100, 21)
    st.write(f"Your selected age is **{age}**.")

    # Rating
    rating = st.slider("Rate this application ⭐", 1, 10, 5)
    st.write(f"You rated this app: {rating}/10")

    st.divider()

    # Random Number
    if st.button("Generate Random Number 🎲"):
        number = random.randint(1, 100)
        st.info(f"Your lucky number is: {number}")

# Data Dashboard Page
elif menu == "Data Dashboard":

    st.header("📊 Data Dashboard")

    data = pd.DataFrame({
        "Month": ["January", "February", "March", "April", "May"],
        "Visitors": [120, 200, 180, 300, 450]
    })

    st.subheader("Monthly Visitors")
    st.bar_chart(data.set_index("Month"))

    st.subheader("Visitor Data")
    st.dataframe(data, use_container_width=True)

# Footer
st.divider()
st.caption("© 2026 My Streamlit App | Developed with Python ❤️")
