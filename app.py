# 🧠 FocusFlow AI - All-in-One Streamlit App

import streamlit as st
import datetime
import os
import pandas as pd
from transformers import pipeline
from fpdf import FPDF
from app.utils import analyze_mood as analyze_mood_nltk

# ────────────────────
# AI Tip Generator
# ────────────────────

def generate_ai_tip():
    tips = [
        "Take a deep breath and give yourself permission to pause. 🌿",
        "Your productivity doesn't define your worth. Rest is productive too. 💆",
        "Try journaling for just 5 minutes a day. It clears the mental fog. ✍️",
        "Avoid multitasking — focus on one thing at a time for better results. 🎯",
        "Sleep is fuel. Prioritize it like you would any important task. 🛌",
        "Practice gratitude today — list 3 small things you're thankful for. 🙏",
        "Feeling overwhelmed? Step outside for 10 minutes. Nature helps. 🌳",
        "Don't wait for motivation. Action creates momentum. 🔄",
        "Limit screen time before bed. Your mind needs time to unwind. 📵",
        "Celebrate small wins. They're proof you're moving forward. 🏆",
    ]
    return tips[datetime.datetime.now().minute % len(tips)]

# ────────────────────
# Mood Analyzer
# ────────────────────

@st.cache_resource(show_spinner=False)
def load_classifier():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

classifier = load_classifier()

def analyze_mood(text):
    result = classifier(text)
    label = result[0][0]['label'].lower()
    if label in ["joy", "happiness", "love"]:
        return "positive"
    elif label in ["neutral", "surprise"]:
        return "neutral"
    else:
        return "negative"

# ────────────────────
# Utilities
# ────────────────────

def get_safe_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def save_journal(username, entry, timestamp):
    user_folder = f"journal_entries/{username}"
    os.makedirs(user_folder, exist_ok=True)
    with open(f"{user_folder}/{timestamp}.txt", "w", encoding="utf-8") as f:
        f.write(entry)

def delete_journal(username, timestamp):
    path = f"journal_entries/{username}/{timestamp}.txt"
    if os.path.exists(path):
        os.remove(path)

def log_habit(username, timestamp, habit, sleep, productivity):
    user_folder = f"habit_data/{username}"
    os.makedirs(user_folder, exist_ok=True)
    file = f"{user_folder}/habit_log.csv"
    new = pd.DataFrame([{"timestamp": timestamp, "habit": habit, "sleep_hours": sleep, "productivity_level": productivity}])
    if os.path.exists(file):
        old = pd.read_csv(file)
        new = pd.concat([old, new], ignore_index=True)
    new.to_csv(file, index=False)

def delete_habit(username, timestamp):
    file = f"habit_data/{username}/habit_log.csv"
    if os.path.exists(file):
        df = pd.read_csv(file)
        df = df[df['timestamp'] != timestamp]
        df.to_csv(file, index=False)

def generate_pdf(df, filename, title):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, title, ln=True, align='C')
    pdf.set_font("Arial", '', 10)
    for _, row in df.iterrows():
        line = ' | '.join(str(val) for val in row.values)
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

# ────────────────────
# Streamlit Setup
# ────────────────────

st.set_page_config("FocusFlow AI", layout="wide")

with st.sidebar.expander("🎨 Theme Settings", expanded=False):
    bg_color = st.color_picker("Background Color", "#fff7fb")
    text_color = st.color_picker("Text Color", "#4a148c")
    accent_color = st.color_picker("Accent Color", "#9575cd")
    font_family = st.selectbox(
        "Font Style",
        ["Poppins", "Roboto", "Montserrat", "Lato", "Courier New", "Georgia"],
        index=0,
    )

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family={font_family.replace(" ", "+")}&display=swap');
    html, body, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="block-container"], .main {{
        font-family: '{font_family}', sans-serif !important;
        color: {text_color} !important;
        background-color: {bg_color} !important;
    }}
    .stButton>button {{
        background-color: {accent_color} !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        transition: 0.3s ease;
    }}
    .stButton>button:hover {{
        filter: brightness(1.1);
    }}
    footer {{ visibility: hidden; }}
    </style>
    """,
    unsafe_allow_html=True
)

# ────────────────────
# User Authentication
# ────────────────────

if 'username' not in st.session_state:
    username_input = st.text_input("Enter your name to start:", key="username_input")
    if username_input:
        st.session_state['username'] = username_input.strip().title()
        st.experimental_rerun()
    st.stop()
else:
    username = st.session_state['username']
    st.sidebar.markdown(f"### 👋 Welcome, {username}!")

    menu = st.sidebar.radio("📌 Menu", [
        "Mood Analyzer", "Daily Journal", "Habit Tracker",
        "Burnout Checker", "Data Dashboard", "Reminders (Coming Soon)", "About"
    ])

    # App main sections would go here (same structure you had)
    st.write(f"## Welcome {username}, your personal clarity assistant is ready ✨")


# ────────────────────
# Menu Navigation
# ────────────────────

menu = st.sidebar.radio("📌 Menu", ["Mood Analyzer", "Daily Journal", "Habit Tracker", "Burnout Checker", "Data Dashboard", "Reminders (Coming Soon)", "About"])

# ────────────────────
# Mood Analyzer
# ────────────────────

if menu == "Mood Analyzer":
    st.title("😌 Mood Analyzer")
    mood_input = st.text_area("How are you feeling today?")
    st.info(f"💡 AI Tip: {generate_ai_tip()}")
    if st.button("Analyze Mood") and mood_input.strip():
        mood = analyze_mood(mood_input)
        st.success(f"Your mood is **{mood.upper()}**")

# ────────────────────
# Daily Journal
# ────────────────────

elif menu == "Daily Journal":
    st.title("📓 Daily Journal")
    entry = st.text_area("Write your journal:")
    timestamp = get_safe_timestamp()
    if st.button("💾 Save Entry") and entry.strip():
        save_journal(username, entry, timestamp)
        st.success(f"Saved at {timestamp}")
    user_folder = f"journal_entries/{username}"
    files = sorted(os.listdir(user_folder)) if os.path.exists(user_folder) else []
    journal_data = []
    for f in files:
        ts = f.replace(".txt", "")
        with open(f"{user_folder}/{f}", encoding="utf-8") as file:
            text = file.read()
        journal_data.append({"timestamp": ts, "content": text})
        with st.expander(f"🗕️ {ts}"):
            st.write(text)
            if st.button(f"❌ Delete", key=ts):
                delete_journal(username, ts)
                st.success(f"Deleted {ts}")
                st.experimental_rerun()
    if journal_data:
        jdf = pd.DataFrame(journal_data)
        st.download_button("📥 Download Journals CSV", jdf.to_csv(index=False), file_name="journal_entries.csv")

# ────────────────────
# Habit Tracker
# ────────────────────

elif menu == "Habit Tracker":
    st.title("✅ Habit Tracker")
    habit = st.text_input("What habit did you practice today?")
    sleep = st.slider("🛌 Sleep hours", 0, 12, 7)
    prod = st.slider("⚙️ Productivity", 0, 10, 5)
    timestamp = get_safe_timestamp()
    if st.button("📈 Log Habit") and habit.strip():
        log_habit(username, timestamp, habit, sleep, prod)
        st.success("Habit logged!")
    file = f"habit_data/{username}/habit_log.csv"
    if os.path.exists(file):
        df = pd.read_csv(file)
        st.subheader("📂 Recent Habit Logs")
        st.dataframe(df.tail(10))

# ────────────────────
# Burnout Checker
# ────────────────────

elif menu == "Burnout Checker":
    st.title("🔥 Burnout Risk Checker")
    file = f"habit_data/{username}/habit_log.csv"
    if os.path.exists(file):
        df = pd.read_csv(file).tail(7)
        avg_sleep = df["sleep_hours"].mean()
        avg_prod = df["productivity_level"].mean()
        score = (5 - avg_prod) + (6 - avg_sleep)
        st.metric("Avg Sleep", f"{avg_sleep:.1f} hrs")
        st.metric("Avg Productivity", f"{avg_prod:.1f}/10")
        if score >= 6: st.error("🚨 High burnout risk")
        elif score >= 4: st.warning("⚠️ Moderate burnout risk")
        else: st.success("✅ Low burnout risk")
    else:
        st.info("No habit data found.")

# ────────────────────
# Data Dashboard
# ────────────────────

elif menu == "Data Dashboard":
    st.title("📊 Data Dashboard")
    file = f"habit_data/{username}/habit_log.csv"
    if os.path.exists(file):
        df = pd.read_csv(file)
        st.bar_chart(df["productivity_level"])
    else:
        st.info("No data yet to show.")

# ────────────────────
# Reminders Coming Soon
# ────────────────────

elif menu == "Reminders (Coming Soon)":
    st.title("⏳ Reminders")
    st.info("Reminders feature coming soon! 🚀")

# ────────────────────
# About
# ────────────────────

elif menu == "About":
    st.title("ℹ️ About FocusFlow AI")
    st.markdown("""
    **FocusFlow AI** is your personal clarity assistant.

    ✅ Journal your thoughts

    ✅ Track sleep & productivity
    
    ✅ AI mood analysis
    
    ✅ Burnout prevention
    
    ✅ Data insights

    Built with ❤️ by Mercy Jacob
    """)
