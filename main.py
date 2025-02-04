import streamlit as st
import subprocess
import re

# Streamlit page configuration
st.set_page_config(page_title="DeepSeek Chat", layout="centered")
st.markdown("""
    <style>
        body { background-color: black; color: white; }
        .stTextInput > div > div > input {
            background-color: white; color: black; font-size: 18px; text-align: center;
            padding: 15px; border-radius: 10px;
        }
        .stButton button {
            background-color: black; color: white; border: 1px solid white; 
            padding: 10px 20px; border-radius: 8px;
        }
        .stMarkdown { font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 DeepSeek Chat Interface")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to interact with DeepSeek via Ollama
def query_deepseek(prompt):
    try:
        process = subprocess.Popen(
            ["ollama", "run", "deepseek-r1:32b"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate(prompt)

        # Clean ANSI escape codes from error output
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        clean_error = ansi_escape.sub('', error)

        if clean_error.strip():
            return f"❗ Error: {clean_error.strip()}"
        return output.strip()

    except Exception as e:
        return f"🚨 Exception: {str(e)}"

# Chat UI
with st.container():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            if "```" in msg["content"]:  # Check for code response
                st.code(msg["content"].replace("```", ""))
            else:
                st.markdown(f"**DeepSeek:** {msg['content']}")

# Input area
user_input = st.text_input("💬 Enter your prompt:", key="user_input", placeholder="Type your message here...")

# Handle Enter key press
if user_input and st.session_state.get("enter_pressed", False):
    st.session_state.enter_pressed = False  # Reset flag
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = query_deepseek(user_input)
    st.session_state.messages.append({"role": "deepseek", "content": response})
    st.rerun()

# Send button
if st.button("Send"):
    st.session_state.enter_pressed = True
    st.rerun()
