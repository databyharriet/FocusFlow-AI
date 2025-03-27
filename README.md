# AI-Powered Mood Tracker🎭

A simple AI-powered sentiment analysis tool that detects moods from text input using FastAPI, Streamlit, and NLP (VADER Sentiment Analysis).

🚀 Features
✅ Real-time sentiment analysis (Positive, Negative, Neutral)
✅ User-friendly web interface with emojis
✅ Lightweight and easy to set up

🛠 Tech Stack
Backend: FastAPI (for sentiment analysis API)
Frontend: Streamlit (for user interaction)
NLP: NLTK (VADER sentiment analysis)
API Communication: Requests

## 📌 Installation & Setup
1️⃣ Clone the Repository
   ```
   git clone https://github.com/yourusername/ai-mood-tracker.git
   cd ai-mood-tracker
   ```
2️⃣ Install Dependencies
   ```pip install fastapi streamlit nltk requests pillow uvicorn```
3️⃣ Run the FastAPI Backend
   ```uvicorn main:app --reload```
It should run on http://127.0.0.1:8000
4️⃣ Run the Streamlit Frontend
   ```streamlit run app.py``
It should open in your browser.

🔬 How It Works
- User enters text in the Streamlit app.
- FastAPI backend processes the text using NLTK's SentimentIntensityAnalyzer.
- Mood is determined as Positive 😃, Negative 😢, or Neutral 😐.
- Result is displayed with an emoji in the UI.


