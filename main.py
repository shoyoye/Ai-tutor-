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

# ✅ Correct answers
correct_answers = {
    "Simultaneous Equations": ["Elimination", "2"],
    "Quadratic Equations": ["Parabola", "x = (-b ± √(b² - 4ac)) / 2a"],
    "Periodic Table": ["Atomic number", "Na"]
}

# ✅ Quiz logic
score = 0
st.subheader(f"📝 Quiz on {topic}")
for i, (q, options) in enumerate(questions[topic].items()):
    user_ans = st.radio(q, options, key=f"{topic}-{i}")
    correct_ans = correct_answers[topic][i]
    if user_ans == correct_ans:
        score += 1

if st.button("🎯 Submit Quiz"):
    st.success(f"You scored {score} out of {len(questions[topic])}!")
    if score < len(questions[topic]):
        st.info("Need help? Ask the AI assistant below 👇")

st.markdown("---")

# 🤖 AI Tutor Section
st.subheader("🤖 Ask AI for Help")
question = st.text_area("Ask your study question (e.g., Explain quadratic equations step-by-step):")

if question:
    with st.spinner("Thinking like your best teacher..."):
        try:
            prompt = f"""
You are an expert secondary school teacher in Nigeria teaching JSS3/SS1 students.
Please respond with:
1. A clear, simple definition of the topic
2. Step-by-step explanation
3. A worked example using real numbers
4. A friendly encouragement at the end

The student's question is: {question}
"""
            response = model.generate_content(prompt)
            answer = response.text.strip()

            if answer:
                st.success(answer)
            else:
                st.warning("The AI didn’t respond. Try asking again or rewording your question.")
        except Exception as e:
            st.error(f"AI error: {e}")
