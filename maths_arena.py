import streamlit as st
import streamlit.components.v1 as components
import base64

# Layout configurations
st.set_page_config(page_title="Dilshad's Cyber Arena 2D", page_icon="👑", layout="centered")

# --- UI STYLING ---
st.markdown("""
<style>
div[data-testid="stAppViewContainer"] { background: radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important; }
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- NAME CREDIT ---
st.markdown("<h1 style='text-align: center; color: #ffffff; font-family: system-ui, sans-serif; font-weight: 900; letter-spacing: -2px; text-shadow: 0 0 20px rgba(168,85,247,0.4); margin-bottom:0px;'>⚡ CYBER ARENA 2D ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #06b6d4; font-family: monospace; font-size: 14px; margin-top:6px; margin-bottom: 0px; font-weight: 900; letter-spacing: 2px; text-shadow: 0 0 10px rgba(6,182,212,0.6);'>🚀 DEVELOPED BY MD DILSHAD AMIR</p>", unsafe_allow_html=True)

def load_local_audio_base64(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            return f"data:audio/mp3;base64,{base64.b64encode(audio_file.read()).decode('utf-8')}"
    except: return ""

right_answer_audio = load_local_audio_base64("faa.mp3")
wrong_answer_audio = load_local_audio_base64("haha.mp3")
background_music = load_local_audio_base64("newmusic.mp3")

raw_template_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
    body, html { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; display: flex; justify-content: center; align-items: center; background: transparent; font-family: 'Courier New', Courier, monospace; }
    .arena-viewport { position: relative; width: 480px; height: 640px; display: flex; justify-content: center; align-items: center; border-radius: 40px; box-shadow: 0 0 40px rgba(6, 182, 212, 0.15); transition: 0.1s; }
    #three-canvas { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; border-radius: 40px; }
    .game-console { position: relative; z-index: 2; width: 90%; height: 94%; background: rgba(4, 10, 26, 0.65); backdrop-filter: blur(25px); border-radius: 36px; padding: 30px; box-sizing: border-box; border: 1px solid rgba(168, 85, 247, 0.25); display: flex; flex-direction: column; justify-content: space-between; box-shadow: inset 0 0 30px rgba(168, 85, 247, 0.1), 0 25px 60px rgba(0,0,0,0.8); }
    .hud-header { display: flex; justify-content: space-between; color: #94a3b8; font-size: 11px; letter-spacing: 1px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding-bottom: 10px; }
    .score-glow { color: #06b6d4; font-weight: 900; font-size: 18px; text-shadow: 0 0 12px #06b6d4; }
    .question-deck { width: 100%; background: linear-gradient(180deg, rgba(15, 23, 42, 0.9) 0%, rgba(2, 6, 23, 0.95) 100%); border-radius: 24px; border: 1px solid rgba(6, 182, 212, 0.25); padding: 25px 10px; text-align: center; }
    #question-text { font-size: 46px; color: #ffffff; font-weight: 900; text-shadow: 0 0 15px rgba(255, 255, 255, 0.3); }
    .orbit-container { position: relative; width: 100%; height: 310px; display: flex; justify-content: center; align-items: center; }
    .orbit-rotor-2d { position: absolute; width: 230px; height: 230px; border-radius: 50%; border: 2px dashed rgba(6, 182, 212, 0.15); display: flex; justify-content: center; align-items: center; animation: spin2D 16s linear infinite; }
    @keyframes spin2D { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    @keyframes keepUpright { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }
    .option-node-2d { position: absolute; width: 76px; height: 76px; background: radial-gradient(circle at 30% 30%, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.98) 100%); border: 1px solid rgba(6, 182, 212, 0.4); border-radius: 50%; color: #38bdf8; font-size: 24px; font-weight: 900; display: flex; justify-content: center; align-items: center; cursor: pointer; transition: all 0.2s; }
    .opt-0 { top: -38px; left: 77px; } .opt-1 { top: 77px; right: -38px; } .opt-2 { bottom: -38px; left: 77px; } .opt-3 { top: 77px; left: -38px; }
    .orbit-rotor-2d .option-node-2d { animation: keepUpright 16s linear infinite; }
    .option-node-2d:hover { transform: scale(1.15); background: #06b6d4; color: #fff; border-color: #fff; }
    #ui-overlay { position:absolute; z-index:10; background:rgba(0,0,0,0.95); width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; border-radius:40px; }
    .mode-btn { margin: 10px; padding: 15px 30px; font-family: monospace; font-weight:900; cursor:pointer; background:#1e293b; color:#38bdf8; border:2px solid #06b6d4; border-radius:10px; transition:0.3s; }
    .mode-btn:hover { background:#06b6d4; color:#fff; }
    .hit-flash { animation: shake 0.2s linear; border: 2px solid #ef4444 !important; }
    @keyframes shake { 0%, 100% {transform: translateX(0);} 25% {transform: translateX(-10px);} 75% {transform: translateX(10px);} }
    /* Dragon & Lion Animations */
    #cinematic-overlay { position:absolute; top:0; left:0; width:100%; height:100%; z-index:20; display:none; pointer-events:none; }
    .dragon-eyes { font-size: 100px; color: red; animation: blink 0.5s infinite; text-shadow: 0 0 50px red; }
    .lion-roar { font-size: 60px; color: gold; animation: popIn 0.5s ease-out; }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    @keyframes popIn { 0% { transform: scale(0); } 100% { transform: scale(1); } }
</style>
</head>
<body>
<div class="arena-viewport" id="viewport">
    <canvas id="three-canvas"></canvas>
    <div id="ui-overlay">
        <h2 style="color:#fff; margin-bottom:20px;">SELECT DIFFICULTY</h2>
        <button class="mode-btn" onclick="selectMode('basic')">BASIC</button>
        <button class="mode-btn" onclick="selectMode('medium')">MEDIUM</button>
        <button class="mode-btn" onclick="selectMode('pro')">PRO</button>
    </div>
    <div class="game-console" id="console-box">
        <div class="hud-header">
            <div>LVL: <span id="lvl-val">1</span> | T: <span id="timer-val">0</span>s | <span id="combo-val" style="color:#f59e0b">x0</span></div>
            <div>SCORE: <span id="score-val" class="score-glow">0</span> | LIVES: <span id="life-val" style="color:red">2</span></div>
        </div>
        <div class="question-deck"><div id="question-text">CORE READY</div></div>
        <div class="orbit-container">
            <div class="orbit-rotor-2d" id="wheel-axis">
                <div class="option-node-2d opt-0" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-1" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-2" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-3" onclick="verifyChoice(this)">0</div>
            </div>
        </div>
    </div>
</div>
<script>
    const RIGHT_AUDIO = "%%RIGHT_AUDIO_REPLACE%%"; const WRONG_AUDIO = "%%WRONG_AUDIO_REPLACE%%"; const BG_AUDIO = "%%BG_AUDIO_REPLACE%%";
    let score = 0, level = 1, combo = 0, lives = 2, isGameOver = false, targetAnswer = 0, userMode = null, timerInterval = null;

    const bgAudio = new Audio(BG_AUDIO); bgAudio.loop = true; bgAudio.volume = 0.3;
    document.addEventListener('click', () => bgAudio.play().catch(e=>{}));
    function playAudio(src) { if(src.length > 50) new Audio(src).play(); }

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(65, 480/640, 0.1, 1000); camera.position.z = 18;
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('three-canvas'), antialias: true, alpha: true });
    renderer.setSize(480, 640);
    const geom = new THREE.BufferGeometry();
    const pos = new Float32Array(1200); for(let i=0; i<1200; i++) pos[i] = (Math.random()-0.5)*45;
    geom.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    const mat = new THREE.PointsMaterial({ size: 0.4, color: 0xa855f7 });
    const pts = new THREE.Points(geom, mat); scene.add(pts);
    function animate() { requestAnimationFrame(animate); pts.rotation.y += 0.004; renderer.render(scene, camera); }
    animate();

    function selectMode(mode) { userMode = mode; document.getElementById("ui-overlay").style.display = 'none'; renderMatchStage(); }

    function startTimer(seconds) {
        clearInterval(timerInterval);
        document.getElementById("timer-val").innerText = seconds;
        timerInterval = setInterval(() => {
            seconds--;
            document.getElementById("timer-val").innerText = seconds;
            if (seconds <= 0) { lives = 0; triggerGameOver("TIME UP!"); }
        }, 1000);
    }

    function generateUniqueProblem() {
        let range = userMode === 'basic' ? 50 : (userMode === 'medium' ? 100 : 200);
        let pool = userMode === 'basic' ? ['+', '-'] : (userMode === 'medium' ? ['+', '-', '*'] : ['+', '-', '*', '/']);
        let op = pool[Math.floor(Math.random()*pool.length)];
        let n1, n2, val, eq;
        if (op === '+') { n1=Math.floor(Math.random()*range); n2=Math.floor(Math.random()*range); eq=n1+"+"+n2; val=n1+n2; }
        else if (op === '-') { n1=Math.floor(Math.random()*range)+10; n2=Math.floor(Math.random()*(n1-10)); eq=n1+"-"+n2; val=n1-n2; }
        else if (op === '*') { n1=Math.floor(Math.random()*20); n2=Math.floor(Math.random()*12); eq=n1+"×"+n2; val=n1*n2; }
        else { n2=Math.floor(Math.random()*10)+2; val=Math.floor(Math.random()*15)+2; n1=n2*val; eq=n1+"÷"+n2; }
        startTimer((op === '*' || op === '/') ? 45 : 20);
        return { text: eq, answer: val };
    }

    function renderMatchStage() {
        if(isGameOver) return;
        const prob = generateUniqueProblem();
        targetAnswer = prob.answer;
        document.getElementById("question-text").innerText = prob.text;
        let opts = new Set([targetAnswer]);
        while(opts.size < 4) opts.add(targetAnswer + Math.floor(Math.random()*20)-10);
        let arr = Array.from(opts).sort(() => Math.random()-0.5);
        let slots = document.getElementsByClassName("option-node-2d");
        for(let i=0; i<4; i++) slots[i].innerText = arr[i];
    }

    function checkMilestone(score) {
    if (score > 0 && score % 100 === 0) {
        const overlay = document.getElementById("cinematic-overlay");
        overlay.style.display = "flex";
        overlay.style.alignItems = "center";
        overlay.style.justifyContent = "center";
        overlay.innerHTML = `<div class="lion-roar">🦁 ROAR! ${score} HITS!</div>`;
        playAudio("path_to_lion_roar.mp3"); // Ensure you have this file
        setTimeout(() => { overlay.style.display = "none"; }, 2000);
    }
}

function verifyChoice(node) {
    if(isGameOver) return;
    clearInterval(timerInterval);
    if(parseInt(node.innerText) === targetAnswer) {
        score += 10; 
        combo++;
        document.getElementById("score-val").innerText = score;
        document.getElementById("combo-val").innerText = "x" + combo;
        checkMilestone(score); // Check for Lion
        playAudio(RIGHT_AUDIO); renderMatchStage();
    } else {
        lives--;
        document.getElementById("life-val").innerText = lives;
        if(lives > 0) {
            playAudio(WRONG_AUDIO); renderMatchStage();
        } else {
            triggerGameOver("DRAGON DEFEAT");
        }
    }
}

function triggerGameOver(msg) {
    isGameOver = true; clearInterval(timerInterval);
    const overlay = document.getElementById("cinematic-overlay");
    overlay.style.display = "flex";
    overlay.style.flexDirection = "column";
    overlay.innerHTML = `
        <div class="dragon-eyes">👁️👁️</div>
        <div style="color:white; font-size:30px;">${msg}</div>
        <button class="mode-btn" onclick="location.reload()">RETRY</button>
    `;
}
</script>
<div id="cinematic-overlay"></div>
</body>
</html>
"""

sanitized_html = raw_template_html.replace("%%RIGHT_AUDIO_REPLACE%%", right_answer_audio).replace("%%WRONG_AUDIO_REPLACE%%", wrong_answer_audio).replace("%%BG_AUDIO_REPLACE%%", background_music)
components.html(sanitized_html, height=660)
