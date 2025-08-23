import streamlit as st
import os
from dotenv import load_dotenv
from src.ai_core import CyberOracle
from src.theme import apply_cyber_theme
from src.secret_key import SecretKeyManager

# Load environment variables
load_dotenv()

def main():
    # Apply retro-cyber theme
    apply_cyber_theme()
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "secret_manager" not in st.session_state:
        st.session_state.secret_manager = SecretKeyManager()
    if "oracle" not in st.session_state:
        st.session_state.oracle = CyberOracle()
    
    # Header with ASCII art
    st.markdown("# 🌐 CYBER-ORACLE TERMINAL")
    st.markdown("*Digital mysteries await those who know how to ask...*")
    
    # Chat interface
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Enter command..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            response = st.session_state.oracle.process_message(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
