import streamlit as st

with open("alarm.wav", "rb") as f:
    audio_bytes = f.read()

st.audio(audio_bytes, format="audio/wav")
st.write("If you hear the alarm sound, audio playback works.")
