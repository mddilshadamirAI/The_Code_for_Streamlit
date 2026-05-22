import streamlit as st

# Page layout configurations
st.set_page_config(
    page_title="Dilshad's 3D Engine OS",
    page_icon="🧮",
    layout="centered"
)

# ==============================================================================
# 🧬 THE 3D SKEUOMORPHIC STYLING MATRIX
# ==============================================================================
st.markdown("""
<style>
/* App workspace depth configuration */
div[data-testid="stAppViewContainer"], .main {
    background: #0b0f17 !important;
}

/* Main Tactile Phone Frame Engine */
.phone-deck {
    background: linear-gradient(145deg, #1e2633, #0f131a);
    border-radius: 36px;
    padding: 28px;
    box-shadow: 12px 12px 25px #05070a, 
                -12px -12px 25px #273142, 
                inset 1px 1px 1px rgba(255, 255, 255, 0.1);
    border: 1px solid #1c232e;
    max-width: 360px;
    margin: 0 auto;
}

/* Inset Bezel Display Screen Engine */
.display-screen {
    background: #06090d;
    border-radius: 18px;
    padding: 20px;
    box-shadow: inset 4px 4px 8px #020304, 
                inset -4px -4px 8px #101621;
    border: 1px solid #131a24;
    min-height: 90px;
    text-align: right;
    margin-bottom: 25px;
}

/* Global Streamlit Button Remapping to Mechanical 3D Keycaps */
div.stButton > button {
    width: 100% !important;
    height: 60px !important;
    background: linear-gradient(135deg, #222b3a, #161b24) !important;
    color: #f8fafc !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    border-radius: 16px !important;
    border: 1px solid #2a3447 !important;
    
    /* 3D Cap Thickness Shadow Layering */
    box-shadow: 0px 6px 0px #090c12, 
                0px 8px 15px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.05s ease-in-out !important;
}

/* Key Hover state glow matrix */
div.stButton > button:hover {
    background: linear-gradient(135deg, #2a3547, #1b212c) !important;
    color: #06b6d4 !important;
    border-color: #06b6d4 !important;
}

/* Physical Mechanical Compress Down Animation */
div.stButton > button:active {
    transform: translateY(5px) !important;
    box-shadow: 0px 1px 0px #090c12, 
                0px 2px 4px rgba(0, 0, 0, 0.5) !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 🧠 MEMORY MANAGEMENT LOOP
# ==============================================================================
if "calc_expression" not in st.session_state:
    st.session_state.calc_expression = ""
if "last_calculation" not in st.session_state:
    st.session_state.last_calculation = ""

# Helper function to append digits/operators
def input_token(token):
    st.session_state.calc_expression += str(token)

# Helper function to compute expression evaluations securely
def evaluate_expression():
    try:
        expr = st.session_state.calc_expression
        if expr:
            # Safe internal evaluations string mapping
            result = eval(expr)
            # Formatting floats cleanly
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            st.session_state.last_calculation = expr + " ="
            st.session_state.calc_expression = str(result)
    except ZeroDivisionError:
        st.session_state.calc_expression = "Error: Div by 0"
    except Exception:
        st.session_state.calc_expression = "Syntax Error"

# ==============================================================================
# 📱 THE TACTILE CONSOLE INTERFACE BUILD
# ==============================================================================
st.write("")
st.write("")

# Layout isolation vector to constrain size like a smartphone
left_space, center_deck, right_space = st.columns([1, 2, 1])

with center_deck:
    # Open HTML Phone Deck Chassis container
    st.markdown('<div class="phone-deck">', unsafe_allow_html=True)
    
    # Render the Custom Inset Depth Screen
    history_view = st.session_state.last_calculation
    current_view = st.session_state.calc_expression or "0"
    
    st.markdown(f"""
    <div class="display-screen">
        <div style="color: #475569; font-size: 13px; font-family: monospace; min-height: 18px; letter-spacing: 1px;">{history_view}</div>
        <div style="color: #06b6d4; font-size: 30px; font-family: monospace; font-weight: bold; overflow-x: auto; white-space: nowrap; direction: ltr;">{current_view}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- ROW 1 CONTROL KEYS ---
    r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
    with r1_c1:
        if st.button("C"):
            st.session_state.calc_expression = ""
            st.session_state.last_calculation = ""
            st.rerun()
    with r1_c2:
        if st.button("("): input_token("("); st.rerun()
    with r1_c3:
        if st.button(")"): input_token(")"); st.rerun()
    with r1_c4:
        if st.button("÷"): input_token("/"); st.rerun()

    # --- ROW 2 NUMERIC GRID ---
    r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
    with r2_c1:
        if st.button("7"): input_token("7"); st.rerun()
    with r2_c2:
        if st.button("8"): input_token("8"); st.rerun()
    with r2_c3:
        if st.button("9"): input_token("9"); st.rerun()
    with r2_c4:
        if st.button("×"): input_token("*"); st.rerun()

    # --- ROW 3 NUMERIC GRID ---
    r3_c1, r3_c2, r3_c3, r3_c4 = st.columns(4)
    with r3_c1:
        if st.button("4"): input_token("4"); st.rerun()
    with r3_c2:
        if st.button("5"): input_token("5"); st.rerun()
    with r3_c3:
        if st.button("6"): input_token("6"); st.rerun()
    with r3_c4:
        if st.button("−"): input_token("-"); st.rerun()

    # --- ROW 4 NUMERIC GRID ---
    r4_c1, r4_c2, r4_c3, r4_c4 = st.columns(4)
    with r4_c1:
        if st.button("1"): input_token("1"); st.rerun()
    with r4_c2:
        if st.button("2"): input_token("2"); st.rerun()
    with r4_c3:
        if st.button("3"): input_token("3"); st.rerun()
    with r4_c4:
        if st.button("+"): input_token("+"); st.rerun()

    # --- ROW 5 BASE DECK GRID ---
    r5_c1, r5_c2, r5_c3, r5_c4 = st.columns(4)
    with r5_c1:
        if st.button("0"): input_token("0"); st.rerun()
    with r5_c2:
        if st.button("."): input_token("."); st.rerun()
    with r5_c3:
        if st.button("◀"):
            st.session_state.calc_expression = st.session_state.calc_expression[:-1]
            st.rerun()
    with r5_c4:
        if st.button("="):
            evaluate_expression()
            st.rerun()
            
    # Close HTML Phone Deck container
    st.markdown('</div>', unsafe_allow_html=True)
