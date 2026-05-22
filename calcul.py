import streamlit as st
import streamlit.components.v1 as components

# Interface Environment Configuration
st.set_page_config(
    page_title="Dilshad's WebGL Core",
    page_icon="🔮",
    layout="centered"
)

# Deep space styling for the native Streamlit container frame
st.markdown("""
<style>
div[data-testid="stAppViewContainer"], .main {
    background: #030712 !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #f8fafc; font-family: sans-serif; font-weight: 900; letter-spacing: -0.5px; margin-bottom:0px;'>Smart Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #06b6d4; font-family: monospace; font-size: 13px; margin-top:4px; margin-bottom: 30px;'>// RUNNING THREE.JS WEBGL ENGINE v128</p>", unsafe_allow_html=True)

# ==============================================================================
# 🎮 THE THREE.JS 3D ENGINE & CALCULATOR RUNTIME
# ==============================================================================
three_engine_html = """
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

    /* 🔌 CONTAINER HOUSING BOTH THE 3D CANVAS AND INTERFACE */
    .app-container {
        position: relative;
        width: 360px;
        height: 560px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* 🎨 THREE.JS GAME ENGINE CANVAS LAYER */
    #webgl-canvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1; /* Sits completely in the background */
        border-radius: 40px;
    }

    /* 💎 FLOATING GLASS INTERFACE CONSOLE LAYER */
    .calc-ui {
        position: relative;
        z-index: 2; /* Floats safely on top of the 3D graphics canvas */
        width: 88%;
        height: 90%;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 32px;
        padding: 24px;
        box-sizing: border-box;
        border: 1px solid rgba(255, 255, 255, 0.07);
        display: flex;
        flex-direction: column;
        box-shadow: 0 30px 60px rgba(0,0,0,0.6);
    }

    /* INSET LCD CORE DISPLAY */
    .display {
        width: 100%;
        height: 90px;
        background: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        border: 1px solid rgba(6, 182, 212, 0.15);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-end;
        padding: 0 20px;
        box-sizing: border-box;
        margin-bottom: 25px;
        box-shadow: inset 0 4px 12px rgba(0,0,0,0.8);
    }

    #expr { font-size: 13px; color: #64748b; font-family: monospace; min-height: 16px; margin-bottom: 4px; }
    #val { font-size: 34px; color: #22d3ee; font-family: monospace; font-weight: bold; text-shadow: 0 0 12px rgba(34, 211, 238, 0.4); }

    /* GRID MATRIX FOR KEYS */
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        flex-grow: 1;
    }

    /* 🔮 3D COMPRESSED GLASS SPHERE BUTTONS */
    .btn-cell {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 50%; /* Pure sphere/circular mask */
        color: #f1f5f9;
        font-size: 20px;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all 0.12s cubic-bezier(0.4, 0, 0.2, 1);
        user-select: none;
        box-shadow: 0 6px 12px rgba(0,0,0,0.3),
                    inset 0 3px 6px rgba(255,255,255,0.05),
                    inset 0 -4px 6px rgba(0,0,0,0.4);
    }

    .btn-cell:hover {
        background: rgba(6, 182, 212, 0.1);
        color: #22d3ee;
        border-color: rgba(6, 182, 212, 0.4);
        box-shadow: 0 6px 15px rgba(6, 182, 212, 0.2), inset 0 2px 4px rgba(255,255,255,0.1);
    }

    .op-btn { color: #22d3ee; background: rgba(6, 182, 212, 0.03); }
    
    .eq-btn {
        background: linear-gradient(135deg, #06b6d4, #0891b2);
        color: #030712;
        font-weight: 700;
        border: none;
        box-shadow: 0 6px 12px rgba(6, 182, 212, 0.3), inset 0 3px 6px rgba(255,255,255,0.2);
    }
    .eq-btn:hover { color: #ffffff; box-shadow: 0 0 20px rgba(6, 182, 212, 0.6); }

    /* 💥 PHYSICAL DEPRESS ANIMATION (Z-AXIS DROP) */
    .btn-cell:active {
        transform: scale(0.9) translateY(4px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
</style>
</head>
<body>

<div class="app-container">
    <canvas id="webgl-canvas"></canvas>

    <div class="calc-ui">
        <div class="display">
            <div id="expr"></div>
            <div id="val">0</div>
        </div>
        
        <div class="grid">
            <div class="btn-cell op-btn" onclick="clearAll()">C</div>
            <div class="btn-cell op-btn" onclick="append('(')">(</div>
            <div class="btn-cell op-btn" onclick="append(')')">)</div>
            <div class="btn-cell op-btn" onclick="append('/')">÷</div>
            
            <div class="btn-cell" onclick="append('7')">7</div>
            <div class="btn-cell" onclick="append('8')">8</div>
            <div class="btn-cell" onclick="append('9')">9</div>
            <div class="btn-cell op-btn" onclick="append('*')">×</div>
            
            <div class="btn-cell" onclick="append('4')">4</div>
            <div class="btn-cell" onclick="append('5')">5</div>
            <div class="btn-cell" onclick="append('6')">6</div>
            <div class="btn-cell op-btn" onclick="append('-')">−</div>
            
            <div class="btn-cell" onclick="append('1')">1</div>
            <div class="btn-cell" onclick="append('2')">2</div>
            <div class="btn-cell" onclick="append('3')">3</div>
            <div class="btn-cell op-btn" onclick="append('+')">+</div>
            
            <div class="btn-cell" onclick="append('0')">0</div>
            <div class="btn-cell" onclick="append('.')">.</div>
            <div class="btn-cell op-btn" onclick="backspace()">◀</div>
            <div class="btn-cell eq-btn" onclick="compute()">=</div>
        </div>
    </div>
</div>

<script>
    // ==========================================================================
    // 🧬 INITIALIZING THE THREE.JS ENGINE INTERNALS
    // ==========================================================================
    const canvasContainer = document.getElementById('webgl-canvas');
    
    // 1. Create the Universal Universe container
    const scene = new THREE.Scene();

    // 2. Instantiate the Camera eye matrix
    const camera = new THREE.PerspectiveCamera(75, 360 / 560, 0.1, 1000);
    camera.position.z = 15; // Back out camera along Z axis to view the center object

    // 3. Instantiate the WebGL Engine Renderer and bind to HTML Canvas
    const renderer = new THREE.WebGLRenderer({ canvas: canvasContainer, antialias: true, alpha: true });
    renderer.setSize(360, 560);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); // Dynamic Chromebook scaling

    // 4. Engine Geometry Node: Construct a 3D Polyhedron Particle Sphere
    const geometry = new THREE.IcosahedronGeometry(8, 2); // Radius of 8 units, detailed vertex density
    
    // Engine Material Node: Wireframe configurations matching custom styling
    const material = new THREE.MeshBasicMaterial({
        color: 0x0ea5e9,       // Neon Cyan Hex code conversion
        wireframe: true,       // Renders structural geometric connecting lines
        transparent: true,
        opacity: 0.18          // Ambient backing glow level
    });

    // Merge geometry data and skin material settings into an engine Mesh Node
    const sphereMesh = new THREE.Mesh(geometry, material);
    scene.add(sphereMesh); // Inject object into active spatial field

    // 🔄 THE HARDWARE INFINITE ENGINE TICK ANIMATION LOOP (60 FPS Engine Run)
    function animateEngine() {
        requestAnimationFrame(animateEngine); // Tells browser to loop smoothly

        // Execute rotation modifications to matrix indices over every system clock tick
        sphereMesh.rotation.x += 0.003;
        sphereMesh.rotation.y += 0.005;
        sphereMesh.rotation.z += 0.001;

        // Command Renderer node to paint updated tracking calculations onto your screen
        renderer.render(scene, camera);
    }
    
    // Launch Infinite Game Engine Loop
    animateEngine();

    // ==========================================================================
    // 🧮 CLIENT SIDE INTERFACE ENGINE COMPREHENSION (Instant Engine Calls)
    // ==========================================================================
    let expressionStr = "";
    const displayExpr = document.getElementById("expr");
    const displayVal = document.getElementById("val");

    function append(key) {
        expressionStr += key;
        displayVal.innerText = expressionStr;
        // Interactive response: Trigger a minor pulse variation inside the 3D Engine on key press
        sphereMesh.scale.set(1.05, 1.05, 1.05);
        setTimeout(() => sphereMesh.scale.set(1, 1, 1), 80);
    }

    function clearAll() {
        expressionStr = "";
        displayExpr.innerText = "";
        displayVal.innerText = "0";
    }

    function backspace() {
        expressionStr = expressionStr.slice(0, -1);
        displayVal.innerText = expressionStr || "0";
    }

    function compute() {
        if (!expressionStr) return;
        try {
            displayExpr.innerText = expressionStr + " =";
            let executionResult = eval(expressionStr);
            if (executionResult.toString().includes('.')) {
                executionResult = parseFloat(executionResult.toFixed(6));
            }
            displayVal.innerText = executionResult;
            expressionStr = executionResult.toString();
            
            // Warp 3D engine background vector velocity forward on successful computation
            sphereMesh.rotation.y += 0.5;
        } catch (err) {
            displayVal.innerText = "Error";
            expressionStr = "";
        }
    }
</script>

</body>
</html>
"""

# Mount the Embedded JavaScript Game Engine securely into Streamlit canvas space
components.html(three_engine_html, height=600)
