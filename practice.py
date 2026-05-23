import streamlit as st
import streamlit.components.v1 as components
import json
import random

# ============================================================
# 📦 EXTERNAL DATA COUPLING
# ============================================================
# Import the master question matrix directly from your custom vault
from database import TEXTBOOK_DB

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Cyber Arena Exhaustive Textbook Engine",
    page_icon="⚡",
    layout="centered"
)

# ============================================================
# 🎛️ STREAMLIT CONTROL PANEL & ROUTER
# ============================================================
st.title("⚡ CYBER ARENA TEXTBOOK ENGINE ⚡")
st.write("Production-grade question matrix pulled directly from NCERT and RS Aggarwal curricula.")

st.sidebar.header("🎯 Target Matrix Router")
grade_selection = st.sidebar.selectbox(
    "Choose Textbook Grade Matrix:",
    options=list(TEXTBOOK_DB.keys())
)

chapter_selection = st.sidebar.selectbox(
    "Select Chapter Modules:",
    options=list(TEXTBOOK_DB[grade_selection].keys())
)

# Fetch the specific textbook question list from the database
active_question_pool = TEXTBOOK_DB[grade_selection][chapter_selection]

# Shuffle and slice based on what the user chooses to play
total_available = len(active_question_pool)
total_questions_to_play = st.sidebar.slider(
    "Number of Arena Rounds:", 
    min_value=1, 
    max_value=total_available, 
    value=min(5, total_available)
)

compiled_questions = random.sample(active_question_pool, total_questions_to_play)
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
    <h2 id="question" style="min-height: 90px; font-size: 19px; line-height: 1.5; padding: 0 10px;"></h2>
    
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
            <h2>Final Result Score: <span style="color:#22d3ee">\${score}</span> / \${{QUESTIONS.length}}</h2>
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
