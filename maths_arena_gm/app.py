import streamlit as st
import sqlite3
import random
import math
import time
import hashlib
from datetime import datetime, date

# ============================================================
# MATHS ARENA PRO
# Single-file Streamlit Edition
# ============================================================

st.set_page_config(
    page_title="Maths Arena PRO",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CONSTANTS
# ============================================================

DB_NAME = "maths_arena.db"

DIFFICULTIES = {
    "Basic": {
        "time": 20,
        "lives": 5,
        "base_xp": 10,
        "base_coins": 2,
    },
    "Medium": {
        "time": 15,
        "lives": 4,
        "base_xp": 15,
        "base_coins": 3,
    },
    "Pro": {
        "time": 12,
        "lives": 3,
        "base_xp": 22,
        "base_coins": 5,
    },
    "Master": {
        "time": 10,
        "lives": 3,
        "base_xp": 30,
        "base_coins": 7,
    },
}

# ============================================================
# DATABASE
# ============================================================

def get_db():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            username TEXT PRIMARY KEY,
            xp INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0,
            games INTEGER DEFAULT 0,
            wins INTEGER DEFAULT 0,
            correct INTEGER DEFAULT 0,
            wrong INTEGER DEFAULT 0,
            best_streak INTEGER DEFAULT 0,
            best_score INTEGER DEFAULT 0,
            created_at TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            mode TEXT,
            difficulty TEXT,
            score INTEGER,
            correct INTEGER,
            wrong INTEGER,
            best_streak INTEGER,
            played_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def ensure_player(username):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT username FROM players WHERE username = ?",
        (username,)
    )

    if cur.fetchone() is None:
        cur.execute("""
            INSERT INTO players
            (username, xp, coins, games, wins, correct, wrong,
             best_streak, best_score, created_at)
            VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, ?)
        """, (username, datetime.now().isoformat()))

        conn.commit()

    conn.close()


def save_match(username, mode, difficulty, score,
               correct, wrong, best_streak, won=False):

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        UPDATE players
        SET
            xp = xp + ?,
            coins = coins + ?,
            games = games + 1,
            wins = wins + ?,
            correct = correct + ?,
            wrong = wrong + ?,
            best_streak =
                CASE
                    WHEN ? > best_streak THEN ?
                    ELSE best_streak
                END,
            best_score =
                CASE
                    WHEN ? > best_score THEN ?
                    ELSE best_score
                END
        WHERE username = ?
    """, (
        max(score, 0),
        max(score // 10, 0),
        1 if won else 0,
        correct,
        wrong,
        best_streak,
        best_streak,
        score,
        score,
        username
    ))

    cur.execute("""
        INSERT INTO matches
        (username, mode, difficulty, score, correct,
         wrong, best_streak, played_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        username,
        mode,
        difficulty,
        score,
        correct,
        wrong,
        best_streak,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def get_player(username):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT username, xp, coins, games, wins,
               correct, wrong, best_streak, best_score
        FROM players
        WHERE username = ?
    """, (username,))

    result = cur.fetchone()
    conn.close()

    return result


def get_leaderboard(limit=10):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT username, xp, coins, games,
               wins, correct, best_streak, best_score
        FROM players
        ORDER BY xp DESC
        LIMIT ?
    """, (limit,))

    result = cur.fetchall()
    conn.close()

    return result


def get_history(username, limit=10):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT mode, difficulty, score,
               correct, wrong, best_streak, played_at
        FROM matches
        WHERE username = ?
        ORDER BY id DESC
        LIMIT ?
    """, (username, limit))

    result = cur.fetchall()
    conn.close()

    return result


# ============================================================
# QUESTION ENGINE
# ============================================================

def make_question(difficulty):
    """
    Generates questions without eval().
    Returns:
        question, answer, category
    """

    if difficulty == "Basic":

        category = random.choice([
            "Addition",
            "Subtraction",
            "Multiplication"
        ])

        if category == "Addition":
            a = random.randint(5, 99)
            b = random.randint(5, 99)
            return f"{a} + {b}", a + b, category

        if category == "Subtraction":
            a = random.randint(20, 120)
            b = random.randint(5, a)
            return f"{a} − {b}", a - b, category

        a = random.randint(2, 15)
        b = random.randint(2, 12)
        return f"{a} × {b}", a * b, category

    if difficulty == "Medium":

        category = random.choice([
            "Mixed",
            "Division",
            "Squares"
        ])

        if category == "Mixed":
            a = random.randint(3, 20)
            b = random.randint(2, 12)
            c = random.randint(1, 20)

            if random.choice([True, False]):
                return f"({a} × {b}) + {c}", (a * b) + c, category

            return f"({a} × {b}) − {c}", (a * b) - c, category

        if category == "Division":
            b = random.randint(2, 12)
            ans = random.randint(2, 15)
            a = b * ans

            return f"{a} ÷ {b}", ans, category

        a = random.randint(5, 25)
        return f"{a}²", a * a, category

    if difficulty == "Pro":

        category = random.choice([
            "Powers",
            "Order of Operations",
            "Percentages"
        ])

        if category == "Powers":
            a = random.randint(2, 12)
            power = random.choice([2, 3])

            return f"{a}^{power}", a ** power, category

        if category == "Order of Operations":
            a = random.randint(2, 15)
            b = random.randint(2, 12)
            c = random.randint(1, 20)

            return f"{a} × {b} + {c}", (a * b) + c, category

        percent = random.choice([10, 20, 25, 50])
        number = random.choice([40, 60, 80, 100, 120, 200])

        return f"{percent}% of {number}", (percent * number) // 100, category

    # MASTER

    category = random.choice([
        "Quadratic",
        "Advanced Arithmetic",
        "Roots"
    ])

    if category == "Quadratic":
        x = random.randint(2, 12)
        b = random.randint(1, 10)

        return (
            f"{x}² + {b}×{x}",
            x * x + b * x,
            category
        )

    if category == "Roots":
        x = random.randint(2, 15)
        return f"√{x*x}", x, category

    a = random.randint(10, 50)
    b = random.randint(2, 15)
    c = random.randint(1, 10)

    return (
        f"({a} + {b}) × {c}",
        (a + b) * c,
        category
    )


# ============================================================
# XP / LEVEL SYSTEM
# ============================================================

def calculate_level(xp):
    return max(1, int(math.sqrt(xp / 25)) + 1)


def xp_for_next_level(level):
    return (level ** 2) * 25


def level_progress(xp):
    level = calculate_level(xp)
    current = (level - 1) ** 2 * 25
    target = level ** 2 * 25

    if target <= current:
        return 0.0

    return min(
        max((xp - current) / (target - current), 0),
        1
    )


# ============================================================
# ACHIEVEMENTS
# ============================================================

def achievements(correct, streak, score, games):

    items = []

    if correct >= 1:
        items.append(("🎯", "First Hit", "Answer your first question"))

    if correct >= 10:
        items.append(("⚡", "10 Correct", "Solve 10 questions"))

    if correct >= 50:
        items.append(("🔥", "Math Machine", "Solve 50 questions"))

    if streak >= 5:
        items.append(("🔥", "Hot Streak", "Reach a 5 combo"))

    if streak >= 10:
        items.append(("💥", "Unstoppable", "Reach a 10 combo"))

    if score >= 100:
        items.append(("🏆", "Century", "Score 100 points"))

    if score >= 500:
        items.append(("👑", "Arena King", "Score 500 points"))

    if games >= 10:
        items.append(("🎮", "Regular", "Play 10 games"))

    return items


# ============================================================
# SOUND SYSTEM
# ============================================================

def play_sound(kind="correct"):

    frequencies = {
        "correct": [520, 660, 880],
        "wrong": [220, 160],
        "level": [440, 660, 880, 1100],
        "click": [400]
    }

    freq_list = frequencies.get(kind, [400])

    notes = ",".join(str(x) for x in freq_list)

    components_html = f"""
    <script>
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    const ctx = new AudioContext();

    const notes = [{notes}];

    notes.forEach((freq, index) => {{
        setTimeout(() => {{
            const oscillator = ctx.createOscillator();
            const gain = ctx.createGain();

            oscillator.frequency.value = freq;
            oscillator.type = "sine";

            gain.gain.setValueAtTime(0.0001, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(
                0.15,
                ctx.currentTime + 0.01
            );

            gain.gain.exponentialRampToValueAtTime(
                0.0001,
                ctx.currentTime + 0.18
            );

            oscillator.connect(gain);
            gain.connect(ctx.destination);

            oscillator.start();
            oscillator.stop(ctx.currentTime + 0.2);
        }}, index * 90);
    }});
    </script>
    """

    components.html(components_html, height=0)


# ============================================================
# PREMIUM CSS
# ============================================================

def inject_css():

    st.markdown("""
    <style>

    /* =====================================================
       GLOBAL
    ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0, 242, 255, 0.08),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 90%,
                rgba(124, 58, 237, 0.10),
                transparent 30%
            ),
            #05070b;
        color: #f5f7ff;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }

    /* =====================================================
       HEADER
    ===================================================== */

    .arena-header {
        padding: 22px 25px;
        border: 1px solid rgba(0,242,255,0.18);
        border-radius: 22px;
        background:
            linear-gradient(
                135deg,
                rgba(10,15,25,0.96),
                rgba(7,10,17,0.88)
            );
        box-shadow:
            0 0 40px rgba(0,242,255,0.07),
            inset 0 0 25px rgba(255,255,255,0.02);
        margin-bottom: 20px;
    }

    .brand {
        font-size: 34px;
        font-weight: 900;
        letter-spacing: 2px;
        background:
            linear-gradient(
                90deg,
                #00f2ff,
                #8b5cf6,
                #00f2ff
            );
        -webkit-background-clip: text;
        color: transparent;
    }

    .tagline {
        color: #8c98ad;
        margin-top: 3px;
        font-size: 14px;
        letter-spacing: 1px;
    }

    /* =====================================================
       CARDS
    ===================================================== */

    .glass-card {
        background:
            linear-gradient(
                145deg,
                rgba(16,23,36,0.96),
                rgba(7,10,17,0.96)
            );
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 20px;
        padding: 22px;
        box-shadow:
            0 20px 60px rgba(0,0,0,0.25),
            inset 0 0 30px rgba(255,255,255,0.015);
    }

    .stat-card {
        background: rgba(12,17,28,0.92);
        border: 1px solid rgba(0,242,255,0.12);
        border-radius: 17px;
        padding: 17px;
        margin-bottom: 12px;
    }

    .stat-title {
        color: #7e8ba3;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1.4px;
    }

    .stat-value {
        font-size: 27px;
        font-weight: 800;
        margin-top: 4px;
    }

    /* =====================================================
       QUESTION
    ===================================================== */

    .question-card {
        min-height: 330px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        background:
            radial-gradient(
                circle at center,
                rgba(0,242,255,0.10),
                transparent 45%
            ),
            linear-gradient(
                145deg,
                #0d1522,
                #060910
            );

        border: 1px solid rgba(0,242,255,0.20);
        border-radius: 25px;

        box-shadow:
            0 0 60px rgba(0,242,255,0.08),
            inset 0 0 50px rgba(0,242,255,0.025);
    }

    .question-category {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #00f2ff;
        margin-bottom: 18px;
    }

    .question-text {
        font-size: clamp(35px, 6vw, 70px);
        font-weight: 900;
        letter-spacing: 2px;
        text-align: center;
        color: white;
        text-shadow:
            0 0 25px rgba(0,242,255,0.18);
    }

    .combo {
        font-size: 17px;
        color: #ffb703;
        font-weight: 800;
        margin-top: 18px;
    }

    /* =====================================================
       BUTTONS
    ===================================================== */

    .stButton > button {
        border-radius: 13px !important;
        border: 1px solid rgba(0,242,255,0.22) !important;
        background:
            linear-gradient(
                135deg,
                rgba(0,242,255,0.12),
                rgba(124,58,237,0.14)
            ) !important;
        color: white !important;
        font-weight: 800 !important;
        min-height: 45px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #00f2ff !important;
        box-shadow:
            0 0 20px rgba(0,242,255,0.15);
        transform: translateY(-1px);
    }

    /* =====================================================
       INPUT
    ===================================================== */

    .stNumberInput input,
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] {
        background: #090e17 !important;
        color: white !important;
        border-radius: 12px !important;
    }

    /* =====================================================
       PROGRESS
    ===================================================== */

    .progress-wrap {
        background: #111827;
        border-radius: 100px;
        height: 9px;
        overflow: hidden;
        margin-top: 8px;
    }

    .progress-bar {
        height: 100%;
        background:
            linear-gradient(
                90deg,
                #00f2ff,
                #8b5cf6
            );
        border-radius: 100px;
        transition: width .4s ease;
    }

    /* =====================================================
       BADGES
    ===================================================== */

    .badge {
        display: inline-block;
        padding: 6px 10px;
        margin: 3px;
        border-radius: 999px;
        background: rgba(0,242,255,0.08);
        border: 1px solid rgba(0,242,255,0.15);
        font-size: 12px;
    }

    /* =====================================================
       MOBILE
    ===================================================== */

    @media(max-width: 800px) {

        .brand {
            font-size: 25px;
        }

        .question-card {
            min-height: 250px;
        }

        .question-text {
            font-size: 40px;
        }
    }

    </style>
    """, unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

def initialize_state():

    defaults = {
        "screen": "home",
        "username": "Player",
        "mode": "Solo",
        "difficulty": "Medium",

        "question": "",
        "answer": 0,
        "category": "",

        "score": 0,
        "correct": 0,
        "wrong": 0,

        "streak": 0,
        "best_streak": 0,

        "lives": 4,

        "round": 0,
        "start_time": None,

        "last_result": None,
        "last_answer": None,

        "xp_session": 0,
        "coins_session": 0,

        "p2_score": 0,
        "p2_lives": 4,

        "game_finished": False,

        "daily_seed": str(date.today())
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# ============================================================
# NEW ROUND
# ============================================================

def new_question():

    q, ans, category = make_question(
        st.session_state.difficulty
    )

    st.session_state.question = q
    st.session_state.answer = ans
    st.session_state.category = category

    st.session_state.start_time = time.time()
    st.session_state.last_result = None
    st.session_state.last_answer = None


# ============================================================
# START GAME
# ============================================================

def start_game():

    settings = DIFFICULTIES[
        st.session_state.difficulty
    ]

    st.session_state.screen = "game"

    st.session_state.score = 0
    st.session_state.correct = 0
    st.session_state.wrong = 0

    st.session_state.streak = 0
    st.session_state.best_streak = 0

    st.session_state.lives = settings["lives"]

    st.session_state.round = 0

    st.session_state.p2_score = 0
    st.session_state.p2_lives = settings["lives"]

    st.session_state.xp_session = 0
    st.session_state.coins_session = 0

    st.session_state.game_finished = False

    ensure_player(
        st.session_state.username
    )

    new_question()


# ============================================================
# FINISH GAME
# ============================================================

def finish_game():

    if st.session_state.game_finished:
        return

    st.session_state.game_finished = True

    save_match(
        username=st.session_state.username,
        mode=st.session_state.mode,
        difficulty=st.session_state.difficulty,
        score=st.session_state.score,
        correct=st.session_state.correct,
        wrong=st.session_state.wrong,
        best_streak=st.session_state.best_streak,
        won=True
    )


# ============================================================
# ANSWER PROCESSING
# ============================================================

def submit_answer(user_answer):

    try:
        user_answer = int(user_answer)
    except:
        user_answer = None

    correct = (
        user_answer is not None
        and user_answer == st.session_state.answer
    )

    settings = DIFFICULTIES[
        st.session_state.difficulty
    ]

    st.session_state.last_answer = user_answer
    st.session_state.round += 1

    if correct:

        st.session_state.correct += 1
        st.session_state.streak += 1

        st.session_state.best_streak = max(
            st.session_state.best_streak,
            st.session_state.streak
        )

        combo_multiplier = min(
            1 + (st.session_state.streak // 5) * 0.25,
            3
        )

        points = int(
            settings["base_xp"] * combo_multiplier
        )

        coins = max(
            1,
            int(settings["base_coins"] * combo_multiplier)
        )

        st.session_state.score += points
        st.session_state.xp_session += points
        st.session_state.coins_session += coins

        st.session_state.last_result = "correct"

        play_sound("correct")

    else:

        st.session_state.wrong += 1
        st.session_state.streak = 0

        st.session_state.lives -= 1

        st.session_state.last_result = "wrong"

        play_sound("wrong")

        if st.session_state.lives <= 0:
            finish_game()
            return

    # Two-player turn
    if st.session_state.mode == "2 Players":

        st.session_state.active_player = (
            "P2"
            if st.session_state.get("active_player", "P1") == "P1"
            else "P1"
        )

    new_question()


# ============================================================
# HEADER
# ============================================================

def render_header():

    st.markdown("""
    <div class="arena-header">
        <div class="brand">
            ⚡ MATHS ARENA PRO
        </div>

        <div class="tagline">
            THINK FAST • SOLVE FASTER • MASTER MATHEMATICS
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HOME
# ============================================================

def render_home():

    col1, col2 = st.columns(
        [1.7, 1],
        gap="large"
    )

    with col1:

        st.markdown("""
        <div class="glass-card">

        <div style="
            font-size:15px;
            color:#00f2ff;
            font-weight:800;
            letter-spacing:2px;
        ">
        THE DIGITAL MATH ARENA
        </div>

        <h1 style="
            font-size:48px;
            margin-top:8px;
            margin-bottom:5px;
        ">
        How fast can you think?
        </h1>

        <p style="
            color:#8c98ad;
            font-size:17px;
            line-height:1.7;
        ">
        Enter the arena, solve mathematical challenges,
        build your combo, earn XP and push your personal
        high score.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        username = st.text_input(
            "PLAYER NAME",
            value=st.session_state.username,
            max_chars=20
        )

        st.session_state.username = (
            username.strip()
            if username.strip()
            else "Player"
        )

        mode = st.selectbox(
            "GAME MODE",
            ["Solo", "2 Players"]
        )

        difficulty = st.selectbox(
            "DIFFICULTY",
            list(DIFFICULTIES.keys()),
            index=1
        )

        st.session_state.mode = mode
        st.session_state.difficulty = difficulty

        st.write("")

        if st.button(
            "⚡ ENTER THE ARENA",
            use_container_width=True
        ):

            start_game()
            st.rerun()

        st.write("")

        st.markdown("""
        <div style="
            display:flex;
            gap:8px;
            flex-wrap:wrap;
        ">
            <span class="badge">🔥 COMBOS</span>
            <span class="badge">⚡ XP SYSTEM</span>
            <span class="badge">🏆 ACHIEVEMENTS</span>
            <span class="badge">💰 COINS</span>
            <span class="badge">👥 2 PLAYER</span>
            <span class="badge">♾️ ENDLESS</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        player = get_player(
            st.session_state.username
        )

        if player:

            (
                name,
                xp,
                coins,
                games,
                wins,
                correct,
                wrong,
                best_streak,
                best_score
            ) = player

            level = calculate_level(xp)

            st.markdown(
                f"""
                <div class="glass-card">

                    <div class="stat-title">
                    PLAYER PROFILE
                    </div>

                    <h2 style="margin-bottom:0;">
                    {name}
                    </h2>

                    <div style="
                        color:#00f2ff;
                        font-size:14px;
                        margin-bottom:20px;
                    ">
                    LEVEL {level}
                    </div>

                    <div class="stat-card">
                        <div class="stat-title">XP</div>
                        <div class="stat-value">{xp:,}</div>
                    </div>

                    <div class="stat-card">
                        <div class="stat-title">COINS</div>
                        <div class="stat-value">🪙 {coins:,}</div>
                    </div>

                    <div class="stat-card">
                        <div class="stat-title">BEST SCORE</div>
                        <div class="stat-value">{best_score:,}</div>
                    </div>

                    <div class="stat-card">
                        <div class="stat-title">BEST COMBO</div>
                        <div class="stat-value">🔥 {best_streak}</div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# GAME
# ============================================================

def render_game():

    settings = DIFFICULTIES[
        st.session_state.difficulty
    ]

    # --------------------------------------------------------
    # GAME OVER
    # --------------------------------------------------------

    if st.session_state.game_finished:

        st.markdown("""
        <div class="question-card">

            <div class="question-category">
            ARENA COMPLETE
            </div>

            <div class="question-text">
            🏆 GAME OVER
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        cols = st.columns(4)

        stats = [
            ("SCORE", st.session_state.score),
            ("CORRECT", st.session_state.correct),
            ("BEST COMBO", st.session_state.best_streak),
            ("XP EARNED", st.session_state.xp_session),
        ]

        for col, (label, value) in zip(cols, stats):

            with col:

                st.markdown(
                    f"""
                    <div class="stat-card"
                         style="text-align:center;">

                        <div class="stat-title">
                        {label}
                        </div>

                        <div class="stat-value">
                        {value}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🔄 PLAY AGAIN",
                use_container_width=True
            ):

                start_game()
                st.rerun()

        with col2:

            if st.button(
                "🏠 MAIN MENU",
                use_container_width=True
            ):

                st.session_state.screen = "home"
                st.rerun()

        return

    # --------------------------------------------------------
    # TOP GAME BAR
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">SCORE</div>
                <div class="stat-value">
                    {st.session_state.score}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">COMBO</div>
                <div class="stat-value">
                    🔥 {st.session_state.streak}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        hearts = "❤️" * st.session_state.lives

        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">LIVES</div>
                <div class="stat-value">
                    {hearts if hearts else "💀"}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">ROUND</div>
                <div class="stat-value">
                    {st.session_state.round}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    combo_text = ""

    if st.session_state.streak >= 3:
        combo_text = (
            f"🔥 {st.session_state.streak}× COMBO"
        )

    st.markdown(
        f"""
        <div class="question-card">

            <div class="question-category">
            {st.session_state.category}
            </div>

            <div class="question-text">
            {st.session_state.question}
            </div>

            <div class="combo">
            {combo_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # RESULT MESSAGE
    # --------------------------------------------------------

    if st.session_state.last_result == "correct":

        st.success(
            f"⚡ CORRECT! +XP • Combo: "
            f"{st.session_state.streak}"
        )

    elif st.session_state.last_result == "wrong":

        st.error(
            f"❌ Incorrect. Correct answer: "
            f"{st.session_state.answer}"
        )

    # --------------------------------------------------------
    # ANSWER
    # --------------------------------------------------------

    with st.form(
        "answer_form",
        clear_on_submit=True
    ):

        answer = st.number_input(
            "YOUR ANSWER",
            step=1,
            value=0
        )

        submitted = st.form_submit_button(
            "⚡ SUBMIT ANSWER",
            use_container_width=True
        )

        if submitted:

            submit_answer(answer)

            st.rerun()

    # --------------------------------------------------------
    # GAME INFO
    # --------------------------------------------------------

    st.caption(
        f"Mode: {st.session_state.mode}  •  "
        f"Difficulty: {st.session_state.difficulty}  •  "
        f"Target: Endless"
    )

    if st.button(
        "🏳️ END MATCH",
        use_container_width=True
    ):

        finish_game()
        st.rerun()


# ============================================================
# PROFILE
# ============================================================

def render_profile():

    ensure_player(
        st.session_state.username
    )

    player = get_player(
        st.session_state.username
    )

    if not player:
        return

    (
        username,
        xp,
        coins,
        games,
        wins,
        correct,
        wrong,
        best_streak,
        best_score
    ) = player

    level = calculate_level(xp)
    progress = level_progress(xp)

    st.markdown(
        f"""
        <div class="glass-card">

            <div class="question-category">
            PLAYER PROFILE
            </div>

            <h1>
            {username}
            </h1>

            <div style="
                font-size:20px;
                color:#00f2ff;
                font-weight:800;
            ">
            LEVEL {level}
            </div>

            <br>

            <div class="progress-wrap">
                <div class="progress-bar"
                     style="width:{progress * 100}%;">
                </div>
            </div>

            <p style="color:#8c98ad;">
            {xp} XP
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    cols = st.columns(4)

    profile_stats = [
        ("🎮 GAMES", games),
        ("🎯 CORRECT", correct),
        ("🔥 BEST COMBO", best_streak),
        ("🏆 BEST SCORE", best_score)
    ]

    for col, (title, value) in zip(
        cols,
        profile_stats
    ):

        with col:

            st.markdown(
                f"""
                <div class="stat-card"
                     style="text-align:center;">

                    <div class="stat-title">
                    {title}
                    </div>

                    <div class="stat-value">
                    {value:,}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    st.subheader("🏅 Achievements")

    unlocked = achievements(
        correct,
        best_streak,
        best_score,
        games
    )

    if unlocked:

        for icon, name, description in unlocked:

            st.markdown(
                f"""
                <div class="stat-card">

                    <span style="font-size:25px;">
                    {icon}
                    </span>

                    <b>{name}</b>

                    <span style="color:#8c98ad;">
                    — {description}
                    </span>

                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "Play your first match to unlock achievements."
        )


# ============================================================
# LEADERBOARD
# ============================================================

def render_leaderboard():

    st.subheader("🏆 GLOBAL ARENA")

    leaderboard = get_leaderboard()

    if not leaderboard:

        st.info(
            "No players yet. Be the first one!"
        )
        return

    for index, row in enumerate(
        leaderboard,
        start=1
    ):

        (
            username,
            xp,
            coins,
            games,
            wins,
            correct,
            best_streak,
            best_score
        ) = row

        if index == 1:
            icon = "👑"
        elif index == 2:
            icon = "🥈"
        elif index == 3:
            icon = "🥉"
        else:
            icon = f"#{index}"

        st.markdown(
            f"""
            <div class="stat-card"
                 style="
                    display:flex;
                    align-items:center;
                    justify-content:space-between;
                 ">

                <div>

                    <span style="
                        font-size:20px;
                        font-weight:900;
                    ">
                    {icon}
                    </span>

                    <span style="
                        margin-left:12px;
                        font-weight:800;
                    ">
                    {username}
                    </span>

                </div>

                <div style="
                    color:#00f2ff;
                    font-weight:900;
                ">
                {xp:,} XP
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# HISTORY
# ============================================================

def render_history():

    history = get_history(
        st.session_state.username
    )

    st.subheader("📜 MATCH HISTORY")

    if not history:

        st.info(
            "No matches recorded yet."
        )
        return

    for row in history:

        (
            mode,
            difficulty,
            score,
            correct,
            wrong,
            streak,
            played_at
        ) = row

        try:
            formatted_time = datetime.fromisoformat(
                played_at
            ).strftime("%d %b %Y • %H:%M")
        except:
            formatted_time = played_at

        st.markdown(
            f"""
            <div class="stat-card">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    gap:10px;
                    flex-wrap:wrap;
                ">

                    <b>
                    {mode} • {difficulty}
                    </b>

                    <b style="color:#00f2ff;">
                    {score} XP
                    </b>

                </div>

                <div style="
                    color:#8c98ad;
                    margin-top:8px;
                ">

                🎯 {correct} correct
                &nbsp; • &nbsp;
                ❌ {wrong} wrong
                &nbsp; • &nbsp;
                🔥 {streak} combo
                &nbsp; • &nbsp;
                {formatted_time}

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# NAVIGATION
# ============================================================

def render_navigation():

    if st.session_state.screen == "game":
        return

    st.write("")

    cols = st.columns(3)

    with cols[0]:

        if st.button(
            "🏠 HOME",
            use_container_width=True
        ):

            st.session_state.screen = "home"
            st.rerun()

    with cols[1]:

        if st.button(
            "👤 PROFILE",
            use_container_width=True
        ):

            st.session_state.screen = "profile"
            st.rerun()

    with cols[2]:

        if st.button(
            "🏆 LEADERBOARD",
            use_container_width=True
        ):

            st.session_state.screen = "leaderboard"
            st.rerun()


# ============================================================
# MAIN
# ============================================================

def main():

    init_db()
    initialize_state()
    inject_css()

    render_header()

    if st.session_state.screen == "home":

        render_home()

        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            render_leaderboard()

        with col2:
            render_history()

    elif st.session_state.screen == "game":

        render_game()

    elif st.session_state.screen == "profile":

        render_profile()

        render_navigation()

    elif st.session_state.screen == "leaderboard":

        render_leaderboard()

        render_navigation()


if __name__ == "__main__":
    main()
