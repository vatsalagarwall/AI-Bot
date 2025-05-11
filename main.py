import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the model
genai.configure(api_key=api_key)

def chat_with_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text

print("Hello, I am a Chatbox! Ask anything!")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    reply = chat_with_gemini(prompt)
    print("Gemini:", reply, "\n")

 