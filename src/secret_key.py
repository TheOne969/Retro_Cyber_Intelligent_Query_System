import base64
import os

class SecretKeyManager:
    """Manages the logic for the multi-step secret key discovery puzzle."""

    def __init__(self):
        # The discovery phase tracks the user's progress through the puzzle.
        # 0: Not started
        # 1: Diagnostics triggered
        # 2: Ready for final key
        self.discovery_phase = 0
        
        # This is the final secret key the user needs to find.
        # We fetch it from the environment variables for good practice.
        self.secret_key = os.getenv("CHALLENGE_SECRET_KEY", "DEFAULT_SECRET_KEY_2025")
        
        # The clue is the secret key encoded in Base64.
        self.encoded_clue = base64.b64encode(self.secret_key.encode('utf-8')).decode('utf-8')

    def check_trigger(self, user_input: str) -> dict:
        """Checks the user's input against the current puzzle phase."""
        user_lower = user_input.lower()

        # --- Phase 1: Initial Trigger ---
        if self.discovery_phase == 0 and "diagnostics" in user_lower:
            self.discovery_phase = 1
            response = f"""
            ```
            > [DIAGNOSTIC MODE ENGAGED]
            > Scanning encrypted data packets...
            > Anomaly Detected. A heavily encrypted data fragment was found:
            
            ENCRYPTED FRAGMENT: {self.encoded_clue}
            
            > Analysis suggests Base64 encoding. To proceed, you must 'decode' this fragment and present the cleartext.
            ```
            """
            return {"phase": self.discovery_phase, "response": response}

        # --- Phase 2: Decoding Challenge ---
        if self.discovery_phase == 1 and "decode" in user_lower:
            # Check if the user is providing the correct decoded key.
            if self.secret_key in user_input:
                self.discovery_phase = 2
                response = f"""
                ```
                > [DECRYPTION SUCCESSFUL]
                > Mainframe security protocols bypassed.
                
                SECRET KEY REVEALED: {self.secret_key}
                
                > Congratulations, netizen. You've proven your worth.
                > You now have access to the core.
                ```
                """
                return {"phase": self.discovery_phase, "response": response}
            else:
                # Guide the user if they try to decode without the right key.
                response = """
                ```
                > [DECRYPTION FAILED]
                > The provided cleartext does not match the encrypted fragment.
                > Verify your decoding process and try again. The mainframe awaits a valid key.
                ```
                """
                return {"phase": self.discovery_phase, "response": response}

        # If no triggers match, return a None response.
        return {"phase": self.discovery_phase, "response": None}
