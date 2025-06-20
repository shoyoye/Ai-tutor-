import streamlit as st

st.set_page_config(page_title="AI Study Assistant", layout="centered")

st.title("📘 Weekly Learning Assistant with AI")
st.write("Choose your weekly topic, take a quick test, and ask AI for help if needed.")

# Weekly topic selector
topic = st.selectbox("🗂️ Choose a topic", [
    "Simultaneous Equations", 
    "Quadratic Equations", 
    "Periodic Table"
])

# Quiz questions per topic
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

# Display quiz
score = 0
st.subheader(f"📝 Quiz on {topic}")
for q, options in questions[topic].items():
    user_ans = st.radio(q, options, key=q)
    correct_ans = options[2] if topic == "Quadratic Equations" else options[1]  # Choose correct based on index
    if user_ans == correct_ans:
        score += 1

# Show results
if st.button("🎯 Submit Quiz"):
    st.success(f"You scored {score} out of {len(questions[topic])}!")
    if score < len(questions[topic]):
        st.info("Need help? Ask the AI assistant below! 👇")

# AI helper
st.subheader("🤖 Ask AI for Help")
question = st.text_input("Enter your question (e.g., Explain quadratic formula)")

if question:
    if "simultaneous" in question.lower():
        st.success("Simultaneous equations are equations with two or more variables. You solve them together to find values that satisfy both.")
    elif "quadratic" in question.lower():
        st.success("A quadratic equation has the form ax² + bx + c = 0. Use the formula: x = (-b ± √(b² - 4ac)) / 2a.")
    elif "periodic" in question.lower():
        st.success("The periodic table organizes elements by increasing atomic number and groups them by similar properties.")
    elif "sodium" in question.lower():
        st.success("The symbol for Sodium is 'Na', derived from the Latin word 'Natrium'.")
    else:
        st.warning("Sorry, I don’t know that yet. Try another topic!")

