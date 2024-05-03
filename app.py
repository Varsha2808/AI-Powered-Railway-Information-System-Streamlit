import streamlit as st
import speech_recognition as sr
import pyttsx3
from llm_util import LLM

# Initialize LLM object
llm_obj = LLM()

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

# Define TextToSpeech class for speech synthesis
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.is_engine_running = False

    def text_to_speech(self, command):
        if not self.is_engine_running:
            self.engine.startLoop(False)
            self.is_engine_running = True
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.say(command)
        self.engine.iterate()  # Process pending events

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
        tts = TextToSpeech()
        tts.text_to_speech(response)
        st.write("Query:", query)
        st.write("Response:", response)

if __name__ == "__main__":
    main()
