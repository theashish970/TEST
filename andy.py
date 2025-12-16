import streamlit as st
import random
import pandas as pd
import os
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Quantum Computing MCQ Exam", page_icon="🧠", layout="centered")

# ================= UI CSS =================
st.markdown("""
<style>
body { background-color: #f4f6f8; }
.exam-container { max-width: 900px; margin: auto; }
.question-card {
    background: white;
    padding: 20px;
    margin-bottom: 18px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}
.question-title {
    font-size: 17px;
    font-weight: 600;
}
.result-card {
    background: #0f172a;
    color: white;
    padding: 22px;
    border-radius: 14px;
    margin-top: 20px;
}
.stButton>button {
    width: 100%;
    font-size: 17px;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='exam-container'>", unsafe_allow_html=True)
st.markdown("## 🧠 Quantum Computing – MCQ Examination")
st.markdown("**50 Questions • 1 Mark Each • Randomized**")
st.markdown("---")

# ================= STUDENT NAME =================
student_name = st.text_input("👤 Student Name")
if not student_name:
    st.info("Please enter your name to start the exam.")
    st.stop()

# ================= FUN MESSAGES =================
FUN_MESSAGES = [
    "Ankit studied so hard that even qubits collapsed 😄",
    "Ashish is still negotiating with Schrödinger’s cat 🐱",
    "Pavan entered superposition between confidence and confusion 🌀",
    "Raj tried entangling coffee with focus ☕",
    "Dikshant almost avoided wavefunction collapse 👀",
    "Selva says decoherence is distraction 😵",
    "Mandar used Grover’s algorithm to find answers 🔍",
    "Ankit thinks superposition is multitasking 😎",
    "Ashish wants quantum speedup for exams 🚀",
    "Pavan attempted teleportation of answers 📡",
    "Raj cooled qubits with ice cream 🍦",
    "Dikshant thinks NISQ is a startup 💡",
    "Selva believes Bloch sphere is a cricket ball 🏏",
    "Mandar trusts interference for life choices ✨",
    "Ankit scared noise away 🤯",
    "Ashish almost convinced IBM for bonus marks 🤝",
    "Pavan ran Grover on his memory 🧠",
    "Raj wants quantum sleep advantage 😴",
    "Dikshant still calculating amplitudes 📐",
    "Selva says classical computers are jealous 😏"
]

# ================= ALL 50 QUESTIONS =================
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
("Deutsch-Jozsa finds:",["Prime numbers","Balanced vs constant function","Sorting order","Hidden string"],"Balanced vs constant function"),
("BV Algorithm finds:",["Hidden string","Optimization","Directions","Sorting"],"Hidden string"),
("Grover’s algorithm solves:",["Search","Encryption","Linear regression","Addition"],"Search"),
("Grover’s speedup is:",["Exponential","Quadratic","No speedup","Negative"],"Quadratic"),
("Teleportation sends:",["Physical particle","Quantum state","Only 0","Noise"],"Quantum state"),
("NISQ stands for:",["New International Super Quantum","Noisy Intermediate-Scale Quantum","Non-Important System Quantum","None"],"Noisy Intermediate-Scale Quantum"),
("NISQ limitation:",["Stable qubits","Short coherence time","Infinite qubits","No noise"],"Short coherence time"),
("NISQ devices limit:",["Circuit depth","Internet speed","Bits","Laser power"],"Circuit depth"),
("VQE is used for:",["Sorting","Ground-state energy finding","Email","Memory"],"Ground-state energy finding"),
("VQE is:",["Fully quantum","Hybrid quantum-classical","Fully classical","Non-variational"],"Hybrid quantum-classical"),
("QEC needed because:",["Qubits are perfect","Qubits are noisy","No errors occur","Always deterministic"],"Qubits are noisy"),
("Logical qubit consists of:",["One physical qubit","Many physical qubits","Electrons","None"],"Many physical qubits"),
("Stabilizer codes:",["Create errors","Detect & correct errors","Remove gates","Always collapse state"],"Detect & correct errors"),
("QGAN used for:",["Synthetic data generation","Sorting","Hardware cooling","Classical only"],"Synthetic data generation"),
("QGAN uses:",["No QC","Parameterized Quantum Circuits","Only AI models","Blockchain"],"Parameterized Quantum Circuits"),
("Decoherence happens due to:",["Ideal isolation","Environmental interaction","Perfect gates","Cooling"],"Environmental interaction"),
("Circuit depth means:",["Parallel operations","Sequential gate layers","Qubit size","Temperature"],"Sequential gate layers"),
("Longer circuits:",["Improve results","Increase errors","Always stable","Faster output"],"Increase errors"),
("|0⟩, |1⟩ represent:",["Invalid states","Basis states","Random","Only classical bits"],"Basis states"),
("Bloch sphere represents:",["Classical bit","Single qubit","Many qubits","Energy spectrum"],"Single qubit"),
("Amplitude of a qubit state can be:",["Complex number","Integer","Boolean","Letter"],"Complex number"),
("Quantum advantage means:",["Classical always better","Quantum better in some tasks","QC obsolete","No benefits"],"Quantum better in some tasks"),
("QCs excel in:",["Emails","Quantum simulation","Gaming","Payroll"],"Quantum simulation"),
("Quantum circuit output is:",["Deterministic","Probabilistic","Always 0","∞"],"Probabilistic"),
("Qubits need:",["High temperature","Very low temperature","Random heat","Wind"],"Very low temperature"),
("Superposition collapses due to:",["Computation","Measurement","Entanglement","Noise only"],"Measurement"),
("Classical computer required for:",["Gate control","Qubit creation","Collapse","Decoherence"],"Gate control"),
("Quantum speedup often due to:",["Interference","RAM","GPU","Energy"],"Interference"),
("Teleportation requires:",["Entanglement","No measurement","No classical channel","No communication"],"Entanglement"),
("Noise causes:",["Perfect info","Decoherence","High fidelity","Infinite precision"],"Decoherence"),
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

    # ===== SAVE TO CSV =====
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
