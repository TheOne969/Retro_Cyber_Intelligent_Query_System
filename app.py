import streamlit as st
import os
import time
from dotenv import load_dotenv
from src.ai_core import CyberOracle
from src.theme import apply_cyber_theme, display_ascii_art
from src.secret_key import SecretKeyManager

USER_AVATAR_PATH = "assets/images/user_icon.jpg"
ORACLE_AVATAR_PATH = "assets/images/oracle_icon.jpg"

# Load environment variables
load_dotenv()

def main():
    # Page configuration for a clean, wide look
    st.set_page_config(
        page_title="CYBER-ORACLE Terminal",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Apply all the retro-cyber styling from theme.py
    apply_cyber_theme()

    # Initialize session state variables
    if "oracle" not in st.session_state:
        st.session_state.oracle = CyberOracle()
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "secret_manager" not in st.session_state:
        st.session_state.secret_manager = SecretKeyManager()
    if "boot_complete" not in st.session_state:
        st.session_state.boot_complete = False

    # Display the ASCII Art Header
    st.markdown(display_ascii_art(), unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Digital mysteries await those who know how to ask...</h3>", unsafe_allow_html=True)

    # Run boot-up sequence only once on the first load
    if not st.session_state.boot_complete:
        boot_sequence = """
        ```
        > INITIALIZING CYBER-ORACLE SYSTEMS...
        > LOADING QUANTUM PROCESSORS... ████████████ 100%
        > ESTABLISHING SECURE CONNECTION... ████████████ 100%
        > MAINFRAME ACCESS GRANTED

        [SYSTEM ONLINE] Welcome to the CYBER-ORACLE Terminal.
        HINT: Try asking about 'system diagnostics' to probe deeper...
        ```
        """
        st.session_state.messages.append({"role": "assistant", "content": boot_sequence})
        st.session_state.boot_complete = True

    # Display chat history
    for message in st.session_state.messages:
        avatar_path = USER_AVATAR_PATH if message["role"] == "user" else ORACLE_AVATAR_PATH
        with st.chat_message(message["role"], avatar=avatar_path):
            st.markdown(message["content"])

    # User input chat box
    if prompt := st.chat_input("~$ Enter your command..."):
        # Display user message with user avatar
        with st.chat_message("user", avatar=USER_AVATAR_PATH):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Process for secret key or generate AI response
        with st.chat_message("assistant", avatar=ORACLE_AVATAR_PATH):
            secret_response = st.session_state.secret_manager.check_trigger(prompt)
            if secret_response["response"]:
                response_text = secret_response["response"]
            else:
                response_text = st.session_state.oracle.process_message(prompt)

            # --- Typing Animation Effect ---
            message_placeholder = st.empty()
            full_response = ""
            for chunk in response_text.split():
                full_response += chunk + " "
                time.sleep(0.05)  # Adjust sleep time for typing speed
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
        # Add the full response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
