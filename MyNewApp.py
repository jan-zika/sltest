import streamlit as st
import pandas as pd
import numpy as np

#st.title('Jan - Welcome to Computer Vision at MDC')

# ---
import streamlit as st
import random

st.title("👑 Ruler of the Universe")

st.write("The universe awaits your decisions... or does it?")

# Cosmic decision generator
if st.button("Ask the universe"):
    responses = [
        "The stars are silent on this matter.",
        "Perhaps it is true, perhaps not.",
        "It depends on what you mean by 'real'.",
        "I cannot say. I was never there.",
        "Some claim it happened, but how can they know?"
    ]
    st.write(random.choice(responses))

# Slider of perception
perception = st.slider("How certain are you?", 0, 100, 42)
st.write(f"Your certainty is set to {perception}%. Does it help?")

# Name input — but the app remains skeptical
name = st.text_input("Who dares to rule?")
if name:
    st.write(f"Welcome, {name}... if that is your name.")

# A final cosmic “fact”
facts = [
    "Reality is often unreliable.",
    "Every answer conceals another question.",
    "Even the ruler cannot rule over uncertainty.",
    "What you perceive may only be your own invention."
]
if st.button("Reveal a truth"):
    st.info(random.choice(facts))

