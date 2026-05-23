import streamlit as st
import streamlit.components.v1 as components
import base64

# Layout configurations
st.set_page_config(
    page_title="Dilshad's Cyber Arena 2D",
    page_icon="👑",
    layout="centered"
)

# ==============================================================================
# 🎛️ NATIVE BASE64 AUDIO INJECTION PIPELINE
# ==============================================================================
def load_local_audio_base64(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            encoded_bytes = base64.b64encode(audio_file.read())
            return f"data:audio/mp3;base64,{encoded_bytes.decode('utf-8')}"
    except Exception as e:
        return ""

# Convert your local repo files into secure memory strings
right_answer_audio = load_local_audio_base64("faa.mp3")
wrong_answer_audio = load_local_audio_base64("haha.mp3")

# Dark space layout overrides
st.markdown("""
<style>
div[data-testid="stAppViewContainer"], .main {
    background: radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffffff; font-family: system-ui, sans-serif; font-weight: 900; letter-spacing: -2px; text-shadow: 0 0 20px rgba(168,85,247,0.4); margin-bottom:0px;'>⚡ CYBER ARENA 2D ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #06b6d4; font-family: monospace; font-size: 14px; margin-top:6px; margin-bottom: 0px; font-weight: 900; letter-spacing: 2px; text-shadow: 0 0 10px rgba(6,182,212,0.6);'>🚀 DEVELOPED BY MD DILSHAD</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a855f7; font-family: monospace; font-size: 11px; margin-top:4px; margin-bottom: 20px; letter-spacing: 2px;'>// ENGINE CORE V3.1 PATCHED // CBSE K-8 SUITE</p>", unsafe_allow_html=True)

# ==============================================================================
# 🎮 THE MULTI-LEVEL EDTECH ENGINE + WEBGL MATRIX (HTML CORE)
# ==============================================================================
raw_template_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<style>
    body, html {
        margin: 0; padding: 0;
        width: 100%; height: 100%;
        overflow: hidden;
        display: flex; justify-content: center; align-items: center;
        background: transparent;
        font-family: 'Courier New', Courier, monospace;
    }

    /* 🌌 MAIN SYSTEM VIEWPORT CONTAINER */
    .arena-viewport {
        position: relative;
        width: 520px;
        height: 660px;
        display: flex; justify-content: center; align-items: center;
        border-radius: 40px;
        box-shadow: 0 0 40px rgba(6, 182, 212, 0.15);
        transition: box-shadow 0.3s ease;
    }

    #three-canvas {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 1;
        border-radius: 40px;
    }

    /* 💎 SEAMLESS INTERACTIVE CORE CONSOLE GLASS */
    .game-console {
        position: relative;
        z-index: 2;
        width: 92%;
        height: 94%;
        background: rgba(4, 10, 26, 0.75);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 36px;
        padding: 25px;
        box-sizing: border-box;
        border: 1px solid rgba(168, 85, 247, 0.25);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: inset 0 0 30px rgba(168, 85, 247, 0.1), 0 25px 60px rgba(0,0,0,0.8);
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .console-correct {
        border-color: #10b981 !important;
        box-shadow: inset 0 0 40px rgba(16, 185, 129, 0.2), 0 25px 60px rgba(0,0,0,0.8) !important;
    }
    .console-incorrect {
        border-color: #ef4444 !important;
        box-shadow: inset 0 0 40px rgba(239, 68, 68, 0.2), 0 25px 60px rgba(0,0,0,0.8) !important;
    }

    /* 🧭 ENGINE SCREEN WRAPPERS */
    .screen-panel {
        width: 100%;
        height: 100%;
        display: none;
        flex-direction: column;
        justify-content: space-between;
    }
    .screen-active { display: flex !important; }

    /* 🎛️ GRID NAVIGATION DESIGN ELEMENTS */
    .menu-title {
        text-align: center; color: #ffffff; font-size: 20px; font-weight: 900;
        letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px;
        text-shadow: 0 0 10px rgba(6, 182, 212, 0.5);
    }
    
    .grid-selector {
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;
        overflow-y: auto; max-height: 420px; padding: 5px;
    }
    
    .grid-selector::-webkit-scrollbar { width: 4px; }
    .grid-selector::-webkit-scrollbar-thumb { background: #a855f7; border-radius: 10px; }

    .matrix-btn {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 16px; color: #38bdf8; font-weight: 900;
        padding: 20px 10px; font-size: 14px; cursor: pointer; text-align: center;
        transition: all 0.2s ease; font-family: monospace;
    }
    .matrix-btn:hover {
        background: linear-gradient(135deg, #06b6d4 0%, #a855f7 100%);
        color: #ffffff; border-color: #ffffff;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.5);
        transform: translateY(-2px);
    }
    
    .back-btn {
        background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.4);
        color: #ef4444; border-radius: 12px; padding: 10px; font-size: 11px;
        cursor: pointer; font-weight: 900; letter-spacing: 1px; width: 100%; margin-top: 10px;
    }
    .back-btn:hover { background: #ef4444; color: #ffffff; }

    /* 📊 EXTREME HUD ARCHITECTURE */
    .hud-header {
        display: flex; justify-content: space-between;
        color: #94a3b8; font-size: 11px; letter-spacing: 1px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding-bottom: 8px;
    }
    .score-glow { 
        color: #06b6d4; font-weight: 900; font-size: 16px;
        text-shadow: 0 0 10px #06b6d4;
    }

    /* 🔮 QUESTION CANVAS MATRIX */
    .question-deck {
        width: 100%; min-height: 110px;
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.9) 0%, rgba(2, 6, 23, 0.95) 100%);
        border-radius: 24px; border: 1px solid rgba(6, 182, 212, 0.25);
        padding: 20px 15px; text-align: center; box-sizing: border-box;
        display: flex; flex-direction: column; justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    #question-text {
        font-size: 24px; color: #ffffff; font-weight: 900;
        text-shadow: 0 0 12px rgba(255, 255, 255, 0.3); line-height: 1.4;
    }

    /* 🔄 KINETIC ROTATIONAL ORBIT ENGINE */
    .orbit-container {
        position: relative; width: 100%; height: 280px;
        display: flex; justify-content: center; align-items: center;
    }
    .orbit-rotor-2d {
        position: absolute; width: 200px; height: 200px;
        border-radius: 50%; border: 2px dashed rgba(6, 182, 212, 0.15);
        display: flex; justify-content: center; align-items: center;
        animation: spin2D 14s linear infinite !important;
    }
    @keyframes spin2D { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    .option-node-2d {
        position: absolute; width: 72px; height: 72px;
        background: radial-gradient(circle at 30% 30%, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 1) 100%);
        border: 1px solid rgba(6, 182, 212, 0.4); border-radius: 50%;
        color: #38bdf8; font-size: 18px; font-weight: 900;
        display: flex; justify-content: center; align-items: center;
        cursor: pointer; user-select: none; text-align: center; overflow: hidden;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        animation: keepUpright 14s linear infinite !important;
    }
    @keyframes keepUpright { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }

    .option-node-2d:hover {
        color: #ffffff; background: radial-gradient(circle at center, #06b6d4 0%, #0891b2 100%);
        border-color: #22d3ee; box-shadow: 0 0 25px #06b6d4; transform: scale(1.15);
    }

    /* ROTATOR TARGETING SLOTS */
    .opt-0 { top: -36px; left: 64px; }   
    .opt-1 { top: 64px; right: -36px; }  
    .opt-2 { bottom: -36px; left: 64px; }
    .opt-3 { top: 64px; left: -36px; }   

    /* 📊 PERFORMANCE SCORECARD SCREEN */
    .scorecard-box {
        text-align: center; padding: 20px; background: rgba(15,23,42,0.8);
        border-radius: 24px; border: 1px solid rgba(168,85,247,0.3);
    }
    .metric-rank {
        font-size: 54px; font-weight: 900; color: #22d3ee;
        text-shadow: 0 0 20px rgba(34,211,238,0.4); margin: 15px 0;
    }
</style>
</head>
<body>

<div class="arena-viewport" id="viewport-frame">
    <canvas id="three-canvas"></canvas>

    <div class="game-console" id="console-box">
        
        <div class="screen-panel screen-active" id="screen-grade">
            <div class="menu-title">SELECT ACADEMIC GRADE</div>
            <div class="grid-selector">
                <button class="matrix-btn" onclick="triggerGradeSelect(1)">GRADE 01<br><small style="color:#a855f7">Basics Core</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(2)">GRADE 02<br><small style="color:#a855f7">Place Values</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(3)">GRADE 03<br><small style="color:#a855f7">Fractions Intro</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(4)">GRADE 04<br><small style="color:#a855f7">LCM & Perimeter</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(5)">GRADE 05<br><small style="color:#a855f7">Decimals Matrix</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(6)">GRADE 06<br><small style="color:#a855f7">Algebra & Integers</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(7)">GRADE 07<br><small style="color:#a855f7">Exponents Core</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(8)">GRADE 08<br><small style="color:#a855f7">Linear Equations</small></button>
            </div>
            <div style="text-align: center; font-size: 10px; color: #475569;">BY: MD DILSHAD // CORE INITIALIZED</div>
        </div>

        <div class="screen-panel" id="screen-chapter">
            <div>
                <div class="menu-title" id="chapter-panel-title">SELECT TOPIC SECTOR</div>
                <div class="grid-selector" id="chapter-injection-grid"></div>
            </div>
            <button class="back-btn" onclick="navigateScreen('grade')">◀ RETURN TO MAIN CORE</button>
        </div>

        <div class="screen-panel" id="screen-game">
            <div class="hud-header">
                <div id="hud-topic-tag" style="max-width: 65%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TOPIC: UNKNOWN</div>
                <div>PROGRESS: <span id="hud-index-tag" class="score-glow">1/10</span></div>
            </div>
            
            <div class="question-deck">
                <div id="question-text">GENERATING MATRIX PROMPT...</div>
            </div>

            <div class="orbit-container">
                <div class="orbit-rotor-2d">
                    <div class="option-node-2d opt-0" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-1" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-2" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-3" onclick="verifyArenaChoice(this)">0</div>
                </div>
            </div>
            
            <div style="text-align: center; font-size: 10px; color: #475569; letter-spacing: 1px;">
                🔥 PERPETUAL MOMENTUM RUNNING // TARGETS SECURE
            </div>
        </div>

        <div class="screen-panel" id="screen-score">
            <div class="menu-title">SECTOR CHALLENGE EVALUATION</div>
            <div class="scorecard-box">
                <div style="color: #94a3b8; font-size: 12px; letter-spacing: 2px;">FINAL EVALUATION RATIO</div>
                <div class="metric-rank" id="score-ratio-display">0 / 10</div>
                <div style="color: #a855f7; font-size: 14px; font-weight: 900; margin-bottom: 10px;" id="performance-phrase">// LEVEL EXPIRED</div>
                <p style="color: #64748b; font-size: 11px; line-height: 1.4;" id="reinforce-alert">Targeted reinforcement loop is prepped to prioritize error sequences.</p>
            </div>
            <div>
                <button class="matrix-btn" style="width:100%; margin-bottom:10px;" onclick="triggerSmartRestart()">🔄 RESTART WITH REINFORCEMENT</button>
                <button class="back-btn" onclick="navigateScreen('grade')">🎓 SELECT NEW GRADE LEVEL</button>
            </div>
        </div>

    </div>
</div>

<script>
    // ==========================================================================
    // 🎵 BINARY TARGET MEMORY STREAMS
    // ==========================================================================
    const RIGHT_AUDIO_STREAM = "%%RIGHT_AUDIO_REPLACE%%"; 
    const WRONG_AUDIO_STREAM = "%%WRONG_AUDIO_REPLACE%%";

    function playFaaCorrect() {
        if (!RIGHT_AUDIO_STREAM || RIGHT_AUDIO_STREAM.length < 50) return;
        new Audio(RIGHT_AUDIO_STREAM).play().catch(e => {});
    }

    function playHahaIncorrect() {
        if (!WRONG_AUDIO_STREAM || WRONG_AUDIO_STREAM.length < 50) return;
        new Audio(WRONG_AUDIO_STREAM).play().catch(e => {});
    }

    // ==========================================================================
    // 🧬 THREE.JS RENDERING ENGINE 
    // ==========================================================================
    const canvasElement = document.getElementById('three-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(65, 520 / 660, 0.1, 1000);
    camera.position.z = 18;

    const renderer = new THREE.WebGLRenderer({ canvas: canvasElement, antialias: true, alpha: true });
    renderer.setSize(520, 660);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const totalParticles = 400; 
    const geometry = new THREE.BufferGeometry();
    const positionArray = new Float32Array(totalParticles * 3);
    for(let i=0; i < totalParticles*3; i+=3) {
        positionArray[i] = (Math.random() - 0.5) * 45;     
        positionArray[i+1] = (Math.random() - 0.5) * 45;   
        positionArray[i+2] = (Math.random() - 0.5) * 25;   
    }
    geometry.setAttribute('position', new THREE.BufferAttribute(positionArray, 3));

    const pointMaterial = new THREE.PointsMaterial({ size: 0.4, transparent: true, opacity: 0.65 });
    pointMaterial.color.setHex(0xa855f7); 
    const engineParticles = new THREE.Points(geometry, pointMaterial);
    scene.add(engineParticles);

    let activeFXState = "ambient"; 

    function tickGraphicsEngine() {
        requestAnimationFrame(tickGraphicsEngine);
        const positions = geometry.attributes.position.array;
        
        if (activeFXState === "ambient") {
            engineParticles.rotation.y += 0.004;
            pointMaterial.color.setHex(0xa855f7); 
        } else if (activeFXState === "correct") {
            pointMaterial.color.setHex(0x10b981); 
            for(let i=1; i < positions.length; i+=3) { positions[i] -= 0.6; if(positions[i] < -22) positions[i] = 22; }
            geometry.attributes.position.needsUpdate = true;
        } else if (activeFXState === "incorrect") {
            pointMaterial.color.setHex(0xef4444); 
            for(let i=1; i < positions.length; i+=3) { positions[i] += 0.8; if(positions[i] > 22) positions[i] = -22; }
            geometry.attributes.position.needsUpdate = true;
        }
        renderer.render(scene, camera);
    }
    tickGraphicsEngine();

    // ==========================================================================
    // 🧠 CBSE ACADEMIC CURRICULUM SYLLABUS MATRIX ARCHITECTURE
    // ==========================================================================
    const syllabusDatabase = {
        1: [
            { id: "g1_num", name: "Numbers Mastery (1-50)" },
            { id: "g1_add", name: "Single Digit Addition" },
            { id: "g1_sub", name: "Single Digit Subtraction" }
        ],
        2: [
            { id: "g2_place", name: "Place Values (Tens/Ones)" },
            { id: "g2_double", name: "2-Digit Computations" },
            { id: "g2_shapes", name: "Geometric Corner Counts" }
        ],
        3: [
            { id: "g3_roman", name: "Roman Numeral Vectors" },
            { id: "g3_mult", name: "Grid Multiplications" },
            { id: "g3_frac", name: "Fraction Parts Recognition" }
        ],
        4: [
            { id: "g4_large", name: "Large Numbers Rounding" },
            { id: "g4_lcm", name: "Factors, LCM & HCF Basics" },
            { id: "g4_perim", name: "Perimeters Matrix" }
        ],
        5: [
            { id: "g5_dec", name: "Decimal Operations" },
            { id: "g5_lcm_adv", name: "Advanced Multi-LCM" },
            { id: "g5_angles", name: "Angle Classification" }
        ],
        6: [
            { id: "g6_int", name: "Integers & Sign Laws" },
            { id: "g6_alg", name: "Algebra: Variable Isolation" },
            { id: "g6_ratio", name: "Ratio Identifiers" }
        ],
        7: [
            { id: "g7_rational", name: "Rational Fractional Steps" },
            { id: "g7_exp", name: "Exponents & Power Laws" },
            { id: "g7_eq", name: "Two-Step Smart Equations" }
        ],
        8: [
            { id: "g8_linear", name: "Linear Expression Matrix" },
            { id: "g8_roots", name: "Squares & Square Roots" },
            { id: "g8_identities", name: "Algebraic Identity Check" }
        ]
    };

    // Global Core Session Variables
    let selectedGrade = null;
    let selectedTopicId = null;
    let currentTopicName = "";
    let questionIndex = 0;
    let scoreCounter = 0;
    let targetDataset = [];
    let currentActiveQuestion = null;
    
    // Smart Memory Tracking Registers
    let analyticalErrorPool = {}; 

    function navigateScreen(screenId) {
        document.querySelectorAll('.screen-panel').forEach(s => s.classList.remove('screen-active'));
        document.getElementById('screen-' + screenId).classList.add('screen-active');
    }

    function triggerGradeSelect(grade) {
        selectedGrade = grade;
        document.getElementById('chapter-panel-title').innerText = "GRADE " + grade + ": SECTORS";
        const grid = document.getElementById('chapter-injection-grid');
        grid.innerHTML = "";
        
        syllabusDatabase[grade].forEach(topic => {
            let btn = document.createElement('button');
            btn.className = "matrix-btn";
            btn.innerHTML = topic.name;
            btn.onclick = () => launchChapterArena(topic.id, topic.name);
            grid.appendChild(btn);
        });
        navigateScreen('chapter');
    }

    // ==========================================================================
    // 🎲 ALGORITHMIC PROCEDURAL PROBLEM MATRIX GENERATORS
    // ==========================================================================
    function createProblemToken(typeId) {
        let text = "", answer = 0, variantRange = 15;
        
        switch(typeId) {
            case "g1_num":
                let num = Math.floor(Math.random() * 40) + 5;
                if(Math.random() > 0.5) { text = "What comes directly AFTER " + num + "?"; answer = num + 1; }
                else { text = "What comes directly BEFORE " + num + "?"; answer = num - 1; }
                break;
            case "g1_add":
                let a1 = Math.floor(Math.random() * 9) + 1; let a2 = Math.floor(Math.random() * 9) + 1;
                text = "Evaluate: " + a1 + " + " + a2; answer = a1 + a2;
                break;
            case "g1_sub":
                let s1 = Math.floor(Math.random() * 9) + 5; let s2 = Math.floor(Math.random() * s1);
                text = "Evaluate: " + s1 + " - " + s2; answer = s1 - s2;
                break;
            case "g2_place":
                let pV = Math.floor(Math.random() * 80) + 10;
                if(Math.random() > 0.5) { text = "How many TENS are in " + pV + "?"; answer = Math.floor(pV / 10); }
                else { text = "How many ONES are in " + pV + "?"; answer = pV % 10; }
                break;
            case "g2_double":
                let d1 = Math.floor(Math.random() * 40) + 10; let d2 = Math.floor(Math.random() * 40) + 10;
                if(Math.random() > 0.5) { text = "Evaluate: " + d1 + " + " + d2; answer = d1 + d2; }
                else { text = "Evaluate: " + (d1+d2) + " - " + d1; answer = d2; }
                break;
            case "g2_shapes":
                let shapes = ["Triangle", "Square", "Pentagon", "Rectangle"];
                let chosenShape = shapes[Math.floor(Math.random() * shapes.length)];
                let ansMap = { "Triangle": 3, "Square": 4, "Pentagon": 5, "Rectangle": 4 };
                text = "How many corners does a " + chosenShape + " have?"; answer = ansMap[chosenShape];
                break;
            case "g3_roman":
                let mapR = { 3:"III", 4:"IV", 5:"V", 6:"VI", 9:"IX", 10:"X", 11:"XI", 15:"XV" };
                let keys = Object.keys(mapR); let rK = keys[Math.floor(Math.random() * keys.length)];
                text = "Convert Roman Numeral '" + mapR[rK] + "' to number"; answer = parseInt(rK);
                break;
            case "g3_mult":
                let m1 = Math.floor(Math.random() * 10) + 2; let m2 = Math.floor(Math.random() * 8) + 2;
                text = "Compute: " + m1 + " x " + m2; answer = m1 * m2;
                break;
            case "g3_frac":
                let den = Math.floor(Math.random() * 6) + 4; let numr = Math.floor(Math.random() * (den - 1)) + 1;
                text = "In fraction " + numr + "/" + den + ", what is the Numerator?"; answer = numr;
                break;
            case "g4_large":
                let baseN = Math.floor(Math.random() * 800) + 150;
                text = "Round off " + baseN + " to the nearest 100"; answer = Math.round(baseN / 100) * 100;
                break;
            case "g4_lcm":
                let lcmPairs = [[2,3,6], [3,4,12], [4,6,12], [5,2,10]];
                let selectPair = lcmPairs[Math.floor(Math.random() * lcmPairs.length)];
                text = "Find LCM of " + selectPair[0] + " and " + selectPair[1]; answer = selectPair[2];
                break;
            case "g4_perim":
                let sideL = Math.floor(Math.random() * 12) + 3;
                text = "Find perimeter of a Square with side = " + sideL + " cm"; answer = sideL * 4;
                break;
            case "g5_dec":
                let decB = Math.floor(Math.random() * 9) + 1;
                text = "Convert " + decB + "/10 into decimal notation form"; answer = decB / 10; variantRange = 2;
                break;
            case "g5_lcm_adv":
                let hcfPairs = [[12,18,6], [10,15,5], [8,20,4], [14,21,7]];
                let sH = hcfPairs[Math.floor(Math.random() * hcfPairs.length)];
                text = "Find HCF of " + sH[0] + " and " + sH[1]; answer = sH[2];
                break;
            case "g5_angles":
                let angV = Math.floor(Math.random() * 150) + 15; if(angV === 90) angV = 95;
                text = "An angle measures " + angV + "°. Is it Acute(1) or Obtuse(2)?";
                answer = angV < 90 ? 1 : 2; variantRange = 3;
                break;
            case "g6_int":
                let i1 = Math.floor(Math.random() * 20) + 5; let i2 = Math.floor(Math.random() * 20) + 5;
                text = "Evaluate sign operation: (-" + i1 + ") + (" + i2 + ")"; answer = (-i1) + i2;
                break;
            case "g6_alg":
                let xVal = Math.floor(Math.random() * 15) + 2; let offset = Math.floor(Math.random() * 20) + 2;
                text = "Solve for x: x + " + offset + " = " + (xVal + offset); answer = xVal;
                break;
            case "g6_ratio":
                let rB = Math.floor(Math.random() * 5) + 2;
                text = "Simplify ratio " + (rB*3) + ":" + (rB*4) + ". Find missing term: 3:?"; answer = 4;
                break;
            case "g7_rational":
                let rf = Math.floor(Math.random() * 4) + 2;
                text = "Find equivalent numerator: 2/5 = ?/" + (5*rf); answer = 2 * rf;
                break;
            case "g7_exp":
                let eB = Math.floor(Math.random() * 3) + 2; let eP = Math.floor(Math.random() * 2) + 2;
                text = "Evaluate exponent power value: " + eB + "^" + eP; answer = Math.pow(eB, eP);
                break;
            case "g7_eq":
                let xV = Math.floor(Math.random() * 8) + 2; let mult = Math.floor(Math.random() * 4) + 2; let addConst = Math.floor(Math.random() * 10) + 1;
                text = "Solve equation matrix: " + mult + "x + " + addConst + " = " + ((mult*xV) + addConst); answer = xV;
                break;
            case "g8_linear":
                let xA = Math.floor(Math.random() * 10) + 2; let divi = Math.floor(Math.random() * 3) + 2;
                text = "Solve for variable: (x / " + divi + ") - 2 = " + ((xA/divi) - 2); answer = xA;
                break;
            case "g8_roots":
                let rootB = Math.floor(Math.random() * 11) + 4;
                text = "Find square root parameter: √" + (rootB * rootB); answer = rootB;
                break;
            case "g8_identities":
                let degV = Math.floor(Math.random() * 3) + 2;
                text = "Find the degree of expression: 7x^" + degV + " + 3x - 9"; answer = degV;
                break;
            default:
                text = "Verification Step: 10 + 10"; answer = 20;
        }

        return { text: text, answer: answer, typeId: typeId, variantRange: variantRange };
    }

    function buildSessionDeck(topicId) {
        let deck = [];
        if(analyticalErrorPool[topicId] && analyticalErrorPool[topicId].length > 0) {
            analyticalErrorPool[topicId].forEach(oldType => {
                if(deck.length < 5) deck.push(createProblemToken(oldType)); 
            });
        }
        while(deck.length < 10) {
            deck.push(createProblemToken(topicId));
        }
        return deck;
    }

    function launchChapterArena(topicId, topicName) {
        selectedTopicId = topicId;
        currentTopicName = topicName;
        questionIndex = 0;
        scoreCounter = 0;
        
        targetDataset = buildSessionDeck(topicId);
        document.getElementById('hud-topic-tag').innerText = topicName;
        
        unpackQuestionStage();
        navigateScreen('game');
    }

    function unpackQuestionStage() {
        if(questionIndex >= 10) {
            terminateArenaChallenge();
            return;
        }
        
        document.getElementById('hud-index-tag').innerText = (questionIndex + 1) + "/10";
        currentActiveQuestion = targetDataset[questionIndex];
        document.getElementById('question-text').innerText = currentActiveQuestion.text;

        let optionsSet = new Set();
        optionsSet.add(currentActiveQuestion.answer);

        while(optionsSet.size < 4) {
            let variance = (Math.random() > 0.5 ? 1 : -1) * (Math.floor(Math.random() * currentActiveQuestion.variantRange) + 1);
            let alternate = currentActiveQuestion.answer + variance;
            
            /* 🛠️ ES6 PATCHED REMAINDER FLOAT VERIFICATION MATRIX CHECK */
            if(currentActiveQuestion.answer % 1 !== 0) {
                alternate = parseFloat((currentActiveQuestion.answer + (variance*0.1)).toFixed(1));
            }
            if(alternate !== currentActiveQuestion.answer) optionsSet.add(alternate);
        }

        let shuffled = Array.from(optionsSet).sort(() => Math.random() - 0.5);
        const slots = document.getElementsByClassName("option-node-2d");
        for(let i=0; i < 4; i++) {
            slots[i].innerText = shuffled[i];
            slots[i].style.borderColor = "rgba(6, 182, 212, 0.4)";
            slots[i].style.background = "radial-gradient(circle at 30% 30%, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 1) 100%)";
            slots[i].style.color = "#38bdf8";
            slots[i].style.boxShadow = "0 10px 25px rgba(0,0,0,0.5)";
        }
    }

    function verifyArenaChoice(node) {
        const userChoice = parseFloat(node.innerText);
        const consoleBox = document.getElementById("console-box");
        
        if(userChoice === currentActiveQuestion.answer) {
            scoreCounter++;
            node.style.borderColor = "#10b981";
            node.style.background = "radial-gradient(circle at center, #10b981 0%, #059669 100%)";
            node.style.color = "#ffffff";
            node.style.boxShadow = "0 0 30px #10b981";
            
            consoleBox.classList.add("console-correct");
            playFaaCorrect();
            activeFXState = "correct";
        } else {
            if(!analyticalErrorPool[selectedTopicId]) analyticalErrorPool[selectedTopicId] = [];
            analyticalErrorPool[selectedTopicId].push(currentActiveQuestion.typeId);

            node.style.borderColor = "#ef4444";
            node.style.background = "radial-gradient(circle at center, #ef4444 0%, #dc2626 100%)";
            node.style.color = "#ffffff";
            node.style.boxShadow = "0 0 30px #ef4444";
            
            consoleBox.classList.add("console-incorrect");
            playHahaIncorrect();
            activeFXState = "incorrect";
        }

        setTimeout(() => {
            consoleBox.classList.remove("console-correct", "console-incorrect");
            activeFXState = "ambient";
            questionIndex++;
            unpackQuestionStage();
        }, 1100);
    }

    function terminateArenaChallenge() {
        document.getElementById('score-ratio-display').innerText = scoreCounter + " / 10";
        let phrase = "";
        if(scoreCounter === 10) phrase = "🔥 PERFECT MATRIX ACCURACY!";
        else if(scoreCounter >= 7) phrase = "⚡ TARGET SECURED - SECTOR CLEARED";
        else phrase = "⚠️ CRITICAL FAILURE: RETRY REQUIRED";
        
        document.getElementById('performance-phrase').innerText = phrase;
        navigateScreen('score');
    }

    function triggerSmartRestart() {
        launchChapterArena(selectedTopicId, currentTopicName);
    }
</script>

</body>
</html>
"""

# Inject audio streams cleanly without using an f-string
sanitized_game_html = raw_template_html.replace(
    "%%RIGHT_AUDIO_REPLACE%%", right_answer_audio
).replace(
    "%%WRONG_AUDIO_REPLACE%%", wrong_answer_audio
)

# Render application matrix into main Streamlit container framework
components.html(sanitized_game_html, height=680)
