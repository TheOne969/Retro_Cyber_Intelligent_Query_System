import streamlit as st

def apply_cyber_theme():
    st.markdown("""
    <style>
    /* Retro-cyber terminal theme */
    .main {
        background-color: #000000;
        color: #00ff00;
    }
    
    .stTextInput > div > div > input {
        background-color: #001100;
        color: #00ff00;
        border: 1px solid #00ff00;
        font-family: 'Courier New', monospace;
    }
    
    .stMarkdown {
        font-family: 'Courier New', monospace;
    }
    
    h1 {
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff;
        font-family: 'Courier New', monospace;
    }
    
    .stChatMessage {
        background-color: rgba(0, 255, 0, 0.1);
        border-left: 3px solid #00ff00;
    }
    
    /* Glitch effect placeholder */
    .glitch {
        animation: glitch 2s infinite;
    }
    
    @keyframes glitch {
        0% { transform: translate(0) }
        20% { transform: translate(-2px, 2px) }
        40% { transform: translate(-2px, -2px) }
        60% { transform: translate(2px, 2px) }
        80% { transform: translate(2px, -2px) }
        100% { transform: translate(0) }
    }
    </style>
    """, unsafe_allow_html=True)
