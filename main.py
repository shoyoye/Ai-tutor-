import streamlit as st
import google.generativeai as genai

# ✅ Use your new Gemini API key
genai.configure(api_key="AIzaSyAgnH1k9pLFBPNDMyjiqhnaRuCmr9-W-m8")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="AI Study Assistant", layout="centered")
st.title("📘 Weekly Learning Assistant with AI")
st.write("Choose your weekly topic, take a quick test, and ask AI for help if needed.")

# 🗂️ Topic selection
topic = st.selectbox("Choose a topic", [
    "Simultaneous Equations", 
    "Quadratic Equations", 
    "Periodic Table"
])

# 📝 Questions for each topic
questions = {
    "Simultaneous Equations": {
        "What is the method to eliminate a variable?": ["Substitution", "Elimination", "Division", "Cross-multiplication"],
        "How many equations are needed to solve two variables?": ["1", "2", "3", "4"]
    },
    "Quadratic Equations": {
        "What shape does a quadratic graph make?": ["Straight Line", "Parabola", "Circle", "Zigzag"],
        "Which formula solves ax² + bx + c = 0?": [
            "x = -b/a", 
            "x = √a", 
            "x = (-b ± √(b² - 4ac)) / 2a", 
            "x = (a + b)²"
        ]
    },
    "Periodic Table": {
        "What does the periodic table arrange elements by?": ["Alphabet", "Atomic number", "Weight", "Date found"],
        "What is the symbol for Sodium?": ["S", "So", "Na", "N"]
    }
}

# ✅ Quiz logic
score = 0
st.subheader(f"📝 Quiz on {topic}")
for i, (q, options) in enumerate(questions[topic].items()):
    user_ans = st.radio(q, options, key=f"{topic}-{i}")
    correct_answers = {
        "Simultaneous Equations": ["El]()
