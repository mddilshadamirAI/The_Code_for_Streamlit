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

# Convert your newly uploaded repo files into secure memory strings
right_answer_audio = load_local_audio_base64("faa.mp3")
wrong_answer_audio = load_local_audio_base64("haha.mp3")
bg_music_audio = load_local_audio_base64("newmusic.mp3")

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
st.markdown("<p style='text-align: center; color: #a855f7; font-family: monospace; font-size: 11px; margin-top:4px; margin-bottom: 20px; letter-spacing: 2px;'>// VISUAL CORE V2.0 ENGINE ENGAGED</p>", unsafe_allow_html=True)

# ==============================================================================
# 🎮 THE THREE.JS FX ENGINE + REPO MEDIA TARGETS (EXTREME UI EDITION)
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
        width: 480px;
        height: 640px;
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

    .game-console {
        position: relative;
        z-index: 2;
        width: 90%;
        height: 94%;
        background: rgba(4, 10, 26, 0.65);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 36px;
        padding: 30px;
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

    .hud-header {
        display: flex; justify-content: space-between;
        color: #94a3b8; font-size: 11px;
        letter-spacing: 1px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        padding-bottom: 10px;
    }
    
    .score-glow { 
        color: #06b6d4; 
        font-weight: 900; 
        font-size: 18px;
        text-shadow: 0 0 12px #06b6d4, 0 0 25px rgba(6, 182, 212, 0.5);
        transition: all 0.2s ease;
    }

    .question-deck {
        width: 100%;
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.9) 0%, rgba(2, 6, 23, 0.95) 100%);
        border-radius: 24px;
        border: 1px solid rgba(6, 182, 212, 0.25);
        padding: 25px 10px;
        text-align: center;
        box-sizing: border-box;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 2px 10px rgba(6, 182, 212, 0.1);
    }
    
    #question-text {
        font-size: 46px; 
        color: #ffffff; 
        font-weight: 900; 
        letter-spacing: -1px;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    }

    .orbit-container {
        position: relative;
        width: 100%;
        height: 310px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .orbit-rotor-2d {
        position: absolute;
        width: 230px;
        height: 230px;
        border-radius: 50%;
        border: 2px dashed rgba(6, 182, 212, 0.15);
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.03);
        display: flex;
        justify-content: center;
        align-items: center;
        animation: spin2D 16s linear infinite;
    }

    @keyframes spin2D {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .orbit-container:hover .orbit-rotor-2d {
        border-color: rgba(168, 85, 247, 0.4);
    }

    .option-node-2d {
        position: absolute;
        width: 76px;
        height: 76px;
        background: radial-gradient(circle at 30% 30%, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.98) 100%);
        border: 1px solid rgba(6, 182, 212, 0.4);
        border-radius: 50%;
        color: #38bdf8;
        font-size: 24px; font-weight: 900;
        display: flex; justify-content: center; align-items: center;
        cursor: pointer;
        user-select: none;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5), inset 0 2px 5px rgba(255,255,255,0.1);
        transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .opt-0 { top: -38px; left: 77px; }   
    .opt-1 { top: 77px; right: -38px; }  
    .opt-2 { bottom: -38px; left: 77px; }
    .opt-3 { top: 77px; left: -38px; }   

    .orbit-rotor-2d .option-node-2d { animation: keepUpright 16s linear infinite; }

    .option-node-2d:hover {
        color: #ffffff;
        background: radial-gradient(circle at center, #06b6d4 0%, #0891b2 100%);
        border-color: #22d3ee;
        box-shadow: 0 0 30px #06b6d4, 0 0 50px rgba(6, 182, 212, 0.4);
        transform: scale(1.18) !important;
    }
    
    .option-node-2d:active { transform: scale(0.88) !important; }
</style>
</head>
<body>

<div class="arena-viewport" id="viewport-frame">
    <canvas id="three-canvas"></canvas>

    <div class="game-console" id="console-box">
        <div class="hud-header">
            <div>BY: MD DILSHAD // SYS.ACTIVE</div>
            <div>SCORE: <span id="score-val" class="score-glow">0</span></div>
        </div>
        
        <div class="question-deck">
            <div id="question-text">LOADING CORE...</div>
        </div>

        <div class="orbit-container">
            <div class="orbit-rotor-2d" id="wheel-axis">
                <div class="option-node-2d opt-0" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-1" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-2" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-3" onclick="verifyChoice(this)">0</div>
            </div>
        </div>
        
        <div style="text-align: center; font-size: 10px; color: #475569; letter-spacing: 1px;">
            🔥 KINETIC ORBIT ACTIVE // VELOCITY LOCK REMOVED
        </div>
    </div>
</div>

<script>
    const RIGHT_AUDIO_STREAM = "%%RIGHT_AUDIO_REPLACE%%"; 
    const WRONG_AUDIO_STREAM = "%%WRONG_AUDIO_REPLACE%%";
    const BG_AUDIO_STREAM = "%%BG_AUDIO_REPLACE%%";

    // BACKGROUND MUSIC ENGINE
    let bgAudio = new Audio(BG_AUDIO_STREAM);
    bgAudio.loop = true;
    bgAudio.volume = 0.25;
    
    function startMusic() {
        bgAudio.play().catch(err => console.log("Audio lock:", err));
        document.removeEventListener('click', startMusic);
    }
    document.addEventListener('click', startMusic);

    function playFaaCorrect() {
        if (!RIGHT_AUDIO_STREAM || RIGHT_AUDIO_STREAM.length < 50) return;
        const audioInstance = new Audio(RIGHT_AUDIO_STREAM);
        audioInstance.volume = 0.85;
        audioInstance.play().catch(err => console.log("Audio lock:", err));
    }

    function playHahaIncorrect() {
        if (!WRONG_AUDIO_STREAM || WRONG_AUDIO_STREAM.length < 50) return;
        const audioInstance = new Audio(WRONG_AUDIO_STREAM);
        audioInstance.volume = 0.85;
        audioInstance.play().catch(err => console.log("Audio lock:", err));
    }

    const canvasElement = document.getElementById('three-canvas');
    const scene = new THREE.Scene();
    
    const camera = new THREE.PerspectiveCamera(65, 480 / 640, 0.1, 1000);
    camera.position.z = 18;

    const renderer = new THREE.WebGLRenderer({ canvas: canvasElement, antialias: true, alpha: true });
    renderer.setSize(480, 640);
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
            engineParticles.rotation.x += 0.001;
            pointMaterial.color.setHex(0xa855f7); 
        } 
        else if (activeFXState === "snow") {
            pointMaterial.color.setHex(0x10b981); 
            for(let i=1; i < positions.length; i+=3) {
                positions[i] -= 0.5; 
                if(positions[i] < -22) positions[i] = 22;
            }
            geometry.attributes.position.needsUpdate = true;
        } 
        else if (activeFXState === "fire") {
            pointMaterial.color.setHex(0xef4444); 
            for(let i=1; i < positions.length; i+=3) {
                positions[i] += 0.65; 
                if(positions[i] > 22) {
                    positions[i] = -22;
                    positions[i-1] = (Math.random() - 0.5) * 35;
                }
            }
            geometry.attributes.position.needsUpdate = true;
        }

        renderer.render(scene, camera);
    }
    tickGraphicsEngine();

    let score = 0;
    let targetAnswer = 0;
    let historyRegister = [];

    function generateUniqueProblem() {
        let op, n1, n2, equation, value;
        const pool = ['+', '-', '*', '/'];
        
        while (true) {
            op = pool[Math.floor(Math.random() * pool.length)];
            
            if (op === '+') {
                n1 = Math.floor(Math.random() * 89) + 10;
                n2 = Math.floor(Math.random() * 89) + 10;
                equation = n1 + " + " + n2; value = n1 + n2;
            } 
            else if (op === '-') {
                n1 = Math.floor(Math.random() * 89) + 10;
                n2 = Math.floor(Math.random() * (n1 - 10 + 1)) + 10; 
                equation = n1 + " - " + n2; value = n1 - n2;
            } 
            else if (op === '*') {
                n1 = Math.floor(Math.random() * 89) + 10;
                n2 = Math.floor(Math.random() * 9) + 2; 
                equation = n1 + " × " + n2; value = n1 * n2;
            } 
            else if (op === '/') {
                n2 = Math.floor(Math.random() * 11) + 2; 
                value = Math.floor(Math.random() * 40) + 5; 
                n1 = n2 * value; 
                equation = n1 + " ÷ " + n2;
            }

            if (!historyRegister.includes(equation)) {
                historyRegister.push(equation);
                if (historyRegister.length > 1000) historyRegister.shift(); 
                break;
            }
        }
        return { text: equation, answer: value };
    }

    function renderMatchStage() {
        const log = generateUniqueProblem();
        targetAnswer = log.answer;
        document.getElementById("question-text").innerText = log.text;

        let optionsSet = new Set();
        optionsSet.add(targetAnswer);

        while(optionsSet.size < 4) {
            let variance = Math.floor(Math.random() * 20) - 10;
            if (variance === 0) variance = 4;
            let alternate = targetAnswer + variance;
            if(alternate >= 0) optionsSet.add(alternate);
        }

        let shuffled = Array.from(optionsSet).sort(() => Math.random() - 0.5);
        const slots = document.getElementsByClassName("option-node-2d");
        
        for(let i=0; i < 4; i++) {
            slots[i].innerText = shuffled[i];
            slots[i].style.borderColor = "rgba(6, 182, 212, 0.4)";
            slots[i].style.background = "radial-gradient(circle at 30% 30%, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.98) 100%)";
            slots[i].style.color = "#38bdf8";
            slots[i].style.boxShadow = "0 10px 25px rgba(0,0,0,0.5)";
        }
    }

    function verifyChoice(node) {
        const input = parseInt(node.innerText);
        const consoleBox = document.getElementById("console-box");
        
        if (input === targetAnswer) {
            score += 10;
            document.getElementById("score-val").innerText = score;
            
            node.style.borderColor = "#10b981";
            node.style.background = "radial-gradient(circle at center, #10b981 0%, #059669 100%)";
            node.style.color = "#ffffff";
            node.style.boxShadow = "0 0 35px #10b981";
            
            consoleBox.classList.add("console-correct");
            
            playFaaCorrect();
            activeFXState = "snow";
            
            setTimeout(() => {
                consoleBox.classList.remove("console-correct");
                activeFXState = "ambient";
                renderMatchStage();
            }, 1200);
        } 
        else {
            node.style.borderColor = "#ef4444";
            node.style.background = "radial-gradient(circle at center, #ef4444 0%, #dc2626 100%)";
            node.style.color = "#ffffff";
            node.style.boxShadow = "0 0 35px #ef4444";
            
            consoleBox.classList.add("console-incorrect");
            
            playHahaIncorrect();
            activeFXState = "fire";
            
            setTimeout(() => {
                consoleBox.classList.remove("console-incorrect");
                activeFXState = "ambient";
                renderMatchStage();
            }, 1200);
        }
    }

    renderMatchStage();
</script>

</body>
</html>
"""

# Inject audio streams cleanly
sanitized_game_html = raw_template_html.replace(
    "%%RIGHT_AUDIO_REPLACE%%", right_answer_audio
).replace(
    "%%WRONG_AUDIO_REPLACE%%", wrong_answer_audio
).replace(
    "%%BG_AUDIO_REPLACE%%", bg_music_audio
)

# Render application matrix into main Streamlit container framework
components.html(sanitized_game_html, height=660)
