import streamlit as st
import streamlit.components.v1 as components

# Application workspace node setup
st.set_page_config(
    page_title="Dilshad's 3D Math Arena",
    page_icon="⚡",
    layout="centered"
)

# Dark space layout overrides
st.markdown("""
<style>
div[data-testid="stAppViewContainer"], .main {
    background: #030712 !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #f8fafc; font-family: sans-serif; font-weight: 900; letter-spacing: -1px; margin-bottom:0px;'>⚔️ Math Arena 3D</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a855f7; font-family: monospace; font-size: 13px; margin-top:4px; margin-bottom: 20px;'>// SYSTEM STATE: RUNNING ENGINE.JS GRAPHICS</p>", unsafe_allow_html=True)

# ==============================================================================
# 🎮 THE THREE.JS 3D ARENA & GAME CORE RUNTIME
# ==============================================================================
game_engine_html = """
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
        font-family: system-ui, -apple-system, sans-serif;
    }

    /* 🌌 GAME STAGE VIEWPORT CONTAINER */
    .arena-viewport {
        position: relative;
        width: 480px;
        height: 640px;
        display: flex; justify-content: center; align-items: center;
        perspective: 1200px;
    }

    /* 🎨 WEBGL HARDWARE-ACCELERATED LAYER */
    #three-canvas {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 1;
        border-radius: 40px;
    }

    /* 💎 SYSTEM CONTROL OVERLAY GLASS PANELS */
    .game-console {
        position: relative;
        z-index: 2;
        width: 85%;
        height: 90%;
        background: rgba(15, 23, 42, 0.2);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 36px;
        padding: 30px;
        box-sizing: border-box;
        border: 1px solid rgba(255, 255, 255, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 30px 70px rgba(0,0,0,0.7);
    }

    /* HUDS & SCREEN DISPLAY MARKS */
    .hud-header {
        display: flex; justify-content: space-between;
        color: #94a3b8; font-family: monospace; font-size: 14px;
        letter-spacing: 1px;
    }
    
    .score-glowing { color: #a855f7; font-weight: bold; text-shadow: 0 0 10px rgba(168, 85, 247, 0.4); }

    .question-deck {
        width: 100%;
        background: rgba(0, 0, 0, 0.5);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        padding: 25px 10px;
        text-align: center;
        box-sizing: border-box;
        box-shadow: inset 0 4px 20px rgba(0,0,0,0.8);
    }
    
    #question-text {
        font-size: 44px; color: #f8fafc; font-weight: 800; font-family: monospace;
        letter-spacing: -1px;
    }

    /* 🔄 THE 3D REVOLVING ORBIT MATRIX CONTEXT */
    .orbit-scene {
        position: relative;
        width: 100%;
        height: 260px;
        margin-top: 20px;
        transform-style: preserve-3d;
        display: flex; justify-content: center; align-items: center;
    }

    .orbit-rotor {
        position: absolute;
        width: 100%; height: 100%;
        transform-style: preserve-3d;
        /* Infinite 3D rotation animation loop */
        animation: spinOrbit 12s linear infinite;
        display: flex; justify-content: center; align-items: center;
    }

    @keyframes spinOrbit {
        0% { transform: rotateY(0deg); }
        100% { transform: rotateY(360deg); }
    }

    /* Pauses the carousel rotation when user attempts an acquisition lock-on */
    .orbit-scene:hover .orbit-rotor {
        animation-play-state: paused;
    }

    /* 🔮 3D HIGH-FIDELITY BUBBLE OPTION SPHERES */
    .option-node {
        position: absolute;
        width: 75px;
        height: 75px;
        background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.01));
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 50%;
        color: #f1f5f9;
        font-size: 22px; font-weight: bold; font-family: monospace;
        display: flex; justify-content: center; align-items: center;
        cursor: pointer;
        user-select: none;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5),
                    inset 0 4px 6px rgba(255,255,255,0.05),
                    inset 0 -6px 10px rgba(0,0,0,0.4);
        transition: transform 0.2s, background 0.2s, border 0.2s, box-shadow 0.2s;
    }

    /* Spatially lock positions across 360-degree cylindrical vectors */
    .opt-0 { transform: rotateY(0deg) translateZ(135px) rotateY(0deg); }
    .opt-1 { transform: rotateY(90deg) translateZ(135px) rotateY(-90deg); }
    .opt-2 { transform: rotateY(180deg) translateZ(135px) rotateY(-180deg); }
    .opt-3 { transform: rotateY(270deg) translateZ(135px) rotateY(-270deg); }

    /* Auto-counter balance rules to keep texts facing forward while rotating */
    .orbit-scene:not(:hover) .opt-0 { animation: reverseLook 12s linear infinite; }
    .orbit-scene:not(:hover) .opt-1 { animation: reverseLookShift1 12s linear infinite; }
    .orbit-scene:not(:hover) .opt-2 { animation: reverseLookShift2 12s linear infinite; }
    .orbit-scene:not(:hover) .opt-3 { animation: reverseLookShift3 12s linear infinite; }

    @keyframes reverseLook { 0% { transform: rotateY(0deg) translateZ(135px) rotateY(0deg); } 100% { transform: rotateY(360deg) translateZ(135px) rotateY(-360deg); } }
    @keyframes reverseLookShift1 { 0% { transform: rotateY(90deg) translateZ(135px) rotateY(-90deg); } 100% { transform: rotateY(450deg) translateZ(135px) rotateY(-450deg); } }
    @keyframes reverseLookShift2 { 0% { transform: rotateY(180deg) translateZ(135px) rotateY(-180deg); } 100% { transform: rotateY(540deg) translateZ(135px) rotateY(-540deg); } }
    @keyframes reverseLookShift3 { 0% { transform: rotateY(270deg) translateZ(135px) rotateY(-270deg); } 100% { transform: rotateY(630deg) translateZ(135px) rotateY(-630deg); } }

    .option-node:hover {
        background: rgba(168, 85, 247, 0.15);
        color: #c084fc;
        border-color: #a855f7;
        box-shadow: 0 0 25px rgba(168, 85, 247, 0.4), inset 0 2px 4px rgba(255,255,255,0.1);
        transform: scale(1.1) !important;
    }
    
    .option-node:active { transform: scale(0.9) !important; }
</style>
</head>
<body>

<div class="arena-viewport">
    <canvas id="three-canvas"></canvas>

    <div class="game-console">
        <div class="hud-header">
            <div>TARGET: SECURE LIQUIDITY</div>
            <div>SCORE: <span id="score-val" class="score-glowing">0</span></div>
        </div>
        
        <div class="question-deck">
            <div id="question-text">LOADING...</div>
        </div>

        <div class="orbit-scene">
            <div class="orbit-rotor" id="btn-rotor">
                <div class="option-node opt-0" onclick="verifyChoice(this)">0</div>
                <div class="option-node opt-1" onclick="verifyChoice(this)">0</div>
                <div class="option-node opt-2" onclick="verifyChoice(this)">0</div>
                <div class="option-node opt-3" onclick="verifyChoice(this)">0</div>
            </div>
        </div>
        
        <div style="text-align: center; font-size: 11px; color: #475569; font-family: monospace; letter-spacing: 0.5px;">
            HINT: HOVER OVER SYSTEM TO LOCK ROTATION ENGINE
        </div>
    </div>
</div>

<script>
    // ==========================================================================
    // 🧬 THREE.JS ENGINE CORE: PARTICLES LOGIC ENGINE
    // ==========================================================================
    const canvas = document.getElementById('three-canvas');
    const scene = new THREE.Scene();
    
    const camera = new THREE.PerspectiveCamera(65, 480 / 640, 0.1, 1000);
    camera.position.z = 20;

    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    renderer.setSize(480, 640);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Instantiating Particle Arrays
    const particleCount = 350;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    
    for(let i=0; i < particleCount*3; i+=3) {
        positions[i] = (Math.random() - 0.5) * 40;     // X Mapping
        positions[i+1] = (Math.random() - 0.5) * 40;   // Y Mapping
        positions[i+2] = (Math.random() - 0.5) * 30;   // Z Mapping
    }
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    // Dynamic point cloud materials mapping
    const matConfig = { size: 0.35, transparent: true, opacity: 0.5 };
    const pMaterial = new THREE.PointsMaterial(matConfig);
    pMaterial.color.setHex(0x64748b); // Ambient Slate Grey Points
    
    const particleSystem = new THREE.Points(geometry, pMaterial);
    scene.add(particleSystem);

    // Engine FX State Variables
    let currentFXState = "ambient"; // Possible states: ambient, snow, fire
    let fxTimer = 0;

    // INFINITE RUNTIME CORE LOOP (60 FPS Execution ticks)
    function tickEngine() {
        requestAnimationFrame(tickEngine);
        
        const posArr = geometry.attributes.position.array;
        
        // Read active global state instructions
        if (currentFXState === "ambient") {
            particleSystem.rotation.y += 0.002;
            particleSystem.rotation.x += 0.001;
            pMaterial.color.setHex(0x5b21b6); // Purple structural tint
        } 
        else if (currentFXState === "snow") {
            pMaterial.color.setHex(0x38bdf8); // Sky blue ice tint
            // Force cascading downward linear vector paths
            for(let i=1; i < posArr.length; i+=3) {
                posArr[i] -= 0.25; 
                if(posArr[i] < -20) posArr[i] = 20; // Recycle position boundary
            }
            geometry.attributes.position.needsUpdate = true;
        } 
        else if (currentFXState === "fire") {
            pMaterial.color.setHex(0xef4444); // Raging Crimson Fire Tint
            // Force upward turbulent vectors
            for(let i=1; i < posArr.length; i+=3) {
                posArr[i] += 0.35;
                if(posArr[i] > 20) {
                    posArr[i] = -20;
                    posArr[i-1] = (Math.random() - 0.5) * 30; // Inject scatter variance
                }
            }
            geometry.attributes.position.needsUpdate = true;
        }

        renderer.render(scene, camera);
    }
    tickEngine();

    // ==========================================================================
    // 🔊 SYNTHETIC AUDIO WAVE MATRIX (WEB AUDIO API GENERATORS)
    // ==========================================================================
    const AudioContextEngine = new (window.AudioContext || window.webkitAudioContext)();

    function playSuccessChime() {
        const now = AudioContextEngine.currentTime;
        const osc = AudioContextEngine.createOscillator();
        const gain = AudioContextEngine.createGain();
        osc.connect(gain); gain.connect(AudioContextEngine.destination);
        
        osc.type = 'triangle';
        // Multi-stage rising chord sequence
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.setValueAtTime(659.25, now + 0.08); // E5
        osc.frequency.setValueAtTime(783.99, now + 0.16); // G5
        osc.frequency.setValueAtTime(1046.50, now + 0.24); // C6
        
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
        osc.start(); osc.stop(now + 0.4);
    }

    function playExplodeBoom() {
        const now = AudioContextEngine.currentTime;
        const osc = AudioContextEngine.createOscillator();
        const noise = AudioContextEngine.createOscillator();
        const gain = AudioContextEngine.createGain();
        osc.connect(gain); noise.connect(gain); gain.connect(AudioContextEngine.destination);
        
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(130, now);
        osc.frequency.linearRampToValueAtTime(30, now + 0.5);
        
        noise.type = 'square';
        noise.frequency.setValueAtTime(55, now);
        noise.frequency.linearRampToValueAtTime(5, now + 0.4);
        
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
        osc.start(); noise.start();
        osc.stop(now + 0.5); noise.stop(now + 0.5);
    }

    // ==========================================================================
    // 🧠 1000+ QUESTION REPETITION COMPREHENSION MATRIX
    // ==========================================================================
    let score = 0;
    let correctAnswer = 0;
    let questionHistoryArray = [];

    function generateUniqueQuestion() {
        let op, num1, num2, statement, result;
        const operations = ['+', '-', '*', '/'];
        
        while (true) {
            op = operations[Math.floor(Math.random() * operations.length)];
            
            if (op === '+') {
                num1 = Math.floor(Math.random() * 90) + 10;
                num2 = Math.floor(Math.random() * 90) + 10;
                statement = `${num1} + ${num2}`; result = num1 + num2;
            } 
            else if (op === '-') {
                num1 = Math.floor(Math.random() * 90) + 10;
                num2 = Math.floor(Math.random() * (num1 - 10 + 1)) + 10; // Guarantees positive targets
                statement = `${num1} - ${num2}`; result = num1 - num2;
            } 
            else if (op === '*') {
                num1 = Math.floor(Math.random() * 90) + 10;
                num2 = Math.floor(Math.random() * 90) + 10;
                statement = `${num1} × ${num2}`; result = num1 * num2;
            } 
            else if (op === '/') {
                num2 = Math.floor(Math.random() * 90) + 10; // Divisor
                result = Math.floor(Math.random() * 90) + 10; // Desired clean quotient
                num1 = num2 * result; // Dividend
                statement = `${num1} ÷ ${num2}`;
            }

            // Repetition tracking verification pipeline
            if (!questionHistoryArray.includes(statement)) {
                questionHistoryArray.push(statement);
                if (questionHistoryArray.length > 1000) questionHistoryArray.shift(); // Evicts overflow logs
                break;
            }
        }
        return { prompt: statement, value: result };
    }

    function initNewMatchTurn() {
        const packet = generateUniqueQuestion();
        correctAnswer = packet.value;
        document.getElementById("question-text").innerText = packet.prompt;

        // Formulate 3 valid distinct deceptive options
        let optionsSet = new Set();
        optionsSet.add(correctAnswer);

        while(optionsSet.size < 4) {
            let offset = Math.floor(Math.random() * 24) - 12;
            if (offset === 0) offset = 5;
            let fakeOption = correctAnswer + offset;
            if(fakeOption >= 0) optionsSet.add(fakeOption);
        }

        // Shuffle tracking mapping array array
        let optionsArray = Array.from(optionsSet).sort(() => Math.random() - 0.5);
        const domNodes = document.getElementsByClassName("option-node");
        
        for(let i=0; i < 4; i++) {
            domNodes[i].innerText = optionsArray[i];
            domNodes[i].style.borderColor = "rgba(255, 255, 255, 0.08)";
        }
    }

    function verifyChoice(selectedNode) {
        const numericalValue = parseInt(selectedNode.innerText);
        
        if (numericalValue === correctAnswer) {
            // SUCCESS PROTOCOL TRIGGER
            score += 10;
            document.getElementById("score-val").innerText = score;
            selectedNode.style.borderColor = "#22c55e"; // Success green illumination
            
            playSuccessChime();
            currentFXState = "snow";
            
            setTimeout(() => {
                currentFXState = "ambient";
                initNewMatchTurn();
            }, 1200);
        } 
        else {
            // FAILURE BURST PROTOCOL TRIGGER
            selectedNode.style.borderColor = "#ef4444"; // Failure red illumination
            
            playExplodeBoom();
            currentFXState = "fire";
            
            setTimeout(() => {
                currentFXState = "ambient";
                initNewMatchTurn();
            }, 1200);
        }
    }

    // Launch Game System Init Sequence
    initNewMatchTurn();
</script>

</body>
</html>
"""

# Mount complete game engine instance to layout container
components.html(game_engine_html, height=660)
