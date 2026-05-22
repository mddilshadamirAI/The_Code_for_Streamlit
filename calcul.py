import streamlit as st
import streamlit.components.v1 as components

# Page configurations
st.set_page_config(
    page_title="Smart Calculator 3D",
    page_icon="🧮",
    layout="centered"
)

# Set a dark, deep background for the Streamlit page to make the glass pop
st.markdown("""
<style>
div[data-testid="stAppViewContainer"], .main {
    background: #0d1117 !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Headline
st.markdown("<h1 style='text-align: center; color: #e2e8f0; font-family: sans-serif; font-weight: 700; letter-spacing: 1px;'>🛸 Smart Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 30px;'>Hyper-Fast • 3D Glassmorphism Engine</p>", unsafe_allow_html=True)

# ==============================================================================
# 🚀 PURE CLIENT-SIDE 3D GRAPHICS & LOGIC ENGINE (HTML/JS/CSS)
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
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        perspective: 1000px; /* Unlocks true 3D spatial depth */
    }

    /* 💎 THE GLASSMORPHISM CHASSIS */
    .calc-container {
        width: 340px;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 28px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transform: rotateX(10deg) rotateY(-5deg); /* Slight 3D angled viewpoint */
        transform-style: preserve-3d;
        transition: transform 0.5s ease;
    }
    
    .calc-container:hover {
        transform: rotateX(5deg) rotateY(-2deg);
    }

    /* 🖥️ GLOWING INSET DISPLAY */
    .display {
        width: 100%;
        height: 85px;
        background: rgba(0, 0, 0, 0.4);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: inset 0 4px 10px rgba(0,0,0,0.9);
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-end;
        padding: 0 20px;
        box-sizing: border-box;
        overflow: hidden;
    }

    #expr {
        font-size: 14px;
        color: #64748b;
        min-height: 18px;
        margin-bottom: 4px;
        letter-spacing: 1px;
    }

    #val {
        font-size: 32px;
        color: #00f2fe;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
        white-space: nowrap;
    }

    /* 🎛️ BUTTON MATRIX GRID */
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 18px;
    }

    /* 📦 3D CUBE BUTTON STRUCTURE */
    .btn-wrapper {
        position: relative;
        height: 60px;
        perspective: 400px;
    }

    .cube-btn {
        position: absolute;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        color: #e2e8f0;
        font-size: 20px;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        justify-content: center;
        align-items: center;
        
        /* The 3D Base Layer (Thickness of the Cube) */
        box-shadow: 0 6px 0px rgba(0, 0, 0, 0.4),
                    0 10px 15px rgba(0, 0, 0, 0.5);
        transform: translateZ(0);
        transition: all 0.06s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        user-select: none;
    }

    /* Hover Glow States */
    .cube-btn:hover {
        background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
        color: #00f2fe;
        border-color: rgba(0, 242, 254, 0.3);
        box-shadow: 0 6px 0px rgba(0, 0, 0, 0.4),
                    0 0 15px rgba(0, 242, 254, 0.4);
    }

    /* Special Operator Cube Variant */
    .op-btn {
        background: linear-gradient(135deg, rgba(0, 242, 254, 0.2), rgba(79, 172, 254, 0.1));
        border-color: rgba(0, 242, 254, 0.2);
        color: #00f2fe;
    }
    
    .eq-btn {
        background: linear-gradient(135deg, #00f2fe, #4facfe);
        color: #0d1117;
        font-weight: bold;
        border: none;
        box-shadow: 0 6px 0px #008ba3, 0 10px 15px rgba(0, 242, 254, 0.3);
    }
    .eq-btn:hover {
        color: #0d1117;
        box-shadow: 0 6px 0px #008ba3, 0 0 20px rgba(0, 242, 254, 0.6);
    }

    /* 🛑 PHYSICAL COMPRESSION ANIMATION (Pushed down along the Z-axis) */
    .cube-btn:active {
        transform: translateY(5px) translateZ(-2px);
        box-shadow: 0 1px 0px rgba(0, 0, 0, 0.4),
                    0 2px 5px rgba(0, 0, 0, 0.5);
    }
    
    .eq-btn:active {
        transform: translateY(5px) translateZ(-2px);
        box-shadow: 0 1px 0px #008ba3, 0 2px 5px rgba(0, 242, 254, 0.2);
    }
</style>
</head>
<body>

<div class="calc-container">
    <div class="display">
        <div id="expr"></div>
        <div id="val">0</div>
    </div>
    
    <div class="grid">
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="clearAll()">C</div></div>
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="append('(')">(</div></div>
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="append(')')">)</div></div>
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="append('/')">÷</div></div>
        
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('7')">7</div></div>
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('8')">8</div></div>
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('9')">9</div></div>
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="append('*')">×</div></div>
        
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('4')">4</div></div>
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('5')">5</div></div>
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('6')">6</div></div>
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="append('-')">−</div></div>
        
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('1')">1</div></div>
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('2')">2</div></div>
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('3')">3</div></div>
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="append('+')">+</div></div>
        
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('0')">0</div></div>
        <div class="btn-wrapper"><div class="cube-btn" onclick="append('.')">.</div></div>
        <div class="btn-wrapper"><div class="cube-btn op-btn" onclick="backspace()">◀</div></div>
        <div class="btn-wrapper"><div class="cube-btn eq-btn" onclick="compute()">=</div></div>
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
            // Secure calculation evaluation within browser runtime
            let result = eval(currentExpression);
            if (Number.isFloat = n => n % 1 !== 0 && !isNaN(n)) {
                if (result.toString().includes('.')) {
                    result = parseFloat(result.toFixed(6));
                }
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

# Render JavaScript/CSS Engine inside Streamlit Workspace
components.html(calculator_html, height=520)
