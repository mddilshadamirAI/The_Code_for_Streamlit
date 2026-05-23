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
# 🚀 INFINITE LIVE ALGORITHMIC QUESTION ENGINE
# ============================================================
USED_QUESTIONS = set()
NAMES = ["Rahul", "Aman", "Priya", "Kabir", "Riya", "Arjun", "Neha", "Sana", "Kunal", "Ananya"]
PLACES = ["Delhi", "Mumbai", "Patna", "Kolkata", "Bangalore", "Chennai", "Hyderabad"]
OBJECTS = ["books", "robots", "machines", "laptops", "packets", "bottles", "devices"]
FRUITS = ["apples", "bananas", "mangoes", "oranges", "cherries"]

def generate_options(answer, step=1):
    """Generates 4 unique options including the correct answer."""
    options = {answer}
    while len(options) < 4:
        variance = random.randint(1, max(5, int(abs(answer) * 0.25) + 1)) * step
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

    def generate(self, chapter_id, sample_size=20):
        if chapter_id not in self.generators:
            return [self.fallback_question() for _ in range(sample_size)]
        
        session_questions = []
        # Attempt to gather highly unique non-repeating questions
        for _ in range(sample_size):
            chosen_func = random.choice(self.generators[chapter_id])
            q = None
            for _ in range(100):  # Retry loop to maintain unique hashes
                candidate = chosen_func()
                q_hash = f"{candidate['question']}_{candidate['answer']}"
                if q_hash not in USED_QUESTIONS:
                    USED_QUESTIONS.add(q_hash)
                    q = candidate
                    break
            if q is None:
                q = chosen_func()  # Fallback to avoid empty entries
            session_questions.append(q)
        return session_questions

    def fallback_question(self):
        a, b = random.randint(10, 100), random.randint(10, 100)
        answer = a + b
        return {
            "question": f"Find the sum of {a} and {b}.",
            "answer": answer,
            "options": generate_options(answer)
        }

engine = InfiniteQuestionEngine()

# ============================================================
# 📚 CLASS-BY-CLASS MATHEMATICAL GENERATORS (GRADES 1-8)
# ============================================================

# --- CLASS 1 ---
def g1_shapes():
    shapes = [("Circle", "0"), ("Triangle", "3"), ("Square", "4")]
    pick = random.choice(shapes)
    return {"question": f"How many straight sides/corners does a flat 2D {pick[0]} layout piece have?", "answer": int(pick[1]), "options": [0, 3, 4, 5]}

def g1_counting():
    count = random.randint(2, 9)
    fruit = random.choice(FRUITS)
    name = random.choice(NAMES)
    return {"question": f"{name} has {count} {fruit} in a basket. If you count them one by one, how many are there in total?", "answer": count, "options": generate_options(count)}

# --- CLASS 2 ---
def g2_place_value():
    tens = random.randint(1, 9)
    ones = random.randint(0, 9)
    answer = (tens * 10) + ones
    return {"question": f"What complete number is made of exactly {tens} Tens and {ones} Ones?", "answer": answer, "options": generate_options(answer)}

def g2_subtraction():
    a = random.randint(10, 99)
    b = random.randint(1, a - 1)
    answer = a - b
    return {"question": f"Subtract the small value from the large value: {a} - {b} = ?", "answer": answer, "options": generate_options(answer)}

# --- CLASS 3 ---
def g3_multiplication():
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    answer = a * b
    return {"question": f"Evaluate the product multiplication array parameters: {a} x {b} = ?", "answer": answer, "options": generate_options(answer)}

def g3_measurement():
    m = random.randint(2, 9)
    answer = m * 100
    return {"question": f"Convert the metric distance from meters into centimeters: {m} meters = ___ cm.", "answer": answer, "options": generate_options(answer, step=100)}

# --- CLASS 4 ---
def g4_large_numbers():
    base = random.randint(1000, 9000)
    step = random.choice([10, 100, 1000])
    answer = base + step
    return {"question": f"What specific number coordinate is exactly {step} more than {base}?", "answer": answer, "options": generate_options(answer)}

def g4_fractions():
    denom = random.choice([4, 6, 8, 10])
    num = random.randint(1, denom - 1)
    rem = denom - num
    return {"question": f"Rohan ate {num}/{denom} of a cake pizza layout. What remaining fraction is left untouched over {denom}?", "answer": rem, "options": generate_options(rem)}

# --- CLASS 5 ---
def g5_decimals():
    a = round(random.uniform(1.1, 9.9), 1)
    b = round(random.uniform(1.1, 9.9), 1)
    answer = round(a + b, 1)
    return {"question": f"Add the decimal float expressions cleanly: {a} + {b} = ?", "answer": float(answer), "options": [float(answer), round(answer+0.5, 1), round(answer-0.3, 1), round(answer+1.1, 1)]}

def g5_perimeter():
    length = random.randint(5, 25)
    width = random.randint(5, 25)
    answer = 2 * (length + width)
    return {"question": f"Find the perimeter boundary of a rectangle with length = {length} cm and width = {width} cm.", "answer": answer, "options": generate_options(answer)}

# --- CLASS 6 ---
def g6_numbers():
    a, b = random.randint(1000, 9999), random.randint(1000, 9999)
    return {"question": f"Find the absolute difference variance gap between {a} and {b}.", "answer": abs(a - b), "options": generate_options(abs(a - b))}

def g6_hcf():
    a, b = random.randint(20, 100), random.randint(20, 100)
    answer = math.gcd(a, b)
    return {"question": f"Find the Highest Common Factor (HCF) of {a} and {b}.", "answer": answer, "options": generate_options(answer)}

# --- CLASS 7 ---
def g7_integers():
    a = random.randint(-50, -10)
    b = random.randint(10, 50)
    answer = a + b
    return {"question": f"Evaluate the negative integer coordinate equation: ({a}) + ({b}) = ?", "answer": answer, "options": generate_options(answer)}

def g7_equations():
    x = random.randint(2, 20)
    b = random.randint(2, 20)
    rhs = x + b
    return {"question": f"Solve the algebraic expression parameter for x: x + {b} = {rhs}", "answer": x, "options": generate_options(x)}

# --- CLASS 8 ---
def g8_linear():
    x = random.randint(2, 25)
    a = random.randint(2, 10)
    b = random.randint(1, 15)
    rhs = (a * x) + b
    return {"question": f"Solve the linear equation configuration for x: {a}x + {b} = {rhs}", "answer": x, "options": generate_options(x)}

def g8_exponents():
    base = random.choice([2, 3, 5])
    pwr = random.choice([2, 3, 4])
    answer = int(math.pow(base, pwr))
    return {"question": f"Evaluate the structural exponential notation value: {base} raised to the power of {pwr} ({base}^{pwr})", "answer": answer, "options": generate_options(answer)}

# ============================================================
# ⚙️ REGISTRATION MAPPING PIPELINES
# ============================================================
engine.register("g1_c1", g1_shapes)
engine.register("g1_c2", g1_counting)
engine.register("g2_c1", g2_place_value)
engine.register("g2_c2", g2_subtraction)
engine.register("g3_c1", g3_multiplication)
engine.register("g3_c2", g3_measurement)
engine.register("g4_c1", g4_large_numbers)
engine.register("g4_c2", g4_fractions)
engine.register("g5_c1", g5_decimals)
engine.register("g5_c2", g5_perimeter)
engine.register("g6_c1", g6_numbers)
engine.register("g6_c2", g6_hcf)
engine.register("g7_c1", g7_integers)
engine.register("g7_c2", g7_equations)
engine.register("g8_c1", g8_linear)
engine.register("g8_c2", g8_exponents)

# ============================================================
# 🎛️ STREAMLIT UX INTERFACE LAYER
# ============================================================
st.title("⚡ CYBER ARENA INFINITE ENGINE ⚡")
st.write("Generating high-volume algorithmic questions across standard pipelines natively.")

st.sidebar.header("🎯 Target Matrix Router")
grade_selection = st.sidebar.selectbox(
    "Choose Grade Level:",
    [f"Class {i}" for i in range(1, 9)]
)

chapter_map = {
    "Class 1": {"g1_c1": "Chapter 1: Shapes & Spaces", "g1_c2": "Chapter 2: Counting & Quantities"},
    "Class 2": {"g2_c1": "Chapter 1: Place Value Dynamics", "g2_c2": "Chapter 2: Subtraction Systems"},
    "Class 3": {"g3_c1": "Chapter 1: Multiplication Frameworks", "g3_c2": "Chapter 2: Metric Transformations"},
    "Class 4": {"g4_c1": "Chapter 1: Advanced Large Values", "g4_c2": "Chapter 2: Fractional Partitioning"},
    "Class 5": {"g5_c1": "Chapter 1: Decimal System Floating", "g5_c2": "Chapter 2: Planar Geometries Perimeter"},
    "Class 6": {"g6_c1": "Chapter 1: Knowing Our Numbers", "g6_c2": "Chapter 2: Factors, HCF & LCM"},
    "Class 7": {"g7_c1": "Chapter 1: Signed Integer Matrices", "g7_c2": "Chapter 2: Algebraic Simple Equations"},
    "Class 8": {"g8_c1": "Chapter 1: Linear Variable Equations", "g8_c2": "Chapter 2: Exponential Component Powers"}
}

selected_chapter_code = st.sidebar.selectbox(
    "Select Chapter Modules:",
    options=list(chapter_map[grade_selection].keys()),
    format_func=lambda x: chapter_map[grade_selection][x]
)

total_questions_to_play = st.sidebar.slider("Number of Arena Rounds:", min_value=5, max_value=50, value=15, step=5)

# Generate current live pipeline session questions 
compiled_questions = engine.generate(selected_chapter_code, sample_size=total_questions_to_play)
question_json = json.dumps(compiled_questions)

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
            <h2>Final Result Score: <span style="color:#22d3ee">\${{score}}</span> / \${{QUESTIONS.length}}</h2>
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
        }} else {{
            buttons[i].style.display = "none";
        }}
    }}
}}

function checkAnswer(btn) {{
    let selected = btn.innerText.trim();
    let correct = String(QUESTIONS[currentIndex].answer).trim();

    if(selected === correct || Number(selected) === Number(correct)) {{
        score++;
    }}
    
    document.getElementById("score").innerText = "Score: " + score;
    currentIndex++;
    loadQuestion();
}}

loadQuestion();
</script>

</body>
</html>
"""

components.html(html_code, height=650, scrolling=False)
