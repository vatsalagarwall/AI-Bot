# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize the Gemini model
# model = genai.GenerativeModel('gemini-2.0-flash')

# # Streamlit app title
# st.title("🤖 Octaine Chatbot")

# # Initialize session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # User input
# user_input = st.text_input("You:", key="input")

# if st.button("Send"):
#     if user_input:
#         # Append user message
#         st.session_state.messages.append(("You", user_input))
        
#         # Generate Gemini response
#         response = model.generate_content(user_input)
#         bot_reply = response.text

#         # Append bot response
#         st.session_state.messages.append(("Octaine", bot_reply))

# # Custom CSS for alignment
# # Custom CSS for alignment and black text color
# st.markdown("""
#     <style>
#         .user-msg {
#             background-color: #DCF8C6;
#             color: black;
#             padding: 10px 15px;
#             border-radius: 15px;
#             margin: 5px;
#             max-width: 70%;
#             text-align: right;
#             align-self: flex-end;
#         }
#         .bot-msg {
#             background-color: #F1F0F0;
#             color: black;
#             padding: 10px 15px;
#             border-radius: 15px;
#             margin: 5px;
#             max-width: 70%;
#             text-align: left;
#             align-self: flex-start;
#         }
#         .msg-container {
#             display: flex;
#             flex-direction: column;
#         }
#     </style>
# """, unsafe_allow_html=True)


# # Display messages
# for sender, message in st.session_state.messages:
#     if sender == "You":
#         st.markdown(f'<div class="msg-container"><div class="user-msg">{message}</div></div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="msg-container"><div class="bot-msg"><b>{sender}:</b> {message}</div></div>', unsafe_allow_html=True)


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
st.set_page_config(page_title="Octaine Chatbot", layout="wide")
st.markdown("<h1 style='text-align: center;'>🤖 Octaine Chatbot</h1>", unsafe_allow_html=True)

# Custom CSS for alignment and fixed input at bottom
st.markdown("""
    <style>
        .user-msg {
            background-color: #DCF8C6;
            color: black;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px;
            max-width: 70%;
            align-self: flex-end;
            text-align: right;
        }
        .bot-msg {
            background-color: #F1F0F0;
            color: black;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px;
            max-width: 70%;
            align-self: flex-start;
            text-align: left;
        }
        .msg-container {
            display: flex;
            flex-direction: column;
        }
        .bottom-input {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 15px 10px;
            box-shadow: 0 -1px 3px rgba(0,0,0,0.1);
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main chat area
chat_area = st.container()

# Show messages in chronological order (top to bottom)
with chat_area:
    for sender, message in st.session_state.messages:
        if sender == "You":
            st.markdown(f'<div class="msg-container"><div class="user-msg">{message}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="msg-container"><div class="bot-msg"><b>{sender}:</b> {message}</div></div>', unsafe_allow_html=True)

# Input field at the bottom
with st.container():
    st.markdown('<div class="bottom-input">', unsafe_allow_html=True)
    user_input = st.text_input("Type your message:", key="input", label_visibility="collapsed")
    send = st.button("Send")
    st.markdown('</div>', unsafe_allow_html=True)

# Handle message sending
if send and user_input:
    st.session_state.messages.append(("You", user_input))
    response = model.generate_content(user_input)
    bot_reply = response.text
    st.session_state.messages.append(("Octaine", bot_reply))
    # sst.experimental_rerun()  # To refresh UI with new messages
