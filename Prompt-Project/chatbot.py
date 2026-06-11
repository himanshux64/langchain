from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st
import os

# ---------------------------------------------------
# Page Config
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Load Environment Variables

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")


# Sidebar

with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------------------------
# Model
# ---------------------------------------------------
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  #  through Api
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0.3
)

model = ChatHuggingFace(llm=llm)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("🤖 AI Chatbot")
st.caption("Powered by Llama 3.1")

# ---------------------------------------------------
# Display Chat History
# ---------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
prompt = st.chat_input("Type your message...")

if prompt:

    # User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = model.invoke(prompt)

            answer = response.content

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )