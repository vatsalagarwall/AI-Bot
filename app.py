# # import streamlit as st
# # import google.generativeai as genai
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()
# # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # model = genai.GenerativeModel('gemini-2.0-flash')

# # st.title("🤖 Octaine Chatbot")

# # user_input = st.text_input("You:", key="input")

# # if st.button("Send"):
# #     if user_input:
# #         response = model.generate_content(user_input)
# #         st.markdown("**Octaine:** " + response.text)


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

# # Initialize session state for chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # User input
# user_input = st.text_input("You:", key="input")

# # Handle user input
# if st.button("Send"):
#     if user_input:
#         # Append user message
#         st.session_state.messages.append(("You", user_input))
        
#         # Generate Gemini response
#         response = model.generate_content(user_input)
#         bot_reply = response.text
        
#         # Append bot message
#         st.session_state.messages.append(("Octaine Ai", bot_reply))

# # Display chat history
# for sender, message in st.session_state.messages:
#     st.markdown(f"**{sender}:** {message}")


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

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        # Append user message
        st.session_state.messages.append(("You", user_input))
        
        # Generate Gemini response
        response = model.generate_content(user_input)
        bot_reply = response.text

        # Append bot response
        st.session_state.messages.append(("Octaine", bot_reply))

# Custom CSS for alignment
st.markdown("""
    <style>
        .user-msg {
            background-color: #DCF8C6;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px;
            max-width: 70%;
            text-align: right;
            align-self: flex-end;
        }
        .bot-msg {
            background-color: #F1F0F0;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px;
            max-width: 70%;
            text-align: left;
            align-self: flex-start;
        }
        .msg-container {
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# Display messages
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f'<div class="msg-container"><div class="user-msg">{message}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="msg-container"><div class="bot-msg"><b>{sender}:</b> {message}</div></div>', unsafe_allow_html=True)
