# 🌐 CYBER-ORACLE: Retro AI Terminal

*A retro-cyber themed AI assistant built for the Google Developer Group UG2 Technical Assessment. Navigate a 1980s-style terminal interface to uncover hidden secrets.*

---

## 🚀 Live Demo

[Watch the full demonstration here.](./docs/demo_video.md)

---

## 📸 Screenshots

**Main Interface:**
*[Insert your main interface screenshot here]*

**Secret Key Discovery:**
*[Insert a screenshot of the puzzle steps here]*

---

## 📋 Project Overview

**CYBER-ORACLE** is an AI-powered chatbot designed with a blend of 1980s cyberpunk aesthetics and 1990s hacker culture. Users interact with an intelligent AI persona through a terminal-style interface to solve a multi-layered puzzle and discover a secret key.

### 🎯 Key Features

-   [x] **Retro-Cyber Terminal Interface:** Custom CSS creates an immersive terminal with neon text, scanlines, and a boot-up sequence.
-   [x] **Intelligent AI Persona:** Powered by the Google Gemini API, the CYBER-ORACLE has a distinct, mysterious personality.
-   [x] **Interactive Elements:** Features include ASCII art and a real-time typing animation for AI responses.
-   [x] **Advanced Multi-Layered Puzzle:** A sophisticated 5-step puzzle that requires logic, observation, and technical knowledge to solve.

---

## 🛠️ Technology Stack

-   **AI Model:** Google Gemini 2.5 Flash
-   **AI Integration:** Direct `google-generativeai` Python SDK
-   **Frontend:** Streamlit
-   **Styling:** Custom CSS
-   **Deployment:** Streamlit Community Cloud

---

## 🔧 Installation & Setup

### Prerequisites
-   Python 3.8+
-   A Google Gemini API Key

### Quick Start

1.  **Clone the repository:**
    ```
    git clone https://github.com/yourusername/retro-cyber-intelligent-query-system.git
    cd retro-cyber-intelligent-query-system
    ```

2.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    -   Create a file named `.env` in the root directory.
    -   Add your Gemini API Key to it:
        ```
        GEMINI_API_KEY=YOUR_API_KEY_HERE
        ```

4.  **Run the application:**
    ```
    streamlit run app.py
    ```

---

## 🔍 Secret Key Discovery

<details>
<summary>🚨 SPOILER ALERT - Solution Guide</summary>

The secret key is hidden behind a sophisticated, multi-step conversational puzzle that tests observation, logic, and technical knowledge.

1.  **Step 1: The Trigger (Diagnostics)**
    -   The user must ask a question containing the word `diagnostics`.
    -   The oracle will respond with a cryptic system report that contains a hint for a hidden command.

2.  **Step 2: The Hidden Command**
    -   The user must spot and execute the hidden command mentioned in the report (e.g., `execute query "system.version"`).

3.  **Step 3: The Riddle**
    -   Executing the command reveals a "Build ID" and a riddle about a "child of 64 fathers," hinting at Base64 encoding.
    -   The user must identify the encoding by name (i.e., respond with "Base64").

4.  **Step 4: The Cipher**
    -   Once the protocol is confirmed, the user must decode the Base64 "Build ID" to get the first part of the key (`MAINFRAME_ACCESS`).
    -   Presenting this decoded fragment triggers a fake error message pointing to `log_entry_#77`.

5.  **Step 5: The Final Revelation**
    -   The user must ask for `log entry 77`.
    -   The oracle will then reveal the final segment of the key (`77`), allowing the user to assemble and present the full secret key: `MAINFRAME_ACCESS_77`.

</details>

---

## 🏗️ Development Progress

-   [x] **Phase 1: Foundation & API Setup** - *Complete*
-   [x] **Phase 2: Retro-Cyber Theming** - *Complete*
-   [x] **Phase 3: Secret Key Mechanism** - *Complete*
-   [ ] **Phase 4: Deployment & Final Documentation** - *In Progress*

---

## 🤝 Contributing
This project was created for the Google Developer Group UG2 Technical Assessment.
