import streamlit as st
import random

st.set_page_config(page_title="Design Thinking MCQ Exam", layout="wide")
st.title("📝 Design Thinking – Full MCQ Examination (40 Questions)")

# ================= QUESTION BANK ================= #
QUESTION_BANK = [

# ================= WEEK 1 (10) ================= #
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
"Which of the following tools is commonly used to capture and organize thoughts, insights, and ideas during design thinking exercises?",
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

(
"What is the first step of Design Thinking?",
[
"Empathize",
"Define",
"Ideate",
"Test"
],
"Empathize"
),

# ================= WEEK 2 (10) ================= #
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
"A restaurant is receiving customer complaints about slow service during peak hours. What is the impact of solving understaffing?",
[
"Improved customer satisfaction and loyalty",
"Higher prices for menu items",
"Increased advertising",
"Expansion of the restaurant"
],
"Improved customer satisfaction and loyalty"
),

# ================= WEEK 3 (10) ================= #
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
"How does the story of the five blind men and the elephant relate to problem-solving?",
[
"It emphasizes the need for trial and error",
"It suggests that only experts can solve complex problems",
"It shows that problems can have multiple correct solutions",
"It highlights the importance of understanding the whole picture"
],
"It highlights the importance of understanding the whole picture"
),

(
"In applying TRIZ to enhance customer service, which Inventive Principle is most suitable?",
[
"Segmentation",
"Prior Action",
"Termination",
"The Other Way Round"
],
"Prior Action"
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
"To grant a patent",
"To license technology"
],
"To trigger an idea to solve the problem"
),

(
"Which activity is NOT part of the Solve phase?",
[
"Brainstorming",
"Conducting user interviews",
"Using TRIZ methodology",
"Collaborative team effort"
],
"Conducting user interviews"
),

(
"How does the Solve phase address bias?",
[
"Relying on experts",
"Involving a diverse team",
"Avoiding feedback",
"Skipping prototyping"
],
"Involving a diverse team"
),

# ================= WEEK 4 (10) ================= #
(
"What is the purpose of prototyping in Design Thinking?",
[
"To test and refine the product through user feedback",
"To deploy the first 100 products",
"To solve future technology problems",
"To generate revenue"
],
"To test and refine the product through user feedback"
),

(
"Why do we need to test assumptions?",
[
"We may not know everything about a customer",
"We may not have budget",
"We may lack technical skills",
"We may not know answers"
],
"We may not know everything about a customer"
),

(
"What are some key elements needed before testing ideas?",
[
"Sticky notes",
"End products",
"Competitor lists",
"List of features, assumptions, and simple prototypes"
],
"List of features, assumptions, and simple prototypes"
),

(
"Prototypes can be made out of:",
[
"Clay",
"Product design tools",
"Marshmallows and spaghetti",
"Paper and cardboard boxes"
],
"Clay"
),

(
"How does the Test Phase contribute to innovation?",
[
"Generating revenue",
"Creative thinking",
"Validating ideas with users",
"Generating ideas"
],
"Validating ideas with users"
),

(
"How does the Test Phase help validate assumptions?",
[
"Confirming users like the design",
"Ensuring the design solves the problem",
"Brand alignment",
"Competitor comparison"
],
"Ensuring the design solves the problem"
),

(
"What role does iteration play in the Test Phase?",
[
"Iteration is not required",
"Repeating the entire process",
"Making small adjustments based on feedback",
"Only if prototype fails"
],
"Making small adjustments based on feedback"
),

(
"Understanding audience preferences stage?",
[
"HMWs",
"5WHY",
"CJM",
"W-H questions"
],
"CJM"
),

(
"Customers’ needs are written down in which phase?",
[
"Empathize",
"Analyze",
"Solve",
"Test"
],
"Analyze"
),

(
"Thinking of many ideas happens in which step?",
[
"Silent brainstorming",
"Prototyping",
"Problem framing",
"Persona creation"
],
"Silent brainstorming"
),
]

# ================= SESSION STATE ================= #
if "quiz" not in st.session_state:
    st.session_state.quiz = random.sample(QUESTION_BANK, len(QUESTION_BANK))
    st.session_state.answers = {}
    st.session_state.submitted = False

# ================= QUIZ UI ================= #
for i, (q, options, correct) in enumerate(st.session_state.quiz):
    st.subheader(f"Q{i+1}. {q}")
    choice = st.radio("Choose one option:", options, key=f"q_{i}", index=None,
                      disabled=st.session_state.submitted)
    if choice:
        st.session_state.answers[i] = choice

    if st.session_state.submitted:
        if st.session_state.answers.get(i) == correct:
            st.success("✅ Correct")
        else:
            st.error(f"❌ Wrong | Correct Answer: {correct}")

    st.divider()

# ================= SUBMIT ================= #
if not st.session_state.submitted:
    if st.button("📊 Submit Exam"):
        st.session_state.submitted = True
        st.rerun()

# ================= RESULT ================= #
if st.session_state.submitted:
    correct = sum(
        1 for i, (_, _, ans) in enumerate(st.session_state.quiz)
        if st.session_state.answers.get(i) == ans
    )
    total = len(st.session_state.quiz)

    st.header("📈 Result")
    st.write(f"✅ Correct: **{correct}**")
    st.write(f"❌ Incorrect: **{total - correct}**")
    st.write(f"🎯 Score: **{correct}/{total}**")

    if st.button("🔄 Take Exam Again"):
        st.session_state.clear()
        st.rerun()
