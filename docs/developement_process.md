# Development Process Documentation

## Overview
This document summarizes the key technical challenges encountered and the solutions implemented during the development of the CYBER-ORACLE: Retro AI Terminal.

## Technical Challenges & Solutions

### 1. LangChain Dependency Issues
- Early integration attempts with LangChain libraries resulted in critical dependency conflicts and incompatibilities.
- After troubleshooting delays, I switched to directly using Google's `google-generativeai` Python SDK, greatly simplifying the AI integration.
- This pivot allowed focusing on building app features without being blocked by unresolved package issues.

### 2. Custom Streamlit Chat Icons and UI Theming
- The default Streamlit chat avatars were not in line with the retro-cyber aesthetic.
- Various approaches were explored including emojis and custom icon images.
- Custom images required robust handling of file paths and CSS tweaks to preserve the thematic neon green text color and readability.
- Extensive CSS debugging was done to ensure consistent color across all messages, including the initial boot message.

### 3. Multi-Step Secret Key Mechanism
- The initial secret key puzzle was too simple (a single Base64 decode step).
- The design was enhanced to a complex five-step puzzle involving:
  - A trigger on "system diagnostics" query
  - Identification and execution of a hidden developer command
  - Solving a riddle about Base64 encoding
  - Decoding a ciphered build ID
  - Retrieving and interpreting an error log entry for the final key segment
- Fuzzy string matching was incorporated to handle user input typos gracefully, improving usability.

## Lessons Learned
- Building complex puzzles requires clear state management; a finite state machine approach was employed.
- Dependency management is critical to avoid blocking progress.
- Small UI details like avatar icons and text colors greatly influence user immersion and experience.
- Handling user errors (like typos) enhances robustness without compromising challenge.

## Future Enhancements
- Add audio narration with retro synthesized voices.
- Support multiple languages or difficulty modes for the puzzle.
- Integrate analytics for user progress and puzzle completion tracking.

---

This documentation captures the major hurdles and strategic decisions made during development to inform reviewers and future maintainers.
