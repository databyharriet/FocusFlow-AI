from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import analyze_mood  

app = FastAPI()

class MoodInput(BaseModel):
    text: str

@app.post("/analyze-mood/")
def analyze_mood_api(input: MoodInput):
    mood = analyze_mood(input.text)  
    return {"mood": mood}
