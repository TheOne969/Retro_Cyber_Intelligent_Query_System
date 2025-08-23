import base64

class SecretKeyManager:
    def __init__(self):
        self.discovery_phase = 0
        self.secret_key = "CYBER_MAINFRAME_ACCESS_2025"
        self.triggers = [
            ["system diagnostics", "mainframe", "access protocols"],
            ["decode", "decrypt", "analyze"],
            ["final sequence", "complete access", "reveal"]
        ]
    
    def check_trigger(self, user_input: str) -> dict:
        user_lower = user_input.lower()
        
        if self.discovery_phase < len(self.triggers):
            current_triggers = self.triggers[self.discovery_phase]
            if any(trigger in user_lower for trigger in current_triggers):
                self.discovery_phase += 1
                return self._generate_phase_response()
        
        return {"phase": self.discovery_phase, "response": None}
    
    def _generate_phase_response(self) -> dict:
        responses = {
            1: "🔍 ACCESSING DIAGNOSTIC PROTOCOLS...\n\nEncoded data detected: `Q1lCRVJfTUFJTkZSQU1FX0FDQ0VTU18yMDI1`\n\nRequires decryption analysis...",
            2: f"🔓 DECRYPTION SUCCESSFUL!\n\nSecret Key: **{self.secret_key}**\n\n*Welcome to the mainframe, digital archaeologist.*",
        }
        
        return {
            "phase": self.discovery_phase,
            "response": responses.get(self.discovery_phase)
        }
