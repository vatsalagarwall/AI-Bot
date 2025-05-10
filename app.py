import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.0-flash')

st.title("🤖 Octaine Chatbot")

user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        response = model.generate_content(user_input)
        st.markdown("**Octaine:** " + response.text)
