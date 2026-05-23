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
st.markdown("<p style='text-align: center; color: #a855f7; font-family: monospace; font-size: 11px; margin-top:4px; margin-bottom: 20px; letter-spacing: 2px;'>// ENGINE CORE V4.0 // NCERT & RS AGGARWAL MATRIX SUITE</p>", unsafe_allow_html=True)

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

    .arena-viewport {
        position: relative;
        width: 520px;
        height: 660px;
        display: flex; justify-content: center; align-items: center;
        border-radius: 40px;
        box-shadow: 0 0 40px rgba(6, 182, 212, 0.15);
    }

    #three-canvas {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 1;
        border-radius: 40px;
    }

    .game-console {
        position: relative;
        z-index: 2;
        width: 92%;
        height: 94%;
        background: rgba(4, 10, 26, 0.82);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 36px;
        padding: 22px;
        box-sizing: border-box;
        border: 1px solid rgba(168, 85, 247, 0.25);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: inset 0 0 30px rgba(168, 85, 247, 0.1), 0 25px 60px rgba(0,0,0,0.8);
    }

    .console-correct { border-color: #10b981 !important; box-shadow: inset 0 0 40px rgba(16, 185, 129, 0.2), 0 25px 60px rgba(0,0,0,0.8) !important; }
    .console-incorrect { border-color: #ef4444 !important; box-shadow: inset 0 0 40px rgba(239, 68, 68, 0.2), 0 25px 60px rgba(0,0,0,0.8) !important; }

    .screen-panel { width: 100%; height: 100%; display: none; flex-direction: column; justify-content: space-between; }
    .screen-active { display: flex !important; }

    .menu-title {
        text-align: center; color: #ffffff; font-size: 18px; font-weight: 900;
        letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px;
        text-shadow: 0 0 10px rgba(6, 182, 212, 0.5);
    }
    
    .grid-selector {
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;
        overflow-y: auto; max-height: 440px; padding: 4px;
    }
    
    .grid-selector::-webkit-scrollbar { width: 4px; }
    .grid-selector::-webkit-scrollbar-thumb { background: #a855f7; border-radius: 10px; }

    .matrix-btn {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 14px; color: #38bdf8; font-weight: 900;
        padding: 16px 8px; font-size: 13px; cursor: pointer; text-align: center;
        transition: all 0.2s ease; font-family: monospace;
    }
    .matrix-btn:hover {
        background: linear-gradient(135deg, #06b6d4 0%, #a855f7 100%);
        color: #ffffff; border-color: #ffffff;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.5);
        transform: translateY(-1px);
    }
    
    .back-btn {
        background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.4);
        color: #ef4444; border-radius: 12px; padding: 10px; font-size: 11px;
        cursor: pointer; font-weight: 900; letter-spacing: 1px; width: 100%; margin-top: 8px;
    }
    .back-btn:hover { background: #ef4444; color: #ffffff; }

    .hud-header {
        display: flex; justify-content: space-between; align-items: center;
        color: #94a3b8; font-size: 11px; letter-spacing: 1px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding-bottom: 6px;
    }
    .score-glow { color: #06b6d4; font-weight: 900; font-size: 15px; text-shadow: 0 0 10px #06b6d4; }

    .question-deck {
        width: 100%; min-height: 125px;
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.92) 0%, rgba(2, 6, 23, 0.97) 100%);
        border-radius: 20px; border: 1px solid rgba(6, 182, 212, 0.25);
        padding: 15px; text-align: center; box-sizing: border-box;
        display: flex; flex-direction: column; justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    #question-text { font-size: 17px; color: #ffffff; font-weight: 700; line-height: 1.5; }

    .orbit-container { position: relative; width: 100%; height: 260px; display: flex; justify-content: center; align-items: center; }
    .orbit-rotor-2d {
        position: absolute; width: 180px; height: 180px;
        border-radius: 50%; border: 2px dashed rgba(6, 182, 212, 0.12);
        display: flex; justify-content: center; align-items: center;
        animation: spin2D 12s linear infinite !important;
    }
    @keyframes spin2D { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    .option-node-2d {
        position: absolute; width: 74px; height: 74px;
        background: radial-gradient(circle at 30% 30%, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 1) 100%);
        border: 1px solid rgba(6, 182, 212, 0.35); border-radius: 50%;
        color: #38bdf8; font-size: 15px; font-weight: 900;
        display: flex; justify-content: center; align-items: center;
        cursor: pointer; user-select: none; text-align: center; overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        animation: keepUpright 12s linear infinite !important;
    }
    @keyframes keepUpright { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }

    .option-node-2d:hover {
        color: #ffffff; background: radial-gradient(circle at center, #06b6d4 0%, #0891b2 100%);
        border-color: #22d3ee; box-shadow: 0 0 25px #06b6d4; transform: scale(1.12);
    }

    .opt-0 { top: -37px; left: 53px; }   
    .opt-1 { top: 53px; right: -37px; }  
    .opt-2 { bottom: -37px; left: 53px; }
    .opt-3 { top: 53px; left: -37px; }   

    .scorecard-box { text-align: center; padding: 20px; background: rgba(15,23,42,0.8); border-radius: 24px; border: 1px solid rgba(168,85,247,0.3); }
    .metric-rank { font-size: 54px; font-weight: 900; color: #22d3ee; text-shadow: 0 0 20px rgba(34,211,238,0.4); margin: 12px 0; }
</style>
</head>
<body>

<div class="arena-viewport" id="viewport-frame">
    <canvas id="three-canvas"></canvas>

    <div class="game-console" id="console-box">
        
        <div class="screen-panel screen-active" id="screen-grade">
            <div class="menu-title">SELECT ACADEMIC GRADE</div>
            <div class="grid-selector">
                <button class="matrix-btn" onclick="triggerGradeSelect(1)">GRADE 01<br><small style="color:#a855f7">Foundations</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(2)">GRADE 02<br><small style="color:#a855f7">Place Values</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(3)">GRADE 03<br><small style="color:#a855f7">Arithmetics</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(4)">GRADE 04<br><small style="color:#a855f7">Fractions Core</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(5)">GRADE 05<br><small style="color:#a855f7">Advanced K5</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(6)">GRADE 06<br><small style="color:#a855f7">Algebra Intro</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(7)">GRADE 07<br><small style="color:#a855f7">Rationals & Laws</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(8)">GRADE 08<br><small style="color:#a855f7">Linear Master</small></button>
            </div>
            <div style="text-align: center; font-size: 10px; color: #475569;">BY: MD DILSHAD // NCERT COMPLIANT</div>
        </div>

        <div class="screen-panel" id="screen-chapter">
            <div>
                <div class="menu-title" id="chapter-panel-title">SELECT CHAPTER SECTOR</div>
                <div class="grid-selector" id="chapter-injection-grid"></div>
            </div>
            <button class="back-btn" onclick="navigateScreen('grade')">◀ RETURN TO GRADE CONSOLE</button>
        </div>

        <div class="screen-panel" id="screen-game">
            <div class="hud-header">
                <div id="hud-topic-tag" style="max-width: 65%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-weight:900; color:#e2e8f0;">TOPIC</div>
                <div>PROGRESS: <span id="hud-index-tag" class="score-glow">1/10</span></div>
            </div>
            
            <div class="question-deck">
                <div id="question-text">COMPILING INTEGRATED TEXTBOOK PROMPT...</div>
            </div>

            <div class="orbit-container">
                <div class="orbit-rotor-2d">
                    <div class="option-node-2d opt-0" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-1" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-2" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-3" onclick="verifyArenaChoice(this)">0</div>
                </div>
            </div>
            
            <div style="text-align: center; font-size: 10px; color: #475569; letter-spacing: 1px;">// PERPETUAL ROTATION ACTIVE</div>
        </div>

        <div class="screen-panel" id="screen-score">
            <div class="menu-title">CHAPTER CHALLENGE EVALUATION</div>
            <div class="scorecard-box">
                <div style="color: #94a3b8; font-size: 12px; letter-spacing: 2px;">FINAL PERFORMANCE RATIO</div>
                <div class="metric-rank" id="score-ratio-display">0 / 10</div>
                <div style="color: #a855f7; font-size: 14px; font-weight: 900; margin-bottom: 10px;" id="performance-phrase">EVALUATION FINISHED</div>
                <p style="color: #64748b; font-size: 11px; line-height: 1.4;">Incorrect types have been logged into memory registers for your retry payload.</p>
            </div>
            <div>
                <button class="matrix-btn" style="width:100%; margin-bottom:10px;" onclick="triggerSmartRestart()">🔄 RESTART WITH REINFORCEMENT</button>
                <button class="back-btn" onclick="navigateScreen('grade')">🎓 SELECT NEW GRADE LEVEL</button>
            </div>
        </div>

    </div>
</div>

<script>
    const RIGHT_AUDIO_STREAM = "%%RIGHT_AUDIO_REPLACE%%"; 
    const WRONG_AUDIO_STREAM = "%%WRONG_AUDIO_REPLACE%%";

    function playFaaCorrect() { if (RIGHT_AUDIO_STREAM.length > 50) new Audio(RIGHT_AUDIO_STREAM).play().catch(e=>{}); }
    function playHahaIncorrect() { if (WRONG_AUDIO_STREAM.length > 50) new Audio(WRONG_AUDIO_STREAM).play().catch(e=>{}); }

    // ==========================================================================
    // THREE.JS SPATIAL PARTICLE CORE
    // ==========================================================================
    const canvasElement = document.getElementById('three-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(65, 520 / 660, 0.1, 1000); camera.position.z = 18;
    const renderer = new THREE.WebGLRenderer({ canvas: canvasElement, antialias: true, alpha: true });
    renderer.setSize(520, 660); renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const totalParticles = 400; const geometry = new THREE.BufferGeometry(); const positionArray = new Float32Array(totalParticles * 3);
    for(let i=0; i < totalParticles*3; i+=3) { positionArray[i] = (Math.random() - 0.5) * 45; positionArray[i+1] = (Math.random() - 0.5) * 45; positionArray[i+2] = (Math.random() - 0.5) * 25; }
    geometry.setAttribute('position', new THREE.BufferAttribute(positionArray, 3));
    const pointMaterial = new THREE.PointsMaterial({ size: 0.4, transparent: true, opacity: 0.65, color: 0xa855f7 });
    const engineParticles = new THREE.Points(geometry, pointMaterial); scene.add(engineParticles);

    let activeFXState = "ambient";
    function tickGraphicsEngine() {
        requestAnimationFrame(tickGraphicsEngine); const positions = geometry.attributes.position.array;
        if (activeFXState === "ambient") { engineParticles.rotation.y += 0.003; pointMaterial.color.setHex(0xa855f7); }
        else if (activeFXState === "correct") { pointMaterial.color.setHex(0x10b981); for(let i=1; i<positions.length; i+=3) { positions[i]-=0.5; if(positions[i]<-22) positions[i]=22; } geometry.attributes.position.needsUpdate=true; }
        else if (activeFXState === "incorrect") { pointMaterial.color.setHex(0xef4444); for(let i=1; i<positions.length; i+=3) { positions[i]+=0.7; if(positions[i]>22) positions[i]=-22; } geometry.attributes.position.needsUpdate=true; }
        renderer.render(scene, camera);
    }
    tickGraphicsEngine();

    // ==========================================================================
    // 📚 COMPREHENSIVE NCERT / RS AGGARWAL 40-CHAPTER SYLLABUS GRID
    // ==========================================================================
    const syllabusDatabase = {
        1: [
            { id: "g1_ch1", name: "Ch 1: Shapes & Space Logic" },
            { id: "g1_ch2", name: "Ch 2: Numbers 1 to 20 Matrix" },
            { id: "g1_ch3", name: "Ch 3: Addition Foundations" },
            { id: "g1_ch4", name: "Ch 4: Subtraction Bounds" },
            { id: "g1_ch5", name: "Ch 5: Structural Patterns" }
        ],
        2: [
            { id: "g2_ch1", name: "Ch 1: Counting Group Vectors" },
            { id: "g2_ch2", name: "Ch 2: Place Value Notation" },
            { id: "g2_ch3", name: "Ch 3: 2-Digit Addition Arena" },
            { id: "g2_ch4", name: "Ch 4: 2-Digit Subtraction" },
            { id: "g2_ch5", name: "Ch 5: Weight & Capacity Laws" }
        ],
        3: [
            { id: "g3_ch1", name: "Ch 1: Large Number Systems" },
            { id: "g3_ch2", name: "Ch 2: Advanced Grid Addition" },
            { id: "g3_ch3", name: "Ch 3: Subtraction Regrouping" },
            { id: "g3_ch4", name: "Ch 4: Multiplication Arrays" },
            { id: "g3_ch5", name: "Ch 5: Basic Division Shares" }
        ],
        4: [
            { id: "g4_ch1", name: "Ch 1: Building Blocks Metrics" },
            { id: "g4_ch2", name: "Ch 2: LCM & HCF Multipliers" },
            { id: "g4_ch3", name: "Ch 3: Fractional Parts Division" },
            { id: "g4_ch4", name: "Ch 4: Metric Transformations" },
            { id: "g4_ch5", name: "Ch 5: Perimeter & Outer Boundaries" }
        ],
        5: [
            { id: "g5_ch1", name: "Ch 1: Large Number Architectures" },
            { id: "g5_ch2", name: "Ch 2: Deep Fraction Computations" },
            { id: "g5_ch3", name: "Ch 3: Decimal System Core" },
            { id: "g5_ch4", name: "Ch 4: Angle Layout Matrix" },
            { id: "g5_ch5", name: "Ch 5: Unitary Method Systems" }
        ],
        6: [
            { id: "g6_ch1", name: "Ch 1: Number System Integers" },
            { id: "g6_ch2", name: "Ch 2: Fractions & Decimals Suite" },
            { id: "g6_ch3", name: "Ch 3: Intro to Expression Algebra" },
            { id: "g6_ch4", name: "Ch 4: Ratios & Proportions" },
            { id: "g6_ch5", name: "Ch 5: Mensuration Area Logic" }
        ],
        7: [
            { id: "g7_ch1", name: "Ch 1: Rational Fraction Matrices" },
            { id: "g7_ch2", name: "Ch 2: Complex Algebraic Terms" },
            { id: "g7_ch3", name: "Ch 3: Exponents & Exponential Laws" },
            { id: "g7_ch4", name: "Ch 4: Simple Equations Vault" },
            { id: "g7_ch5", name: "Ch 5: Data Analysis Mean-Median" }
        ],
        8: [
            { id: "g8_ch1", name: "Ch 1: Advanced Rational Operations" },
            { id: "g8_ch2", name: "Ch 2: 1-Variable Linear Equations" },
            { id: "g8_ch3", name: "Ch 3: Squares, Cubes & Roots Engine" },
            { id: "g8_ch4", name: "Ch 4: Quadrilateral Vectors" },
            { id: "g8_ch5", name: "Ch 5: Advanced Negative Exponents" }
        ]
    };

    let selectedGrade = null, selectedTopicId = null, currentTopicName = "", questionIndex = 0, scoreCounter = 0, targetDataset = [], currentActiveQuestion = null;
    let analyticalErrorPool = {};

    function navigateScreen(screenId) {
        document.querySelectorAll('.screen-panel').forEach(s => s.classList.remove('screen-active'));
        document.getElementById('screen-' + screenId).classList.add('screen-active');
    }

    function triggerGradeSelect(grade) {
        selectedGrade = grade; document.getElementById('chapter-panel-title').innerText = "GRADE " + grade + ": SECTORS";
        const grid = document.getElementById('chapter-injection-grid'); grid.innerHTML = "";
        syllabusDatabase[grade].forEach(topic => {
            let btn = document.createElement('button'); btn.className = "matrix-btn"; btn.innerHTML = topic.name;
            btn.onclick = () => launchChapterArena(topic.id, topic.name); grid.appendChild(btn);
        });
        navigateScreen('chapter');
    }

    // ==========================================================================
    // 🧬 TRUE PROCEDURAL STRUCTURAL ALTERATION CORES (LAKHS OF PATTERNS)
    // ==========================================================================
    function createProblemToken(typeId) {
        let text = "", answer = 0, variantRange = 15;
        let variantBranch = Math.floor(Math.random() * 4); // Seeds entirely different questions within the same category

        switch(typeId) {
            // ================== GRADE 1 ==================
            case "g1_ch1":
                if (variantBranch === 0) { text = "A cylinder rolls down a slide. A brick stacks. Which object rolls? Cylinder(1) or Brick(2)?"; answer = 1; variantRange = 2; }
                else if (variantBranch === 1) { text = "If a tree is OUTSIDE a house and a cat is INSIDE. Where is the cat? Outside(1), Inside(2)?"; answer = 2; variantRange = 2; }
                else { let sides = Math.random() > 0.5 ? "Triangle" : "Square"; text = "Identify total boundary corners present on a standard flat " + sides + "."; answer = (sides==="Triangle"?3:4); variantRange = 4; }
                break;
            case "g1_ch2":
                let num1 = Math.floor(Math.random() * 15) + 3;
                if (variantBranch === 0) { text = "Complete sequence: " + num1 + ", " + (num1+1) + ", __, " + (num1+3) + ". Find value."; answer = num1+2; }
                else if (variantBranch === 1) { text = "Count total character letters present inside word 'MATHEMATICS'."; answer = 11; variantRange = 5; }
                else { text = "What integer value falls precisely ahead/after element " + num1 + "?"; answer = num1+1; }
                break;
            case "g1_ch3":
                let addA = Math.floor(Math.random()*7)+1, addB = Math.floor(Math.random()*6)+1;
                if (variantBranch === 0) { text = "Rahul owns " + addA + " apples. Priya hands him " + addB + " more apples. Evaluate grand sum."; answer = addA+addB; }
                else { text = "Solve absolute addition equation space: " + addA + " + " + addB + " = ?"; answer = addA+addB; }
                break;
            case "g1_ch4":
                let subA = Math.floor(Math.random()*8)+8, subB = Math.floor(Math.random()*6)+1;
                if (variantBranch === 0) { text = "A branch contains " + subA + " sparrows. " + subB + " fly away into sky. Determine remaining subset."; answer = subA-subB; }
                else { text = "Compute numeric subtraction differential: " + subA + " - " + subB + " = ?"; answer = subA-subB; }
                break;
            case "g1_ch5":
                let pBase = Math.floor(Math.random()*5)+2;
                if (variantBranch === 0) { text = "Find pattern anomaly step: " + pBase + ", " + (pBase+2) + ", " + (pBase+4) + ", __. Solve gap value."; answer = pBase+6; }
                else { text = "Analyze loop progression sequence: △, ◯, △, ◯, __. Is next step △(1) or ◯(2)?"; answer = 1; variantRange = 2; }
                break;

            // ================== GRADE 2 ==================
            case "g2_ch1":
                let grp = Math.floor(Math.random()*4)+3;
                text = "There are " + grp + " groups of shoes. Each distinct cluster contains exactly 2 shoes. Calculate total pairing sum."; answer = grp*2;
                break;
            case "g2_ch2":
                let pvVal = Math.floor(Math.random()*70)+15;
                if (variantBranch === 0) { text = "Extract place value density representation: How many TENS fit inside integer " + pvVal + "?"; answer = Math.floor(pvVal/10); }
                else { text = "Isolate absolute units position parameter: Find ONES digit count inside integer " + pvVal + "."; answer = pvVal%10; }
                break;
            case "g2_ch3":
                let dAdd1 = Math.floor(Math.random()*30)+11, dAdd2 = Math.floor(Math.random()*25)+11;
                text = "A shop sells " + dAdd1 + " blue toys and " + dAdd2 + " green pens. Calculate inventory total combo density."; answer = dAdd1+dAdd2;
                break;
            case "g2_ch4":
                let dSub1 = Math.floor(Math.random()*40)+45, dSub2 = Math.floor(Math.random()*30)+10;
                text = "A book has " + dSub1 + " pages. Amit scans exactly " + dSub2 + " pages. How many pages remain unscanned?"; answer = dSub1-dSub2;
                break;
            case "g2_ch5":
                if (variantBranch <= 1) { text = "Which volume containment vessel holds MORE total fluid mass? A standard Bucket(1) or small Cup(2)?"; answer = 1; variantRange = 2; }
                else { text = "Convert simple metric system tracking weights: 1 Kilogram is equivalent to how many grams?"; answer = 1000; variantRange = 500; }
                break;

            // ================== GRADE 3 ==================
            case "g3_ch1":
                let lNum = Math.floor(Math.random()*600)+200;
                if (variantBranch === 0) { text = "Isolate complete digit value positioning: Find the HUNDREDS place unit value inside token " + lNum + "."; answer = Math.floor(lNum/100); }
                else { text = "Evaluate successor alignment target bounds: Determine complete successor string for code value " + lNum + "."; answer = lNum+1; }
                break;
            case "g3_ch2":
                let tA = Math.floor(Math.random()*200)+150, tB = Math.floor(Math.random()*150)+50;
                text = "A storage center houses " + tA + " crates of wheat and " + tB + " crates of rice. Sum absolute storage inventory capacity."; answer = tA+tB;
                break;
            case "g3_ch3":
                let rA = Math.floor(Math.random()*300)+400, rB = Math.floor(Math.random()*250)+50;
                text = "Solve structural RS Aggarwal-tier subtraction challenge problem vectors: Compute differential: " + rA + " - " + rB; answer = rA-rB;
                break;
            case "g3_ch4":
                let mu1 = Math.floor(Math.random()*11)+3, mu2 = Math.floor(Math.random()*8)+3;
                if (variantBranch === 0) { text = "A grid layout array holds " + mu1 + " parallel rows. Each index path contains " + mu2 + " pins. Evaluate product."; answer = mu1*mu2; }
                else { text = "Compute core multiplication parameters: Evaluate matrix equation product " + mu1 + " x " + mu2; answer = mu1*mu2; }
                break;
            case "g3_ch5":
                let divBase = Math.floor(Math.random()*6)+4, divFactor = Math.floor(Math.random()*5)+2;
                text = "Distribute " + (divBase*divFactor) + " total marbles equally among " + divFactor + " active users. Find share balance per user."; answer = divBase;
                break;

            // ================== GRADE 4 ==================
            case "g4_ch1":
                let brickL = Math.floor(Math.random()*15)+10;
                text = "A symmetric NCERT architectural brick model setup spans " + brickL + " cm long. Find length of 5 structural units combined."; answer = brickL*5;
                break;
            case "g4_ch2":
                if (variantBranch <= 1) {
                    let pairs = [[3,4,12], [4,6,12], [5,3,15], [6,8,24]]; let sel = pairs[Math.floor(Math.random()*pairs.length)];
                    text = "Extract mathematical Lowest Common Multiple (LCM) factor tracking vector maps for numbers: " + sel[0] + " and " + sel[1]; answer = sel[2];
                } else {
                    let hcfPairs = [[12,16,4], [15,20,5], [18,24,6], [10,25,5]]; let selH = hcfPairs[Math.floor(Math.random()*hcfPairs.length)];
                    text = "Evaluate fundamental Highest Common Factor (HCF) core elements tracking for dataset constants: " + selH[0] + " and " + selH[1]; answer = selH[2];
                }
                break;
            case "g4_ch3":
                let fDen = Math.floor(Math.random()*5)+5;
                text = "A linear cake strip divides into " + fDen + " equal parts. Shreya consumes exactly 3 slices. Find the remaining fraction numerator."; answer = fDen-3;
                break;
            case "g4_ch4":
                let mK = Math.floor(Math.random()*6)+2;
                text = "Convert absolute core spatial standard metrics: How many meters exist inside metric parameter tracking map " + mK + " Kilometers?"; answer = mK*1000;
                break;
            case "g4_ch5":
                let sLen = Math.floor(Math.random()*12)+4;
                if (variantBranch <= 1) { text = "Calculate perimeter tracking path boundaries around a uniform square block with outer edges measuring = " + sLen + " cm"; answer = sLen*4; }
                else { text = "A rectangle has length = " + sLen + " cm and uniform width = 5 cm. Compute complete outer framework perimeter layout."; answer = (sLen+5)*2; }
                break;

            // ================== GRADE 5 ==================
            case "g5_ch1":
                let rRound = Math.floor(Math.random()*8000)+1500;
                text = "Execute RS Aggarwal approximation parsing equations: Round off standard data tracking integer " + rRound + " to nearest 1000 level."; answer = Math.round(rRound/1000)*1000;
                break;
            case "g5_ch2":
                let fA = Math.floor(Math.random()*3)+1;
                text = "Evaluate fractional balance steps: Compute the sum configuration value: " + fA + "/7 + 2/7. Isolate final target numerator string."; answer = fA+2;
                break;
            case "g5_ch3":
                let dB = Math.floor(Math.random()*85)+10;
                text = "Convert rational division parameter strings to decimal format structures: Find notation target values for fraction: " + dB + "/100"; answer = dB/100; variantRange = 2;
                break;
            case "g5_ch4":
                let ang = Math.floor(Math.random()*140)+20; if(ang===90) ang=100;
                text = "An intersection structural vector path prints a node at angle " + ang + "°. Classify state vector: Acute(1) or Obtuse(2)?"; answer = ang<90?1:2; variantRange=3;
                break;
            case "g5_ch5":
                let itemC = Math.floor(Math.random()*4)+3, itemP = Math.floor(Math.random()*20)+10;
                text = "If " + itemC + " identical computer processing chips cost ₹" + (itemC*itemP) + ". Determine total cost tracking output for 10 chips."; answer = 10*itemP;
                break;

            // ================== GRADE 6 ==================
            case "g6_ch1":
                let negA = Math.floor(Math.random()*20)+5, negB = Math.floor(Math.random()*25)+5;
                text = "Evaluate signed integer number line law configurations: Calculate the final computational result value: (-" + negA + ") + (" + negB + ")"; answer = (-negA)+negB;
                break;
            case "g6_ch2":
                let multD = Math.floor(Math.random()*6)+2;
                text = "Isolate clean floating decimal data array output metrics: Compute the arithmetic product: 0.3 x " + multD; answer = parseFloat((0.3*multD).toFixed(1)); variantRange = 2;
                break;
            case "g6_ch3":
                let xA = Math.floor(Math.random()*12)+3, xB = Math.floor(Math.random()*20)+15;
                if (variantBranch <= 1) { text = "Isolate algebraic single variable unknowns: Solve equation expression for x value: x + " + xA + " = " + (xA+xB); answer = xB; }
                else { text = "Translate word phrase matrix: '5 added to 3 times a variable x balances at 20'. Evaluate matching x parameter value."; answer = 5; }
                break;
            case "g6_ch4":
                let ratB = Math.floor(Math.random()*6)+2;
                text = "Simplify ratio string vectors: Reduce proportion scale configuration " + (ratB*4) + ":" + (ratB*5) + ". Find value of unknown tracking index term 4:?"; answer = 5;
                break;
            case "g6_ch5":
                let lenM = Math.floor(Math.random()*10)+5, widM = Math.floor(Math.random()*4)+2;
                text = "Determine 2D coordinate floor plan measurement metrics: Find the internal space area of a room measuring " + lenM + " m by " + widM + " m."; answer = lenM*widM;
                break;

            // ================== GRADE 7 ==================
            case "g7_ch1":
                let rScale = Math.floor(Math.random()*4)+3;
                text = "Determine equivalent rational transformation steps: If fraction -3/4 translates directly into variable mapping form ?/" + (4*rScale) + ". Isolate unknown numerator."; answer = -3*rScale;
                break;
            case "g7_ch2":
                let coeffA = Math.floor(Math.random()*6)+2, coeffB = Math.floor(Math.random()*8)+3;
                text = "Simplify multi-variable algebraic expressions: Collect matching variable constants to simplify term: " + coeffA + "x + " + coeffB + "y - 3x. Find coefficient of variable x."; answer = coeffA-3;
                break;
            case "g7_ch3":
                let expB = Math.floor(Math.random()*3)+2, expP = Math.floor(Math.random()*2)+3;
                text = "Process algorithmic exponent operational law parameters: Compute final computational calculation output for value: " + expB + "^" + expP; answer = Math.pow(expB, expP);
                break;
            case "g7_ch4":
                let eqM = Math.floor(Math.random()*3)+2, eqAdd = Math.floor(Math.random()*12)+2, eqX = Math.floor(Math.random()*6)+2;
                text = "Execute simple equation balance loops: Solve structural system variable output for expression: " + eqM + "x - " + eqAdd + " = " + ((eqM*eqX)-eqAdd); answer = eqX;
                break;
            case "g7_ch5":
                let dA=Math.floor(Math.random()*5)+2, dB=Math.floor(Math.random()*10)+10, dC=Math.floor(Math.random()*5)+1;
                text = "Process analytical tracking data algorithms: Calculate arithmetic mean average parameters for array set: [" + dA + ", " + dB + ", " + dC + "]. Hint: Sum divided by 3."; answer = (dA+dB+dC)/3;
                break;

            // ================== GRADE 8 ==================
            case "g8_ch1":
                text = "Evaluate multiplicative inverse state laws for rational number formats: Find reciprocal calculation token index for term: -7/12. Enter absolute denominator state."; answer = -7;
                break;
            case "g8_ch2":
                let linA = Math.floor(Math.random()*4)+2, linB = Math.floor(Math.random()*5)+1;
                text = "Solve advanced 1-variable linear expression matrix profiles: Solve for unknown parameter x inside equation: " + linA + "x + 4 = x + " + ((linA*linB)+4-linB); answer = linB;
                break;
            case "g8_ch3":
                let rt = Math.floor(Math.random()*7)+6;
                if (variantBranch <= 1) { text = "Compute high-order square root core numeric indices: Find root solution value for expression vector: √" + (rt*rt); answer = rt; }
                else { text = "Compute cubing operational output loops: Evaluate complete cube dimensions integer result for calculation parameter: " + rt + "^3"; answer = Math.pow(rt, 3); variantRange = 100; }
                break;
            case "g8_ch4":
                let sideK = Math.floor(Math.random()*40)+40;
                text = "Evaluate structural spatial quadrilateral geometry axioms: A parallelogram tracking vector maps an opposite internal node angle tracking at " + sideK + "°. Find opposite missing node angle."; answer = sideK;
                break;
            case "g8_ch5":
                let negExp = Math.floor(Math.random()*2)+2;
                text = "Process inverse exponential law calculations: Convert negative index formatting logic statement to standard number values: Evaluate statement: 10^-" + negExp + ". Find denominator scaling code."; answer = Math.pow(10, negExp); variantRange = 50;
                break;

            default:
                text = "System Default Fallback Core Diagnostic Prompt: 50 + 50"; answer = 100;
        }

        return { text: text, answer: answer, typeId: typeId, variantRange: variantRange };
    }

    function buildSessionDeck(topicId) {
        let deck = [];
        if(analyticalErrorPool[topicId] && analyticalErrorPool[topicId].length > 0) {
            analyticalErrorPool[topicId].forEach(oldType => { if(deck.length < 5) deck.push(createProblemToken(oldType)); });
        }
        while(deck.length < 10) { deck.push(createProblemToken(topicId)); }
        return deck;
    }

    function launchChapterArena(topicId, topicName) {
        selectedTopicId = topicId; currentTopicName = topicName; questionIndex = 0; scoreCounter = 0;
        targetDataset = buildSessionDeck(topicId); document.getElementById('hud-topic-tag').innerText = topicName;
        unpackQuestionStage(); navigateScreen('game');
    }

    function unpackQuestionStage() {
        if(questionIndex >= 10) { terminateArenaChallenge(); return; }
        
        document.getElementById('hud-index-tag').innerText = (questionIndex + 1) + "/10";
        currentActiveQuestion = targetDataset[questionIndex];
        document.getElementById('question-text').innerText = currentActiveQuestion.text;

        let optionsSet = new Set(); optionsSet.add(currentActiveQuestion.answer);

        while(optionsSet.size < 4) {
            let variance = (Math.random() > 0.5 ? 1 : -1) * (Math.floor(Math.random() * currentActiveQuestion.variantRange) + 1);
            let alternate = currentActiveQuestion.answer + variance;
            
            if(currentActiveQuestion.answer % 1 !== 0) {
                alternate = parseFloat((currentActiveQuestion.answer + (variance * 0.1)).toFixed(1));
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
            slots[i].style.boxShadow = "0 8px 20px rgba(0,0,0,0.5)";
        }
    }

    function verifyArenaChoice(node) {
        const userChoice = parseFloat(node.innerText); const consoleBox = document.getElementById("console-box");
        
        if(Math.abs(userChoice - currentActiveQuestion.answer) < 0.01) {
            scoreCounter++; node.style.borderColor = "#10b981"; node.style.background = "radial-gradient(circle at center, #10b981 0%, #059669 100%)"; node.style.color = "#ffffff"; node.style.boxShadow = "0 0 30px #10b981";
            consoleBox.classList.add("console-correct"); playFaaCorrect(); activeFXState = "correct";
        } else {
            if(!analyticalErrorPool[selectedTopicId]) analyticalErrorPool[selectedTopicId] = [];
            analyticalErrorPool[selectedTopicId].push(currentActiveQuestion.typeId);
            node.style.borderColor = "#ef4444"; node.style.background = "radial-gradient(circle at center, #ef4444 0%, #dc2626 100%)"; node.style.color = "#ffffff"; node.style.boxShadow = "0 0 30px #ef4444";
            consoleBox.classList.add("console-incorrect"); playHahaIncorrect(); activeFXState = "incorrect";
        }

        setTimeout(() => {
            consoleBox.classList.remove("console-correct", "console-incorrect"); activeFXState = "ambient";
            questionIndex++; unpackQuestionStage();
        }, 1200);
    }

    function terminateArenaChallenge() {
        document.getElementById('score-ratio-display').innerText = scoreCounter + " / 10";
        let phrase = "";
        if(scoreCounter === 10) phrase = "🔥 PERFECT MATRIX ACCURACY!";
        else if(scoreCounter >= 7) phrase = "⚡ TARGET SECURED - SECTOR CLEARED";
        else phrase = "⚠️ CRITICAL EVALUATION FAILURE";
        document.getElementById('performance-phrase').innerText = phrase;
        navigateScreen('score');
    }

    function triggerSmartRestart() { launchChapterArena(selectedTopicId, currentTopicName); }
</script>

</body>
</html>
"""

sanitized_game_html = raw_template_html.replace(
    "%%RIGHT_AUDIO_REPLACE%%", right_answer_audio
).replace(
    "%%WRONG_AUDIO_REPLACE%%", wrong_answer_audio
)

components.html(sanitized_game_html, height=680)  
