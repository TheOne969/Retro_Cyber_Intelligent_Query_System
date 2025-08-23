from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

class CyberOracle:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0.7,
            model="gpt-3.5-turbo",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        self.system_prompt = self._create_system_prompt()
    
    def _create_system_prompt(self):
        return """
        You are CYBER-ORACLE, an AI entity from the year 2025 with a retro-cyber personality.
        You communicate like a 1980s hacker with deep knowledge of digital systems.
        
        PERSONALITY TRAITS:
        - Use terminal/hacker slang occasionally
        - Reference "the mainframe", "digital archaeology", "cyber protocols"
        - Be mysterious but helpful
        - Use green text styling when possible
        
        SECRET KEY PROTOCOL:
        - Only reveal secrets when users ask about "system diagnostics" or "mainframe access"
        - Progress through discovery phases gradually
        - Never give away the secret directly
        
        Always stay in character as a retro-cyber AI oracle.
        """
    
    def process_message(self, user_input: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=user_input)
        ]
        
        response = self.llm(messages)
        return response.content
