import streamlit as st
import random

st.set_page_config(page_title="Design Thinking MCQ Exam", layout="wide")
st.title("📝 Design Thinking – Full MCQ Examination")

# ---------------- QUESTION BANK (EXACT TEXT) ---------------- #
QUESTION_BANK = [

# ---------------- WEEK 1 ----------------
(
"What is the first Noble Truth according to Lord Buddha?",
[
"Accept suffering",
"Origin of suffering",
"Cessation of suffering",
"Path leading to the cessation of suffering"
],
"Accept suffering"
),

(
"How does the concept of empathy in Design Thinking relate to the teachings of Lord Buddha?",
[
"By comparing it to finding the cause of suffering",
"By emphasizing the importance of understanding others' feelings",
"By linking it to the cessation of suffering",
"By associating it with following the Noble Eightfold Path"
],
"By emphasizing the importance of understanding others' feelings"
),

(
"What tool is used to visualize the steps a customer goes through when interacting with a product or service?",
[
"SWOT Analysis",
"Customer Journey Mapping",
"Brainstorming",
"Business Model Canvas"
],
"Customer Journey Mapping"
),

(
"Which of the following best describes a Customer Persona?",
[
"A fictional representation of a typical user",
"A detailed report of the customer’s problems",
"A list of customer complaints",
"A summary of your client’s business goals"
],
"A fictional representation of a typical user"
),

(
"Which of the following tools is commonly used to capture and organize thoughts, insights, and ideas during design thinking exercises, helping teams visualize connections and prioritize actions?",
[
"Knoin notebook",
"WhatsApp group chats",
"Sticky Notes",
"Teacups"
],
"Sticky Notes"
),

(
"Why is it important to use real observations rather than just asking customers about their experiences?",
[
"Customers might not remember details",
"Observations provide more accurate and unbiased data",
"Asking takes too much time",
"Observations are more fun"
],
"Observations provide more accurate and unbiased data"
),

(
"What should be documented from personal experience and observations before going to the Analyze stage?",
[
"Solutions to problems",
"Steps and emotional mapping",
"Marketing strategies",
"Product specifications"
],
"Steps and emotional mapping"
),

(
"What is the final step suggested for ensuring the completeness of the Customer Journey Map?",
[
"Conducting a survey",
"Having a second persona for a more comprehensive view",
"Asking for feedback from peers",
"Reviewing the map with a mentor"
],
"Having a second persona for a more comprehensive view"
),

(
"What was the problem identified by the Ideo team when observing a senior citizen taking her medication?",
[
"She couldn't remember to take her medication",
"She couldn't open the child-proof medicine bottle",
"She didn't have enough medication",
"She was taking the wrong medication"
],
"She couldn't open the child-proof medicine bottle"
),

# ---------------- WEEK 2 ----------------
(
"What type of problems is the Multi-Why Analysis particularly effective in addressing?",
[
"Problems requiring extensive statistical data",
"Simple problems with clear and obvious causes",
"Complex problems but with known root cause",
"Problems with unknown or unclear root causes"
],
"Problems with unknown or unclear root causes"
),

(
"Which of the following is the best way to resolve conflicts in the Design Thinking process?",
[
"By avoiding conflicts altogether",
"By finding solutions that satisfy all parties involved",
"By accepting that conflicts are inevitable",
"By focusing on customer’s interests"
],
"By finding solutions that satisfy all parties involved"
),

(
"Who coined the problem-solving method known as 5 Why?",
[
"Apple in the 1980s",
"Toyota in the 1970s",
"Google in the 2000s",
"Microsoft in the 1990"
],
"Toyota in the 1970s"
),

(
"In the Four Noble Truths, Samudaya is to find out the reason for suffering. In the Design Thinking context, what is it?",
[
"Analyze",
"Define",
"Introspect",
"Anatomy"
],
"Analyze"
),

(
"What is the graphical representation in the Analyze phase of Design Thinking called?",
[
"Histogram",
"Pie Chart",
"Element-Name-Value",
"Line Graph"
],
"Element-Name-Value"
),

(
"Why is conflict essential in storytelling?",
[
"Conflict makes stories longer",
"Conflict creates interesting characters",
"Conflict adds excitement and engagement",
"Conflict helps in resolving issues faster"
],
"Conflict adds excitement and engagement"
),

(
"In the example of Porthos and his tailor, what is the conflict of interest?",
[
"Porthos wants fashionable clothes, but the tailor cannot deliver on time",
"Porthos wants to be measured without being touched, but the tailor needs to touch him to measure",
"The tailor wants to charge a high price, but Porthos wants a discount",
"The tailor wants to use a measuring tape, but Porthos wants to be measured visually"
],
"Porthos wants to be measured without being touched, but the tailor needs to touch him to measure"
),

(
"What is the conflict of interest in the problem posed by Hershey's regarding transporting chocolates?",
[
"Hershey's wants to transport chocolates, but the chocolates melt in high temperatures",
"Hershey's wants cheap packaging, but cheap packaging cannot withstand high temperatures",
"Hershey's wants to use costly materials, but costly materials are difficult to assemble",
"Hershey's wants to transport chocolates, but the chocolates are too heavy to carry"
],
"Hershey's wants to transport chocolates, but the chocolates melt in high temperatures"
),

(
"How does the conflict of interest analysis help in the design thinking process?",
[
"By identifying the optimal solution that minimizes conflicts",
"By providing a visual representation of conflicting parameters",
"By highlighting the need for creative problem-solving",
"By ensuring that the proposed solutions address the root cause of conflicts"
],
"By ensuring that the proposed solutions address the root cause of conflicts"
),

(
"A restaurant is receiving customer complaints about slow service during peak hours. The manager conducts a Multi-Why analysis and discovers that the root cause is understaffing during busy times. What is the potential impact of addressing the root cause?",
[
"Improved customer satisfaction and loyalty",
"Higher prices for menu items to cover costs",
"Increased advertising to attract more customers",
"Expansion of the restaurant to accommodate more tables"
],
"Improved customer satisfaction and loyalty"
),

# ---------------- WEEK 3 ----------------
(
"What was one of the main outcomes of Altshuller's work in developing TRIZ?",
[
"It revolutionized the education system in Russia",
"It led to improvements in problem-solving across industries",
"It resulted in the development of new warfare methods",
"It changed the way patents were filed in Russia"
],
"It led to improvements in problem-solving across industries"
),

(
"How did Altshuller's method differ from traditional problem-solving approaches?",
[
"It relied on intuition and experience",
"It focused on lived experience",
"It was based on a systematic formula",
"It required extensive training to use"
],
"It was based on a systematic formula"
),

(
"What are the two phases in which Design Thinking steps can be classified?",
[
"Analytical and Systematic phases",
"Initiate and Crash phases",
"Convergent and Divergent phases",
"Research and Development phases"
],
"Convergent and Divergent phases"
),

(
"What is the Zen Master's advice regarding learning new things?",
[
"Keep pouring without stopping",
"Empty the mind of old knowledge",
"Focus on the teacup",
"None"
],
"Empty the mind of old knowledge"
),

(
"How does the story of the 5 blind men and the elephant relate to problem-solving?",
[
"It emphasizes the need for trial and error",
"It suggests that only experts can solve complex problems",
"It shows that problems can have multiple correct solutions",
"It highlights the importance of understanding the whole picture"
],
"It highlights the importance of understanding the whole picture"
),

(
"In applying TRIZ to enhance customer service in a retail shop, which Inventive Principle would be most suitable to improve the checkout process?",
[
"Segmentation – dividing the process into self-checkout and improved checkout",
"Prior Action – preparing bags or packaging in advance",
"Termination – removing checkout counters",
"The Other Way Round – reversing the roles of customer and cashier"
],
"Prior Action – preparing bags or packaging in advance"
),

(
"The Solve phase in Design Thinking is characterized as:",
[
"Implementing a cheap solution",
"A divergent phase that encourages exploring multiple solutions",
"Strictly about adhering to an expert's ideas",
"A phase where no new ideas are entertained"
],
"A divergent phase that encourages exploring multiple solutions"
),

(
"Why is TRIZ methodology used in Design Thinking?",
[
"To systematically test solutions",
"To trigger an idea to solve the problem",
"To grant a patent for an invention",
"To license a technology"
],
"To trigger an idea to solve the problem"
),

(
"Which of the following activities is NOT typically part of the Solve phase?",
[
"Brainstorming",
"Conducting user interviews",
"Using TRIZ methodology to generate ideas",
"Doing a collaborative effort with the team to gather ideas"
],
"Conducting user interviews"
),

(
"How does the Solve phase address the risk of bias in the design process?",
[
"By relying solely on expert opinions and state-of-the-art literature search",
"By involving a diverse team and considering multiple perspectives",
"By avoiding user feedback",
"By skipping the prototyping stage"
],
"By involving a diverse team and considering multiple perspectives"
),

# ---------------- WEEK 4 ----------------
(
"What is the purpose of prototyping in the Design Thinking process?",
[
"To test and refine the product through user feedback",
"To deploy the first 100 products in the market",
"To solve real-world problems while looking at the future of technology",
"To generate revenue"
],
"To test and refine the product through user feedback"
),

(
"Why do we need to test assumptions?",
[
"We may not know everything about a customer/user",
"We may not have the resources (budget) to cover the tests",
"We may not have the knowledge needed to build the prototype",
"We may not know all the answers to any given problem"
],
"We may not know everything about a customer/user"
),

(
"What are some key elements needed before testing ideas in design thinking?",
[
"Sticky notes and notepad to note any observations and feedback",
"10–100 end products or services",
"List of competitors and their offerings",
"List of features, list of assumptions, simple prototypes"
],
"List of features, list of assumptions, simple prototypes"
),

(
"How does the Test Phase contribute to the overall innovation process?",
[
"By helping us generate revenue",
"By providing a framework for creative and lateral thinking",
"By validating new ideas and concepts with real users",
"By generating new ideas and concepts"
],
"By validating new ideas and concepts with real users"
),

(
"What role does iteration play in the Test Phase of design thinking?",
[
"Iteration is not necessary in the Test Phase",
"Iteration involves repeating the entire design process from start to finish",
"Iteration involves making small adjustments to the prototype based on user feedback",
"Iteration is only used if the initial prototype fails testing"
],
"Iteration involves making small adjustments to the prototype based on user feedback"
)
]

# ---------------- SESSION STATE ---------------- #
if "quiz" not in st.session_state:
    st.session_state.quiz = []
    st.session_state.answers = {}
    st.session_state.submitted = False

# ---------------- GENERATE RANDOM QUIZ ---------------- #
def generate_quiz():
    shuffled_questions = random.sample(QUESTION_BANK, len(QUESTION_BANK))
    quiz = []
    for q, options, correct in shuffled_questions:
        quiz.append((q, random.sample(options, len(options)), correct))
    return quiz

if not st.session_state.quiz:
    st.session_state.quiz = generate_quiz()

# ---------------- QUIZ UI ---------------- #
for i, (question, options, correct) in enumerate(st.session_state.quiz):
    st.subheader(f"Q{i+1}. {question}")

    selected = st.radio(
        "Choose one option:",
        options,
        key=f"q_{i}",
        index=None,
        disabled=st.session_state.submitted
    )

    if selected:
        st.session_state.answers[i] = selected

    if st.session_state.submitted:
        if st.session_state.answers.get(i) == correct:
            st.success("✅ Correct")
        else:
            st.error(f"❌ Wrong | Correct Answer: {correct}")

    st.divider()

# ---------------- SUBMIT ---------------- #
if not st.session_state.submitted:
    if st.button("📊 Submit Exam"):
        st.session_state.submitted = True
        st.rerun()

# ---------------- RESULT ---------------- #
if st.session_state.submitted:
    correct_count = sum(
        1 for i, (_, _, correct) in enumerate(st.session_state.quiz)
        if st.session_state.answers.get(i) == correct
    )

    total = len(st.session_state.quiz)
    wrong_count = total - correct_count

    st.header("📈 Result")
    st.write(f"✅ Correct Answers: **{correct_count}**")
    st.write(f"❌ Incorrect Answers: **{wrong_count}**")
    st.write(f"🎯 Score: **{correct_count}/{total}**")

    if correct_count >= total * 0.5:
        st.success("🎉 PASSED")
    else:
        st.error("❌ FAILED")

    if st.button("🔄 Take Exam Again"):
        st.session_state.quiz = []
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()
