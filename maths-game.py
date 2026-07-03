import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Maths Arena Tournament", layout="centered")
st.markdown("<style>div[data-testid='stAppViewContainer'] { background: #020617; } #MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)

def get_audio(f):
    try:
        with open(f, "rb") as a: return f"data:audio/mp3;base64,{base64.b64encode(a.read()).decode('utf-8')}"
    except: return ""

# Note the {{ and }} to escape the braces for Python's f-string
raw_html = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body{{ margin:0; overflow:hidden; font-family:'Courier New', monospace; color:white; }}
        .arena{{ width:480px; height:640px; margin:auto; position:relative; border-radius:40px; background:#000; overflow:hidden; }}
        #ui{{ position:absolute; z-index:20; width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; background:rgba(0,0,0,0.9); }}
        .hud{{ position:absolute; top:20px; width:100%; display:flex; justify-content:space-around; z-index:5; font-size:16px; font-weight:900; color:#06b6d4; }}
        .node{{ position:absolute; width:80px; height:80px; border:2px solid #38bdf8; border-radius:50%; display:flex; justify-content:center; align-items:center; cursor:pointer; background:rgba(0,0,0,0.8); transition:0.3s; }}
        .node:hover{{ transform:scale(1.2); box-shadow:0 0 20px #38bdf8; }}
        .q-box{{ font-size:50px; font-weight:900; text-shadow:0 0 20px #fff; }}
    </style>
</head>
<body>
<div class="arena">
    <canvas id="three"></canvas>
    <div id="ui">
        <input id="n1" placeholder="Player 1 Name">
        <input id="n2" placeholder="Player 2 Name">
        <button onclick="start('medium')">START TOURNAMENT</button>
    </div>
    <div id="game" style="display:none; text-align:center; padding-top:100px;">
        <div class="hud"><span id="hud1"></span> | <span id="hud2"></span></div>
        <div id="q" class="q-box"></div>
        <div id="wheel" style="position:relative; width:200px; height:200px; margin:100px auto;"></div>
    </div>
</div>
<script>
    const R_A = "{get_audio('faa.mp3')}";
    const W_A = "{get_audio('haha.mp3')}";
    let turn = 1, qCount = 0;
    let p1 = {{n:'P1', s:0, l:3}}, p2 = {{n:'P2', s:0, l:3}};

    function start(m) {{
        p1.n = document.getElementById('n1').value || 'P1';
        p2.n = document.getElementById('n2').value || 'P2';
        document.getElementById('ui').style.display='none';
        document.getElementById('game').style.display='block';
        next();
    }}

    function next() {{
        let ops = ['+', '-', '*', '/'], op = ops[Math.floor(Math.random()*4)];
        let a = Math.floor(Math.random()*50)+1, b = Math.floor(Math.random()*50)+1;
        if(op==='/') {{ a = b * (Math.floor(Math.random()*10)+1); }}
        let ans = eval(a+op+b);
        document.getElementById('q').innerText = a + " " + op + " " + b;
        let w = document.getElementById('wheel'); w.innerHTML='';
        [ans, ans+5, ans-3, ans+10].sort(()=>Math.random()-0.5).forEach(v => {{
            let d = document.createElement('div'); d.className='node'; d.innerText=v;
            d.onclick=()=>check(v, ans); w.appendChild(d);
        }});
    }}

    function check(v, ans) {{
        let p = (turn==1?p1:p2);
        if(v===ans) {{ p.s+=10; new Audio(R_A).play(); }} else {{ p.l--; new Audio(W_A).play(); }}
        
        document.getElementById('hud1').innerText = p1.n + ": " + p1.s;
        document.getElementById('hud2').innerText = p2.n + ": " + p2.s;
        
        if(p.l <= 0) {{ alert(p.n + " Eliminated!"); location.reload(); }}
        turn = (turn==1?2:1); qCount++;
        if(qCount >= 20) {{ 
            let win = (p1.s>p2.s?p1.n:p2.n);
            alert("TOURNAMENT OVER! Winner: " + win); location.reload();
        }} else {{ next(); }}
    }}

    const s = new THREE.Scene(), c = new THREE.PerspectiveCamera(75, 480/640, 0.1, 1000);
    const r = new THREE.WebGLRenderer({{canvas:document.getElementById('three'), alpha:true}});
    r.setSize(480,640); c.position.z = 5;
    function anim() {{ requestAnimationFrame(anim); r.render(s, c); }} anim();
</script>
</body>
</html>
"""
components.html(raw_html, height=660)
