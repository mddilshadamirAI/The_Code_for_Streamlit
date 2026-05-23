import streamlit as st
import streamlit.components.v1 as components
import json
import random
import base64
import os

# ============================================================
# 📦 EXTERNAL DATA COUPLING & AUDIO LOADER
# ============================================================
from database import TEXTBOOK_DB

def load_audio_as_base64(file_name):
    """Safely converts local MP3 files to base64 for embedding directly inside the HTML iframe."""
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            data = f.read()
        return f"data:audio/mp3;base64,{base64.b64encode(data).decode()}"
    return ""

# Convert your audio assets
correct_audio_uri = load_audio_as_base64("faa.mp3")
wrong_audio_uri = load_audio_as_base64("haha.mp3")

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
    value=min(10, total_available)  # 🧠 Defaulting to 10 rounds per session!
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
    overflow-x: hidden;
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
    box-shadow: 0 0 20px rgba(6, 182, 212, 0.15);
    position: relative;
    transition: all 0.3s ease;
}}

.option-btn {{
    display: block;
    width: 100%;
    margin: 14px auto;
    padding: 16px;
    background: #1e293b;
    color: #38bdf8;
    border: 1px solid #06b6d4;
    border-radius: 12px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    text-align: center;
    outline: none;
}}

.option-btn:hover:not([disabled]) {{
    background: #06b6d4;
    color: white;
    transform: scale(1.02);
    box-shadow: 0 0 10px rgba(6, 182, 212, 0.4);
}}

/* Dynamic Action States */
.correct-flash {{
    background: #10b981 !important;
    color: white !important;
    border-color: #059669 !important;
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.6);
}}

.wrong-flash {{
    background: #ef4444 !important;
    color: white !important;
    border-color: #dc2626 !important;
    box-shadow: 0 0 15px rgba(239, 68, 68, 0.6);
}}

.score {{
    font-size: 22px;
    color: #22d3ee;
    margin-top: 25px;
    letter-spacing: 1px;
    font-weight: bold;
}}

/* Floating Animation Elements */
.emoji-particle {{
    position: absolute;
    bottom: -50px;
    pointer-events: none;
    z-index: 999;
    animation: floatUp 3s ease-out forwards;
}}

@keyframes floatUp {{
    0% {{
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }}
    100% {{
        transform: translateY(-700px) rotate(360deg);
        opacity: 0;
    }}
}}
</style>
</head>
<body>

<div class="question-box" id="arena-card">
    <h2 id="question" style="min-height: 90px; font-size: 20px; line-height: 1.5; padding: 0 10px; color: #f8fafc;"></h2>
    
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    <button class="option-btn" onclick="checkAnswer(this)"></button>
    
    <h3 class="score" id="score-display">Score: 0</h3>
</div>

<script>
const QUESTIONS = {question_json};
const audioCorrect = new Audio("{correct_audio_uri}");
const audioWrong = new Audio("{wrong_audio_uri}");

let currentIndex = 0;
let score = 0;
let canClick = true;

function loadQuestion() {{
    canClick = true;
    
    if(QUESTIONS.length === 0) {{
        document.body.innerHTML = `
        <div class="question-box">
            <h1 style='color:#ef4444'>⚠️ ENGINE EMPTY</h1>
            <h2>No questions compiled for this subset target.</h2>
        </div>`;
        return;
    }}

    if(currentIndex >= QUESTIONS.length) {{
        renderFinalScreen();
        return;
    }}

    let q = QUESTIONS[currentIndex];
    document.getElementById("question").innerText = q.question;
    let buttons = document.getElementsByClassName("option-btn");
    
    for(let i = 0; i < 4; i++) {{
        if(q.options && q.options[i] !== undefined) {{
            buttons[i].innerText = q.options[i];
            buttons[i].className = "option-btn"; // Reset color classes
            buttons[i].style.display = "block";
            buttons[i].removeAttribute("disabled");
        }} else {{
            buttons[i].style.display = "none";
        }}
    }}
}}

function checkAnswer(btn) {{
    if (!canClick) return;
    canClick = false; // Block multiple rapid taps

    let selected = btn.innerText.trim();
    let correct = String(QUESTIONS[currentIndex].answer).trim();
    let isCorrect = (selected === correct || Number(selected) === Number(correct));
    
    // Disable all options during feedback window
    let buttons = document.getElementsByClassName("option-btn");
    for(let b of buttons) b.setAttribute("disabled", "true");

    if(isCorrect) {{
        score++;
        btn.classList.add("correct-flash");
        if(audioCorrect.src) audioCorrect.play().catch(e => console.log("Audio play error:", e));
    }} else {{
        btn.classList.add("wrong-flash");
        if(audioWrong.src) audioWrong.play().catch(e => console.log("Audio play error:", e));
        
        // Show the student the right answer instantly by turning it green
        for(let b of buttons) {{
            if(b.innerText.trim() === correct || Number(b.innerText.trim()) === Number(correct)) {{
                b.classList.add("correct-flash");
            }}
        }}
    }}
    
    document.getElementById("score-display").innerText = "Score: " + score;
    currentIndex++;
    
    // Smooth transition delay so they can learn from feedback
    setTimeout(loadQuestion, 800);
}}

function renderFinalScreen() {{
    let isEpicWin = (score >= 9);
    let finalHTML = `
    <div class="question-box" style="border-color: ${{isEpicWin ? '#10b981' : '#06b6d4'}}; box-shadow: 0 0 25px ${{isEpicWin ? 'rgba(16,185,129,0.3)' : 'rgba(6,182,212,0.2)'}};">
        <h1 style="color: ${{isEpicWin ? '#10b981' : '#22d3ee'}}; margin-bottom: 5px;">
            ${{isEpicWin ? '🏆 MASTER UNLOCKED 🏆' : '🏁 ARENA COMPLETED'}}
        </h1>
        <h2 style="font-size: 26px; margin-top: 10px;">Final Result Score: <span style="color:#22d3ee">\${score}</span> / \${QUESTIONS.length}</h2>
        <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">
            ${{isEpicWin ? 'Absolutely legendary performance! You have completely crushed this chapter.' : 'Good run! Adjust sidebar filters to run a new round generation simulation!'}}
        </p>
    </div>`;
    
    document.body.innerHTML = finalHTML;

    // Trigger Clapping visual effect engine if score is 9 or higher
    if (isEpicWin) {{
        triggerClaps();
    }}
}}

function triggerClaps() {{
    const emojis = ['👏', '🎉', '✨', '🔥'];
    for (let i = 0; i < 35; i++) {{
        setTimeout(() => {{
            const particle = document.createElement('div');
            particle.className = 'emoji-particle';
            particle.innerText = emojis[Math.floor(Math.random() * emojis.length)];
            particle.style.left = Math.random() * 100 + 'vw';
            particle.style.fontSize = (Math.random() * 20 + 24) + 'px';
            document.body.appendChild(particle);
            
            // Cleanup memory safely after animation completes
            setTimeout(() => particle.remove(), 3000);
        }}, i * 80);
    }}
}}

loadQuestion();
</script>

</body>
</html>
"""

components.html(html_code, height=650, scrolling=False)
