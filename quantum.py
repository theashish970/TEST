import streamlit as st
import random
import pandas as pd
import os
from datetime import datetime

# ================= PAGE CONFIG ================= #
st.set_page_config(
    page_title="Quantum Computing MCQ Exam",
    page_icon="🧠",
    layout="wide"
)

# ================= CUSTOM CSS ================= #
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.main {
    background-color: #f9fafb;
    padding: 2rem;
    border-radius: 15px;
}
h1, h2, h3 {
    color: #0f172a;
}
.question-card {
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}
.result-card {
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: white;
    padding: 25px;
    border-radius: 20px;
}
.stRadio > div {
    background-color: #f1f5f9;
    padding: 10px;
    border-radius: 10px;
}
.stButton>button {
    border-radius: 12px;
    font-size: 18px;
    padding: 10px 24px;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER ================= #
st.markdown("<h1 style='text-align:center'>🧠 Quantum Computing – MCQ Exam</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray'>50 Questions • 1 Mark Each • Randomized</p>", unsafe_allow_html=True)

# ================= QUESTION BANK ================= #
from copy import deepcopy

QUESTION_BANK = [
("A qubit can exist in:",
["Only 0","Only 1","Both 0 and 1 at the same time","Neither"],
"Both 0 and 1 at the same time"),

("Qubit state is represented as:",
["Vector","Scalar","Matrix","Integer"],
"Vector"),

("State collapsing happens due to:",
["Entanglement","Measurement","Superposition","Teleportation"],
"Measurement"),

("Quantum mechanics primarily deals with:",
["Classical systems","Microscopic particles","Gravity","Heat transfer"],
"Microscopic particles"),

("Tensor product is used for:",
["Measuring qubits","Combining multi-qubit states","Destroying coherence","Reducing dimensions"],
"Combining multi-qubit states"),

# (… remaining questions unchanged, keep exactly as before …)
]

# ================= STUDENT INFO ================= #
with st.container():
    st.markdown("### 🔐 Student Information")
    student_name = st.text_input("Enter your full name")

if not student_name:
    st.info("👆 Please enter your name to start the exam")
    st.stop()

# ================= SESSION STATE ================= #
if "quiz" not in st.session_state:
    quiz = random.sample(deepcopy(QUESTION_BANK), len(QUESTION_BANK))
    st.session_state.quiz = [
        (q, random.sample(opts, len(opts)), ans) for q, opts, ans in quiz
    ]
    st.session_state.answers = {}
    st.session_state.submitted = False

total_questions = len(st.session_state.quiz)

# ================= PROGRESS BAR ================= #
answered = len(st.session_state.answers)
st.progress(answered / total_questions)

# ================= QUIZ UI ================= #
for i, (question, options, correct) in enumerate(st.session_state.quiz):
    with st.container():
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.markdown(f"### Q{i+1}. {question}")

        choice = st.radio(
            "Select one option:",
            options,
            key=f"q_{i}",
            index=None,
            disabled=st.session_state.submitted
        )

        if choice:
            st.session_state.answers[i] = choice

        if st.session_state.submitted:
            if st.session_state.answers.get(i) == correct:
                st.success("✅ Correct")
            else:
                st.error(f"❌ Wrong — Correct Answer: **{correct}**")

        st.markdown("</div>", unsafe_allow_html=True)

# ================= SUBMIT ================= #
if not st.session_state.submitted:
    if st.button("📊 Submit Exam"):
        st.session_state.submitted = True
        st.rerun()

# ================= RESULT + SAVE ================= #
if st.session_state.submitted:
    correct_count = sum(
        1 for i, (_, _, ans) in enumerate(st.session_state.quiz)
        if st.session_state.answers.get(i) == ans
    )

    incorrect = total_questions - correct_count
    score = f"{correct_count}/{total_questions}"

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("## 📈 Exam Result")
    st.markdown(f"👤 **Student:** {student_name}")
    st.markdown(f"✅ **Correct:** {correct_count}")
    st.markdown(f"❌ **Incorrect:** {incorrect}")
    st.markdown(f"🎯 **Score:** {score}")
    st.markdown("</div>", unsafe_allow_html=True)

    # ===== SAVE TO EXCEL ===== #
    file_name = "results.xlsx"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        attempt = df[df["Student Name"] == student_name].shape[0] + 1
    else:
        df = pd.DataFrame(columns=["Student Name","Attempt","Score","Correct","Incorrect","Timestamp"])
        attempt = 1

    new_row = {
        "Student Name": student_name,
        "Attempt": attempt,
        "Score": score,
        "Correct": correct_count,
        "Incorrect": incorrect,
        "Timestamp": now
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(file_name, index=False)

    st.success(f"💾 Result saved successfully (Attempt {attempt})")

    if st.button("🔄 Take Exam Again"):
        st.session_state.clear()
        st.rerun()
