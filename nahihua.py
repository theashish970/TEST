import streamlit as st
import random
import pandas as pd
import os
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Quantum Computing MCQ Exam",
    page_icon="🧠",
    layout="centered"
)

# ================= CLEAN EXAM UI CSS =================
st.markdown("""
<style>
body { background-color: #f4f6f8; }
.exam-container { max-width: 900px; margin: auto; }
.question-card {
    background: #ffffff;
    padding: 22px;
    margin-bottom: 20px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
}
.question-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 12px;
}
.result-card {
    background: #0f172a;
    color: white;
    padding: 25px;
    border-radius: 16px;
    margin-top: 20px;
}
.stButton>button {
    width: 100%;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='exam-container'>", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("## 🧠 Quantum Computing – MCQ Examination")
st.markdown("**50 Questions • 1 Mark Each • Randomized**")
st.markdown("---")

# ================= STUDENT INFO =================
student_name = st.text_input("👤 Student Name")
if not student_name:
    st.info("Please enter your name to begin the exam.")
    st.stop()

# ================= FUN MESSAGES =================
FUN_MESSAGES = [
    "Ankit studied so hard that even qubits collapsed out of fear 😄",
    "Ashish is still negotiating with Schrödinger’s cat 🐱",
    "Pavan entered superposition between confidence and confusion 🌀",
    "Raj tried to entangle coffee with concentration ☕",
    "Dikshant almost measured the qubit without collapsing it 👀",
    "Selva says decoherence is just distraction in disguise 😵",
    "Mandar searched answers using Grover’s algorithm 🔍",
    "Ankit believes superposition is multitasking done right 😎",
    "Ashish thinks quantum speedup should apply to exams 🚀",
    "Pavan tried teleporting answers but lost the entanglement 📡",
    "Raj attempted to cool qubits using ice cream 🍦",
    "Dikshant thinks NISQ sounds like a startup name 💡",
    "Selva claims Bloch sphere is actually a cricket ball 🏏",
    "Mandar says interference improves decision making ✨",
    "Ankit prepared so well even noise avoided him 🤯",
    "Ashish tried convincing IBM Quantum for bonus marks 🤝",
    "Pavan ran Grover’s algorithm on his memory 🧠",
    "Raj believes quantum advantage should help with sleep 😴",
    "Dikshant is still calculating amplitudes mentally 📐",
    "Selva says classical computers are just jealous 😏"
]

# ================= QUESTION BANK (50 QUESTIONS) =================
QUESTION_BANK = [
("A qubit can exist in:",["Only 0","Only 1","Both 0 and 1 at the same time","Neither"],"Both 0 and 1 at the same time"),
("Qubit state is represented as:",["Vector","Scalar","Matrix","Integer"],"Vector"),
("State collapsing happens due to:",["Entanglement","Measurement","Superposition","Teleportation"],"Measurement"),
("Quantum mechanics primarily deals with:",["Classical systems","Microscopic particles","Gravity","Heat transfer"],"Microscopic particles"),
("Tensor product is used for:",["Measuring qubits","Combining multi-qubit states","Destroying coherence","Reducing dimensions"],"Combining multi-qubit states"),
("Measurement gives:",["Real numbers","0 or 1","∞","Undefined"],"0 or 1"),
("Measurement causes:",["Noise","State collapse","Entanglement","Teleportation"],"State collapse"),
("Probability of outcome =",["Real part","Squared amplitude","Phase angle","Magnitude only"],"Squared amplitude"),
("Gate that creates superposition:",["X","H","Z","CNOT"],"H"),
("Quantum NOT gate:",["H","X","Z","S"],"X"),
("Two-qubit gate:",["H","X","CNOT","T"],"CNOT"),
("Unitary operations must be:",["Irreversible","Reversible","Random","Measured"],"Reversible"),
("Z gate performs:",["Bit flip","Phase flip","Amplitude increase","None"],"Phase flip"),
("IBM QE allows:",["Classical simulation only","Access to real quantum hardware","Blockchain apps","Neural networks only"],"Access to real quantum hardware"),
("Circuit Composer is used for:",["Drawing quantum circuits","Database design","Electronics","Audio editing"],"Drawing quantum circuits"),
("Qiskit is a:",["Operating system","Quantum framework","Hardware","Measurement device"],"Quantum framework"),
("Output of quantum circuits:",["Classical bits","Qubit pulses","Continuous waves","Images"],"Classical bits"),
("Entanglement creates:",["Independent qubits","Correlated qubits","Superposed bits only","Noise"],"Correlated qubits"),
("Interference:",["Increases errors","Removes correct states","Amplifies correct states","Measures phases only"],"Amplifies correct states"),
("Bell state contains:",["One qubit","Two entangled qubits","Classical data","Noise only"],"Two entangled qubits"),
]

# ================= SESSION STATE =================
if "quiz" not in st.session_state:
    quiz = random.sample(QUESTION_BANK, len(QUESTION_BANK))
    st.session_state.quiz = [(q, random.sample(opts, len(opts)), ans) for q, opts, ans in quiz]
    st.session_state.answers = {}
    st.session_state.submitted = False

# ================= QUESTIONS =================
for i, (q, options, correct) in enumerate(st.session_state.quiz):
    st.markdown("<div class='question-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='question-title'>Q{i+1}. {q}</div>", unsafe_allow_html=True)

    choice = st.radio("Select one option:", options, key=f"q_{i}", index=None,
                      disabled=st.session_state.submitted)

    if choice:
        st.session_state.answers[i] = choice

    st.markdown("</div>", unsafe_allow_html=True)

# ================= SUBMIT =================
if not st.session_state.submitted:
    if st.button("📊 Submit Exam"):
        st.session_state.submitted = True
        st.rerun()

# ================= RESULT + FUN + SAVE =================
if st.session_state.submitted:
    correct = sum(
        1 for i, (_, _, ans) in enumerate(st.session_state.quiz)
        if st.session_state.answers.get(i) == ans
    )
    total = len(st.session_state.quiz)

    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.markdown("### 📈 Exam Result")
    st.markdown(f"✅ Correct: {correct}")
    st.markdown(f"❌ Incorrect: {total - correct}")
    st.markdown(f"🎯 Score: {correct}/{total}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 🎉 Fun Zone")
    st.info(random.choice(FUN_MESSAGES))

    # ===== SAVE TO CSV (NO ERRORS) =====
    file = "results.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file):
        df = pd.read_csv(file)
        attempt = df[df["Student Name"] == student_name].shape[0] + 1
    else:
        df = pd.DataFrame(columns=["Student Name","Attempt","Score","Timestamp"])
        attempt = 1

    df.loc[len(df)] = [student_name, attempt, f"{correct}/{total}", now]
    df.to_csv(file, index=False)

    if st.button("🔄 Take Exam Again"):
        st.session_state.clear()
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
