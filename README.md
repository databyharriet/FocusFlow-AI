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

## 🚀 Setup

1. **Clone the repo**  
   ```sh
   git clone https://github.com/mruna18/AI-Powered_MoodTracker.git
   cd AI-Powered_MoodTracker
2. ** Create and activate a virtual environment
    ```sh
    python -m venv myenv
    myenv\Scripts\activate

3. Install dependencies
    ```sh
   pip install -r requirements.txt

4.Run the API
    ```sh
    uvicorn main:app --reload
    
📌 Endpoints
Method	Endpoint	Description
POST	/analyze	Analyze text sentiment
GET	/history	Get past mood records
More features coming soon! 🚧

