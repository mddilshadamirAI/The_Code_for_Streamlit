import streamlit as st
import streamlit.components.v1 as components

# Application workspace vector configuration
st.set_page_config(
    page_title="Dilshad's Detonation Matrix",
    page_icon="🔥",
    layout="centered"
)

# Dark matrix background injection
st.markdown("""
<style>
div[data-testid="stAppViewContainer"], .main {
    background: #02040a !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #f8fafc; font-family: sans-serif; font-weight: 900; letter-spacing: -1px; margin-bottom:0px;'>Smart Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ef4444; font-family: monospace; font-size: 13px; margin-top:4px; margin-bottom: 25px;'>// CORE MODULE: IGNITION STATE ACTIVATED</p>", unsafe_allow_html=True)

# ==============================================================================
# 🎮 THE THREE.JS FX ENGINE + SYNTH AUDIO MATRIX
# ==============================================================================
hologram_engine_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<style>
    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        background: transparent;
        font-family: system-ui, sans-serif;
    }

    /* 🌌 THE SPATIAL UNIVERSE ENGINE CONTAINER */
    .viewport-3d {
        position: relative;
        width: 450px;
        height: 620px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* 🎨 INTERACTIVE WebGL RUNTIME LAYER */
    #canvas-3d {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1; /* Sits underneath to wrap around edges */
    }

    /* 💎 THE CENTRAL SUSPENDED GLASS FRAME */
    .glass-console {
        position: relative;
        z-index: 2; /* Floats inside the core of the 3D net */
        width: 330px;
        height: 510px;
        background: rgba(10, 15, 30, 0.3);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 36px;
        padding: 24px;
        box-sizing: border-box;
        border: 1px solid rgba(255, 255, 255, 0.05);
        display: flex;
        flex-direction: column;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        transition: all 0.2s ease;
    }

    /* 🖥️ CYBER INS-LCD SCREEN */
    .lcd-screen {
        width: 100%;
        height: 85px;
        background: rgba(0, 0, 0, 0.7);
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.04);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-end;
        padding: 0 20px;
        box-sizing: border-box;
        margin-bottom: 25px;
        box-shadow: inset 0 4px 15px rgba(0,0,0,0.9);
        transition: all 0.1s ease;
    }

    #expr { font-size: 13px; color: #475569; font-family: monospace; min-height: 16px; margin-bottom: 2px; }
    #val { font-size: 34px; color: #ffffff; font-family: monospace; font-weight: bold; }

    /* BUTTON CONTROL SYSTEMS */
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        flex-grow: 1;
    }

    .key-node {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 50%;
        color: #94a3b8;
        font-size: 19px;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all 0.1s cubic-bezier(0.4, 0, 0.2, 1);
        user-select: none;
        box-shadow: 0 5px 10px rgba(0,0,0,0.4), inset 0 -3px 6px rgba(0,0,0,0.3);
    }

    .key-node:hover {
        background: rgba(255, 255, 255, 0.08);
        color: #ffffff;
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    .op-node { color: #f43f5e; background: rgba(244, 63, 94, 0.02); }

    /* IGNITION TRIGGER BUTTON (=) */
    .ignite-node {
        background: linear-gradient(135deg, #ef4444, #b91c1c);
        color: #ffffff;
        font-weight: bold;
        border: none;
        box-shadow: 0 6px 15px rgba(239, 68, 68, 0.3);
    }
    .ignite-node:hover {
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.6);
    }

    /* MECHANICAL KEYPRESS DEPRESSION EFFECT */
    .key-node:active {
        transform: scale(0.88) translateY(3px);
    }

    /* 🔥 SYSTEM FIRE IGNITION OVERLAY STYLES */
    .fire-blast {
        border-color: rgba(239, 68, 68, 0.6) !important;
        box-shadow: 0 0 60px rgba(239, 68, 68, 0.5), inset 0 0 20px rgba(239, 68, 68, 0.3) !important;
        transform: scale(1.03) rotateX(10deg);
    }
    
    .screen-flash {
        background: rgba(239, 68, 68, 0.15) !important;
        border-color: #ef4444 !important;
        box-shadow: inset 0 0 25px rgba(239, 68, 68, 0.5) !important;
    }
</style>
</head>
<body>

<div class="viewport-3d">
    <canvas id="canvas-3d"></canvas>

    <div class="glass-console" id="console-frame">
        <div class="lcd-screen" id="screen-frame">
            <div id="expr"></div>
            <div id="val">0</div>
        </div>
        
        <div class="grid">
            <div class="key-node op-node" onclick="appendToken('C')">C</div>
            <div class="key-node op-node" onclick="appendToken('(')">(</div>
            <div class="key-node op-node" onclick="appendToken(')')">)</div>
            <div class="key-node op-node" onclick="appendToken('/')">÷</div>
            
            <div class="key-node" onclick="appendToken('7')">7</div>
            <div class="key-node" onclick="appendToken('8')">8</div>
            <div class="key-node" onclick="appendToken('9')">9</div>
            <div class="key-node op-node" onclick="appendToken('*')">×</div>
            
            <div class="key-node" onclick="appendToken('4')">4</div>
            <div class="key-node" onclick="appendToken('5')">5</div>
            <div class="key-node" onclick="appendToken('6')">6</div>
            <div class="key-node op-node" onclick="appendToken('-')">−</div>
            
            <div class="key-node" onclick="appendToken('1')">1</div>
            <div class="key-node" onclick="appendToken('2')">2</div>
            <div class="key-node" onclick="appendToken('3')">3</div>
            <div class="key-node op-node" onclick="appendToken('+')">+</div>
            
            <div class="key-node" onclick="appendToken('0')">0</div>
            <div class="key-node" onclick="appendToken('.')">.</div>
            <div class="key-node op-node" onclick="backspace()">◀</div>
            <div class="key-node ignite-node" onclick="triggerIgnition()">=</div>
        </div>
    </div>
</div>

<script>
    // ==========================================================================
    // 🔮 THREE.JS ENVELOPE ENGINE SYSTEM
    // ==========================================================================
    const canvasElement = document.getElementById('canvas-3d');
    const scene = new THREE.Scene();

    // Perspective focal calculation mapping
    const camera = new THREE.PerspectiveCamera(60, 450 / 620, 0.1, 1000);
    camera.position.z = 18; 

    const renderer = new THREE.WebGLRenderer({ canvas: canvasElement, antialias: true, alpha: true });
    renderer.setSize(450, 620);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Creating a massive matrix net structure that expands PAST the console dimensions
    const geometry = new THREE.IcosahedronGeometry(11, 2); 
    
    const material = new THREE.MeshBasicMaterial({
        color: 0x334155, // Base industrial dark grey lines
        wireframe: true,
        transparent: true,
        opacity: 0.3
    });

    const netMesh = new THREE.Mesh(geometry, material);
    scene.add(netMesh);

    // Engine Speed Track Variables
    let rotationalVelocityX = 0.002;
    let rotationalVelocityY = 0.004;
    let targetScale = 1;

    // 🔄 CONTINUOUS ENGINE LOGIC TICK RUN (60 FPS)
    function runEngineTick() {
        requestAnimationFrame(runEngineTick);

        // Run rotation delta calculations
        netMesh.rotation.x += rotationalVelocityX;
        netMesh.rotation.y += rotationalVelocityY;

        // Smoothly interpolate scale matrix transformations
        netMesh.scale.x += (targetScale - netMesh.scale.x) * 0.1;
        netMesh.scale.y += (targetScale - netMesh.scale.y) * 0.1;
        netMesh.scale.z += (targetScale - netMesh.scale.z) * 0.1;

        // Cool-down velocity dampening logic after calculation bursts
        if (rotationalVelocityY > 0.004) rotationalVelocityY -= 0.01;
        if (rotationalVelocityX > 0.002) rotationalVelocityX -= 0.005;

        renderer.render(scene, camera);
    }
    runEngineTick();

    // ==========================================================================
    // 🔊 SYNTHETIC AUDIO DETONATION CORE (WEB AUDIO API ENGINE)
    // ==========================================================================
    function playAudioBoom() {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        // Setup raw synthesizers nodes
        const mainOscillator = audioCtx.createOscillator();
        const noiseOscillator = audioCtx.createOscillator();
        const volumeGainNode = audioCtx.createGain();
        
        mainOscillator.connect(volumeGainNode);
        noiseOscillator.connect(volumeGainNode);
        volumeGainNode.connect(audioCtx.destination);

        // Configure a heavy, explosive low-frequency Sawtooth profile
        mainOscillator.type = 'sawtooth';
        mainOscillator.frequency.setValueAtTime(160, audioCtx.currentTime);
        mainOscillator.frequency.exponentialRampToValueAtTime(10, audioCtx.currentTime + 0.6);

        // Mix in structural crackle using a high frequency square sound vector
        noiseOscillator.type = 'square';
        noiseOscillator.frequency.setValueAtTime(40, audioCtx.currentTime);
        noiseOscillator.frequency.linearRampToValueAtTime(1, audioCtx.currentTime + 0.4);

        // Set detonation volume amplitude envelop decay curve
        volumeGainNode.gain.setValueAtTime(0.6, audioCtx.currentTime);
        volumeGainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.7);

        // Trigger Audio Context Engine execution lifecycle
        mainOscillator.start();
        noiseOscillator.start();
        mainOscillator.stop(audioCtx.currentTime + 0.7);
        noiseOscillator.stop(audioCtx.currentTime + 0.7);
    }

    // ==========================================================================
    // 🧮 SYSTEM OPERATION INTERFACE COMPREHENSION
    // ==========================================================================
    let equationSequence = "";
    const viewExpr = document.getElementById("expr");
    const viewVal = document.getElementById("val");
    const consoleUI = document.getElementById("console-frame");
    const screenUI = document.getElementById("screen-frame");

    function appendToken(token) {
        if (token === 'C') {
            equationSequence = "";
            viewExpr.innerText = "";
            viewVal.innerText = "0";
            return;
        }
        equationSequence += token;
        viewVal.innerText = equationSequence;
        
        // Structural feedback: Reactive micro-flex whenever keys register inputs
        netMesh.scale.set(1.02, 1.02, 1.02);
        setTimeout(() => targetScale = 1, 50);
    }

    function backspace() {
        equationSequence = equationSequence.slice(0, -1);
        viewVal.innerText = equationSequence || "0";
    }

    // 🔥 THE BOOM STATE CALCULATOR IGNITION INTERFACE
    function triggerIgnition() {
        if (!equationSequence) return;
        try {
            viewExpr.innerText = equationSequence + " =";
            let calculationOutput = eval(equationSequence);
            if (calculationOutput.toString().includes('.')) {
                calculationOutput = parseFloat(calculationOutput.toFixed(6));
            }
            viewVal.innerText = calculationOutput;
            equationSequence = calculationOutput.toString();

            // 1. Fire Web Audio Synth explosion
            playAudioBoom();

            // 2. Warp 3D Matrix mesh parameters to Fiery Blast Configuration
            netMesh.material.color.setHex(0xff3300); // Shift line colors to Magma Orange
            netMesh.material.opacity = 0.8;          // Force full wireframe brightness
            rotationalVelocityY = 0.35;               // Accelerate orbital rotation to warp speed
            rotationalVelocityX = 0.15;
            targetScale = 1.4;                       // Blow out the 3D grid cage past the device borders

            // 3. Inject CSS Fire Glow classes to device chassis elements
            consoleUI.classList.add("fire-blast");
            screenUI.classList.add("screen-flash");

            // 🔄 THE ENGINE RECOVERY MATRIX (Cooling the system back to normal state)
            setTimeout(() => {
                netMesh.material.color.setHex(0x334155); // Reset to Slate Steel Grey
                netMesh.material.opacity = 0.3;
                targetScale = 1.0;
                consoleUI.classList.remove("fire-blast");
                screenUI.classList.remove("screen-flash");
            }, 750);

        } catch (err) {
            viewVal.innerText = "Error";
            equationSequence = "";
        }
    }
</script>

</body>
</html>
"""

# Embed spatial application layers inside Streamlit layout tree
components.html(hologram_engine_html, height=650)
