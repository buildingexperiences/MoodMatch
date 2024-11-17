import streamlit as st
import random

# Title of the app
st.title("Wisdom Whisper")

# User input for mood selection
mood = st.selectbox("Feeling", ["Happy", "Anxious", "Calm", "Stressed"])

# Predefined wisdom responses
wisdom_dict = {
    "Happy": [
        "Embrace this moment fully. Your joy is contagious! 😊",
        "Let your smile be the sunshine for someone else's day. 🌞",
        "Happiness is a state of being—cherish it and spread it around! 💛"
    ],
    "Anxious": [
        "Take a deep breath. Remember, it’s okay to slow down and pause. You are enough. 🌿",
        "This moment will pass—focus on what you can control and let go of the rest. 💛",
        "Close your eyes, breathe deeply, and remind yourself that you are safe. Everything is temporary. 🌱"
    ],
    "Calm": [
        "Enjoy the stillness. Let this peaceful moment fill you with gratitude. ✨",
        "Your calm is your strength. Stay present and breathe deeply. 🌼",
        "Hold onto this feeling of inner peace—it’s your true nature. 🌿"
    ],
    "Stressed": [
        "Pause and take a deep breath. You’ve got this, one step at a time. 🌱",
        "It’s okay to rest. Give yourself permission to pause and recharge. 💛",
        "Focus on the present moment. You are capable of handling whatever comes your way. 🌿"
    ]
}

# Generate a random response based on the selected mood
if st.button("Get Wisdom"):
    response = random.choice(wisdom_dict[mood])
    st.write(response)