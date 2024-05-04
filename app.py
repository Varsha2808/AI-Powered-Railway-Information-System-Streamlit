import streamlit as st
import speech_recognition as sr
import pyttsx3
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
from langchain_community.callbacks import get_openai_callback

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize Streamlit app
st.title("AI-Powered Railway Information System")
st.write("Welcome aboard! Explore the future of railway assistance with our AI-powered system.")

# Define speech recognition class
class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()

    def extract_text_from_speech(self):
        with sr.Microphone() as source:
            st.write("Listening...")
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            text = self.r.recognize_google(audio)
            return text.lower()

# Define text-to-speech class
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Define LLM utility
class LLM:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        # Initialize other components as needed

    # Add other methods as needed

# Define functions to read PDF and process text

# Initialize LLM object
llm = LLM(openai_api_key)

# Speech-to-text interaction
speak_button = st.button("Speak")

if speak_button:
    stt = SpeechToText()
    query = stt.extract_text_from_speech()
    response = llm.answer_to_the_question(query)
    tts = TextToSpeech()
    tts.speak_text(response)
    st.write("Query:", query)
    st.write("Response:", response)

# Display image and other UI elements
st.image('images/steps_to_interact.png', use_column_width=True)

# Text input and response display
query = st.text_input("Enter your query:")
submit_button = st.button("Submit")

if submit_button:
    response = llm.answer_to_the_question(query)
    st.write("Response:", response)
