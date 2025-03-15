import streamlit as st
import requests
from PIL import Image

# Custom CSS for better styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }
        .stTextArea>label {
            font-size: 18px;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #007BFF !important;
            color: white !important;
            font-size: 16px;
            border-radius: 10px;
        }
        .stAlert {
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section with Logo
st.image("https://cdn-icons-png.flaticon.com/512/3563/3563642.png", width=80)
st.title("🧠 AI-Powered Mood Tracker")
st.write("Analyze the mood of your text using AI & Sentiment Analysis.")

# User Input
text = st.text_area("💬 Enter your text below:", "")

# Mood Emoji Mapping
mood_emojis = {
    "positive": "😃",
    "negative": "😢",
    "neutral": "😐"
}

# Button to Analyze Mood
if st.button("🔍 Analyze Mood"):
    if text.strip():
        with st.spinner("Analyzing mood... Please wait ⏳"):
            response = requests.post("http://127.0.0.1:8000/analyze-mood/", json={"text": text})

        if response.status_code == 200:
            mood = response.json().get("mood", "Unknown")
            emoji = mood_emojis.get(mood, "🤔")
            st.success(f"Detected Mood: **{mood.capitalize()}** {emoji}")
        else:
            st.error("🚨 Error analyzing mood. Please try again.")
    else:
        st.warning("⚠️ Please enter some text before analyzing.")

# Sidebar Section
st.sidebar.title("📌 About This App")
st.sidebar.write("🔹 **Built with:** FastAPI & Streamlit")  
st.sidebar.write("🔹 **Functionality:** Uses NLP to analyze mood.")  
st.sidebar.write("🔹 **Status:** In Development 🚀")  
st.sidebar.write("👨‍💻 Developed by **Mrunali**")

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using AI</center>", unsafe_allow_html=True)
