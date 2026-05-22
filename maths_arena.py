import streamlit as st
import streamlit.components.v1 as components
import base64

# Layout configurations
st.set_page_config(
    page_title="Dilshad's Trend Arena",
    page_icon="⚡",
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
        # Fallback empty string if files are temporarily unlocked during initial boot
        return ""

# Convert your newly uploaded repo files into secure memory strings
right_answer_audio = load_local_audio_base64("faa.mp3")
wrong_answer_audio = load_local_audio_base64("haha.mp3")

# Dark space layout overrides
st.markdown("""
<style>
div[data-testid="stAppViewContainer"], .main {
    background: #020617 !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #f8fafc; font-family: sans-serif; font-weight: 900; letter-spacing: -1px; margin-bottom:0px;'>⚔️ Math Arena 2D</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #38bdf8; font-family: monospace; font-size: 13px; margin-top:4px; margin-bottom: 20px;'>// AUDIO SYSTEM: REPO MP3 PIPELINE LOADED SUCCESSFUL</p>", unsafe_allow_html=True)

# ==============================================================================
# 🎮 THE THREE.JS FX ENGINE + REPO MEDIA TARGETS
# ==============================================================================
game_engine_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<style>
    body, html {{
        margin: 0; padding: 0;
        width: 100%; height: 100%;
        overflow: hidden;
        display: flex; justify-content: center; align-items: center;
        background: transparent;
        font-family: system-ui, -apple-system, sans-serif;
    }}

    /* 🌌 ARENA CONTAINER */
    .arena-viewport {{
        position: relative;
        width: 480px;
        height: 640px;
        display: flex; justify-content: center; align-items: center;
    }}

    /* 🎨 THREE.JS CORE WEBGL BACKING */
    #three-canvas {{
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 1;
        border-radius: 40px;
    }}

    /* 💎 GLASSMORPHIC INTERACTIVE CONSOLE FRAME */
    .game-console {{
        position: relative;
        z-index: 2;
        width: 88%;
        height: 92%;
        background: rgba(15, 23, 42, 0.3);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 36px;
        padding: 30px;
        box-sizing: border-box;
        border: 1px solid rgba(255, 255, 255, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 30px 70px rgba(0,0,0,0.7);
    }}

    /* HUD PANELS */
    .hud-header {{
        display: flex; justify-content: space-between;
        color: #64748b; font-family: monospace; font-size: 13px;
        letter-spacing: 1px;
    }}
    
    .score-glow {{ color: #38bdf8; font-weight: bold; text-shadow: 0 0 10px rgba(56, 189, 248, 0.4); }}

    /* CORE QUESTION AREA */
    .question-deck {{
        width: 100%;
        background: rgba(0, 0, 0, 0.6);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        padding: 22px 10px;
        text-align: center;
        box-sizing: border-box;
        box-shadow: inset 0 4px 20px rgba(0,0,0,0.8);
    }}
    
    #question-text {{
        font-size: 42px; color: #f8fafc; font-weight: 800; font-family: monospace;
    }}

    /* 🔄 2D PLANETARY ORBIT SYSTEM */
    .orbit-container {{
        position: relative;
        width: 100%;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .orbit-rotor-2d {{
        position: absolute;
        width: 240px;
        height: 240px;
        border-radius: 50%;
        border: 1px dashed rgba(255, 255, 255, 0.05);
        display: flex;
        justify-content: center;
        align-items: center;
        animation: spin2D 14s linear infinite;
    }}

    @keyframes spin2D {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}

    .orbit-container:hover .orbit-rotor-2d {{
        animation-play-state: paused;
    }}

    /* 🔮 PRECISE 2D OPTION BUBBLES */
    .option-node-2d {{
        position: absolute;
        width: 72px;
        height: 72px;
        background: linear-gradient(135deg, rgba(255,255,255,0.07), rgba(255,255,255,0.01));
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 50%;
        color: #f1f5f9;
        font-size: 22px; font-weight: bold; font-family: monospace;
        display: flex; justify-content: center; align-items: center;
        cursor: pointer;
        user-select: none;
        box-shadow: 0 8px 16px rgba(0,0,0,0.4),
                    inset 0 3px 6px rgba(255,255,255,0.05),
                    inset 0 -5px 8px rgba(0,0,0,0.4);
        transition: transform 0.15s, background 0.15s, border 0.15s, box-shadow 0.15s;
    }}

    /* 🧭 PLANETARY GEOMETRIC POSITION LOGIC */
    .opt-0 {{ top: -36px; left: 84px; }}   
    .opt-1 {{ top: 84px; right: -36px; }}  
    .opt-2 {{ bottom: -36px; left: 84px; }}
    .opt-3 {{ top: 84px; left: -36px; }}   

    /* 🛡️ COUNTER-AXIS STABILIZER */
    .orbit-rotor-2d .option-node-2d {{ animation: keepUpright 14s linear infinite; }}
    .orbit-container:hover .option-node-2d {{ animation-play-state: paused !important; }}

    @keyframes keepUpright {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(-360deg); }} 
    }}

    .option-node-2d:hover {{
        background: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        border-color: #38bdf8;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
        transform: scale(1.1) !important;
    }}
    
    .option-node-2d:active {{ transform: scale(0.9) !important; }}
</style>
</head>
<body>

<div class="arena-viewport">
    <canvas id="three-canvas"></canvas>

    <div class="game-console">
        <div class="hud-header">
            <div>ARENA: REPO AUDIO DATA ACTIVATED</div>
            <div>SCORE: <span id="score-val" class="score-glow">0</span></div>
        </div>
        
        <div class="question-deck">
            <div id="question-text">LOADING ENGINE...</div>
        </div>

        <div class="orbit-container">
            <div class="orbit-rotor-2d" id="wheel-axis">
                <div class="option-node-2d opt-0" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-1" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-2" onclick="verifyChoice(this)">0</div>
                <div class="option-node-2d opt-3" onclick="verifyChoice(this)">0</div>
            </div>
        </div>
        
        <div style="text-align: center; font-size: 11px; color: #475569; font-family: monospace; letter-spacing: 0.5px;">
            HINT: HOVER OVER INTERFACE TO LOCK VECTOR ROTATION
        </div>
    </div>
</div>

<script>
    // ==========================================================================
    // 🎵 INJECTED AUDIO RESOURCE MEMORY STREAMS
    // ==========================================================================
    const RIGHT_AUDIO_STREAM = "{right_answer_audio}"; 
    const WRONG_AUDIO_STREAM = "{wrong_answer_audio}";

    function playFaaCorrect() {{
        if (!RIGHT_AUDIO_STREAM) return;
        const audioInstance = new Audio(RIGHT_AUDIO_STREAM);
        audioInstance.volume = 0.85;
        audioInstance.play().catch(err => console.log("Audio lock:", err));
    }}

    function playHahaIncorrect() {{
        if (!WRONG_AUDIO_STREAM) return;
        const audioInstance = new Audio(WRONG_AUDIO_STREAM);
        audioInstance.volume = 0.85;
        audioInstance.play().catch(err => console.log("Audio lock:", err));
    }}

    // ==========================================================================
    // 🧬 THREE.JS GRID PARTICLES SYSTEM
    // ==========================================================================
    const canvasElement = document.getElementById('three-canvas');
    const scene = new THREE.Scene();
    
    const camera = new THREE.PerspectiveCamera(65, 480 / 640, 0.1, 1000);
    camera.position.z = 20;

    const renderer = new THREE.WebGLRenderer({ canvas: canvasElement, antialias: true, alpha: true });
    renderer.setSize(480, 640);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const totalParticles = 350;
    const geometry = new THREE.BufferGeometry();
    const positionArray = new Float32Array(totalParticles * 3);
    
    for(let i=0; i < totalParticles*3; i+=3) {{
        positionArray[i] = (Math.random() - 0.5) * 40;     
        positionArray[i+1] = (Math.random() - 0.5) * 40;   
        positionArray[i+2] = (Math.random() - 0.5) * 30;   
    }}
    geometry.setAttribute('position', new THREE.BufferAttribute(positionArray, 3));

    const pointMaterial = new THREE.PointsMaterial({{ size: 0.35, transparent: true, opacity: 0.5 }});
    pointMaterial.color.setHex(0x38bdf8); 
    
    const engineParticles = new THREE.Points(geometry, pointMaterial);
    scene.add(engineParticles);

    let activeFXState = "ambient"; 

    function tickGraphicsEngine() {{
        requestAnimationFrame(tickGraphicsEngine);
        const positions = geometry.attributes.position.array;
        
        if (activeFXState === "ambient") {{
            engineParticles.rotation.y += 0.003;
            pointMaterial.color.setHex(0x1e1b4b); 
        }} 
        else if (activeFXState === "snow") {{
            pointMaterial.color.setHex(0x38bdf8); 
            for(let i=1; i < positions.length; i+=3) {{
                positions[i] -= 0.3; 
                if(positions[i] < -20) positions[i] = 20;
            }}
            geometry.attributes.position.needsUpdate = true;
        }} 
        else if (activeFXState === "fire") {{
            pointMaterial.color.setHex(0xef4444); 
            for(let i=1; i < positions.length; i+=3) {{
                positions[i] += 0.45; 
                if(positions[i] > 20) {{
                    positions[i] = -20;
                    positions[i-1] = (Math.random() - 0.5) * 30;
                }
            }}
            geometry.attributes.position.needsUpdate = true;
        }}

        renderer.render(scene, camera);
    }
    tickGraphicsEngine();

    // ==========================================================================
    // 🧠 1000+ NON-REPETITIVE MATCH OPERATIONS CONTROLLER
    // ==========================================================================
    let score = 0;
    let targetAnswer = 0;
    let historyRegister = [];

    function generateUniqueProblem() {{
        let op, n1, n2, equation, value;
        const pool = ['+', '-', '*', '/'];
        
        while (true) {{
            op = pool[Math.floor(Math.random() * pool.length)];
            
            if (op === '+') {{
                n1 = Math.floor(Math.random() * 89) + 10;
                n2 = Math.floor(Math.random() * 89) + 10;
                equation = n1 + " + " + n2; value = n1 + n2;
            }} 
            else if (op === '-') {{
                n1 = Math.floor(Math.random() * 89) + 10;
                n2 = Math.floor(Math.random() * (n1 - 10 + 1)) + 10; 
                equation = n1 + " - " + n2; value = n1 - n2;
            }} 
            else if (op === '*') {{
                n1 = Math.floor(Math.random() * 89) + 10;
                n2 = Math.floor(Math.random() * 9) + 2; 
                equation = n1 + " × " + n2; value = n1 * n2;
            }} 
            else if (op === '/') {{
                n2 = Math.floor(Math.random() * 11) + 2; 
                value = Math.floor(Math.random() * 40) + 5; 
                n1 = n2 * value; 
                equation = n1 + " ÷ " + n2;
            }}

            if (!historyRegister.includes(equation)) {{
                historyRegister.push(equation);
                if (historyRegister.length > 1000) historyRegister.shift(); 
                break;
            }}
        }}
        return {{ text: equation, answer: value }};
    }

    function renderMatchStage() {{
        const log = generateUniqueProblem();
        targetAnswer = log.answer;
        document.getElementById("question-text").innerText = log.text;

        let optionsSet = new Set();
        optionsSet.add(targetAnswer);

        while(optionsSet.size < 4) {{
            let variance = Math.floor(Math.random() * 20) - 10;
            if (variance === 0) variance = 4;
            let alternate = targetAnswer + variance;
            if(alternate >= 0) optionsSet.add(alternate);
        }}

        let shuffled = Array.from(optionsSet).sort(() => Math.random() - 0.5);
        const slots = document.getElementsByClassName("option-node-2d");
        
        for(let i=0; i < 4; i++) {{
            slots[i].innerText = shuffled[i];
            slots[i].style.borderColor = "rgba(255, 255, 255, 0.08)";
            slots[i].style.background = "linear-gradient(135deg, rgba(255,255,255,0.07), rgba(255,255,255,0.01))";
        }}
    }

    function verifyChoice(node) {{
        const input = parseInt(node.innerText);
        
        if (input === targetAnswer) {{
            score += 10;
            document.getElementById("score-val").innerText = score;
            node.style.borderColor = "#22c55e";
            node.style.background = "rgba(34, 197, 94, 0.2)";
            
            // Trigger updated trend rules
            playFaaCorrect();
            activeFXState = "snow";
            
            setTimeout(() => {{
                activeFXState = "ambient";
                renderMatchStage();
            }}, 1300);
        }} 
        else {{
            node.style.borderColor = "#ef4444";
            node.style.background = "rgba(239, 68, 68, 0.2)";
            
            // Trigger updated trend rules
            playHahaIncorrect();
            activeFXState = "fire";
            
            setTimeout(() => {{
                activeFXState = "ambient";
                renderMatchStage();
            }}, 1300);
        }}
    }

    renderMatchStage();
</script>

</body>
</html>
"""

# Render application matrix into main Streamlit container framework
components.html(game_engine_html, height=660)
