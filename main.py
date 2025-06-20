# 🤖 AI Help Section
st.subheader("🤖 Ask AI for Help")
question = st.text_area("Ask your study question (e.g., Explain quadratic equations step-by-step):")

if question:
    with st.spinner("Thinking like your best teacher..."):
        try:
            # ✅ use correct model path
            model = genai.GenerativeModel("models/gemini-pro")

            prompt = f"""
You are a secondary school teacher in Nigeria teaching JSS3/SS1.
The student asked: "{question}"

1. Define the topic in simple terms.
2. Break it down step-by-step.
3. Give at least one relatable example.
4. Solve a sample question in full.
5. End with a short tip or encouragement.
"""

            # ✅ use correct generation method
            response = model.generate_content(prompt)
            answer = response.text.strip()

            if answer:
                st.success(answer)
            else:
                st.warning("The AI didn't respond. Try asking again differently.")
        except Exception as e:
            st.error(f"AI error: {e}")
