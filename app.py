# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel('gemini-2.0-flash')

# st.title("🤖 Octaine Chatbot")

# user_input = st.text_input("You:", key="input")

# if st.button("Send"):
#     if user_input:
#         response = model.generate_content(user_input)
#         st.markdown("**Octaine:** " + response.text)


import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Streamlit app title
st.title("🤖 Octaine Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", key="input")

# Handle user input
if st.button("Send"):
    if user_input:
        # Append user message
        st.session_state.messages.append(("You", user_input))
        
        # Generate Gemini response
        response = model.generate_content(user_input)
        bot_reply = response.text
        
        # Append bot message
        st.session_state.messages.append(("Octaine", bot_reply))

# Display chat history
for sender, message in st.session_state.messages:
    st.markdown(f"**{sender}:** {message}")
