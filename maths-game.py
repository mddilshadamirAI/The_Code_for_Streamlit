import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Maths Arena", page_icon="☠️", layout="centered")
st.markdown("<style>div[data-testid='stAppViewContainer'] { background: radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important; } #MainMenu, footer, header {visibility: hidden;}</style>", unsafe_allow_html=True)

def get_audio(f):
    try:
        with open(f, "rb") as a: return f"data:audio/mp3;base64,{base64.b64encode(a.read()).decode('utf-8')}"
    except: return ""

raw_template_html = f"""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
    body{{ margin:0; overflow:hidden; font-family:'Courier New', monospace; color:white; }}
    .arena-viewport{{ position:relative; width:480px; height:640px; margin:auto; border-radius:40px; }}
    #three-canvas{{ position:absolute; top:0; z-index:0; }}
    #ui-overlay, #cinematic-overlay{{ position:absolute; z-index:10; width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; background:rgba(0,0,0,0.95); border-radius:40px; }}
    #game{{ position:relative; z-index:2; width:100%; height:100%; padding:30px; box-sizing:border-box; display:none; }}
    .option-node-2d{{ position:absolute; width:76px; height:76px; background:#0f172a; border:1px solid #06b6d4; border-radius:50%; display:flex; justify-content:center; align-items:center; cursor:pointer; font-weight:900; color:#38bdf8; }}
    .mode-btn{{ margin:10px; padding:15px 30px; cursor:pointer; background:#1e293b; color:#38bdf8; border:2px solid #06b6d4; border-radius:10px; }}
    input{{ margin:5px; padding:10px; border-radius:5px; background:#0f172a; color:white; border:1px solid #38bdf8; }}
</style>
</head>
<body>
<div class="arena-viewport">
    <canvas id="three-canvas"></canvas>
    <div id="cinematic-overlay" style="display:none; z-index:20;"></div>
    <div id="ui-overlay">
        <input id="p1n" placeholder="Player 1 Name"><input id="p2n" placeholder="Player 2 Name (Optional)">
        <h2 style="color:#fff;">SELECT DIFFICULTY</h2>
        <button class="mode-btn" onclick="init('basic')">BASIC</button>
        <button class="mode-btn" onclick="init('medium')">MEDIUM</button>
        <button class="mode-btn" onclick="init('pro')">PRO</button>
    </div>
    <div id="game">
        <div id="status">SCORE: 0 | LIVES: 2</div>
        <div id="q-text" style="font-size:40px; text-align:center; margin:50px 0;">READY</div>
        <div id="wheel" style="position:relative; width:200px; height:200px; margin:auto;"></div>
    </div>
</div>
<script>
    const R_A = "{get_audio('faa.mp3')}", W_A = "{get_audio('haha.mp3')}", ROAR = "{get_audio('roar.mp3')}";
    let turn=1, qCount=0, startTime=0, target=0, mode='basic', gType='single', timer=null;
    let p1={{n:'P1', s:0, l:2, t:0}}, p2={{n:'P2', s:0, l:2, t:0}};

    function init(m) {{
        mode = m;
        p1.n = document.getElementById("p1n").value || "P1";
        p2.n = document.getElementById("p2n").value || "P2";
        gType = document.getElementById("p2n").value ? 'dual' : 'single';
        document.getElementById("ui-overlay").style.display = 'none';
        document.getElementById("game").style.display = 'block';
        next();
    }}

    function next() {{
        let n1 = Math.floor(Math.random()*(mode=='basic'?20:mode=='medium'?100:500)), n2 = Math.floor(Math.random()*(mode=='basic'?20:mode=='medium'?100:500));
        target = n1 + n2;
        document.getElementById("q-text").innerText = n1 + " + " + n2;
        document.getElementById("status").innerText = (turn==1?p1.n:p2.n) + " | SCORE: " + (turn==1?p1.s:p2.s) + " | LIVES: " + (turn==1?p1.l:p2.l);
        startTime = Date.now();
        let w = document.getElementById("wheel"); w.innerHTML = '';
        [target, target+3, target-2, target+5].sort(()=>Math.random()-0.5).forEach((v, i) => {{
            let r = (i*90)*(Math.PI/180);
            w.innerHTML += `<div class="option-node-2d" style="left:${{100+70*Math.cos(r)-35}}px; top:${{100+70*Math.sin(r)-35}}px;" onclick="check(${{v}})">${{v}}</div>`;
        }});
    }}

    function check(v) {{
        let p = (turn==1?p1:p2);
        if(v === target) {{
            p.s += 10; p.t += (Date.now() - startTime);
            new Audio(R_A).play();
            if(p.s % 100 === 0) {{
                let o = document.getElementById("cinematic-overlay");
                o.style.display="flex"; o.innerHTML="<div style='font-size:50px; color:gold;'>ROAR!</div>";
                new Audio(ROAR).play(); setTimeout(()=>o.style.display="none", 2000);
            }}
        }} else {{ p.l--; new Audio(W_A).play(); }}
        
        if(p.l <= 0) {{ alert(p.n + " LOST!"); location.reload(); }}
        qCount++;
        if(gType === 'dual') turn = (turn == 1 ? 2 : 1);
        
        if(qCount >= (gType == 'dual' ? 20 : 10)) {{
            let w = (p1.s > p2.s ? p1.n : (p2.s > p1.s ? p2.n : (p1.t < p2.t ? p1.n : p2.n)));
            alert("WINNER: " + w); location.reload();
        }} else next();
    }}

    const s = new THREE.Scene(), c = new THREE.PerspectiveCamera(75, 480/640, 0.1, 1000);
    const r = new THREE.WebGLRenderer({{canvas: document.getElementById('three-canvas'), alpha:true}});
    r.setSize(480, 640); c.position.z = 10;
    function anim() {{ requestAnimationFrame(anim); r.render(s, c); }} anim();
</script>
</body>
</html>
"""
components.html(raw_template_html, height=660)
