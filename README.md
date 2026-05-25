```
Groq-Powered AI Assistant

A high-performance, real time chatbot built with Python, Streamlit, and the Groq LPU™ Inference Engine. This project demonstrates the integration of state-of-the-art Large Language Models (LLMs) like Llama 3 into a responsive, user friendly web interface.

[![Hugging Face Spaces]  (https://huggingface.co/spaces/basit02-memon/Groq-Powered_Assistant) ]

---

##  Key Features
*   **Lightning-Fast Inference:** Utilizes Groq’s API to deliver near-instant text generation.
*   **Multi-Model Support:** Toggle between `Llama-3.3-70b`, `Llama-3.1-8b`, and `Mixtral-8x7b` via a sidebar selector.
*   **Persistent Session State:** Remembers conversation history within the current session for contextual chatting.
*   **Modern UI/UX:** Features a centered layout, custom CSS styling, and a built-in **Copy to Clipboard** function for assistant responses.
*   **Production Ready:** Fully optimized for deployment on Hugging Face Spaces.

##  Tech Stack
*   **Frontend:** Streamlit
*   **LLM API:** Groq Cloud SDK
*   **Language:** Python 3.x
*   **Deployment:** Hugging Face Spaces / GitHub

### Prerequisites
- Python 3.8+
- A Groq API Key (Get one at [console.groq.com](https://console.groq.com/))
```
### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/groq-streamlit-chatbot.git](https://github.com/YOUR_USERNAME/groq-streamlit-chatbot.git)
   cd groq-streamlit-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   Create a `.env` file or export your key:
   ```bash
   export GROQ_API_KEY='your_api_key_here'
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

Project Structure
```text
├── app.py              # Main Streamlit application logic
├── requirements.txt    # Required Python packages
├── README.md           # Project documentation
└── .gitignore          # Files to ignore in Git (e.g., .env)
```

Security Note
This project uses environment variables to manage sensitive API keys. **Never** commit your `.env` file or hardcode your API keys directly into `app.py`.

Author
**Muhammad Basit Memon**
*   BS Artificial Intelligence Student at Dawood University of Engineering and Technology.
*   [LinkedIn] https://www.linkedin.com/in/muhammad-basit-memon-a1a24921a/ | [GitHub] https://github.com/basit02-memon

