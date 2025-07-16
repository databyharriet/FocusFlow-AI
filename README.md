# 📌 FocusFlow AI

A mental clarity and productivity assistant powered by AI. FocusFlow AI helps you track your mood, habits, and journaling activities with interactive dashboards, AI mood analysis, and productivity insights — all in one Streamlit web app.

## 🚀 Live Demo
👉 [Launch the App on Streamlit](https://focusflow-ai-5irs3nxlnotuyafydyx3si.streamlit.app)

---

## 💡 Features

- ✅ AI-Powered Mood Analysis (using NLP models)
- ✅ Daily Journal Entries with Sentiment Scoring
- ✅ Habit Tracking System (Productivity & Sleep)
- ✅ Data Dashboard for Weekly & Monthly Overviews
- ✅ Downloadable Reports (CSV/PDF)
- ✅ Fully Responsive UI using Streamlit

---

## 🛠️ Tech Stack

- **Streamlit** for the interactive web app
- **HuggingFace Transformers** for mood analysis
- **Pandas** for data manipulation
- **Matplotlib & Altair** for data visualization
- **FPDF** for report downloads

---

## 📂 Folder Structure
FocusFlow AI/
│
├── app.py # Main Streamlit app
├── app/
│ └── utils.py # Custom utilities for mood analysis
├── habit_data/ # Habit log CSV files
├── journal_entries/ # Saved journal text entries
├── requirements.txt # Python dependencies
└── README.md # Project documentati

---

## ⚙️ Local Development

```bash
# Clone the repo
git clone https://github.com/databyharriet/focusflow-ai.git
cd focusflow-ai

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

🖥️ Deployment
FocusFlow AI is deployed on Streamlit Cloud.
You can fork the repository and deploy your own version by linking it to Streamlit.
📧 Contact
For inquiries or collaborations, reach out on GitHub: @databyharriet