import os
import streamlit as st
import speech_recognition as sr
import pyttsx3
from llm_util import LLM
# from tts_stt import TextToSpeech  # Import the TextToSpeech class
from tts_stt import text_to_speech  # Import the text_to_speech function


# Initialize LLM object
llm_obj = LLM()

# Get OpenAI API key from environment variables
openai_api_key = os.environ.get('OPENAI_API_KEY')

# Define SpeechToText class for speech recognition
class SpeechToText:
    def __init__(self, lang='en'):
        self.r = sr.Recognizer()
        self.language = lang

    def extract_text_from_speech(self):
        with sr.Microphone() as source2:
            st.write("Listening....")
            self.r.adjust_for_ambient_noise(source2, duration=0.3)
            audio2 = self.r.listen(source2)
            MyText = self.r.recognize_google(audio2)
            MyText = MyText.lower()
            return MyText

# Define Streamlit UI
def main():
    st.title("AI-Powered Railway Information System")
    st.write("Welcome aboard! Explore the future of railway assistance with our AI-powered system.")

    # Display image
    st.image('images/steps_to_interact.png', use_column_width=True)

    # Define user input section
    query = st.text_input("Enter your query:")
    submit_button = st.button("Submit")

    if submit_button:
        response = llm_obj.answer_to_the_question(query)
        st.write("Response:", response)

    # Speech-to-text functionality
    st.write("Or, if you prefer, use the Speak button for voice interaction:")
    speak_button = st.button("Speak")

    if speak_button:
        stt = SpeechToText()
        query = stt.extract_text_from_speech()
        response = llm_obj.answer_to_the_question(query)
        
        # Convert response to speech
        tts = TextToSpeech()
        tts.text_to_speech(response)  # Convert response to speech
        st.write("Query:", query)
        st.write("Response:", response)

if __name__ == "__main__":
    main()
