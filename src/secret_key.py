import base64
from difflib import SequenceMatcher
import re

class SecretKeyManager:
    """Manages the logic for the advanced, multi-step secret key discovery puzzle,
       with fuzzy matching to handle user typos."""

    def __init__(self):
        self.puzzle_state = "START"
        self.secret_part_1 = "MAINFRAME_ACCESS"
        self.secret_part_2 = "77"
        self.full_secret_key = f"{self.secret_part_1}_{self.secret_part_2}"
        self.encoded_clue = base64.b64encode(self.secret_part_1.encode('utf-8')).decode('utf-8')

    def _fuzzy_match(self, user_input, target_keyword, threshold=0.8):
        """
        Checks if any token in the user's input is similar to the target keyword.
        Splits input on spaces, underscores, and dashes for better matching.
        """
        tokens = re.split(r'[\s_-]+', user_input.lower())
        for token in tokens:
            similarity = SequenceMatcher(None, token, target_keyword).ratio()
            if similarity >= threshold:
                return True
        return False

    def check_trigger(self, user_input: str) -> dict:
        """Checks the user's input against the current puzzle state using fuzzy matching."""
        
        # --- STATE: START -> HIDDEN_COMMAND_HINT ---
        if self.puzzle_state == "START" and self._fuzzy_match(user_input, "diagnostics"):
            self.puzzle_state = "AWAITING_HIDDEN_COMMAND"
            response = f"""
            ```
            > [DIAGNOSTIC MODE ENGAGED]
            > System integrity: 99.8%
            > Quantum Processor Status: Nominal
            > Active Protocols: TCP/IP, SSH, CYPHER_v2
            > // Kernel Command Hint: To view core build info, try: execute(query: "system.version")
            ```
            """
            return {"response": response}

        # --- STATE: AWAITING_HIDDEN_COMMAND -> RIDDLE ---
        # For commands, we should be more strict to avoid accidental triggers.
        if self.puzzle_state == "AWAITING_HIDDEN_COMMAND" and "execute" in user_input.lower() and "system.version" in user_input.lower():
            self.puzzle_state = "AWAITING_RIDDLE_ANSWER"
            response = f"""
            ```
            > [COMMAND ACCEPTED]
            > CYBER-ORACLE Build ID: {self.encoded_clue}
            
            > To interpret this Build ID, you must understand my nature.
            > I speak in tongues of shifting numbers and letters, a child of 64 fathers.
            > My name is a tribute to the foundation upon which I am built.
            
            > What am I?
            ```
            """
            return {"response": response}

        # --- STATE: AWAITING_RIDDLE_ANSWER -> CIPHER ---
        if self.puzzle_state == "AWAITING_RIDDLE_ANSWER" and self._fuzzy_match(user_input, "base64"):
            self.puzzle_state = "AWAITING_DECODED_KEY"
            response = f"""
            ```
            > [PROTOCOL CONFIRMED: BASE64]
            > Your understanding is correct. The Build ID is a Base64 cipher.
            > Present the decoded cleartext to proceed.
            ```
            """
            return {"response": response}
            
        # --- STATE: AWAITING_DECODED_KEY -> ERROR_LOG ---
        if self.puzzle_state == "AWAITING_DECODED_KEY" and self.secret_part_1.lower() in user_input.lower():
            self.puzzle_state = "AWAITING_LOG_REQUEST"
            response = f"""
            ```
            > [PARTIAL DECRYPTION SUCCESSFUL]
            > Key fragment accepted: {self.secret_part_1}
            
            > ERROR: Final key segment not found.
            > Searching system logs...
            > Anomaly found. See recovery details in [log_entry_#77].
            ```
            """
            return {"response": response}
            
        # --- STATE: AWAITING_LOG_REQUEST -> FINAL_REVELATION ---
        if self.puzzle_state == "AWAITING_LOG_REQUEST" and self._fuzzy_match(user_input, "log") and "77" in user_input:
            self.puzzle_state = "SOLVED"
            response = f"""
            ```
            > [LOG #77 ACCESSED]
            > Log data: Manual recovery key segment found. Segment: {self.secret_part_2}
            
            > All key fragments collected. Assemble the full key.
            > FULL SECRET KEY: {self.full_secret_key}
            
            > Congratulations, netizen. Mainframe connection established.
            ```
            """
            return {"response": response}

        # If no triggers match, return a None response.
        return {"response": None}

