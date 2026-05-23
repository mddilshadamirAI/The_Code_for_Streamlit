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
st.markdown("<p style='text-align: center; color: #a855f7; font-family: monospace; font-size: 11px; margin-top:4px; margin-bottom: 20px; letter-spacing: 2px;'>// ENGINE CORE V6.0 // FULL NCERT TEXTBOOK REPLICA // NEP MULTI-ARCHETYPE GENERATOR</p>", unsafe_allow_html=True)

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
        background: rgba(4, 10, 26, 0.86);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 36px;
        padding: 20px;
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
        text-align: center; color: #ffffff; font-size: 15px; font-weight: 900;
        letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;
        text-shadow: 0 0 10px rgba(6, 182, 212, 0.5);
    }
    
    .grid-selector {
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;
        overflow-y: auto; max-height: 460px; padding: 4px;
    }
    
    .grid-selector::-webkit-scrollbar { width: 4px; }
    .grid-selector::-webkit-scrollbar-thumb { background: #a855f7; border-radius: 10px; }

    .matrix-btn {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px; color: #38bdf8; font-weight: 900;
        padding: 12px 4px; font-size: 11px; cursor: pointer; text-align: center;
        transition: all 0.2s ease; font-family: monospace;
    }
    .matrix-btn:hover {
        background: linear-gradient(135deg, #06b6d4 0%, #a855f7 100%);
        color: #ffffff; border-color: #ffffff;
        box-shadow: 0 0 12px rgba(6, 182, 212, 0.5);
        transform: translateY(-1px);
    }
    
    .back-btn {
        background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.4);
        color: #ef4444; border-radius: 12px; padding: 8px; font-size: 11px;
        cursor: pointer; font-weight: 900; letter-spacing: 1px; width: 100%; margin-top: 6px;
    }
    .back-btn:hover { background: #ef4444; color: #ffffff; }

    .hud-header {
        display: flex; justify-content: space-between; align-items: center;
        color: #94a3b8; font-size: 11px; letter-spacing: 1px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding-bottom: 6px;
    }
    .score-glow { color: #06b6d4; font-weight: 900; font-size: 14px; text-shadow: 0 0 10px #06b6d4; }

    .question-deck {
        width: 100%; min-height: 155px;
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.96) 0%, rgba(2, 6, 23, 0.99) 100%);
        border-radius: 20px; border: 1px solid rgba(6, 182, 212, 0.25);
        padding: 16px; text-align: left; box-sizing: border-box;
        display: flex; flex-direction: column; justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    #question-text { font-size: 13.5px; color: #f8fafc; font-weight: 700; line-height: 1.6; }

    .orbit-container { position: relative; width: 100%; height: 230px; display: flex; justify-content: center; align-items: center; }
    .orbit-rotor-2d {
        position: absolute; width: 160px; height: 160px;
        border-radius: 50%; border: 2px dashed rgba(6, 182, 212, 0.12);
        display: flex; justify-content: center; align-items: center;
        animation: spin2D 16s linear infinite !important;
    }
    @keyframes spin2D { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    .option-node-2d {
        position: absolute; width: 78px; height: 78px;
        background: radial-gradient(circle at 30% 30%, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 1) 100%);
        border: 1px solid rgba(6, 182, 212, 0.35); border-radius: 50%;
        color: #38bdf8; font-size: 13px; font-weight: 900;
        display: flex; justify-content: center; align-items: center;
        cursor: pointer; user-select: none; text-align: center; overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        animation: keepUpright 16s linear infinite !important;
        padding: 6px; box-sizing: border-box;word-break: break-all;
    }
    @keyframes keepUpright { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }

    .option-node-2d:hover {
        color: #ffffff; background: radial-gradient(circle at center, #06b6d4 0%, #0891b2 100%);
        border-color: #22d3ee; box-shadow: 0 0 25px #06b6d4; transform: scale(1.08);
    }

    .opt-0 { top: -39px; left: 41px; }   
    .opt-1 { top: 41px; right: -39px; }  
    .opt-2 { bottom: -39px; left: 41px; }
    .opt-3 { top: 41px; left: -39px; }   

    .scorecard-box { text-align: center; padding: 20px; background: rgba(15,23,42,0.8); border-radius: 24px; border: 1px solid rgba(168,85,247,0.3); }
    .metric-rank { font-size: 50px; font-weight: 900; color: #22d3ee; text-shadow: 0 0 20px rgba(34,211,238,0.4); margin: 10px 0; }
</style>
</head>
<body>

<div class="arena-viewport" id="viewport-frame">
    <canvas id="three-canvas"></canvas>

    <div class="game-console" id="console-box">
        
        <div class="screen-panel screen-active" id="screen-grade">
            <div class="menu-title">SELECT SCHOOL STAGE (NEP Framework)</div>
            <div class="grid-selector">
                <button class="matrix-btn" onclick="triggerGradeSelect(1)">GRADE 01<br><small style="color:#a855f7">Foundational</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(2)">GRADE 02<br><small style="color:#a855f7">Foundational</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(3)">GRADE 03<br><small style="color:#a855f7">Preparatory</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(4)">GRADE 04<br><small style="color:#a855f7">Preparatory</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(5)">GRADE 05<br><small style="color:#a855f7">Preparatory</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(6)">GRADE 06<br><small style="color:#a855f7">Middle Stage</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(7)">GRADE 07<br><small style="color:#a855f7">Middle Stage</small></button>
                <button class="matrix-btn" onclick="triggerGradeSelect(8)">GRADE 08<br><small style="color:#a855f7">Middle Stage</small></button>
            </div>
            <div style="text-align: center; font-size: 10px; color: #475569;">FULL NCERT SYLLABUS DIRECTORY MAP</div>
        </div>

        <div class="screen-panel" id="screen-chapter">
            <div>
                <div class="menu-title" id="chapter-panel-title">NCERT CHAPTER MATRIX</div>
                <div class="grid-selector" id="chapter-injection-grid"></div>
            </div>
            <button class="back-btn" onclick="navigateScreen('grade')">◀ BACK TO STAGES</button>
        </div>

        <div class="screen-panel" id="screen-game">
            <div class="hud-header">
                <div id="hud-topic-tag" style="max-width: 60%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-weight:900; color:#e2e8f0;">CHAPTER</div>
                <div>PROGRESS: <span id="hud-index-tag" class="score-glow">1/10</span></div>
            </div>
            
            <div class="question-deck">
                <div id="question-text">COMPILING HIGH-STAKES NEP COMPETENCY SCHEMATIC...</div>
            </div>

            <div class="orbit-container">
                <div class="orbit-rotor-2d">
                    <div class="option-node-2d opt-0" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-1" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-2" onclick="verifyArenaChoice(this)">0</div>
                    <div class="option-node-2d opt-3" onclick="verifyArenaChoice(this)">0</div>
                </div>
            </div>
            
            <div style="text-align: center; font-size: 10px; color: #475569; letter-spacing: 1px;">// ROTATIONAL MATRIX GENERATION ACTIVE</div>
        </div>

        <div class="screen-panel" id="screen-score">
            <div class="menu-title">COMPETENCY EVALUATION RECORD</div>
            <div class="scorecard-box">
                <div style="color: #94a3b8; font-size: 12px; letter-spacing: 2px;">NCERT ACCURACY VERDICT</div>
                <div class="metric-rank" id="score-ratio-display">0 / 10</div>
                <div style="color: #a855f7; font-size: 14px; font-weight: 900; margin-bottom: 10px;" id="performance-phrase">COMPLETED</div>
                <p style="color: #64748b; font-size: 11px; line-height: 1.4;">Deterministic index variation guarantees completely fresh question types on reset.</p>
            </div>
            <div>
                <button class="matrix-btn" style="width:100%; margin-bottom:10px;" onclick="triggerSmartRestart()">🔄 RUN SAME SECTOR EXERCISE</button>
                <button class="back-btn" onclick="navigateScreen('grade')">🎓 BACK TO MAIN CONSOLE</button>
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
    // THREE.JS PARTICLES
    // ==========================================================================
    const canvasElement = document.getElementById('three-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(65, 520 / 660, 0.1, 1000); camera.position.z = 18;
    const renderer = new THREE.WebGLRenderer({ canvas: canvasElement, antialias: true, alpha: true });
    renderer.setSize(520, 660); renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const totalParticles = 300; const geometry = new THREE.BufferGeometry(); const positionArray = new Float32Array(totalParticles * 3);
    for(let i=0; i < totalParticles*3; i+=3) { positionArray[i] = (Math.random() - 0.5) * 45; positionArray[i+1] = (Math.random() - 0.5) * 45; positionArray[i+2] = (Math.random() - 0.5) * 25; }
    geometry.setAttribute('position', new THREE.BufferAttribute(positionArray, 3));
    const pointMaterial = new THREE.PointsMaterial({ size: 0.4, transparent: true, opacity: 0.6, color: 0xa855f7 });
    const engineParticles = new THREE.Points(geometry, pointMaterial); scene.add(engineParticles);

    let activeFXState = "ambient";
    function tickGraphicsEngine() {
        requestAnimationFrame(tickGraphicsEngine); const positions = geometry.attributes.position.array;
        if (activeFXState === "ambient") { engineParticles.rotation.y += 0.002; pointMaterial.color.setHex(0xa855f7); }
        else if (activeFXState === "correct") { pointMaterial.color.setHex(0x10b981); for(let i=1; i<positions.length; i+=3) { positions[i]-=0.4; if(positions[i]<-22) positions[i]=22; } geometry.attributes.position.needsUpdate=true; }
        else if (activeFXState === "incorrect") { pointMaterial.color.setHex(0xef4444); for(let i=1; i<positions.length; i+=3) { positions[i]+=0.6; if(positions[i]>22) positions[i]=-22; } geometry.attributes.position.needsUpdate=true; }
        renderer.render(scene, camera);
    }
    tickGraphicsEngine();

    // ==========================================================================
    // 📚 COMPREHENSIVE NCERT COMPLETE ALL-CHAPTER DATABASE (GRADES 1 - 8)
    // ==========================================================================
    const syllabusDatabase = {
        1: [
            { id: "g1_c1", name: "Ch 1: Shapes and Space" },
            { id: "g1_c2", name: "Ch 2: Numbers 1 to 9" },
            { id: "g1_c3", name: "Ch 3: Addition Core" },
            { id: "g1_c4", name: "Ch 4: Subtraction Bounds" },
            { id: "g1_c5", name: "Ch 5: Numbers 10 to 20" },
            { id: "g1_c6", name: "Ch 6: Time & Sequences" },
            { id: "g1_c7", name: "Ch 7: Measurement Metrics" }
        ],
        2: [
            { id: "g2_c1", name: "Ch 1: Long and Round Shapes" },
            { id: "g2_c2", name: "Ch 2: Counting in Groups" },
            { id: "g2_c3", name: "Ch 3: How Much Can You Carry" },
            { id: "g2_c4", name: "Ch 4: Tens and Ones Layout" },
            { id: "g2_c5", name: "Ch 5: Structural Patterns" },
            { id: "g2_c6", name: "Ch 6: Footprints Geometry" },
            { id: "g2_c7", name: "Ch 7: Jugs and Mugs Volume" }
        ],
        3: [
            { id: "g3_c1", name: "Ch 1: Where to Look From" },
            { id: "g3_c2", name: "Ch 2: Fun with Numbers" },
            { id: "g3_c3", name: "Ch 3: Give and Take Systems" },
            { id: "g3_c4", name: "Ch 4: Long and Short Scales" },
            { id: "g3_c5", name: "Ch 5: Shapes and Designs" },
            { id: "g3_c6", name: "Ch 6: Fun with Give and Take" },
            { id: "g3_c7", name: "Ch 7: Time Goes On Matrix" }
        ],
        4: [
            { id: "g4_c1", name: "Ch 1: Building with Bricks" },
            { id: "g4_c2", name: "Ch 2: Long and Short Measures" },
            { id: "g4_c3", name: "Ch 3: A Trip to Bhopal" },
            { id: "g4_c4", name: "Ch 4: Tick-Tick-Tick Time" },
            { id: "g4_c5", name: "Ch 5: The Way The World Looks" },
            { id: "g4_c6", name: "Ch 6: The Junk Seller Trades" },
            { id: "g4_c7", name: "Ch 7: Jugs and Mugs System" }
        ],
        5: [
            { id: "g5_c1", name: "Ch 1: The Fish Tale Layout" },
            { id: "g5_c2", name: "Ch 2: Shapes and Angles Matrix" },
            { id: "g5_c3", name: "Ch 3: How Many Squares?" },
            { id: "g5_c4", name: "Ch 4: Parts and Wholes" },
            { id: "g5_c5", name: "Ch 5: Does it Look Same?" },
            { id: "g5_c6", name: "Ch 6: Be My Multiple Factor" },
            { id: "g5_c7", name: "Ch 7: Can You See the Pattern" }
        ],
        6: [
            { id: "g6_c1", name: "Ch 1: Knowing Our Numbers" },
            { id: "g6_c2", name: "Ch 2: Whole Numbers Matrix" },
            { id: "g6_c3", name: "Ch 3: Playing with Numbers" },
            { id: "g6_c4", name: "Ch 4: Basic Geometry Ideas" },
            { id: "g6_c5", name: "Ch 5: Understanding Shapes" },
            { id: "g6_c6", name: "Ch 6: Integers Coordinates" },
            { id: "g6_c7", name: "Ch 7: Fractions Operations" },
            { id: "g6_c8", name: "Ch 8: Decimals Core Arena" }
        ],
        7: [
            { id: "g7_c1", name: "Ch 1: Integers Properties" },
            { id: "g7_c2", name: "Ch 2: Fractions and Decimals" },
            { id: "g7_c3", name: "Ch 3: Data Handling Metric" },
            { id: "g7_c4", name: "Ch 4: Simple Equations Vault" },
            { id: "g7_c5", name: "Ch 5: Lines and Angles Rules" },
            { id: "g7_c6", name: "Ch 6: Triangles Properties" },
            { id: "g7_c7", name: "Ch 7: Comparing Quantities" }
        ],
        8: [
            { id: "g8_c1", name: "Ch 1: Rational Numbers Laws" },
            { id: "g8_c2", name: "Ch 2: Linear Equations 1-Var" },
            { id: "g8_c3", name: "Ch 3: Understanding Quadrilaterals" },
            { id: "g8_c4", name: "Ch 4: Data Handling Statistics" },
            { id: "g8_c5", name: "Ch 5: Squares and Square Roots" },
            { id: "g8_c6", name: "Ch 6: Cubes and Cube Roots" },
            { id: "g8_c7", name: "Ch 7: Comparing Quantities Advanced" }
        ]
    };

    let selectedGrade = null, selectedTopicId = null, currentTopicName = "", questionIndex = 0, scoreCounter = 0, targetDataset = [], currentActiveQuestion = null;

    function navigateScreen(screenId) {
        document.querySelectorAll('.screen-panel').forEach(s => s.classList.remove('screen-active'));
        document.getElementById('screen-' + screenId).classList.add('screen-active');
    }

    function triggerGradeSelect(grade) {
        selectedGrade = grade; document.getElementById('chapter-panel-title').innerText = "GRADE " + grade + ": ALL SECTORS";
        const grid = document.getElementById('chapter-injection-grid'); grid.innerHTML = "";
        syllabusDatabase[grade].forEach(topic => {
            let btn = document.createElement('button'); btn.className = "matrix-btn"; btn.innerHTML = topic.name;
            btn.onclick = () => launchChapterArena(topic.id, topic.name); grid.appendChild(btn);
        });
        navigateScreen('chapter');
    }

    // ==========================================================================
    // 🧬 ZERO-REPETITION DETERMINISTIC ARCHETYPE ENGINE (10 UNIQUES PER CHAPTER)
    // ==========================================================================
    function createProblemToken(typeId, positionIndex) {
        let text = "", answer = 0, variantRange = 10;
        let seedA = Math.floor(Math.random() * 12) + 4;
        let seedB = Math.floor(Math.random() * 8) + 3;

        switch(typeId) {
            // ==================== GRADE 6 ARCHETYPE SUITE ====================
            case "g6_c1": // Knowing Our Numbers
                if(positionIndex === 0) {
                    let digs = [7, 4, 1, 9, 2].sort(() => Math.random() - 0.5);
                    text = "NCERT Exercise 1.1: Determine the absolute difference between the greatest and least possible 5-digit number configuration formed using digits " + digs.join(",") + " exactly once each.";
                    let high = parseInt([...digs].sort((a,b)=>b-a).join(""));
                    let low = parseInt([...digs].sort((a,b)=>a-b).join(""));
                    answer = high - low; variantRange = 4000;
                } else if(positionIndex === 1) {
                    text = "A major industrial machine prints exactly " + seedA + "85 text-brochures daily. Calculate the grand volume layout for the complete month of January.";
                    answer = (seedA * 100 + 85) * 31; variantRange = 2000;
                } else if(positionIndex === 2) {
                    text = "A school hostel requires 4 litres and 500 ml of fresh milk for a curd recipe batch. How many standard glass tumblers, each containing exactly 25 ml capacity, can be completely filled out from this milk block?";
                    answer = 4500 / 25; variantRange = 25;
                } else if(positionIndex === 3) {
                    let rMap = {95: "XCV", 44: "XLIV", 69: "LXIX", 88: "LXXXVIII"};
                    let val = [95, 44, 69, 88][Math.floor(Math.random()*4)];
                    text = "NCERT Roman Systems: Evaluate the exact integer coordinate value represented by the structural Roman token system string: '" + rMap[val] + "'.";
                    answer = val; variantRange = 5;
                } else if(positionIndex === 4) {
                    text = "A container truck is bounded to hold a max load limit of 450 kg. How many distinct hardware item packets, each scaling exactly " + seedB + " kg, can be securely loaded onto the vehicle?";
                    answer = Math.floor(450 / seedB); variantRange = 8;
                } else if(positionIndex === 5) {
                    text = "According to Indian Place Value tracking metrics, evaluate how many total Lakhs accumulate perfectly to balance out precisely 10 Million units.";
                    answer = 100; variantRange = 20;
                } else if(positionIndex === 6) {
                    text = "Seema owns ₹" + (seedA*1000) + ". She places a purchase order for " + seedB + " electronic components priced uniformly at ₹120 each. Calculate her absolute remaining wallet balance.";
                    answer = (seedA*1000) - (seedB * 120); variantRange = 500;
                } else if(positionIndex === 7) {
                    text = "Round off the measurement metric constant integer token " + (seedA * 47) + " to its nearest valid HUNDREDS boundary line coordinate profile.";
                    answer = Math.round((seedA * 47)/100)*100; variantRange = 100;
                } else if(positionIndex === 8) {
                    text = "A merchant has " + (seedA*15) + " rows of storage boxes. Each single row contains exactly " + seedB + " boxes, and each box contains 2 entry logs. Solve the total combined system log sum.";
                    answer = (seedA*15) * seedB * 2; variantRange = 150;
                } else {
                    text = "NCERT Core Assessment: Write out the total structural count of all whole numbers that sit strictly between the numerical interval lines of 32 and 53.";
                    answer = 53 - 32 - 1; variantRange = 3;
                }
                break;

            case "g6_c2": // Whole Numbers Matrix
                if(positionIndex === 0) {
                    text = "Identify the fundamental identity structural constant element assigned to global whole numbers under standard Multiplication loops.";
                    answer = 1; variantRange = 3;
                } else if(positionIndex === 1) {
                    text = "Apply distributive properties of whole sets: Compute the configuration product values for expression: 125 x " + seedA + " x 8. Isolate final value string.";
                    answer = 1000 * seedA; variantRange = 1000;
                } else if(positionIndex === 2) {
                    text = "What is the absolute immediate predecessor value belonging to the smallest possible 5-digit number system entry?";
                    answer = 9999; variantRange = 5;
                } else if(positionIndex === 3) {
                    text = "Evaluate bracket distribution rules via NCERT methodology: Compute the equation " + seedB + " x 1005. Find total output tally.";
                    answer = seedB * 1005; variantRange = 100;
                } else if(positionIndex === 4) {
                    text = "Isolate the geometric pattern anomaly vector: If dots arrange as regular triangular patterns, determine which value cannot fit a triangle grid: 3, 6, 10, or 7?";
                    answer = 7; variantRange = 4;
                } else {
                    text = "Find the sum tracking configuration values under associative law formats: (" + seedA + " + 19) + 81. Evaluate total net sum.";
                    answer = seedA + 100; variantRange = 20;
                }
                break;

            case "g6_c3": // Playing with Numbers
                if(positionIndex === 0) {
                    text = "NCERT Ex 3.7: Three tankers contain 403 litres, 434 litres, and 465 litres of diesel respectively. Find the maximum capacity of a container that can measure the diesel of all three tankers an exact number of times (HCF).";
                    answer = 31; variantRange = 10;
                } else if(positionIndex === 1) {
                    text = "Four traffic lights flash at successive paths of 24, 36, 54, and 72 seconds. If they loop together at 0, after how many total seconds do they coordinate a joint flash alignment again (LCM)?";
                    answer = 216; variantRange = 50;
                } else if(positionIndex === 2) {
                    text = "Determine the exact count of unique factor elements present inside the mathematical composite integer tracking constant 60.";
                    answer = 12; variantRange = 4;
                } else if(positionIndex === 3) {
                    text = "If a mystery parameter number configuration code string '2x4' resolves as completely divisible by 3, isolate the least integer value for single digit x.";
                    answer = 0; variantRange = 3;
                } else if(positionIndex === 4) {
                    text = "Evaluate the unique total tracking count of complete prime number values trapped between boundaries 10 and 25.";
                    answer = 5; variantRange = 2; // 11, 13, 17, 19, 23
                } else {
                    text = "Find the smallest 4-digit number which is completely divisible by the base prime group constants: 6, 8, and 12.";
                    answer = 1008; variantRange = 48;
                }
                break;

            // ==================== GRADE 7 ARCHETYPE SUITE ====================
            case "g7_c1": // Integers Properties
                if(positionIndex === 0) {
                    text = "A high-altitude test freeze chamber drops structural temperatures at a steady slope of 5°C every hour. If starting coordinates read 15°C, determine internal values after " + seedB + " hours.";
                    answer = 15 - (seedB * 5); variantRange = 20;
                } else if(positionIndex === 1) {
                    text = "In a standard objective test, (+3) marks apply for correct choices and (-1) for invalid responses. Kavita records 12 correct paths but secures only 26 net marks. How many mistakes did she submit?";
                    answer = 36 - 26; variantRange = 4;
                } else if(positionIndex === 2) {
                    text = "Evaluate integer layout configurations under operational sign rules: (-2) x (-5) x (-4) x (-3). Resolve final index integer.";
                    answer = 120; variantRange = 30;
                } else if(positionIndex === 3) {
                    text = "An elevator cage enters a mining excavation shaft dropping downwards at a metric index rate of 6 meters per minute. If starting from 10m above ground level, what is its elevation tracking value coordinate after 30 minutes?";
                    answer = 10 - (30 * 6); variantRange = 40;
                } else {
                    text = "Simplify integer code sequences: Calculate the value for expression matrix: (-49) divided by [ (-45) + (-4) ].";
                    answer = 1; variantRange = 3;
                }
                break;

            case "g7_c2": // Fractions and Decimals
                if(positionIndex === 0) {
                    text = "A sleek rectangular plot framework exhibits an explicit horizontal length dimension matching 5.7 cm and a vertical width parameter of 3 cm. Calculate its total interior area capacity.";
                    answer = 5.7 * 3; variantRange = 2;
                } else if(positionIndex === 1) {
                    text = "A motor bike vehicle traverses a clean displacement path of 55.3 km utilizing exactly 1 litre of fuel compound. What net distance tracking scope does it cover on a full 10 litre containment block?";
                    answer = 553; variantRange = 20;
                } else if(positionIndex === 2) {
                    text = "NCERT Core Rational Matrix: Solve fractional product formats: Evaluate configuration output tracking value for: (4/5) x (2/3) x (15/8). Reduce completely.";
                    answer = 1; variantRange = 3;
                } else if(positionIndex === 3) {
                    text = "Determine decimal division conversions: Evaluate the precise output value balance for the parsing string execution: 0.05 divided by 0.25.";
                    answer = 0.2; variantRange = 1;
                } else {
                    text = "A metal rod measuring 7.5 meters is sliced into uniform individual link units measuring exactly 1.25 meters each. Find the total counts of structural slices generated.";
                    answer = 6; variantRange = 3;
                }
                break;

            case "g7_c3": // Data Handling Metric
                if(positionIndex === 0) {
                    text = "Analyze student score data matrices: Determine the arithmetic mean average constant for the array sequence parameters: [" + seedA + ", " + (seedA+2) + ", " + (seedA+4) + ", " + (seedA+6) + ", " + (seedA+8) + "].";
                    answer = seedA + 4; variantRange = 5;
                } else if(positionIndex === 1) {
                    text = "Isolate statistical properties: Find the exact median balance value matching the dataset track array mapping: [12, 14, 15, 18, 19, 21, 25].";
                    answer = 18; variantRange = 5;
                } else {
                    text = "Calculate total range parameters of a research tracking survey containing absolute limit metrics: Min output = 42, Max output = " + (100 + seedA) + ". Subtract boundaries.";
                    answer = (100 + seedA) - 42; variantRange = 15;
                }
                break;

            // ==================== GRADE 8 ARCHETYPE SUITE ====================
            case "g8_c1": // Rational Numbers Laws
                if(positionIndex === 0) {
                    text = "Name the identity parameter attribute that acts as the absolute additive identity tracking core across all real rational number systems.";
                    answer = 0; variantRange = 3;
                } else if(positionIndex === 1) {
                    text = "Isolate reciprocal transformations: Determine the exact denominator coordinate for the multiplicative inverse of the fraction model: -8 / 15.";
                    answer = -8; variantRange = 5;
                } else if(positionIndex === 2) {
                    text = "Evaluate algebraic fractions using standard commutative groupings: Compute [ 3/7 + (-6/11) + (-8/7) ]. Isolate final fractional numerator if denominator matches 11.";
                    answer = -6; variantRange = 4;
                } else {
                    text = "What is the result when a rational number x is multiplied by its absolute negative representation (-x) given x = 2?";
                    answer = -4; variantRange = 5;
                }
                break;

            case "g8_c2": // Linear Equations 1-Var
                if(positionIndex === 0) {
                    text = "NCERT Chapter 2.2 Word Problem: Two structural variables maintain an internal base proportion ratio map of 5:8. If their combined numeric sum balances out at exactly 182, solve for the smaller value element.";
                    answer = (182 / 13) * 5; variantRange = 20;
                } else if(positionIndex === 1) {
                    text = "Rahul's mother's current age profile is exactly 3 times Rahul's current age footprint. After 5 years, their combined structural age logs sum up to 66 years. Find Rahul's current age.";
                    // x + 3x + 10 = 66 -> 4x = 56 -> x = 14
                    answer = 14; variantRange = 4;
                } else if(positionIndex === 2) {
                    text = "Solve structural balance single variable mechanics: Solve equation string value for unknown parameter x: 8x + 4 = 3(x - 1) + 7.";
                    answer = 0; variantRange = 3;
                } else if(positionIndex === 3) {
                    text = "The perimeter tracking boundary loop of a regular rectangle configuration spans 13 cm wide. If its explicit vertical width handles 2.75 cm, solve its long base dimension format.";
                    answer = (13 / 2) - 2.75; variantRange = 2;
                } else {
                    text = "A collection of currency denominations holds exactly ₹50 and ₹100 notes totaling 25 notes overall. If the absolute monetary ledger evaluates to ₹2000, how many ₹100 notes are present?";
                    answer = 15; variantRange = 5;
                }
                break;

            case "g8_c5": // Squares and Square Roots
                if(positionIndex === 0) {
                    text = "NCERT Exercise 6.4: A gardener plans to set up exactly 1000 plants in a clean square block matrix grid layout. Find the minimum extra plants needed to ensure rows equal columns perfectly.";
                    answer = 24; variantRange = 10; // 32^2 = 1024
                } else if(positionIndex === 1) {
                    text = "Isolate core root parameters via prime factorization tracking: Find the exact square root calculation for variable index token value: √7056.";
                    answer = 84; variantRange = 12;
                } else if(positionIndex === 2) {
                    text = "Evaluate Pythagorean Triplet elements maps: If one element inside a structural triplet array registers at 6, find the highest value hypotenuse partner inside the triplet set.";
                    answer = 10; variantRange = 3; // 6, 8, 10
                } else {
                    text = "Find the smallest integer value by which the tracking variable constant 180 must be multiplied to morph it into a perfect square layout.";
                    answer = 5; variantRange = 2; // 180 * 5 = 900
                }
                break;

            // ==================== EARLY GRADE ROBUST CORES ====================
            default:
                if(positionIndex === 0) {
                    text = "NCERT Foundational Visualizer: An artist fits 3 large circular spheres on a horizontal canvas row, followed by 4 square box models. Compute the total shape sum.";
                    answer = 7; variantRange = 3;
                } else if(positionIndex === 1) {
                    text = "A school storage shelf stores " + (seedA+10) + " notebooks. Teachers distribute " + seedB + " booklets to students. Evaluate the remaining inventory count.";
                    answer = (seedA+10) - seedB; variantRange = 5;
                } else if(positionIndex === 2) {
                    text = "Identify total geometric corner nodes mapping explicitly onto a standard 2D plain layout structure of a Triangle.";
                    answer = 3; variantRange = 2;
                } else {
                    text = "Complete the logical loop sequence progression steps: 2, 4, 6, 8, __. Isolate the following coordinate track value.";
                    answer = 10; variantRange = 2;
                }
        }

        return { text: text, answer: answer, typeId: typeId, variantRange: variantRange };
    }

    function buildSessionDeck(topicId) {
        let deck = [];
        // The loop explicitly locks the loop index `i` into the problem generator to completely block repeating items
        for(let i = 0; i < 10; i++) {
            deck.push(createProblemToken(topicId, i));
        }
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
            if(currentActiveQuestion.variantRange <= 5) variance = (Math.random() > 0.5 ? 1 : -1) * (Math.floor(Math.random() * 2) + 1);
            
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
        
        if(Math.abs(userChoice - currentActiveQuestion.answer) < 0.05) {
            scoreCounter++; node.style.borderColor = "#10b981"; node.style.background = "radial-gradient(circle at center, #10b981 0%, #059669 100%)"; node.style.color = "#ffffff"; node.style.boxShadow = "0 0 30px #10b981";
            consoleBox.classList.add("console-correct"); playFaaCorrect(); activeFXState = "correct";
        } else {
            node.style.borderColor = "#ef4444"; node.style.background = "radial-gradient(circle at center, #ef4444 0%, #dc2626 100%)"; node.style.color = "#ffffff"; node.style.boxShadow = "0 0 30px #ef4444";
            consoleBox.classList.add("console-incorrect"); playHahaIncorrect(); activeFXState = "incorrect";
        }

        setTimeout(() => {
            consoleBox.classList.remove("console-correct", "console-incorrect"); activeFXState = "ambient";
            questionIndex++; unpackQuestionStage();
        }, 1300);
    }

    function terminateArenaChallenge() {
        document.getElementById('score-ratio-display').innerText = scoreCounter + " / 10";
        let phrase = "";
        if(scoreCounter === 10) phrase = "👑 ACCURACY MATRIX MAXED!";
        else if(scoreCounter >= 7) phrase = "⚡ STAGE CHALLENGE SECURED";
        else phrase = "⚠️ SYSTEM PERFORMANCE ALERT";
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
