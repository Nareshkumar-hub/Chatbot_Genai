import streamlit as st
from langchain.chat_models import ChatGooglePalm
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("AIzaSyBc0I2Cf1FW2xEgm6aI4OX7C2zOt2iazVU")

if not api_key:
    st.error("GOOGLE_API_KEY not found! Please set it in your .env file.")
    st.stop()

palm = ChatGooglePalm(google_api_key=api_key, temperature=0.4)
I
st.title("🤖 Google Palm Chatbot Demo")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        st.markdown(f"**You:** {message.content}")
    else:
        st.markdown(f"**Bot:** {message.content}")

# User input
user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:

    user_message = HumanMessage(content=user_input)
    st.session_state.messages.append(user_message)

    response = palm.invoke(st.session_state.messages)

    st.session_state.messages.append(response)

    st.experimental_rerun()
