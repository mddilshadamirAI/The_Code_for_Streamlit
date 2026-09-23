import streamlit as st
import sqlite3
import random
import math
from datetime import datetime

# ============================================================
# MATHS ARENA PRO
# Single-file edition
# No API
# No JavaScript
# No sound
# No external database
# ============================================================

st.set_page_config(
    page_title="Maths Arena PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

DB_FILE = "maths_arena.db"


# ============================================================
# DATABASE
# ============================================================

def db():
    return sqlite3.connect(DB_FILE)


def init_database():
    conn = db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            username TEXT PRIMARY KEY,
            xp INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0,
            games INTEGER DEFAULT 0,
            correct INTEGER DEFAULT 0,
            wrong INTEGER DEFAULT 0,
            best_score INTEGER DEFAULT 0,
            best_streak INTEGER DEFAULT 0,
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
            streak INTEGER,
            played_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def ensure_player(username):
    conn = db()
    cur = conn.cursor()

    cur.execute(
        "SELECT username FROM players WHERE username=?",
        (username,)
    )

    if cur.fetchone() is None:
        cur.execute("""
            INSERT INTO players
            (username, xp, coins, games, correct, wrong,
             best_score, best_streak, created_at)
            VALUES (?, 0, 0, 0, 0, 0, 0, 0, ?)
        """, (
            username,
            datetime.now().isoformat()
        ))

    conn.commit()
    conn.close()


def get_player(username):
    conn = db()
    cur = conn.cursor()

    cur.execute("""
        SELECT username, xp, coins, games, correct, wrong,
               best_score, best_streak
        FROM players
        WHERE username=?
    """, (username,))

    result = cur.fetchone()

    conn.close()
    return result


def save_match(
    username,
    mode,
    difficulty,
    score,
    correct,
    wrong,
    streak
):
    conn = db()
    cur = conn.cursor()

    xp_gain = max(score, 0)
    coins_gain = max(score // 10, 1)

    cur.execute("""
        UPDATE players
        SET
            xp = xp + ?,
            coins = coins + ?,
            games = games + 1,
            correct = correct + ?,
            wrong = wrong + ?,
            best_score =
                CASE
                    WHEN ? > best_score THEN ?
                    ELSE best_score
                END,
            best_streak =
                CASE
                    WHEN ? > best_streak THEN ?
                    ELSE best_streak
                END
        WHERE username=?
    """, (
        xp_gain,
        coins_gain,
        correct,
        wrong,
        score,
        score,
        streak,
        streak,
        username
    ))

    cur.execute("""
        INSERT INTO matches
        (
            username,
            mode,
            difficulty,
            score,
            correct,
            wrong,
            streak,
            played_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        username,
        mode,
        difficulty,
        score,
        correct,
        wrong,
        streak,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def leaderboard():
    conn = db()
    cur = conn.cursor()

    cur.execute("""
        SELECT username, xp, best_score, best_streak
        FROM players
        ORDER BY xp DESC
        LIMIT 10
    """)

    data = cur.fetchall()

    conn.close()

    return data


def history(username):
    conn = db()
    cur = conn.cursor()

    cur.execute("""
        SELECT mode, difficulty, score,
               correct, wrong, streak, played_at
        FROM matches
        WHERE username=?
        ORDER BY id DESC
        LIMIT 10
    """, (username,))

    data = cur.fetchall()

    conn.close()

    return data


# ============================================================
# DIFFICULTY
# ============================================================

DIFFICULTY = {
    "Basic": {
        "lives": 5,
        "points": 10,
    },
    "Medium": {
        "lives": 4,
        "points": 15,
    },
    "Pro": {
        "lives": 3,
        "points": 25,
    },
    "Master": {
        "lives": 3,
        "points": 40,
    },
}


# ============================================================
# QUESTION ENGINE
# ============================================================

def generate_question(level):
    """
    Returns:
        question_text,
        answer,
        category,
        explanation
    """

    # --------------------------------------------------------
    # BASIC
    # --------------------------------------------------------

    if level == "Basic":

        category = random.choice([
            "Addition",
            "Subtraction",
            "Multiplication",
        ])

        if category == "Addition":
            a = random.randint(10, 99)
            b = random.randint(10, 99)

            answer = a + b

            return (
                f"What is {a} + {b}?",
                answer,
                category,
                f"{a} + {b} = {answer}"
            )

        if category == "Subtraction":
            a = random.randint(30, 120)
            b = random.randint(5, a)

            answer = a - b

            return (
                f"What is {a} − {b}?",
                answer,
                category,
                f"{a} − {b} = {answer}"
            )

        a = random.randint(2, 15)
        b = random.randint(2, 12)

        answer = a * b

        return (
            f"What is {a} × {b}?",
            answer,
            category,
            f"{a} × {b} = {answer}"
        )

    # --------------------------------------------------------
    # MEDIUM
    # --------------------------------------------------------

    if level == "Medium":

        category = random.choice([
            "Division",
            "Squares",
            "Mixed Operations",
            "Multiplication",
        ])

        if category == "Division":

            divisor = random.randint(2, 12)
            answer = random.randint(3, 20)
            dividend = divisor * answer

            return (
                f"What is {dividend} ÷ {divisor}?",
                answer,
                category,
                f"{dividend} ÷ {divisor} = {answer}"
            )

        if category == "Squares":

            a = random.randint(5, 25)
            answer = a * a

            return (
                f"What is {a}²?",
                answer,
                category,
                f"{a} × {a} = {answer}"
            )

        if category == "Multiplication":

            a = random.randint(8, 25)
            b = random.randint(5, 15)

            answer = a * b

            return (
                f"What is {a} × {b}?",
                answer,
                category,
                f"{a} × {b} = {answer}"
            )

        a = random.randint(3, 15)
        b = random.randint(2, 12)
        c = random.randint(2, 20)

        if random.choice([True, False]):
            answer = a * b + c

            return (
                f"What is ({a} × {b}) + {c}?",
                answer,
                category,
                f"({a} × {b}) + {c} = {answer}"
            )

        answer = a * b - c

        return (
            f"What is ({a} × {b}) − {c}?",
            answer,
            category,
            f"({a} × {b}) − {c} = {answer}"
        )

    # --------------------------------------------------------
    # PRO
    # --------------------------------------------------------

    if level == "Pro":

        category = random.choice([
            "Percentage",
            "Powers",
            "Order of Operations",
            "Square Root",
        ])

        if category == "Percentage":

            percentage = random.choice([
                10, 20, 25, 50
            ])

            number = random.choice([
                40, 60, 80, 100,
                120, 200, 300
            ])

            answer = percentage * number // 100

            return (
                f"What is {percentage}% of {number}?",
                answer,
                category,
                f"{percentage}% of {number} = {answer}"
            )

        if category == "Powers":

            base = random.randint(2, 10)
            power = random.choice([2, 3])

            answer = base ** power

            return (
                f"What is {base}^{power}?",
                answer,
                category,
                f"{base}^{power} = {answer}"
            )

        if category == "Square Root":

            number = random.randint(2, 15)
            square = number * number

            return (
                f"What is √{square}?",
                number,
                category,
                f"√{square} = {number}"
            )

        a = random.randint(2, 15)
        b = random.randint(2, 10)
        c = random.randint(1, 15)

        answer = a + b * c

        return (
            f"What is {a} + ({b} × {c})?",
            answer,
            category,
            f"{a} + ({b} × {c}) = {answer}"
        )

    # --------------------------------------------------------
    # MASTER
    # --------------------------------------------------------

    category = random.choice([
        "Advanced Arithmetic",
        "Powers",
        "Roots",
        "Mixed Challenge",
    ])

    if category == "Powers":

        base = random.randint(3, 12)
        power = random.choice([2, 3])

        answer = base ** power

        return (
            f"Calculate {base}^{power}",
            answer,
            category,
            f"{base}^{power} = {answer}"
        )

    if category == "Roots":

        number = random.randint(4, 20)
        square = number * number

        return (
            f"Calculate √{square}",
            number,
            category,
            f"√{square} = {number}"
        )

    if category == "Advanced Arithmetic":

        a = random.randint(10, 40)
        b = random.randint(5, 20)
        c = random.randint(2, 10)

        answer = (a + b) * c

        return (
            f"Calculate ({a} + {b}) × {c}",
            answer,
            category,
            f"({a} + {b}) × {c} = {answer}"
        )

    a = random.randint(3, 15)
    b = random.randint(2, 10)
    c = random.randint(2, 8)
    d = random.randint(1, 15)

    answer = (a * b) + (c * d)

    return (
        f"Calculate ({a} × {b}) + ({c} × {d})",
        answer,
        category,
        f"({a} × {b}) + ({c} × {d}) = {answer}"
    )


# ============================================================
# LEVEL SYSTEM
# ============================================================

def get_level(xp):
    return max(1, int(math.sqrt(xp / 50)) + 1)


def level_progress(xp):

    level = get_level(xp)

    previous = (level - 1) ** 2 * 50
    target = level ** 2 * 50

    if target <= previous:
        return 0

    return min(
        1,
        max(
            0,
            (xp - previous) / (target - previous)
        )
    )


# ============================================================
# SESSION STATE
# ============================================================

def initialize_state():

    defaults = {
        "page": "home",

        "username": "Player",

        "mode": "Solo",

        "difficulty": "Medium",

        "question": "",

        "answer": 0,

        "category": "",

        "explanation": "",

        "score": 0,

        "correct": 0,

        "wrong": 0,

        "streak": 0,

        "best_streak": 0,

        "lives": 4,

        "round": 0,

        "game_over": False,

        "last_result": None,

        "last_answer": None,

        "xp_earned": 0,

        "coins_earned": 0,

        "question_number": 0,

    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value


# ============================================================
# NEW QUESTION
# ============================================================

def next_question():

    (
        question,
        answer,
        category,
        explanation
    ) = generate_question(
        st.session_state.difficulty
    )

    st.session_state.question = question
    st.session_state.answer = answer
    st.session_state.category = category
    st.session_state.explanation = explanation

    st.session_state.last_result = None
    st.session_state.last_answer = None

    st.session_state.question_number += 1


# ============================================================
# START GAME
# ============================================================

def start_game():

    settings = DIFFICULTY[
        st.session_state.difficulty
    ]

    ensure_player(
        st.session_state.username
    )

    st.session_state.score = 0
    st.session_state.correct = 0
    st.session_state.wrong = 0

    st.session_state.streak = 0
    st.session_state.best_streak = 0

    st.session_state.lives = settings["lives"]

    st.session_state.round = 0
    st.session_state.question_number = 0

    st.session_state.xp_earned = 0
    st.session_state.coins_earned = 0

    st.session_state.game_over = False

    st.session_state.page = "game"

    next_question()


# ============================================================
# END GAME
# ============================================================

def end_game():

    if st.session_state.game_over:
        return

    st.session_state.game_over = True

    save_match(
        st.session_state.username,
        st.session_state.mode,
        st.session_state.difficulty,
        st.session_state.score,
        st.session_state.correct,
        st.session_state.wrong,
        st.session_state.best_streak
    )


# ============================================================
# ANSWER
# ============================================================

def check_answer(user_answer):

    try:
        user_answer = int(user_answer)
    except:
        user_answer = None

    correct = (
        user_answer is not None
        and user_answer == st.session_state.answer
    )

    st.session_state.last_answer = user_answer
    st.session_state.round += 1

    settings = DIFFICULTY[
        st.session_state.difficulty
    ]

    if correct:

        st.session_state.correct += 1
        st.session_state.streak += 1

        st.session_state.best_streak = max(
            st.session_state.best_streak,
            st.session_state.streak
        )

        # Combo multiplier
        multiplier = 1

        if st.session_state.streak >= 5:
            multiplier = 1.5

        if st.session_state.streak >= 10:
            multiplier = 2

        if st.session_state.streak >= 20:
            multiplier = 3

        points = int(
            settings["points"] * multiplier
        )

        coins = max(
            1,
            points // 10
        )

        st.session_state.score += points
        st.session_state.xp_earned += points
        st.session_state.coins_earned += coins

        st.session_state.last_result = "correct"

    else:

        st.session_state.wrong += 1

        st.session_state.streak = 0

        st.session_state.lives -= 1

        st.session_state.last_result = "wrong"

        if st.session_state.lives <= 0:
            end_game()
            return

    next_question()


# ============================================================
# CSS
# ============================================================

def css():

    st.markdown("""
    <style>

    /* ================================================
       APP
    ================================================ */

    .stApp {
        background:
            radial-gradient(
                circle at 0% 0%,
                rgba(0, 229, 255, 0.09),
                transparent 30%
            ),
            radial-gradient(
                circle at 100% 100%,
                rgba(124, 58, 237, 0.10),
                transparent 30%
            ),
            #05070c;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 25px;
        padding-bottom: 60px;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* ================================================
       HEADER
    ================================================ */

    .hero {
        padding: 28px;
        border-radius: 24px;
        border: 1px solid rgba(0, 229, 255, .15);

        background:
            linear-gradient(
                135deg,
                rgba(15, 23, 42, .96),
                rgba(5, 10, 18, .96)
            );

        box-shadow:
            0 20px 80px rgba(0,0,0,.35);

        margin-bottom: 22px;
    }

    .logo {
        font-size: 36px;
        font-weight: 950;
        letter-spacing: 2px;

        background:
            linear-gradient(
                90deg,
                #00e5ff,
                #7c3aed,
                #00e5ff
            );

        -webkit-background-clip: text;
        color: transparent;
    }

    .tagline {
        color: #8793a8;
        margin-top: 4px;
        font-size: 13px;
        letter-spacing: 2px;
    }

    /* ================================================
       CARDS
    ================================================ */

    .card {
        background:
            linear-gradient(
                145deg,
                rgba(15, 23, 42, .96),
                rgba(6, 10, 18, .96)
            );

        border: 1px solid rgba(255,255,255,.07);

        border-radius: 22px;

        padding: 24px;

        box-shadow:
            0 18px 55px rgba(0,0,0,.28);
    }

    .mini-card {
        background: rgba(10,15,25,.9);

        border: 1px solid rgba(0,229,255,.10);

        border-radius: 16px;

        padding: 17px;

        text-align: center;
    }

    .mini-label {
        font-size: 11px;
        letter-spacing: 1.5px;
        color: #748096;
        font-weight: 700;
    }

    .mini-value {
        font-size: 27px;
        font-weight: 900;
        margin-top: 4px;
    }

    /* ================================================
       QUESTION
    ================================================ */

    .question-box {
        min-height: 330px;

        display: flex;
        flex-direction: column;

        justify-content: center;
        align-items: center;

        text-align: center;

        border-radius: 28px;

        background:
            radial-gradient(
                circle at center,
                rgba(0,229,255,.11),
                transparent 42%
            ),
            linear-gradient(
                145deg,
                #0d1726,
                #050910
            );

        border: 1px solid rgba(0,229,255,.20);

        box-shadow:
            inset 0 0 80px rgba(0,229,255,.025),
            0 25px 70px rgba(0,0,0,.35);

        margin-bottom: 20px;
    }

    .question-category {
        color: #00e5ff;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 18px;
    }

    .question {
        color: #ffffff;
        font-size: clamp(30px, 5vw, 65px);
        font-weight: 950;
        letter-spacing: 1px;
        line-height: 1.2;
    }

    .combo-text {
        margin-top: 20px;
        color: #ffb703;
        font-size: 18px;
        font-weight: 900;
    }

    /* ================================================
       RESULT
    ================================================ */

    .correct-box {
        padding: 14px 18px;
        border-radius: 14px;
        background: rgba(34,197,94,.09);
        border: 1px solid rgba(34,197,94,.18);
        color: #86efac;
        font-weight: 800;
        margin-bottom: 15px;
    }

    .wrong-box {
        padding: 14px 18px;
        border-radius: 14px;
        background: rgba(239,68,68,.09);
        border: 1px solid rgba(239,68,68,.18);
        color: #fca5a5;
        font-weight: 800;
        margin-bottom: 15px;
    }

    /* ================================================
       BUTTONS
    ================================================ */

    .stButton > button {

        min-height: 48px;

        border-radius: 14px !important;

        border:
            1px solid
            rgba(0,229,255,.18) !important;

        background:
            linear-gradient(
                135deg,
                rgba(0,229,255,.10),
                rgba(124,58,237,.12)
            ) !important;

        color: white !important;

        font-weight: 850 !important;

        transition: .18s ease;
    }

    .stButton > button:hover {

        border-color:
            rgba(0,229,255,.65) !important;

        box-shadow:
            0 0 25px
            rgba(0,229,255,.12);

        transform: translateY(-1px);
    }

    /* ================================================
       INPUT
    ================================================ */

    .stNumberInput input,
    .stTextInput input {

        background:
            #080d16 !important;

        color:
            white !important;

        border-radius:
            13px !important;
    }

    /* ================================================
       DIVIDER
    ================================================ */

    hr {
        border-color:
            rgba(255,255,255,.06);
    }

    /* ================================================
       MOBILE
    ================================================ */

    @media(max-width: 800px) {

        .logo {
            font-size: 27px;
        }

        .hero {
            padding: 20px;
        }

        .question-box {
            min-height: 250px;
        }

        .question {
            font-size: 38px;
        }
    }

    </style>
    """, unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

def header():

    st.markdown("""
    <div class="hero">

        <div class="logo">
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

def home():

    left, right = st.columns(
        [1.55, 1],
        gap="large"
    )

    with left:

        st.markdown("""
        <div class="card">

            <div style="
                color:#00e5ff;
                font-size:12px;
                font-weight:900;
                letter-spacing:3px;
            ">
                WELCOME TO THE ARENA
            </div>

            <h1 style="
                font-size:44px;
                margin-top:10px;
            ">
                Train your brain.
            </h1>

            <p style="
                color:#8b97aa;
                font-size:16px;
                line-height:1.7;
            ">
                Solve increasingly challenging mathematics
                problems, build your streak, collect XP,
                unlock achievements and compete on the arena
                leaderboard.
            </p>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        username = st.text_input(
            "PLAYER NAME",
            value=st.session_state.username,
            max_chars=20
        )

        if username.strip():
            st.session_state.username = username.strip()

        col1, col2 = st.columns(2)

        with col1:

            st.session_state.mode = st.selectbox(
                "GAME MODE",
                ["Solo", "2 Players"]
            )

        with col2:

            st.session_state.difficulty = st.selectbox(
                "DIFFICULTY",
                list(DIFFICULTY.keys()),
                index=1
            )

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
            gap:7px;
            flex-wrap:wrap;
        ">

            <span class="mini-card">
                🔥 COMBO
            </span>

            <span class="mini-card">
                🏆 XP
            </span>

            <span class="mini-card">
                🪙 COINS
            </span>

            <span class="mini-card">
                🎯 ACHIEVEMENTS
            </span>

            <span class="mini-card">
                ♾️ ENDLESS
            </span>

        </div>
        """, unsafe_allow_html=True)

    with right:

        ensure_player(
            st.session_state.username
        )

        player = get_player(
            st.session_state.username
        )

        if player:

            (
                username,
                xp,
                coins,
                games,
                correct,
                wrong,
                best_score,
                best_streak
            ) = player

            level = get_level(xp)
            progress = level_progress(xp)

            st.markdown(
                f"""
                <div class="card">

                    <div class="question-category">
                    PLAYER PROFILE
                    </div>

                    <h2>
                    {username}
                    </h2>

                    <div style="
                        font-size:20px;
                        color:#00e5ff;
                        font-weight:900;
                    ">
                    LEVEL {level}
                    </div>

                    <br>

                    <div class="mini-card">
                        <div class="mini-label">
                        XP
                        </div>

                        <div class="mini-value">
                        {xp:,}
                        </div>
                    </div>

                    <br>

                    <div class="mini-card">
                        <div class="mini-label">
                        COINS
                        </div>

                        <div class="mini-value">
                        🪙 {coins:,}
                        </div>
                    </div>

                    <br>

                    <div class="mini-card">
                        <div class="mini-label">
                        BEST SCORE
                        </div>

                        <div class="mini-value">
                        {best_score:,}
                        </div>
                    </div>

                    <br>

                    <div class="mini-card">
                        <div class="mini-label">
                        BEST COMBO
                        </div>

                        <div class="mini-value">
                        🔥 {best_streak}
                        </div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# GAME
# ============================================================

def game():

    # --------------------------------------------------------
    # GAME OVER
    # --------------------------------------------------------

    if st.session_state.game_over:

        st.markdown("""
        <div class="question-box">

            <div class="question-category">
            ARENA COMPLETE
            </div>

            <div class="question">
            🏆 MATCH OVER
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        cols = st.columns(4)

        stats = [
            ("SCORE", st.session_state.score),
            ("CORRECT", st.session_state.correct),
            ("BEST COMBO", st.session_state.best_streak),
            ("XP EARNED", st.session_state.xp_earned),
        ]

        for col, (label, value) in zip(
            cols,
            stats
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="mini-card">

                        <div class="mini-label">
                        {label}
                        </div>

                        <div class="mini-value">
                        {value:,}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.write("")

        st.success(
            f"You earned {st.session_state.xp_earned} XP "
            f"and 🪙 {st.session_state.coins_earned} coins."
        )

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

                st.session_state.page = "home"
                st.rerun()

        return

    # --------------------------------------------------------
    # TOP STATS
    # --------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            f"""
            <div class="mini-card">

                <div class="mini-label">
                SCORE
                </div>

                <div class="mini-value">
                {st.session_state.score}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="mini-card">

                <div class="mini-label">
                COMBO
                </div>

                <div class="mini-value">
                🔥 {st.session_state.streak}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        hearts = (
            "❤️" * st.session_state.lives
            if st.session_state.lives > 0
            else "💀"
        )

        st.markdown(
            f"""
            <div class="mini-card">

                <div class="mini-label">
                LIVES
                </div>

                <div class="mini-value">
                {hearts}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        st.markdown(
            f"""
            <div class="mini-card">

                <div class="mini-label">
                ROUND
                </div>

                <div class="mini-value">
                {st.session_state.round}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    combo = ""

    if st.session_state.streak >= 3:
        combo = (
            f"🔥 {st.session_state.streak} COMBO"
        )

    st.markdown(
        f"""
        <div class="question-box">

            <div class="question-category">
            {st.session_state.category}
            </div>

            <div class="question">
            {st.session_state.question}
            </div>

            <div class="combo-text">
            {combo}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # LAST RESULT
    # --------------------------------------------------------

    if st.session_state.last_result == "correct":

        st.markdown(
            f"""
            <div class="correct-box">
                ⚡ CORRECT!
                &nbsp;&nbsp;
                +{DIFFICULTY[st.session_state.difficulty]["points"]}
                XP
                &nbsp;&nbsp; • &nbsp;&nbsp;
                🔥 COMBO {st.session_state.streak}
            </div>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state.last_result == "wrong":

        st.markdown(
            f"""
            <div class="wrong-box">
                ❌ NOT QUITE.
                &nbsp;&nbsp;
                Correct answer:
                {st.session_state.answer}
                &nbsp;&nbsp; • &nbsp;&nbsp;
                {st.session_state.explanation}
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # ANSWER INPUT
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

            check_answer(answer)

            st.rerun()

    st.caption(
        f"Mode: {st.session_state.mode}  •  "
        f"Difficulty: {st.session_state.difficulty}  •  "
        f"Question #{st.session_state.question_number}"
    )

    st.write("")

    if st.button(
        "🏳️ END MATCH",
        use_container_width=True
    ):

        end_game()
        st.rerun()


# ============================================================
# PROFILE
# ============================================================

def profile():

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
        correct,
        wrong,
        best_score,
        best_streak
    ) = player

    level = get_level(xp)
    progress = level_progress(xp)

    st.markdown(
        f"""
        <div class="card">

            <div class="question-category">
            PLAYER PROFILE
            </div>

            <h1>
            {username}
            </h1>

            <h3 style="color:#00e5ff;">
            LEVEL {level}
            </h3>

            <div style="
                width:100%;
                height:10px;
                background:#111827;
                border-radius:20px;
                overflow:hidden;
            ">

                <div style="
                    width:{progress * 100}%;
                    height:100%;
                    background:linear-gradient(
                        90deg,
                        #00e5ff,
                        #7c3aed
                    );
                ">
                </div>

            </div>

            <p style="color:#7d899c;">
            Progress toward Level {level + 1}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    cols = st.columns(4)

    values = [
        ("🎮 GAMES", games),
        ("🎯 CORRECT", correct),
        ("🔥 BEST COMBO", best_streak),
        ("🏆 BEST SCORE", best_score),
    ]

    for col, (title, value) in zip(
        cols,
        values
    ):

        with col:

            st.markdown(
                f"""
                <div class="mini-card">

                    <div class="mini-label">
                    {title}
                    </div>

                    <div class="mini-value">
                    {value:,}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    st.subheader("📊 Accuracy")

    total = correct + wrong

    accuracy = (
        (correct / total) * 100
        if total > 0
        else 0
    )

    st.progress(
        int(accuracy)
    )

    st.write(
        f"**{accuracy:.1f}%** accuracy"
    )


# ============================================================
# LEADERBOARD
# ============================================================

def show_leaderboard():

    st.subheader("🏆 ARENA LEADERBOARD")

    data = leaderboard()

    if not data:

        st.info(
            "No players yet. Become the first player!"
        )

        return

    for index, row in enumerate(
        data,
        start=1
    ):

        username, xp, best_score, best_streak = row

        if index == 1:
            rank = "👑"
        elif index == 2:
            rank = "🥈"
        elif index == 3:
            rank = "🥉"
        else:
            rank = f"#{index}"

        st.markdown(
            f"""
            <div class="mini-card"
                 style="
                    margin-bottom:10px;
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                 ">

                <div style="
                    font-size:16px;
                    font-weight:850;
                ">
                    {rank}&nbsp;&nbsp; {username}
                </div>

                <div style="
                    color:#00e5ff;
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

def show_history():

    st.subheader("📜 RECENT MATCHES")

    data = history(
        st.session_state.username
    )

    if not data:

        st.info(
            "Your match history will appear here."
        )

        return

    for row in data:

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

            formatted = datetime.fromisoformat(
                played_at
            ).strftime(
                "%d %b %Y • %H:%M"
            )

        except:

            formatted = played_at

        st.markdown(
            f"""
            <div class="mini-card"
                 style="
                    text-align:left;
                    margin-bottom:10px;
                 ">

                <b>
                {mode} • {difficulty}
                </b>

                <br>

                <span style="color:#7f8ba0;">
                🎯 {correct} correct
                &nbsp; • &nbsp;
                ❌ {wrong} wrong
                &nbsp; • &nbsp;
                🔥 {streak} combo
                &nbsp; • &nbsp;
                {formatted}
                </span>

                <br>

                <b style="color:#00e5ff;">
                {score} XP
                </b>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# NAVIGATION
# ============================================================

def navigation():

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button(
            "🏠 HOME",
            use_container_width=True
        ):

            st.session_state.page = "home"
            st.rerun()

    with c2:

        if st.button(
            "👤 PROFILE",
            use_container_width=True
        ):

            st.session_state.page = "profile"
            st.rerun()

    with c3:

        if st.button(
            "🏆 LEADERBOARD",
            use_container_width=True
        ):

            st.session_state.page = "leaderboard"
            st.rerun()


# ============================================================
# MAIN
# ============================================================

def main():

    init_database()
    initialize_state()
    css()
    header()

    page = st.session_state.page

    if page == "home":

        home()

        st.write("")

        left, right = st.columns(2)

        with left:
            show_leaderboard()

        with right:
            show_history()

    elif page == "game":

        game()

    elif page == "profile":

        profile()
        navigation()

    elif page == "leaderboard":

        show_leaderboard()
        navigation()


main()
