import streamlit as st
from groq import Groq
import os

# Page configuration
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="wide")

# --- CUSTOM CSS FOR CENTERING ---
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        color: white;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    /* This centers the specific block */
    div.stHeading h1 {
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Perfectly centered title
st.markdown("<h1 class='centered-title'>Groq-Powered Assistant</h1>", unsafe_allow_html=True)

# Fetch API Key
API_KEY = os.getenv('GROQ_API_KEY')

if not API_KEY:
    st.error("API Key not found! Please add 'GROQ_API_KEY' to Settings > Secrets.")
    st.stop()

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    model_option = st.selectbox(
        "Model Selector:",
        ("llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768")
    )
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Use st.code for assistant to show the copy button
        if message["role"] == "assistant":
            st.code(message["content"], language=None)
        else:
            st.markdown(message["content"])

# Chat logic
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        client = Groq(api_key=API_KEY)
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            completion = client.chat.completions.create(
                model=model_option,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            )
            for chunk in completion:
                content = chunk.choices[0].delta.content
                if content:
                    full_response += content
                    response_placeholder.markdown(full_response + "▌")
            
            # RE-RENDER WITH COPY BUTTON
            # Wrapping the final response in st.code creates the copy button automatically
            response_placeholder.code(full_response, language=None)
            
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    except Exception as e:
        st.error(f"Error: {str(e)}")
