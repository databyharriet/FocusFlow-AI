# AI-Powered Mood Tracker API

A FastAPI-based project for analyzing user mood using sentiment analysis.

## 🚀 Setup

1. **Clone the repo**  
   ```sh
   git clone https://github.com/mruna18/AI-Powered_MoodTracker.git
   cd AI-Powered_MoodTracker
2. ** Create and activate a viretual envirnoment
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # Windows: myenv\Scripts\activate

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

