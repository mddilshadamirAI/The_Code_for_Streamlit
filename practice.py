import streamlit as st
import streamlit.components.v1 as components
import random
import math
import json
from collections import defaultdict

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Cyber Arena Infinite Engine",
    page_icon="⚡",
    layout="centered"
)

# ============================================================
# 📦 STATIC TEXTBOOK QUESTION BANK (CLASS 1)
# ============================================================
# Embedded directly so your app works instantly without extra files
STATIC_BANK = {
    "g1_c1": [
        {"question": "A cat is sitting inside a basket and a puppy is playing outside. Where is the cat? Inside(1) or Outside(2)?", "answer": 1, "options": [1, 2, 3, 4]},
        {"question": "A sparrow is sitting on top of a tree, and a snake is at the bottom on the ground. Where is the sparrow? Top(1) or Bottom(2)?", "answer": 1, "options": [1, 2, 3, 4]},
        {"question": "Rohan parks his cycle near the door, and leaves his ball far away. Which object is far from the house? Cycle(1) or Ball(2)?", "answer": 2, "options": [1, 2, 3, 4]},
        {"question": "You are comparing a massive elephant to a tiny garden ant. Which animal is bigger? Elephant(1) or Ant(2)?", "answer": 1, "options": [1, 2, 3, 4]},
        {"question": "Look closely at a round currency coin. What geometric shape does it look like? Circle(1), Triangle(2), Square(3)?", "answer": 1, "options": [1, 2, 3, 4]},
        {"question": "How many sharp corner vertices are present on a standard flat 2D Triangle layout piece?", "answer": 3, "options": [2, 3, 4, 5]},
        {"question": "How many straight equal boundary sides wrap around to form a perfect flat Square cardboard sheet?", "answer": 4, "options": [3, 4, 5, 6]},
        {"question": "A round marble rolls down a ramp, while a rectangular eraser slides down flat. Which object rolls? Marble(1) or Eraser(2)?", "answer": 1, "options": [1, 2, 3, 4]},
        {"question": "Tree A sits closer to the school wall than Tree B. Which tree is sitting farther away? Tree A(1) or Tree B(2)?", "answer": 2, "options": [1, 2, 3, 4]},
        {"question": "Which geometric shape possesses absolutely zero straight sharp corners and is round? Square(1), Triangle(2), Circle(3)?", "answer": 3, "options": [1, 2, 3, 4]}
    ],
    "g1_c2": [
        {"question": "Count all the individual letters spelling out the exact word 'MATH'. How many letters are there?", "answer": 4, "options": [3, 4, 5, 6]},
        {"question": "What fundamental integer value follows directly after the number 5?", "answer": 6, "options": [4, 5, 6, 7]},
        {"question": "What standalone natural number coordinate falls precisely before the entry index 3?", "answer": 2, "options": [1, 2, 3, 4]},
        {"question": "Identify the missing structural integer element that completes the sequence line: 6, 7, __, 9.", "answer": 8, "options": [7, 8, 9, 10]},
        {"question": "Amit holds 3 balloons. Identify which choice represents a value strictly GREATER than 3.", "answer": 5, "options": [1, 2, 3, 5]}
    ],
    "g1_c3": [
        {"question": "Rohan gets 2 red marbles and 3 blue marbles. Compute his grand total marble pool.", "answer": 5, "options": [4, 5, 6, 7]},
        {"question": "Evaluate the elementary arithmetic addition equation result parameters: 4 + 2 = ?", "answer": 6, "options": [5, 6, 7, 8]},
        {"question": "Process the expression values to find the final integrated answer token: 5 + 3 = ?", "answer": 8, "options": [7, 8, 9, 10]}
    ]
}

# ============================================================
# 🚀 INFINITE LIVE ALGORITHMIC QUESTION ENGINE
# ============================================================
USED_QUESTIONS = set()
NAMES = ["Rahul", "Aman", "Priya", "Kabir", "Riya", "Arjun", "Neha", "Sana", "Kunal", "Ananya"]
PLACES = ["Delhi", "Mumbai", "Patna", "Kolkata", "Bangalore", "Chennai", "Hyderabad"]
OBJECTS = ["books", "robots", "machines", "laptops", "packets", "bottles", "devices"]

def generate_options(answer):
    options = {answer}
    while len(options) < 4:
        variance = random.randint(1, max(5, int(abs(answer) * 0.25) + 1))
        fake = answer + random.choice([-1, 1]) * variance
        if fake != answer:
            options.add(fake)
    options = list(options)
    random.shuffle(options)
    return options

class InfiniteQuestionEngine:
    def __init__(self):
        self.generators = defaultdict(list)

    def register(self, chapter_id, func):
        self.generators[chapter_id].append(func)

    def generate(self, chapter_id):
        if chapter_id not in self.generators:
            return self.fallback_question()

        for _ in range(500):
            generator = random.choice(self.generators[chapter_id])
            q = generator()
            q_hash = self.hash_question(q)
            if q_hash not in USED_QUESTIONS:
                USED_QUESTIONS.add(q_hash)
                return q
        return generator()

    def hash_question(self, q):
        return f"{q['question']}_{q['answer']}"

    def fallback_question(self):
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        answer = a + b
        return {
            "question": f"Find the sum of {a} and {b}.",
            "answer": answer,
            "options": generate_options(answer)
        }

engine = InfiniteQuestionEngine()

# --- CLASS 6 GENERATORS ---
def g6_numbers_1():
    a, b = random.randint(1000, 9999), random.randint(1000, 9999)
    person = random.choice(NAMES)
    answer = abs(a - b)
    return {"question": f"{person} found the difference between {a} and {b}. What is the answer?", "answer": answer, "options": generate_options(answer)}

def g6_numbers_2():
    digits = random.sample(range(1, 10), 5)
    greatest = int("".join(map(str, sorted(digits, reverse=True))))
    smallest = int("".join(map(str, sorted(digits))))
    answer = greatest - smallest
    return {"question": f"Using digits {digits}, form the greatest and smallest 5-digit numbers and find their difference.", "answer": answer, "options": generate_options(answer)}

def g6_numbers_3():
    city = random.choice(PLACES)
    a, b = random.randint(20000, 90000), random.randint(20000, 90000)
    answer = a + b
    return {"question": f"A factory in {city} produced {a} machines in January and {b} in February. Find total production.", "answer": answer, "options": generate_options(answer)}

def g6_numbers_4():
    obj = random.choice(OBJECTS)
    total, boxes = random.randint(1000, 5000), random.randint(10, 50)
    answer = total // boxes
    return {"question": f"A warehouse contains {total} {obj}. They are packed equally into {boxes} boxes. How many are in each box?", "answer": answer, "options": generate_options(answer)}

def g6_numbers_5():
    a, b, c = random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)
    answer = math.gcd(math.gcd(a, b), c)
    return {"question": f"Find the HCF of {a}, {b}, and {c}.", "answer": answer, "options": generate_options(answer)}

# --- CLASS 7 GENERATORS ---
def g7_algebra_1():
    x, b = random.randint(2, 20), random.randint(2, 20)
    result = x + b
    return {"question": f"Solve: x + {b} = {result}", "answer": x, "options": generate_options(x)}

def g7_algebra_2():
    x, a, b = random.randint(2, 30), random.randint(2, 10), random.randint(5, 20)
    rhs = (a * x) + b
    return {"question": f"Solve: {a}x + {b} = {rhs}", "answer": x, "options": generate_options(x)}

# --- CLASS 8 GENERATORS ---
def g8_linear_1():
    x, a, b = random.randint(2, 40), random.randint(2, 12), random.randint(1, 20)
    rhs = a * x + b
    return {"question": f"Solve: {a}x + {b} = {rhs}", "answer": x, "options": generate_options(x)}

def g8_linear_2():
    x, a, b = random.randint(2, 25), random.randint(2, 10), random.randint(1, 15)
    lhs = a * x - b
    return {"question": f"Solve: {a}x - {b} = {lhs}", "answer": x, "options": generate_options(x)}

# Register Programmatic Map Links
engine.register("g6_c1", g6_numbers_1)
engine.register("g6_c1", g6_numbers_2)
engine.register("g6_c1", g6_numbers_3)
engine.register("g6_c1", g6_numbers_4)
engine.register("g6_c1", g6_numbers_5)
engine.register("g7_c4", g7_algebra_1)
engine.register("g7_c4", g7_algebra_2)
engine.register("g8_c2", g8_linear_1)
engine.register("g8_c2", g8_linear_2)

# ============================================================
# 🎛️ STREAMLIT CONTROL PANEL INTERFACE
# ============================================================
st.title("⚡ CYBER ARENA DATA ENGINE ⚡")
st.write("Welcome to the infinite quiz pipeline. Select your target chapter below:")

# Sidebar routing controls
st.sidebar.header("🎯 Chapter Selector")
grade_selection = st.sidebar.selectbox(
    "Choose Grade Level:",
    ["Class 1 (Textbook Pool)", "Class 6 (Infinite Math Engine)", "Class 7 (Infinite Math Engine)", "Class 8 (Infinite Math Engine)"]
)

# Chapter routing dictionary maps
chapter_map = {
    "Class 1 (Textbook Pool)": {"g1_c1": "Chapter 1: Shapes & Space", "g1_c2": "Chapter 2: Numbers 1 to 9", "g1_c3": "Chapter 3: Addition Basics"},
    "Class 6 (Infinite Math Engine)": {"g6_c1": "Chapter 1: Knowing Our Numbers"},
    "Class 7 (Infinite Math Engine)": {"g7_c4": "Chapter 4: Simple Equations"},
    "Class 8 (Infinite Math Engine)": {"g8_c2": "Chapter 2: Linear Equations"}
}

selected_chapter_code = st.sidebar.selectbox(
    "Select Chapter Modules:",
    options=list(chapter_map[grade_selection].keys()),
    format_func=lambda x: chapter_map[grade_selection][x]
)

total_questions_to_play = st.sidebar.slider("Number of Arena Rounds:", min_value=5, max_value=50, value=20, step=5)

# ============================================================
# ⚙️ MULTI-PIPELINE CONSOLIDATOR DATA GENERATION
# ============================================================
questions = []

# Router Checks if selected chapter belongs to Algorithmic Engine or Static JSON Bank
if selected_chapter_code in engine.generators:
    # Run the live generation loop to compile custom fresh non-repeating sessions
    for _ in range(total_questions_to_play):
        questions.append(engine.generate(selected_chapter_code))
elif selected_chapter_code in STATIC_BANK:
    # Read straight from the pre-generated textbook data array pool
    available_pool = STATIC_BANK[selected_chapter_code]
    questions = random.sample(available_pool, min(total_questions_to_play, len(available_pool)))
else:
    # Safety fallback mechanism
    for _ in range(total_questions_to_play):
        questions.append(engine.fallback_question())

question_json = json.dumps(questions)

# ============================================================
# 🎨 EMBEDDED HIGH-PERFORMANCE HTML/JS VIEW ENGINE
# ============================================================
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    background: #020617;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    text-align: center;
    margin: 0;
    padding: 10px;
}}

.question-box {{
    width: 90%;
    max-width: 600px;
    margin: auto;
    margin-top: 20px;
    background: #111827;
    padding: 25px;
    border-radius: 20px;
    border: 2px solid #06b6d4;
    box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
}}

.option-btn {{
    display: block;
    width: 100%;
    margin: 12px auto;
    padding: 16px;
    background: #1e293b;
    color: #38bdf8;
    border: 1px solid #06b6d4;
    border-radius: 12px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.2s ease;
    text-align: center;
}}

.option-btn:hover {{
    background: #06b6d4;
    color: white;
    transform: scale(1.02);
}}

.score {{
    font-size: 22px;
    color: #22d3ee;
    margin-top: 20px;
    letter-spacing: 1px;
}}
</style>
</head>
<body>

<div class="question-box">
    <h2 id="question" style="min-height: 70px; font-size: 20px;"></h2>
    
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    
    <h3 class="score" id="score">Score: 0</h3>
</div>

<script>
// Parse data directly from Python Pipeline safely via JSON string serialization
const QUESTIONS = {question_json};

let currentIndex = 0;
let score = 0;

function loadQuestion() {{
    if(QUESTIONS.length === 0) {{
        document.body.innerHTML = `
        <div class="question-box">
            <h1 style='color:#ef4444'>⚠️ ENGINE EMPTY</h1>
            <h2>No questions compiled for this subset target.</h2>
        </div>`;
        return;
    }}

    if(currentIndex >= QUESTIONS.length) {{
        document.body.innerHTML = `
        <div class="question-box" style="border-color: #10b981;">
            <h1 style='color:#10b981'>🏆 ARENA COMPLETED</h1>
            <h2>Final Result Score: <span style="color:#22d3ee">${{score}}</span> / ${{QUESTIONS.length}}</h2>
            <p style="color: #64748b;">Adjust sidebar filters to run a new round generation simulation!</p>
        </div>`;
        return;
    }}

    let q = QUESTIONS[currentIndex];
    document.getElementById("question").innerText = q.question;
    let buttons = document.getElementsByClassName("option-btn");
    
    for(let i = 0; i < 4; i++) {{
        if(q.options && q.options[i] !== undefined) {{
            buttons[i].innerText = q.options[i];
            buttons[i].style.display = "block";
        } else {{
            buttons[i].style.display = "none";
        }
    }}
}}

function checkAnswer(btn) {{
    let selected = btn.innerText.trim();
    let correct = String(QUESTIONS[currentIndex].answer).trim();

    // Check both numeric equivalent evaluations string-wise safely
    if(selected === correct || Number(selected) === Number(correct)) {{
        score++;
    }}
    
    document.getElementById("score").innerText = "Score: " + score;
    currentIndex++;
    loadQuestion();
}}

// Initialize setup script execution loops
loadQuestion();
</script>

</body>
</html>
"""

# Render application UI layers securely inside Streamlit frames
components.html(html_code, height=650, scrolling=False)
