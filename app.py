import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model
model = genai.GenerativeModel('gemini-2.0-flash')

st.set_page_config(page_title="Octaine Chatbot", layout="wide")

st.markdown("""
    <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .user-msg, .bot-msg {
            max-width: 60%;
            padding: 10px 15px;
            border-radius: 18px;
            font-size: 16px;
            color: black;
        }
        .user-msg {
            align-self: flex-end;
            background-color: #dcf8c6;
            text-align: right;
        }
        .bot-msg {
            align-self: flex-start;
            background-color: #f1f0f0;
            text-align: left;
        }
        .input-area {
            position: fixed;
            bottom: 20px;
            width: 100%;
            display: flex;
            justify-content: center;
        }
        .stTextInput > div > div > input {
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Octaine Chatbot")

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input field
user_input = st.text_input("Ask anything", "", key="input", label_visibility="collapsed")

# Display chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for entry in st.session_state.chat_history:
    st.markdown(f'<div class="{entry["type"]}-msg">{entry["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Handle input
if user_input:
    st.session_state.chat_history.append({"type": "user", "text": user_input})
    response = model.generate_content(user_input)
    st.session_state.chat_history.append({"type": "bot", "text": response.text})
    st.experimental_rerun()
