import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Maths Arena", layout="centered")

def get_audio(f):
    try:
        with open(f, "rb") as a: return f"data:audio/mp3;base64,{base64.b64encode(a.read()).decode('utf-8')}"
    except: return ""

raw_html = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ margin:0; padding:0; background:#020617; font-family:sans-serif; color:white; overflow:hidden; }}
        #arena {{ width:480px; height:640px; margin:auto; position:relative; background:#000; border:2px solid #38bdf8; }}
        #ui {{ position:absolute; z-index:50; width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; background:#000; }}
        .game-ui {{ display:none; text-align:center; padding-top:50px; }}
        .btn {{ padding:15px 30px; margin:10px; cursor:pointer; background:#06b6d4; color:white; border:none; border-radius:10px; font-weight:bold; }}
        .q-text {{ font-size:40px; margin:20px; }}
        .node {{ width:70px; height:70px; border:2px solid #06b6d4; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; margin:10px; cursor:pointer; }}
    </style>
</head>
<body>
    <div id="arena">
        <canvas id="three" style="position:absolute; top:0; left:0;"></canvas>
        
        <div id="ui">
            <input id="n1" placeholder="Player 1 Name" style="margin:5px;">
            <input id="n2" placeholder="Player 2 Name" style="margin:5px;">
            <button class="btn" onclick="startGame()">START TOURNAMENT</button>
        </div>

        <div id="game" class="game-ui">
            <div id="hud" style="color:#06b6d4; font-weight:bold;"></div>
            <div id="q" class="q-text"></div>
            <div id="options"></div>
        </div>
    </div>

<script>
    const R_A = "{get_audio('faa.mp3')}";
    const W_A = "{get_audio('haha.mp3')}";
    let p1={{n:'P1', s:0, l:3}}, p2={{n:'P2', s:0, l:3}}, turn=1, qCount=0, ans=0;

    function startGame() {{
        p1.n = document.getElementById('n1').value || 'P1';
        p2.n = document.getElementById('n2').value || 'P2';
        document.getElementById('ui').style.display = 'none';
        document.getElementById('game').style.display = 'block';
        nextQuestion();
    }}

    function nextQuestion() {{
        let a = Math.floor(Math.random()*50)+1, b = Math.floor(Math.random()*50)+1;
        ans = a + b;
        document.getElementById('q').innerText = a + " + " + b;
        document.getElementById('hud').innerText = p1.n + ": " + p1.s + " | " + p2.n + ": " + p2.s;
        
        let opts = [ans, ans+5, ans-3, ans+10].sort(() => Math.random() - 0.5);
        let cont = document.getElementById('options'); cont.innerHTML = '';
        opts.forEach(v => {{
            let d = document.createElement('div'); d.className = 'node'; d.innerText = v;
            d.onclick = () => checkAns(v); cont.appendChild(d);
        }});
    }}

    function checkAns(v) {{
        let p = (turn==1 ? p1 : p2);
        if(v === ans) {{ p.s += 10; new Audio(R_A).play(); }} 
        else {{ p.l -= 1; new Audio(W_A).play(); }}
        
        if(p.l <= 0) {{ alert(p.n + " ELIMINATED!"); location.reload(); }}
        
        turn = (turn==1 ? 2 : 1); qCount++;
        if(qCount >= 20) {{ alert("WINNER: " + (p1.s > p2.s ? p1.n : p2.n)); location.reload(); }}
        else {{ nextQuestion(); }}
    }}

    // Three.js Background
    const scene = new THREE.Scene(), cam = new THREE.PerspectiveCamera(75, 480/640, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({{canvas:document.getElementById('three'), alpha:true}});
    renderer.setSize(480, 640); cam.position.z = 5;
    function anim() {{ requestAnimationFrame(anim); renderer.render(scene, cam); }} anim();
</script>
</body>
</html>
"""
components.html(raw_html, height=660)
