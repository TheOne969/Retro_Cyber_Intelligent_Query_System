import streamlit as st

def apply_cyber_theme():
    """Applies the full retro-cyber theme with fonts, colors, and effects."""
    st.markdown("""
    <style>
    /* Import retro-cyber font */
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    /* Global dark theme with neon green text */
    .main {
        background: #000000;
        color: #00ff00;
        font-family: 'Share Tech Mono', 'Courier New', monospace;
    }

    /* Fix for horizontal scrolling & word wrapping */
    .stChatMessage {
        max-width: 100% !important;
        overflow-x: auto !important;
        word-wrap: break-word !important;
        white-space: pre-wrap !important;
    }
    .stChatMessage pre, .stChatMessage code {
        white-space: pre-wrap !important;
        word-wrap: break-word !important;
        overflow-x: auto !important;
        max-width: 100% !important;
    }

    /* Terminal-style input box */
    .stTextInput > div > div > input {
        background: rgba(0, 20, 0, 0.8);
        color: #00ff00;
        border: 2px solid #00ff00;
        border-radius: 0;
        font-family: 'Share Tech Mono', monospace;
        box-shadow: 0 0 10px #00ff00;
    }
    .stTextInput > div > div > input:focus {
        border-color: #00ffff;
        box-shadow: 0 0 20px #00ffff;
    }

    /* Header with glitch/flicker effect */
    h1 {
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
        font-family: 'Share Tech Mono', monospace;
        text-align: center;
        animation: flicker 2s infinite alternate;
    }

    @keyframes flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
            text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
        }
        20%, 24%, 55% {
            text-shadow: none;
        }
    }

    /* Scanlines overlay effect */
    .main::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: repeating-linear-gradient(
            0deg,
            transparent,
            transparent 2px,
            rgba(0, 255, 0, 0.05) 2px,
            rgba(0, 255, 0, 0.05) 4px
        );
        pointer-events: none;
        z-index: 1000;
    }
                


    /* This rule specifically targets the paragraph text inside both user and assistant messages */
    [data-testid="chat-message-container"] .st-emotion-cache-1f1dhpb p {
        color: #00ff00;
    }

    /* This targets the user message specifically to ensure it's distinct */
    [data-testid="chat-message-container"] [data-testid="stChatMessageContent"] p {
        color: #ffffff; /* Or a light blue like #87ceeb for the user */
    }

    /* This specifically targets the assistant's response to make it green */
    [data-testid="chat-message-container"] [data-testid="stChatMessageContent"] p {
        color: #00ff00;
    }

    </style>
    """, unsafe_allow_html=True)

def display_ascii_art():
    """Generates the ASCII art header."""
    ascii_art = """
    ```
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █   >>> CYBER-ORACLE // PROTOCOL 2025 // INITIATE_COMM <<<<   █
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
    ```
    """
    return ascii_art
