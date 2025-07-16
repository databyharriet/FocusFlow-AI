import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download only if not already present
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_mood(text: str) -> str:
    """Analyze mood using NLTK VADER sentiment scoring."""
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "positive"
    elif score['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"
