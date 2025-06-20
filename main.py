import streamlit as st
import google.generativeai as genai

# ✅ Set your Gemini API key here
genai.configure(api_key="YOUR_NEW_API_KEY")  # Replace with your real API key

st.set_page_config(page_title="AI Study Assistant", layout="centered")
st.title("📘 Weekly Learning Assistant with AI")
st.write("Choose your weekly topic, take a quick test, and ask AI for help if needed.")

# 🗂️ Weekly topic dropdown
topic = st.selectbox("Choose a topic", [
    "Simultaneous Equations", 
    "Quadratic Equations", 
    "Periodic Table"
])

# 📝 Quiz questions
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
correct_answers = {
    "Simultaneous Equations": ["Elimination", "2"],
    "Quadratic Equations": ["Parabola", "x = (-b ± √(b² - 4ac)) / 2a"],
    "Periodic Table": ["Atomic number", "Na"]
}
for i, (question_text, options) in enumerate(questions[topic].items()):
    user_ans = st.radio(question_text, options, key=f"{topic}-{i}")
    if user_ans == correct_answers[topic][i]:
        score += 1

# ✅ Submit score
if st.button("🎯 Submit Quiz"):
    st.success(f"You scored {score} out of {len(questions[topic])}!")
    if score < len(questions[topic]):
        st.info("Need help? Ask the AI tutor below 👇")

st.markdown("---")

# 🤖 AI Tutor Section
st.subheader("🤖 Ask AI for Help")
question = st.text_area("Ask your study question (e.g., Explain quadratic equations step-by-step):")

if question:
    with st.spinner("Thinking like your best teacher..."):
        try:
            # ✅ Use correct Gemini model path
            model = genai.GenerativeModel("models/gemini-pro")
            
            prompt = f"""
You are a brilliant, friendly teacher for Nigerian JSS3/SS1 students.

Here’s the student’s question: "{question}"

Respond with:
1. A clear and simple definition
2. Step-by-step breakdown
3. A real-world or relatable example
4. At least one solved question with working
5. End with an encouraging tip
"""

            response = model.generate_content(prompt)
            answer = response.text.strip()

            if answer:
                st.success(answer)
            else:
                st.warning("The AI did not return an answer. Try again.")
        except Exception as e:
            st.error(f"AI error: {e}")
