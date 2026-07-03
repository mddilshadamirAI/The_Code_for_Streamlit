import streamlit as st
import streamlit.components.v1 as components

from core_engine import TournamentEngine
from database_layer import ArenaDatabase
from render_bridge import RenderBridge
from assets_and_physics import ParticleEngine, SoundAssetManager
"""
MATHS ARENA PRO: SYSTEM ORCHESTRATOR (MODULE 4/5)
This module acts as the Main Controller (MVC pattern). 
It integrates all sub-systems into a unified Streamlit application.
"""

import streamlit as st
import streamlit.components.v1 as components
from core_engine import TournamentEngine
from database_layer import ArenaDatabase
from render_bridge import RenderBridge, EventDispatcher

# Replace your main() initialization block with this:
def main():
    st.set_page_config(page_title="Maths Arena Pro", layout="wide")
    
    # 1. Initialize Engine properly
    if 'engine' not in st.session_state or st.session_state.engine is None:
        st.session_state.engine = TournamentEngine()
        
    # 2. Initialize Database
    if 'db' not in st.session_state:
        st.session_state.db = ArenaDatabase()

    # 3. Initialize Game Variables
    if 'current_q' not in st.session_state:
        # Direct access to the method from the imported class
        q, ans = st.session_state.engine.next_round("medium")
        st.session_state.current_q = q
        st.session_state.current_ans = ans

    # UI Header
    st.markdown("<h1 style='text-align: center; color: #00f2ff;'>☠️ MATHS ARENA: ENTERPRISE ENGINE ☠️</h1>", unsafe_allow_html=True)

    # Layout: Visual Arena (Left) & Stats (Right)
    col1, col2 = st.columns([3, 1])

    with col1:
        # Inject the HTML/JS Frontend
        game_html = RenderBridge.get_html_layout() + f"<script>{RenderBridge.get_javascript_client()}</script>"
        components.html(game_html, height=550)

    with col2:
        st.subheader("Match Stats")
        stats = st.session_state.engine.get_match_stats()
        st.metric("Player 1 Score", stats['p1']['score'])
        st.metric("Player 2 Score", stats['p2']['score'])
        st.write(f"Active Turn: {stats['turn']}")
        
        if st.button("RESET TOURNAMENT"):
            st.session_state.engine = TournamentEngine()
            st.rerun()

    # Message Handling (The "Bridge" implementation)
    # This logic listens for the 'SUBMIT_MOVE' signal from the JS side
    if 'input_received' in st.session_state:
        user_val = st.session_state.input_received
        correct = st.session_state.engine.process_turn(
            st.session_state.engine.active_turn, 
            user_val, 
            st.session_state.current_ans
        )
        
        # Log to Database
        st.session_state.db.log_match(st.session_state.engine.match_id, "P1", "P2", "Pending")
        
        # Prepare next round
        st.session_state.current_q, st.session_state.current_ans = st.session_state.engine.next_round("medium")
        del st.session_state.input_received
        st.rerun()

if __name__ == "__main__":
    main()
