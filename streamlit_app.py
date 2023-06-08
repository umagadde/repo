import streamlit as st
import requests
import json
import speech_recognition as sr

# Define the Hugging Face API endpoint
API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"

# Create a SpeechRecognizer instance
recognizer = sr.Recognizer()

# Create the Streamlit app
st.title("Speech Transcription")

# Add a button to start recording
if st.button("Start Recording"):
    # Record audio from the microphone
    with sr.Microphone() as source:
        st.write("Recording...")
        audio_data = recognizer.record(source, duration=5)  # Adjust duration as needed

    # Set the Hugging Face API token
    api_token = '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'
    headers = {"Authorization": f"Bearer {api_token}"}

    # Send a POST request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, data=audio_data.get_wav_data())

    # Parse the response JSON
    data = json.loads(response.content.decode("utf-8"))

    # Extract the transcription text from the response
    transcription = data["result"]

    # Display the transcription
    st.write("Transcription:")
    st.write(transcription)
