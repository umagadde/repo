import streamlit as st
import requests
import json
import speech_recognition as sr
st.set_page_config(
    page_title="Speech-to-Text Transcription APP",page_icon="🔉",
    layout="wide"
    )
c30, c31, c32 = st.columns([2.5, 1, 3])
def _max_width_():
    max_width_str=f"max-width: 1200px;"
    st.markdown(
        f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
            
        }}
        </style>
        """,
            unsafe_allow_html=True
        )
_max_width_()
st.title("Speech Transcription")

st.text("")
st.markdown(
    f"""
                    The speech to text recognition is done via the [Facebook's Wav2Vec2 model.](https://huggingface.co/facebook/wav2vec2-large-960h)
                    """
)
st.text("")
with st.expander("ℹ️ - About this app", expanded=False):

    st.write(
        """     
-   u can record upto 5 sces and transcribe the speech
-   click on 'start recording' to record audio and the result will be displayed 
     """
    )

    st.markdown("")


#---------------------------------MAIN CODE------------------------------
# Define the Hugging Face API endpoint
API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"

# Create a SpeechRecognizer instance
recognizer = sr.Recognizer()

# Create the Streamlit app


# Add a button to start recording
if st.button("Start Recording"):
    # Record audio from the microphone
    with sr.Microphone() as source:
        st.write("Recording...")
        audio_data = recognizer.record(source, duration=5)  # Adjust duration as needed
    st.write("recording stopped")
    # Set the Hugging Face API token
    api_token = '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'
    headers = {"Authorization": f"Bearer {api_token}"}

    # Send a POST request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, data=audio_data.get_wav_data())

    # Parse the response JSON
    data = json.loads(response.content.decode("utf-8"))

    # Extract the transcription text from the response
    transcription = data["text"]

    # Display the transcription
    st.write("Transcription:")
    st.write(transcription)

