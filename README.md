# 🌐 CYBER-ORACLE: Retro AI Terminal

*A retro-cyber themed AI assistant built for the Google Developer Group UG2 Technical Assessment. Navigate a 1980s-style terminal interface to uncover hidden secrets.*

---

## 🚀 Live Demo

[Watch the full demonstration here.](./docs/demo_video.md)

---

## 📸 Screenshots

**Main Interface:**
[1]

**Secret Key Discovery:**
*(A screenshot showing the puzzle steps, like the one you just took)*

---

## 📋 Project Overview

**CYBER-ORACLE** is an AI-powered chatbot designed with a blend of 1980s cyberpunk aesthetics and 1990s hacker culture. Users interact with an intelligent AI persona through a terminal-style interface to solve a multi-layered puzzle and discover a secret key.

### 🎯 Key Features

- [x] **Retro-Cyber Terminal Interface:** Custom CSS creates an immersive terminal with neon text, scanlines, and a boot-up sequence.
- [x] **Intelligent AI Persona:** Powered by the Google Gemini API, the CYBER-ORACLE has a distinct, mysterious personality.
- [x] **Interactive Elements:** Features include ASCII art and a real-time typing animation for AI responses.
- [x] **Multi-Layered Secret Discovery:** A 2-step puzzle is integrated into the conversation flow, requiring logical deduction to solve.

---

## 🛠️ Technology Stack

- **AI Model:** Google Gemini 2.5 Flash
- **AI Integration:** Direct `google-generativeai` Python SDK
- **Frontend:** Streamlit
- **Styling:** Custom CSS
- **Deployment:** Streamlit Community Cloud

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- A Google Gemini API Key

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
    - Create a file named `.env` in the root directory.
    - Add your Gemini API Key and the challenge's secret key:
      ```
      GEMINI_API_KEY=YOUR_API_KEY_HERE
      CHALLENGE_SECRET_KEY=RETRO_WAVE_ACCESS_77
      ```

4.  **Run the application:**
    ```
    streamlit run app.py
    ```

---

## 🔍 Secret Key Discovery

<details>
<summary>🚨 SPOILER ALERT - Solution Guide</summary>

The secret key is hidden behind a two-step conversational puzzle:

1.  **Step 1: Trigger the Puzzle**
    - The user must ask the CYBER-ORACLE a question containing the word `diagnostics`.
    - The AI will respond with a data fragment encoded in Base64.

2.  **Step 2: Decode and Reveal**
    - The user must decode the Base64 string.
    - They then present the decoded string back to the oracle in a message that includes the word `decode`.
    - Upon receiving the correct decoded key, the AI confirms the decryption and reveals the final secret key.

</details>

---

## 🏗️ Development Progress

- [x] **Phase 1: Foundation & API Setup** - *Complete*
- [x] **Phase 2: Retro-Cyber Theming** - *Complete*
- [x] **Phase 3: Secret Key Mechanism** - *Complete*
- [ ] **Phase 4: Deployment & Final Documentation** - *In Progress*

---

## 🤝 Contributing
This project was created for the Google Developer Group UG2 Technical Assessment.
