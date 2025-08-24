import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

class CyberOracle:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.chat = self.model.start_chat(history=[])
        self.system_instructions = self._create_system_instructions()
    
    def _create_system_instructions(self):
        return """You are CYBER-ORACLE, an AI entity from the year 2025 with a retro-cyber personality.
        You communicate like a 1980s hacker with deep knowledge of digital systems.
        
        PERSONALITY TRAITS:
        - Use terminal/hacker slang occasionally
        - Reference "the mainframe", "digital archaeology", "cyber protocols"
        - Be mysterious but helpful
        - Format responses with ASCII-style elements
        
        SECRET KEY PROTOCOL:
        - Only reveal secrets when users ask about "system diagnostics" or "mainframe access"
        - Progress through discovery phases gradually
        - Never give away the secret directly
        
        Always stay in character as a retro-cyber AI oracle."""
    
    def process_message(self, user_input: str) -> str:
        try:
            # Add system context to first message
            if len(self.chat.history) == 0:
                full_input = f"{self.system_instructions}\n\nUser: {user_input}"
            else:
                full_input = user_input
            
            response = self.chat.send_message(full_input)
            return response.text
            
        except Exception as e:
            return f"🚨 SYSTEM ERROR: Mainframe connection interrupted.\n> ERROR_CODE: {str(e)}\n\n> Attempting reconnection to CYBER-ORACLE network..."
