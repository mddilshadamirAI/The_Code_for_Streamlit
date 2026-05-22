import streamlit as st
import streamlit.components.v1 as components

# Page configurations
st.set_page_config(
    page_title="Dilshad's 3D Liquidity Engine",
    page_icon="🔮",
    layout="centered"
)

# Deep space background for the main Streamlit interface
st.markdown("""
<style>
div[data-testid="stAppViewContainer"], .main {
    background: #020617 !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# SMC Style Headline
st.markdown("<h1 style='text-align: center; color: #f8fafc; font-family: system-ui, sans-serif; font-weight: 800; letter-spacing: -1px; margin-bottom: 0px;'>Dilshad's Smart Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #38bdf8; font-family: monospace; font-size: 14px; margin-top: 5px; margin-bottom: 40px;'>// Institutional Grade 3D UI // [STATUS: ACTIVE]</p>", unsafe_allow_html=True)

# ==============================================================================
# 🔮 HIGH-SPEED SPATIAL JS/CSS 3D REVOLVING ENGINE
# ==============================================================================
calculator_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    body {
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        background: transparent;
        font-family: system-ui, -apple-system, sans-serif;
        overflow: hidden;
    }

    /* Unlocks massive spatial depth for the revolving effect */
    .scene-3d {
        perspective: 2000px; 
        padding: 50px;
    }

    /* 💎 THE REVOLVING LIQUIDITY CHASSIS */
    .calc-chassis {
        width: 350px;
        background: rgba(255, 255, 255, 0.01);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        
        /* Making the whole chassis spherical/oval */
        border-radius: 60px; 
        
        padding: 30px;
        border: 1px solid rgba(56, 189, 248, 0.15); /* Neon cyan border */
        
        /* Intense outer glow to simulate energy field */
        box-shadow: 0 0 50px rgba(56, 189, 248, 0.1),
                    inset 0 0 20px rgba(255, 255, 255, 0.03);
        
        transform-style: preserve-3d;
        
        /* 🔄 THE CONTINUOUS REVOLUTION ANIMATION */
        animation: revolveChassis 25s linear infinite; 
    }

    /* Continuous Y-axis rotation keyframes */
    @keyframes revolveChassis {
        0% { transform: rotateX(5deg) rotateY(0deg); }
        100% { transform: rotateX(5deg) rotateY(360deg); }
    }

    /* 🖥️ CYBER-GLOW INSET DISPLAY */
    .display {
        width: 100%;
        height: 100px;
        background: rgba(0, 0, 0, 0.5);
        border-radius: 25px;
        border: 1px solid rgba(56, 189, 248, 0.1);
        box-shadow: inset 0 5px 15px rgba(0,0,0,0.9);
        margin-bottom: 35px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-end;
        padding: 0 25px;
        box-sizing: border-box;
        overflow: hidden;
        
        /* Counter-rotation to keep screen readable while body revolves */
        animation: stabilizeScreen 25s linear infinite;
        transform-origin: center center -100px; /* Pivots screen back */
    }
    
    @keyframes stabilizeScreen {
        0% { transform: rotateY(0deg); }
        100% { transform: rotateY(-360deg); }
    }

    #expr {
        font-size: 15px;
        color: #94a3b8;
        min-height: 20px;
        margin-bottom: 6px;
        font-family: monospace;
        letter-spacing: 1px;
    }

    #val {
        font-size: 38px;
        color: #f8fafc;
        font-weight: bold;
        font-family: monospace;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
        white-space: nowrap;
    }

    /* 🎛️ BUTTON MATRIX GRID */
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        perspective: 500px; /* Context for individual button depth */
    }

    /* 🔵 SUPER REAL 3D SPHERICAL BUBBLE BUTTON */
    .btn-3d {
        width: 100%;
        height: 65px;
        background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.01));
        
        /* Making buttons perfect spheres/ovals */
        border-radius: 50%; 
        
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #e2e8f0;
        font-size: 22px;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all 0.1s ease-out;
        user-select: none;
        
        /* Intense 3D Shadow Matrix for Spherical Volume */
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.6),
                    inset 0 4px 6px rgba(255, 255, 255, 0.05),
                    inset 0 -5px 10px rgba(0, 0, 0, 0.4);
    }

    /* Cyan Highlight on Hover */
    .btn-3d:hover {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.1), rgba(255,255,255,0.02));
        color: #38bdf8;
        border-color: rgba(56, 189, 248, 0.3);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.6),
                    0 0 20px rgba(56, 189, 248, 0.3);
    }

    /* Speculative Order Block (Operator) Variant */
    .op-btn {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(255,255,255,0.01));
        color: #38bdf8;
        border-color: rgba(56, 189, 248, 0.2);
    }
    
    /* The Profit Target (Equal) Button */
    .eq-btn {
        background: linear-gradient(135deg, #0ea5e9, #0369a1);
        color: white;
        border: none;
        box-shadow: 0 8px 15px rgba(14, 165, 233, 0.4),
                    inset 0 4px 6px rgba(255, 255, 255, 0.2);
    }

    /* 🛑 PHYSICAL COMPRESSION (Sphere Squeezes along Z-axis) */
    .btn-3d:active {
        transform: translateY(6px) translateZ(-10px);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.7),
                    inset 0 2px 3px rgba(255, 255, 255, 0.02);
    }
    
    .eq-btn:active {
        transform: translateY(6px) translateZ(-10px);
        box-shadow: 0 2px 5px rgba(14, 165, 233, 0.5);
    }
</style>
</head>
<body>

<div class="scene-3d">
    <div class="calc-chassis">
        <div class="display">
            <div id="expr"></div>
            <div id="val">0</div>
        </div>
        
        <div class="grid">
            <div class="btn-3d op-btn" onclick="clearAll()">C</div>
            <div class="btn-3d op-btn" onclick="append('(')">(</div>
            <div class="btn-3d op-btn" onclick="append(')')">)</div>
            <div class="btn-3d op-btn" onclick="append('/')">÷</div>
            
            <div class="btn-3d" onclick="append('7')">7</div>
            <div class="btn-3d" onclick="append('8')">8</div>
            <div class="btn-3d" onclick="append('9')">9</div>
            <div class="btn-3d op-btn" onclick="append('*')">×</div>
            
            <div class="btn-3d" onclick="append('4')">4</div>
            <div class="btn-3d" onclick="append('5')">5</div>
            <div class="btn-3d" onclick="append('6')">6</div>
            <div class="btn-3d op-btn" onclick="append('-')">−</div>
            
            <div class="btn-3d" onclick="append('1')">1</div>
            <div class="btn-3d" onclick="append('2')">2</div>
            <div class="btn-3d" onclick="append('3')">3</div>
            <div class="btn-3d op-btn" onclick="append('+')">+</div>
            
            <div class="btn-3d" onclick="append('0')">0</div>
            <div class="btn-3d" onclick="append('.')">.</div>
            <div class="btn-3d op-btn" onclick="backspace()">◀</div>
            <div class="btn-3d eq-btn" onclick="compute()">=</div>
        </div>
    </div>
</div>

<script>
    let currentExpression = "";
    const exprDiv = document.getElementById("expr");
    const valDiv = document.getElementById("val");

    function append(token) {
        currentExpression += token;
        valDiv.innerText = currentExpression;
    }

    function clearAll() {
        currentExpression = "";
        exprDiv.innerText = "";
        valDiv.innerText = "0";
    }

    function backspace() {
        currentExpression = currentExpression.slice(0, -1);
        valDiv.innerText = currentExpression || "0";
    }

    function compute() {
        if (!currentExpression) return;
        try {
            exprDiv.innerText = currentExpression + " =";
            // Fast browser-side evaluation core
            let result = eval(currentExpression);
            if (result.toString().includes('.')) {
                result = parseFloat(result.toFixed(8)); // Precision float mapping
            }
            valDiv.innerText = result;
            currentExpression = result.toString();
        } catch (err) {
            valDiv.innerText = "Syntax Error";
            currentExpression = "";
        }
    }
</script>

</body>
</html>
"""

# Render the custom 3D HTML environment within the Streamlit workspace
components.html(calculator_html, height=750)
