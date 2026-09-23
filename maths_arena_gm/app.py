import streamlit as st
import random
import math
from datetime import datetime

# ============================================================
# MATHS ARENA PRO
# Single-file Streamlit game
# 1 PLAYER + 2 PLAYER LOCAL BATTLE
# ============================================================

st.set_page_config(
    page_title="Maths Arena Pro",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PREMIUM CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Orbitron:wght@500;600;700;800;900&display=swap');

    * {
        box-sizing: border-box;
    }

    body {
        background:
            radial-gradient(circle at 15% 10%, rgba(99,102,241,.18), transparent 30%),
            radial-gradient(circle at 85% 20%, rgba(168,85,247,.15), transparent 30%),
            radial-gradient(circle at 50% 100%, rgba(14,165,233,.10), transparent 35%),
            #050816;
    }

    .stApp {
        background:
            radial-gradient(circle at 15% 10%, rgba(99,102,241,.14), transparent 30%),
            radial-gradient(circle at 85% 20%, rgba(168,85,247,.10), transparent 30%),
            #050816;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
    }

    p, div, span, label {
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit default menu/footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid rgba(148,163,184,.18);
        background: linear-gradient(
            135deg,
            rgba(30,41,59,.95),
            rgba(15,23,42,.95)
        );
        color: white;
        font-weight: 700;
        min-height: 48px;
        transition: all .18s ease;
        box-shadow: 0 8px 25px rgba(0,0,0,.18);
    }

    .stButton > button:hover {
        border-color: rgba(129,140,248,.7);
        transform: translateY(-2px);
        box-shadow:
            0 12px 30px rgba(79,70,229,.22),
            0 0 20px rgba(99,102,241,.10);
    }

    /* Input */
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"],
    .stRadio div[data-baseweb="radio"] {
        border-radius: 12px !important;
    }

    /* Progress */
    .stProgress > div > div > div > div {
        border-radius: 20px;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background: linear-gradient(
            145deg,
            rgba(15,23,42,.92),
            rgba(30,41,59,.72)
        );
        border: 1px solid rgba(148,163,184,.13);
        border-radius: 16px;
        padding: 14px;
        box-shadow: 0 10px 30px rgba(0,0,0,.15);
    }

    /* Radio */
    div[role="radiogroup"] {
        gap: 10px;
    }

    /* Divider */
    hr {
        border-color: rgba(148,163,184,.10) !important;
    }

    .hero {
        padding: 45px 20px 30px 20px;
        text-align: center;
    }

    .hero-badge {
        display: inline-block;
        padding: 8px 15px;
        border-radius: 999px;
        background: rgba(99,102,241,.12);
        border: 1px solid rgba(129,140,248,.28);
        color: #c7d2fe;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 1.2px;
        margin-bottom: 16px;
    }

    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(38px, 7vw, 78px);
        line-height: 1;
        font-weight: 900;
        letter-spacing: -3px;
        margin: 0;
        background: linear-gradient(
            90deg,
            #ffffff,
            #a5b4fc,
            #c084fc,
            #67e8f9
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #94a3b8;
        margin-top: 18px;
        font-size: 15px;
        letter-spacing: 2px;
    }

    .game-card {
        padding: 24px;
        border-radius: 22px;
        border: 1px solid rgba(148,163,184,.12);
        background:
            linear-gradient(
                145deg,
                rgba(15,23,42,.90),
                rgba(15,23,42,.58)
            );
        box-shadow:
            0 20px 60px rgba(0,0,0,.20),
            inset 0 1px 0 rgba(255,255,255,.03);
        margin-bottom: 18px;
    }

    .player-card {
        padding: 20px;
        border-radius: 22px;
        background:
            linear-gradient(
                145deg,
                rgba(15,23,42,.98),
                rgba(30,41,59,.78)
            );
        border: 1px solid rgba(129,140,248,.20);
        box-shadow: 0 20px 50px rgba(0,0,0,.22);
        min-height: 190px;
    }

    .enemy-card {
        padding: 20px;
        border-radius: 22px;
        background:
            linear-gradient(
                145deg,
                rgba(40,10,25,.95),
                rgba(30,15,35,.82)
            );
        border: 1px solid rgba(244,63,94,.20);
        box-shadow: 0 20px 50px rgba(0,0,0,.22);
        min-height: 190px;
    }

    .fighter-name {
        font-family: 'Orbitron', sans-serif;
        font-size: 20px;
        font-weight: 800;
    }

    .fighter-icon {
        font-size: 45px;
    }

    .vs {
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 32px;
        font-weight: 900;
        color: #a5b4fc;
        padding-top: 70px;
    }

    .question-box {
        margin: 20px 0;
        padding: 35px 20px;
        text-align: center;
        border-radius: 25px;
        background:
            radial-gradient(
                circle at center,
                rgba(99,102,241,.13),
                rgba(15,23,42,.90) 65%
            );
        border: 1px solid rgba(129,140,248,.18);
        box-shadow:
            0 20px 60px rgba(0,0,0,.22),
            inset 0 0 50px rgba(99,102,241,.04);
    }

    .question-label {
        color: #818cf8;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 3px;
        margin-bottom: 15px;
    }

    .question-text {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(30px, 6vw, 60px);
        font-weight: 900;
        color: white;
    }

    .combo-box {
        text-align: center;
        padding: 15px;
        border-radius: 18px;
        background: rgba(245,158,11,.08);
        border: 1px solid rgba(245,158,11,.20);
    }

    .combo-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 35px;
        font-weight: 900;
        color: #fbbf24;
    }

    .power-card {
        padding: 15px;
        text-align: center;
        border-radius: 16px;
        background: rgba(30,41,59,.70);
        border: 1px solid rgba(148,163,184,.12);
    }

    .power-icon {
        font-size: 28px;
    }

    .result-box {
        text-align: center;
        padding: 50px 20px;
        border-radius: 28px;
        background:
            radial-gradient(
                circle at center,
                rgba(99,102,241,.14),
                rgba(15,23,42,.92) 65%
            );
        border: 1px solid rgba(129,140,248,.18);
    }

    .result-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 48px;
        font-weight: 900;
    }

    .small-muted {
        color: #94a3b8;
        font-size: 13px;
    }

    .feature-icon {
        font-size: 34px;
    }

    .feature-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 17px;
        font-weight: 800;
        margin-top: 10px;
    }

    .feature-text {
        color: #94a3b8;
        font-size: 13px;
        margin-top: 7px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# GAME CONFIG
# ============================================================

DIFFICULTIES = {
    "Basic": {
        "player_hp": 120,
        "enemy_hp": 90,
        "damage": 24,
        "enemy_damage": 12,
        "xp": 8,
        "coins": 2,
    },
    "Medium": {
        "player_hp": 110,
        "enemy_hp": 125,
        "damage": 27,
        "enemy_damage": 16,
        "xp": 12,
        "coins": 3,
    },
    "Pro": {
        "player_hp": 100,
        "enemy_hp": 165,
        "damage": 30,
        "enemy_damage": 20,
        "xp": 16,
        "coins": 4,
    },
    "Master": {
        "player_hp": 95,
        "enemy_hp": 205,
        "damage": 34,
        "enemy_damage": 25,
        "xp": 21,
        "coins": 5,
    },
}


ENEMIES = {
    "Basic": [
        ("🟢", "Number Goblin"),
        ("🤖", "Digit Droid"),
        ("👾", "Sum Beast"),
        ("🐲", "Quick Calculator"),
    ],
    "Medium": [
        ("👻", "Fraction Phantom"),
        ("🤖", "Equation Raider"),
        ("🦂", "Logic Droid"),
        ("⚔️", "Algebra Hunter"),
    ],
    "Pro": [
        ("💀", "Formula Reaper"),
        ("🛡️", "Algebra Knight"),
        ("👹", "Prime Destroyer"),
        ("🤖", "Matrix Warrior"),
    ],
    "Master": [
        ("👑", "Infinity Lord"),
        ("☠️", "Zero King"),
        ("🔥", "Formula Titan"),
        ("🌌", "Math Overlord"),
    ],
}


BOSSES = [
    ("👑", "THE CALCULATOR"),
    ("☠️", "THE ZERO KING"),
    ("🔥", "MATH TITAN"),
    ("🌌", "INFINITY LORD"),
]


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "screen": "home",

    "mode": "1 Player",
    "difficulty": "Basic",
    "battle_type": "Endless Arena",

    "player1_name": "Player 1",
    "player2_name": "Player 2",

    "current_player": 1,

    "p1_hp": 120,
    "p2_hp": 120,
    "enemy_hp": 90,

    "p1_max_hp": 120,
    "p2_max_hp": 120,
    "enemy_max_hp": 90,

    "p1_score": 0,
    "p2_score": 0,

    "p1_combo": 0,
    "p2_combo": 0,

    "p1_best_combo": 0,
    "p2_best_combo": 0,

    "p1_xp": 0,
    "p2_xp": 0,

    "p1_coins": 0,
    "p2_coins": 0,

    "p1_correct": 0,
    "p2_correct": 0,

    "p1_attempts": 0,
    "p2_attempts": 0,

    "round": 1,

    "question": "",
    "correct_answer": None,
    "options": [],

    "enemy_icon": "👾",
    "enemy_name": "Number Goblin",

    "shield1": False,
    "shield2": False,

    "crit1": False,
    "crit2": False,

    "overdrive1": False,
    "overdrive2": False,

    "message": "",
    "battle_log": [],

    "result": None,

    "history": [],

    "total_wins": 0,
    "total_losses": 0,

    "achievements": [],

    "used_questions": [],

    "game_started": False,
}


for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def reset_session_game():
    """Reset current game only."""

    config = DIFFICULTIES[st.session_state.difficulty]

    st.session_state.p1_hp = config["player_hp"]
    st.session_state.p2_hp = config["player_hp"]

    st.session_state.p1_max_hp = config["player_hp"]
    st.session_state.p2_max_hp = config["player_hp"]

    st.session_state.enemy_hp = config["enemy_hp"]
    st.session_state.enemy_max_hp = config["enemy_hp"]

    st.session_state.p1_score = 0
    st.session_state.p2_score = 0

    st.session_state.p1_combo = 0
    st.session_state.p2_combo = 0

    st.session_state.p1_best_combo = 0
    st.session_state.p2_best_combo = 0

    st.session_state.p1_xp = 0
    st.session_state.p2_xp = 0

    st.session_state.p1_coins = 0
    st.session_state.p2_coins = 0

    st.session_state.p1_correct = 0
    st.session_state.p2_correct = 0

    st.session_state.p1_attempts = 0
    st.session_state.p2_attempts = 0

    st.session_state.round = 1
    st.session_state.current_player = 1

    st.session_state.shield1 = False
    st.session_state.shield2 = False

    st.session_state.crit1 = False
    st.session_state.crit2 = False

    st.session_state.overdrive1 = False
    st.session_state.overdrive2 = False

    st.session_state.message = ""
    st.session_state.battle_log = []

    st.session_state.result = None

    st.session_state.used_questions = []

    st.session_state.game_started = True

    create_enemy()

    new_question()


def combo_multiplier(combo):
    if combo >= 12:
        return 2.5
    if combo >= 8:
        return 2.0
    if combo >= 5:
        return 1.5
    if combo >= 3:
        return 1.25

    return 1.0


def get_current_player_name():
    if st.session_state.current_player == 1:
        return st.session_state.player1_name

    return st.session_state.player2_name


def get_current_combo():
    if st.session_state.current_player == 1:
        return st.session_state.p1_combo

    return st.session_state.p2_combo


def get_current_hp():
    if st.session_state.current_player == 1:
        return st.session_state.p1_hp

    return st.session_state.p2_hp


def get_current_score():
    if st.session_state.current_player == 1:
        return st.session_state.p1_score

    return st.session_state.p2_score


def add_log(text):
    st.session_state.battle_log.insert(0, text)

    if len(st.session_state.battle_log) > 8:
        st.session_state.battle_log = st.session_state.battle_log[:8]


# ============================================================
# QUESTION ENGINE
# ============================================================

def make_question(difficulty):
    """
    Returns:
        question_text,
        correct_answer

    Correct answer is ALWAYS explicitly returned.
    """

    if difficulty == "Basic":

        operation = random.choice([
            "add",
            "subtract",
            "multiply",
            "division",
        ])

        if operation == "add":
            a = random.randint(5, 60)
            b = random.randint(5, 60)

            return f"{a} + {b}", a + b

        if operation == "subtract":
            a = random.randint(20, 80)
            b = random.randint(5, a)

            return f"{a} − {b}", a - b

        if operation == "multiply":
            a = random.randint(2, 12)
            b = random.randint(2, 12)

            return f"{a} × {b}", a * b

        a = random.randint(2, 12)
        answer = random.randint(2, 12)

        b = a * answer

        return f"{b} ÷ {a}", answer


    if difficulty == "Medium":

        operation = random.choice([
            "add",
            "subtract",
            "multiply",
            "division",
            "percentage",
            "square",
        ])

        if operation == "add":
            a = random.randint(30, 150)
            b = random.randint(20, 150)

            return f"{a} + {b}", a + b

        if operation == "subtract":
            a = random.randint(80, 250)
            b = random.randint(20, a)

            return f"{a} − {b}", a - b

        if operation == "multiply":
            a = random.randint(6, 25)
            b = random.randint(5, 20)

            return f"{a} × {b}", a * b

        if operation == "division":
            divisor = random.randint(3, 15)
            answer = random.randint(4, 30)

            dividend = divisor * answer

            return f"{dividend} ÷ {divisor}", answer

        if operation == "percentage":
            percent = random.choice([10, 20, 25, 50])
            number = random.choice([40, 60, 80, 100, 120, 200])

            answer = int(number * percent / 100)

            return f"{percent}% of {number}", answer

        number = random.randint(3, 18)

        return f"{number}²", number ** 2


    if difficulty == "Pro":

        operation = random.choice([
            "mixed",
            "percentage",
            "square",
            "division",
            "equation",
        ])

        if operation == "mixed":
            a = random.randint(5, 30)
            b = random.randint(2, 15)
            c = random.randint(2, 20)

            answer = a + b * c

            return f"{a} + {b} × {c}", answer

        if operation == "percentage":
            percent = random.choice([15, 20, 25, 30, 40])
            number = random.choice([
                80,
                100,
                120,
                160,
                200,
                240,
            ])

            answer = int(number * percent / 100)

            return f"{percent}% of {number}", answer

        if operation == "square":
            number = random.randint(10, 30)

            return f"{number}²", number ** 2

        if operation == "division":
            divisor = random.randint(4, 18)
            answer = random.randint(5, 40)

            dividend = divisor * answer

            return f"{dividend} ÷ {divisor}", answer

        x = random.randint(2, 20)
        b = random.randint(2, 30)

        answer = x

        return f"x + {b} = {x + b}", answer


    # MASTER

    operation = random.choice([
        "mixed",
        "equation",
        "percentage",
        "power",
        "fraction",
    ])

    if operation == "mixed":
        a = random.randint(5, 30)
        b = random.randint(3, 15)
        c = random.randint(2, 10)
        d = random.randint(2, 10)

        answer = a + b * c - d

        return f"{a} + {b} × {c} − {d}", answer

    if operation == "equation":

        x = random.randint(3, 30)
        multiplier = random.randint(2, 8)
        addition = random.randint(2, 25)

        result = multiplier * x + addition

        return (
            f"{multiplier}x + {addition} = {result}",
            x
        )

    if operation == "percentage":

        percent = random.choice([
            12,
            15,
            18,
            20,
            25,
            30,
        ])

        number = random.choice([
            100,
            120,
            150,
            200,
            240,
            300,
            400,
        ])

        value = number * percent

        answer = value // 100

        return f"{percent}% of {number}", answer

    if operation == "power":

        base = random.randint(2, 9)
        exponent = random.choice([2, 3])

        answer = base ** exponent

        return f"{base}^{exponent}", answer

    numerator = random.randint(1, 9)
    denominator = random.randint(2, 10)

    multiplier = random.randint(2, 10)

    actual_numerator = numerator * multiplier
    actual_denominator = denominator * multiplier

    # Integer-safe fraction question
    answer = numerator

    return (
        f"{actual_numerator} ÷ {actual_denominator} × {denominator}",
        answer
    )


def generate_options(correct):
    """
    IMPORTANT:
    The correct answer is inserted FIRST.
    Then 3 unique distractors are generated.

    This guarantees that the correct answer exists
    in the final option list.
    """

    try:
        correct = int(correct)
    except Exception:
        correct = int(float(correct))

    options = [correct]

    attempts = 0

    while len(options) < 4 and attempts < 100:

        attempts += 1

        strategy = random.choice([
            "near",
            "near",
            "random",
            "offset",
            "multiply",
        ])

        if strategy == "near":
            delta = random.randint(1, 12)

            if random.choice([True, False]):
                candidate = correct + delta
            else:
                candidate = correct - delta

        elif strategy == "offset":
            candidate = correct + random.choice([
                -20,
                -15,
                -10,
                -5,
                5,
                10,
                15,
                20,
            ])

        elif strategy == "multiply":
            candidate = correct + random.randint(
                max(1, abs(correct) // 4),
                max(2, abs(correct) // 2 + 5)
            )

            if random.choice([True, False]):
                candidate = -candidate

        else:
            if correct >= 0:
                candidate = random.randint(
                    max(0, correct - 30),
                    correct + 30
                )
            else:
                candidate = random.randint(
                    correct - 30,
                    correct + 30
                )

        if candidate != correct and candidate not in options:
            options.append(candidate)

    # Absolute fallback.
    # There is no possible situation where fewer than 4
    # options are returned.
    fallback = 1

    while len(options) < 4:

        candidate = correct + fallback

        if candidate not in options:
            options.append(candidate)

        fallback += 1

    random.shuffle(options)

    # FINAL SAFETY CHECK
    if correct not in options:
        options[0] = correct
        random.shuffle(options)

    return options


def new_question():
    difficulty = st.session_state.difficulty

    # Try to avoid immediate duplicate questions.
    for _ in range(30):

        question, answer = make_question(difficulty)

        signature = f"{question}={answer}"

        if signature not in st.session_state.used_questions:
            st.session_state.used_questions.append(signature)

            st.session_state.question = question
            st.session_state.correct_answer = answer
            st.session_state.options = generate_options(answer)

            # FINAL GUARANTEE
            if answer not in st.session_state.options:
                st.session_state.options[0] = answer
                random.shuffle(st.session_state.options)

            return

    # Fallback if too many questions already used.
    question, answer = make_question(difficulty)

    st.session_state.question = question
    st.session_state.correct_answer = answer
    st.session_state.options = generate_options(answer)

    if answer not in st.session_state.options:
        st.session_state.options[0] = answer
        random.shuffle(st.session_state.options)


# ============================================================
# ENEMY SYSTEM
# ============================================================

def create_enemy():
    difficulty = st.session_state.difficulty
    round_number = st.session_state.round

    config = DIFFICULTIES[difficulty]

    # Boss every 5 rounds
    if round_number % 5 == 0:

        icon, name = random.choice(BOSSES)

        boss_multiplier = 1 + (round_number // 5) * 0.20

        hp = int(config["enemy_hp"] * boss_multiplier * 1.35)

        st.session_state.enemy_icon = icon
        st.session_state.enemy_name = name
        st.session_state.enemy_hp = hp
        st.session_state.enemy_max_hp = hp

        add_log(f"👑 BOSS ARRIVED: {name}")

    else:

        icon, name = random.choice(ENEMIES[difficulty])

        round_multiplier = 1 + max(0, round_number - 1) * 0.06

        hp = int(config["enemy_hp"] * round_multiplier)

        st.session_state.enemy_icon = icon
        st.session_state.enemy_name = name
        st.session_state.enemy_hp = hp
        st.session_state.enemy_max_hp = hp


# ============================================================
# START GAME
# ============================================================

def start_game():
    reset_session_game()
    st.session_state.screen = "battle"


# ============================================================
# PLAYER STATS HELPERS
# ============================================================

def get_player_stat(player, stat):
    key = f"p{player}_{stat}"
    return st.session_state[key]


def set_player_stat(player, stat, value):
    key = f"p{player}_{stat}"
    st.session_state[key] = value


def add_player_stat(player, stat, amount):
    key = f"p{player}_{stat}"
    st.session_state[key] += amount


# ============================================================
# ACHIEVEMENTS
# ============================================================

def check_achievements():

    achievements = []

    p1_combo = st.session_state.p1_best_combo
    p2_combo = st.session_state.p2_best_combo

    best_combo = max(p1_combo, p2_combo)

    total_score = (
        st.session_state.p1_score
        + st.session_state.p2_score
    )

    total_correct = (
        st.session_state.p1_correct
        + st.session_state.p2_correct
    )

    if total_correct >= 1:
        achievements.append("🎯 First Hit")

    if best_combo >= 3:
        achievements.append("🔥 Combo Starter")

    if best_combo >= 5:
        achievements.append("⚡ Combo Hunter")

    if best_combo >= 10:
        achievements.append("👑 Combo Master")

    if total_score >= 1000:
        achievements.append("💰 Score Grinder")

    if total_score >= 5000:
        achievements.append("🤖 Math Machine")

    if st.session_state.round >= 5:
        achievements.append("🛡️ Arena Survivor")

    if st.session_state.round >= 10:
        achievements.append("💎 Elite Fighter")

    if st.session_state.round >= 15:
        achievements.append("🌌 Brain Power")

    st.session_state.achievements = achievements


# ============================================================
# ANSWER HANDLING
# ============================================================

def answer_question(selected_answer):

    player = st.session_state.current_player

    correct = st.session_state.correct_answer

    # --------------------------------------------------------
    # Safety:
    # If for ANY reason the selected answer isn't in the
    # generated options, regenerate instead of crashing.
    # --------------------------------------------------------

    if correct not in st.session_state.options:

        st.session_state.options = generate_options(correct)

        if correct not in st.session_state.options:
            st.session_state.options[0] = correct

        st.session_state.message = (
            "⚠️ Question refreshed — correct answer protected."
        )

        return

    # --------------------------------------------------------
    # ATTEMPT
    # --------------------------------------------------------

    add_player_stat(player, "attempts", 1)

    is_correct = selected_answer == correct

    config = DIFFICULTIES[st.session_state.difficulty]

    player_name = get_current_player_name()

    # ========================================================
    # CORRECT
    # ========================================================

    if is_correct:

        add_player_stat(player, "correct", 1)

        combo_key = f"p{player}_combo"

        st.session_state[combo_key] += 1

        combo = st.session_state[combo_key]

        best_key = f"p{player}_best_combo"

        if combo > st.session_state[best_key]:
            st.session_state[best_key] = combo

        multiplier = combo_multiplier(combo)

        damage = int(config["damage"] * multiplier)

        # ----------------------------------------------------
        # CRITICAL
        # ----------------------------------------------------

        crit_key = f"crit{player}"

        if st.session_state[crit_key]:

            damage *= 2

            st.session_state[crit_key] = False

            st.session_state.message = (
                f"💥 CRITICAL HIT! {player_name} dealt {damage} damage!"
            )

        # ----------------------------------------------------
        # OVERDRIVE
        # ----------------------------------------------------

        elif st.session_state[f"overdrive{player}"]:

            damage *= 3

            st.session_state[f"overdrive{player}"] = False

            st.session_state.message = (
                f"⚡ OVERDRIVE! {player_name} dealt {damage} damage!"
            )

        else:

            st.session_state.message = (
                f"⚔️ {player_name} attacked for {damage} damage!"
            )

        # ----------------------------------------------------
        # ENEMY DAMAGE
        # ----------------------------------------------------

        st.session_state.enemy_hp -= damage

        score_gain = damage * 10

        xp_gain = config["xp"] + combo

        coin_gain = config["coins"]

        add_player_stat(player, "score", score_gain)
        add_player_stat(player, "xp", xp_gain)
        add_player_stat(player, "coins", coin_gain)

        add_log(
            f"✅ {player_name}: +{score_gain} score | "
            f"{damage} damage"
        )

        # ----------------------------------------------------
        # COMBO REWARDS
        # ----------------------------------------------------

        if combo == 3:

            st.session_state[f"shield{player}"] = True

            add_log(
                f"🛡️ {player_name} unlocked SHIELD!"
            )

        if combo == 5:

            st.session_state[f"crit{player}"] = True

            add_log(
                f"💥 {player_name} unlocked CRITICAL!"
            )

        if combo == 8:

            st.session_state[f"overdrive{player}"] = True

            add_log(
                f"⚡ {player_name} unlocked OVERDRIVE!"
            )

        # ====================================================
        # ENEMY DEFEATED
        # ====================================================

        if st.session_state.enemy_hp <= 0:

            bonus = 500 + st.session_state.round * 100

            add_player_stat(player, "score", bonus)

            add_player_stat(
                player,
                "coins",
                10
            )

            add_player_stat(
                player,
                "xp",
                25
            )

            add_log(
                f"💀 {player_name} defeated "
                f"{st.session_state.enemy_name}!"
            )

            st.session_state.message = (
                f"🏆 {player_name} defeated "
                f"{st.session_state.enemy_name}!"
            )

            # QUICK BATTLE ends at round 5
            if (
                st.session_state.battle_type
                == "Quick Battle"
                and st.session_state.round >= 5
            ):

                finish_game("victory")

                return

            # Next round
            st.session_state.round += 1

            create_enemy()

            new_question()

            # In 2-player mode, switch turn
            if st.session_state.mode == "2 Players":

                if player == 1:
                    st.session_state.current_player = 2
                else:
                    st.session_state.current_player = 1

            return

        # If enemy still alive:
        # switch player in 2-player mode
        if st.session_state.mode == "2 Players":

            if player == 1:
                st.session_state.current_player = 2
            else:
                st.session_state.current_player = 1

        new_question()

        return

    # ========================================================
    # WRONG
    # ========================================================

    st.session_state[f"p{player}_combo"] = 0

    damage_taken = config["enemy_damage"]

    # Boss damage
    if st.session_state.round % 5 == 0:

        damage_taken = int(
            damage_taken * 1.35
        )

    shield_key = f"shield{player}"

    if st.session_state[shield_key]:

        st.session_state[shield_key] = False

        st.session_state.message = (
            f"🛡️ SHIELD BLOCKED THE ATTACK!"
        )

        add_log(
            f"🛡️ {player_name}'s shield blocked damage."
        )

    else:

        hp_key = f"p{player}_hp"

        st.session_state[hp_key] -= damage_taken

        st.session_state.message = (
            f"💔 Wrong answer! "
            f"{player_name} lost {damage_taken} HP."
        )

        add_log(
            f"❌ {player_name} took {damage_taken} damage."
        )

    # ========================================================
    # PLAYER DEFEATED
    # ========================================================

    if st.session_state[f"p{player}_hp"] <= 0:

        st.session_state[f"p{player}_hp"] = 0

        if st.session_state.mode == "1 Player":

            finish_game("defeat")

            return

        else:

            # In 2-player mode, one player can be eliminated.
            # The other player continues.

            other_player = 2 if player == 1 else 1

            other_hp = st.session_state[
                f"p{other_player}_hp"
            ]

            if other_hp <= 0:

                finish_game("draw")

                return

            st.session_state.message = (
                f"💀 {player_name} has been eliminated!"
            )

            st.session_state.current_player = other_player

    else:

        if st.session_state.mode == "2 Players":

            if player == 1:
                st.session_state.current_player = 2
            else:
                st.session_state.current_player = 1

    new_question()


# ============================================================
# POWER UPS
# ============================================================

def use_shield():

    player = st.session_state.current_player

    coin_key = f"p{player}_coins"
    shield_key = f"shield{player}"

    if st.session_state[shield_key]:

        st.session_state.message = (
            "🛡️ Shield is already active."
        )

        return

    if st.session_state[coin_key] < 5:

        st.session_state.message = (
            "🪙 You need 5 coins."
        )

        return

    st.session_state[coin_key] -= 5

    st.session_state[shield_key] = True

    st.session_state.message = (
        "🛡️ Shield activated!"
    )


def use_critical():

    player = st.session_state.current_player

    coin_key = f"p{player}_coins"
    crit_key = f"crit{player}"

    if st.session_state[crit_key]:

        st.session_state.message = (
            "💥 Critical is already active."
        )

        return

    if st.session_state[coin_key] < 8:

        st.session_state.message = (
            "🪙 You need 8 coins."
        )

        return

    st.session_state[coin_key] -= 8

    st.session_state[crit_key] = True

    st.session_state.message = (
        "💥 Critical Attack armed!"
    )


def use_heal():

    player = st.session_state.current_player

    coin_key = f"p{player}_coins"
    hp_key = f"p{player}_hp"
    max_hp_key = f"p{player}_max_hp"

    if st.session_state[coin_key] < 10:

        st.session_state.message = (
            "🪙 You need 10 coins."
        )

        return

    if st.session_state[hp_key] >= st.session_state[max_hp_key]:

        st.session_state.message = (
            "❤️ HP is already full."
        )

        return

    st.session_state[coin_key] -= 10

    st.session_state[hp_key] = min(
        st.session_state[max_hp_key],
        st.session_state[hp_key] + 30
    )

    st.session_state.message = (
        "❤️ +30 HP restored!"
    )


# ============================================================
# FINISH GAME
# ============================================================

def finish_game(result):

    check_achievements()

    st.session_state.result = result

    if result == "victory":
        st.session_state.total_wins += 1

    elif result == "defeat":
        st.session_state.total_losses += 1

    timestamp = datetime.now().strftime(
        "%d %b %Y • %I:%M %p"
    )

    record = {
        "time": timestamp,
        "mode": st.session_state.mode,
        "difficulty": st.session_state.difficulty,
        "round": st.session_state.round,
        "p1": st.session_state.player1_name,
        "p2": st.session_state.player2_name
        if st.session_state.mode == "2 Players"
        else "-",
        "p1_score": st.session_state.p1_score,
        "p2_score": st.session_state.p2_score,
        "result": result,
    }

    st.session_state.history.insert(
        0,
        record
    )

    if len(st.session_state.history) > 20:

        st.session_state.history = (
            st.session_state.history[:20]
        )

    st.session_state.screen = "result"


# ============================================================
# LEVEL SYSTEM
# ============================================================

def get_level(xp):

    return max(
        1,
        int(xp / 100) + 1
    )


def get_level_progress(xp):

    current_level = get_level(xp)

    previous = (current_level - 1) * 100

    progress = xp - previous

    return progress


# ============================================================
# HOME
# ============================================================

def home_screen():

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                ⚔️ THE ULTIMATE MATH BATTLE
            </div>

            <div class="hero-title">
                MATHS ARENA PRO
            </div>

            <div class="hero-subtitle">
                THINK FAST • ATTACK SMART • MASTER MATHEMATICS
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # MODE
    # --------------------------------------------------------

    st.markdown("### 🎮 Enter The Arena")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.player1_name = st.text_input(
            "PLAYER 1",
            value=st.session_state.player1_name,
            max_chars=18
        )

    with c2:

        mode = st.radio(
            "GAME MODE",
            [
                "1 Player",
                "2 Players"
            ],
            horizontal=True,
            index=(
                1
                if st.session_state.mode == "2 Players"
                else 0
            )
        )

        st.session_state.mode = mode

    if mode == "2 Players":

        st.session_state.player2_name = st.text_input(
            "PLAYER 2",
            value=st.session_state.player2_name,
            max_chars=18
        )

    else:

        st.session_state.player2_name = "Player 2"

    st.markdown("### ⚔️ Battle Settings")

    c1, c2 = st.columns(2)

    with c1:

        battle_type = st.selectbox(
            "BATTLE TYPE",
            [
                "Endless Arena",
                "Quick Battle"
            ]
        )

        st.session_state.battle_type = battle_type

    with c2:

        difficulty = st.selectbox(
            "DIFFICULTY",
            [
                "Basic",
                "Medium",
                "Pro",
                "Master"
            ]
        )

        st.session_state.difficulty = difficulty

    st.markdown("")

    start_col, profile_col = st.columns([2, 1])

    with start_col:

        if st.button(
            "⚔️ ENTER THE ARENA",
            use_container_width=True
        ):

            if not st.session_state.player1_name.strip():

                st.session_state.player1_name = "Player 1"

            if mode == "2 Players":

                if not st.session_state.player2_name.strip():

                    st.session_state.player2_name = "Player 2"

            start_game()

            st.rerun()

    with profile_col:

        if st.button(
            "👤 PROFILE",
            use_container_width=True
        ):

            st.session_state.screen = "profile"

            st.rerun()

    st.markdown("---")

    # --------------------------------------------------------
    # FEATURES
    # --------------------------------------------------------

    st.markdown("### 🔥 Why This Is A Game")

    f1, f2, f3, f4 = st.columns(4)

    features = [
        (
            "⚔️",
            "Battle System",
            "Solve maths to attack enemies."
        ),
        (
            "🔥",
            "Combo",
            "Keep answering correctly to increase damage."
        ),
        (
            "👥",
            "2 Player",
            "Two players can battle on one device."
        ),
        (
            "👑",
            "Boss Battles",
            "Survive powerful enemies every 5 rounds."
        ),
    ]

    for column, feature in zip(
        [f1, f2, f3, f4],
        features
    ):

        icon, title, description = feature

        with column:

            st.markdown(
                f"""
                <div class="game-card">

                    <div class="feature-icon">
                        {icon}
                    </div>

                    <div class="feature-title">
                        {title}
                    </div>

                    <div class="feature-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # --------------------------------------------------------
    # SESSION HISTORY
    # --------------------------------------------------------

    st.markdown("### 🏆 Recent Arena Runs")

    if not st.session_state.history:

        st.info(
            "No battles yet. Enter the arena and create your first record."
        )

    else:

        for match in st.session_state.history[:5]:

            result_icon = {
                "victory": "🏆",
                "defeat": "💀",
                "draw": "🤝"
            }.get(
                match["result"],
                "⚔️"
            )

            st.write(
                f"{result_icon} "
                f"**{match['p1']}** "
                f"vs "
                f"**{match['p2']}** "
                f"• Round {match['round']} "
                f"• {match['difficulty']} "
                f"• P1 Score: {match['p1_score']}"
            )


# ============================================================
# PLAYER CARD
# ============================================================

def render_player_card(player):

    if player == 1:

        name = st.session_state.player1_name
        hp = st.session_state.p1_hp
        max_hp = st.session_state.p1_max_hp
        score = st.session_state.p1_score
        combo = st.session_state.p1_combo
        coins = st.session_state.p1_coins
        xp = st.session_state.p1_xp

    else:

        name = st.session_state.player2_name
        hp = st.session_state.p2_hp
        max_hp = st.session_state.p2_max_hp
        score = st.session_state.p2_score
        combo = st.session_state.p2_combo
        coins = st.session_state.p2_coins
        xp = st.session_state.p2_xp

    level = get_level(xp)

    st.markdown(
        f"""
        <div class="player-card">

            <div class="fighter-icon">
                {"🧙" if player == 1 else "🥷"}
            </div>

            <div class="fighter-name">
                {name}
            </div>

            <div class="small-muted">
                PLAYER {player} • LEVEL {level}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        max(
            0.0,
            min(
                1.0,
                hp / max_hp
            )
        )
    )

    st.caption(
        f"❤️ {hp}/{max_hp} HP"
    )

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "SCORE",
            score
        )

    with m2:
        st.metric(
            "COMBO",
            combo
        )

    with m3:
        st.metric(
            "🪙",
            coins
        )


# ============================================================
# ENEMY CARD
# ============================================================

def render_enemy_card():

    hp = st.session_state.enemy_hp
    max_hp = st.session_state.enemy_max_hp

    is_boss = (
        st.session_state.round % 5 == 0
    )

    title = (
        "👑 BOSS"
        if is_boss
        else "ENEMY"
    )

    st.markdown(
        f"""
        <div class="enemy-card">

            <div class="fighter-icon">
                {st.session_state.enemy_icon}
            </div>

            <div class="fighter-name">
                {st.session_state.enemy_name}
            </div>

            <div class="small-muted">
                {title} • ROUND {st.session_state.round}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        max(
            0.0,
            min(
                1.0,
                hp / max_hp
            )
        )
    )

    st.caption(
        f"❤️ {max(0, hp)}/{max_hp} HP"
    )


# ============================================================
# BATTLE SCREEN
# ============================================================

def battle_screen():

    current_name = get_current_player_name()

    current_combo = get_current_combo()

    multiplier = combo_multiplier(
        current_combo
    )

    is_boss = (
        st.session_state.round % 5 == 0
    )

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="text-align:center; padding:10px 0 20px 0;">

            <div style="
                color:#818cf8;
                font-weight:800;
                letter-spacing:2px;
                font-size:12px;
            ">
                {"👑 BOSS ROUND" if is_boss else "⚔️ ARENA BATTLE"}
            </div>

            <div style="
                font-family:Orbitron;
                font-size:32px;
                font-weight:900;
                margin-top:8px;
            ">
                ROUND {st.session_state.round}
            </div>

            <div style="
                color:#94a3b8;
                margin-top:5px;
            ">
                {current_name}'s turn
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # TOP METRICS
    # --------------------------------------------------------

    if st.session_state.mode == "1 Player":

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "⚔️ SCORE",
                st.session_state.p1_score
            )

        with c2:
            st.metric(
                "🔥 COMBO",
                st.session_state.p1_combo
            )

        with c3:
            st.metric(
                "🪙 COINS",
                st.session_state.p1_coins
            )

        with c4:
            st.metric(
                "⭐ XP",
                st.session_state.p1_xp
            )

    else:

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                st.session_state.player1_name,
                st.session_state.p1_score
            )

        with c2:
            st.metric(
                st.session_state.player2_name,
                st.session_state.p2_score
            )

        with c3:
            st.metric(
                "ROUND",
                st.session_state.round
            )

        with c4:
            st.metric(
                "TURN",
                current_name
            )

    st.markdown("---")

    # --------------------------------------------------------
    # FIGHTERS
    # --------------------------------------------------------

    if st.session_state.mode == "1 Player":

        left, middle, right = st.columns(
            [1, .35, 1]
        )

        with left:
            render_player_card(1)

        with middle:

            st.markdown(
                """
                <div class="vs">
                    VS
                </div>
                """,
                unsafe_allow_html=True
            )

        with right:
            render_enemy_card()

    else:

        p1, vs, p2 = st.columns(
            [1, .35, 1]
        )

        with p1:
            render_player_card(1)

        with vs:

            st.markdown(
                """
                <div class="vs">
                    ⚔️
                </div>
                """,
                unsafe_allow_html=True
            )

        with p2:
            render_player_card(2)

        st.markdown(
            f"""
            <div style="
                text-align:center;
                margin:15px 0;
                color:#f87171;
                font-family:Orbitron;
                font-size:18px;
                font-weight:800;
            ">
                TARGET: {st.session_state.enemy_name}
                • {st.session_state.enemy_hp} HP
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # CURRENT PLAYER COMBO
    # --------------------------------------------------------

    st.markdown("")

    st.markdown(
        f"""
        <div class="combo-box">

            <div class="small-muted">
                CURRENT COMBO
            </div>

            <div class="combo-number">
                🔥 {current_combo}
            </div>

            <div class="small-muted">
                DAMAGE MULTIPLIER: {multiplier}×
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="question-box">

            <div class="question-label">
                SOLVE TO ATTACK
            </div>

            <div class="question-text">
                {st.session_state.question}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # MESSAGE
    # --------------------------------------------------------

    if st.session_state.message:

        st.info(
            st.session_state.message
        )

    # --------------------------------------------------------
    # ANSWERS
    # --------------------------------------------------------

    st.markdown(
        f"### 🎯 {current_name}, choose your attack"
    )

    options = list(
        st.session_state.options
    )

    # --------------------------------------------------------
    # ABSOLUTE CORRECT-ANSWER SAFETY
    # --------------------------------------------------------

    correct = st.session_state.correct_answer

    if correct not in options:

        options = generate_options(correct)

        if correct not in options:
            options[0] = correct

        st.session_state.options = options

    # Final safety assertion.
    # This should NEVER fail.
    if correct not in st.session_state.options:

        st.session_state.options = [
            correct,
            correct + 1,
            correct + 2,
            correct + 3
        ]

        random.shuffle(
            st.session_state.options
        )

    options = st.session_state.options

    a1, a2 = st.columns(2)

    with a1:

        if st.button(
            f"⚔️  {options[0]}",
            key="answer_0",
            use_container_width=True
        ):

            answer_question(
                options[0]
            )

            st.rerun()

        if st.button(
            f"⚔️  {options[2]}",
            key="answer_2",
            use_container_width=True
        ):

            answer_question(
                options[2]
            )

            st.rerun()

    with a2:

        if st.button(
            f"⚔️  {options[1]}",
            key="answer_1",
            use_container_width=True
        ):

            answer_question(
                options[1]
            )

            st.rerun()

        if st.button(
            f"⚔️  {options[3]}",
            key="answer_3",
            use_container_width=True
        ):

            answer_question(
                options[3]
            )

            st.rerun()

    # --------------------------------------------------------
    # POWER UPS
    # --------------------------------------------------------

    st.markdown("---")

    st.markdown("### ⚡ Power Arsenal")

    p1, p2, p3 = st.columns(3)

    with p1:

        shield_active = st.session_state[
            f"shield{st.session_state.current_player}"
        ]

        if st.button(
            "🛡️ SHIELD • 5 🪙",
            use_container_width=True
        ):

            use_shield()

            st.rerun()

        if shield_active:
            st.caption(
                "🛡️ SHIELD ACTIVE"
            )

    with p2:

        crit_active = st.session_state[
            f"crit{st.session_state.current_player}"
        ]

        if st.button(
            "💥 CRITICAL • 8 🪙",
            use_container_width=True
        ):

            use_critical()

            st.rerun()

        if crit_active:
            st.caption(
                "💥 CRITICAL ARMED"
            )

    with p3:

        if st.button(
            "❤️ HEAL +30 • 10 🪙",
            use_container_width=True
        ):

            use_heal()

            st.rerun()

    # --------------------------------------------------------
    # ACTIVE EFFECTS
    # --------------------------------------------------------

    player = st.session_state.current_player

    effects = []

    if st.session_state[f"shield{player}"]:
        effects.append("🛡️ Shield")

    if st.session_state[f"crit{player}"]:
        effects.append("💥 Critical")

    if st.session_state[f"overdrive{player}"]:
        effects.append("⚡ Overdrive")

    if effects:

        st.success(
            "ACTIVE: " + " • ".join(effects)
        )

    # --------------------------------------------------------
    # BATTLE LOG
    # --------------------------------------------------------

    with st.expander(
        "📜 Battle Log",
        expanded=False
    ):

        if st.session_state.battle_log:

            for log in st.session_state.battle_log:

                st.write(
                    log
                )

        else:

            st.caption(
                "Battle events will appear here."
            )

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    st.markdown("")

    if st.button(
        "🏳️ END RUN",
        use_container_width=True
    ):

        finish_game("defeat")

        st.rerun()


# ============================================================
# RESULT SCREEN
# ============================================================

def result_screen():

    result = st.session_state.result

    if result == "victory":

        title = "🏆 VICTORY"
        subtitle = "THE ARENA HAS BEEN CONQUERED."

    elif result == "draw":

        title = "🤝 DRAW"
        subtitle = "BOTH FIGHTERS HAVE FALLEN."

    else:

        title = "💀 RUN OVER"
        subtitle = "THE ARENA DEFEATED YOU THIS TIME."

    st.markdown(
        f"""
        <div class="result-box">

            <div class="result-title">
                {title}
            </div>

            <div style="
                color:#94a3b8;
                margin-top:12px;
                font-size:15px;
            ">
                {subtitle}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    # --------------------------------------------------------
    # SCORES
    # --------------------------------------------------------

    if st.session_state.mode == "1 Player":

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "SCORE",
                st.session_state.p1_score
            )

        with c2:
            st.metric(
                "BEST COMBO",
                st.session_state.p1_best_combo
            )

        with c3:
            st.metric(
                "CORRECT",
                st.session_state.p1_correct
            )

        with c4:
            st.metric(
                "🪙 COINS",
                st.session_state.p1_coins
            )

    else:

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(
                f"### 🧙 {st.session_state.player1_name}"
            )

            st.metric(
                "SCORE",
                st.session_state.p1_score
            )

            st.metric(
                "BEST COMBO",
                st.session_state.p1_best_combo
            )

            st.metric(
                "CORRECT",
                st.session_state.p1_correct
            )

        with c2:

            st.markdown(
                f"### 🥷 {st.session_state.player2_name}"
            )

            st.metric(
                "SCORE",
                st.session_state.p2_score
            )

            st.metric(
                "BEST COMBO",
                st.session_state.p2_best_combo
            )

            st.metric(
                "CORRECT",
                st.session_state.p2_correct
            )

    # --------------------------------------------------------
    # ACCURACY
    # --------------------------------------------------------

    p1_accuracy = 0

    if st.session_state.p1_attempts > 0:

        p1_accuracy = (
            st.session_state.p1_correct
            / st.session_state.p1_attempts
        ) * 100

    p2_accuracy = 0

    if st.session_state.p2_attempts > 0:

        p2_accuracy = (
            st.session_state.p2_correct
            / st.session_state.p2_attempts
        ) * 100

    st.markdown("### 🎯 Accuracy")

    if st.session_state.mode == "1 Player":

        st.progress(
            p1_accuracy / 100
        )

        st.caption(
            f"{p1_accuracy:.1f}%"
        )

    else:

        a1, a2 = st.columns(2)

        with a1:

            st.write(
                st.session_state.player1_name
            )

            st.progress(
                p1_accuracy / 100
            )

            st.caption(
                f"{p1_accuracy:.1f}%"
            )

        with a2:

            st.write(
                st.session_state.player2_name
            )

            st.progress(
                p2_accuracy / 100
            )

            st.caption(
                f"{p2_accuracy:.1f}%"
            )

    # --------------------------------------------------------
    # ACHIEVEMENTS
    # --------------------------------------------------------

    st.markdown("### 🏅 Achievements")

    if st.session_state.achievements:

        cols = st.columns(3)

        for index, achievement in enumerate(
            st.session_state.achievements
        ):

            with cols[index % 3]:

                st.success(
                    achievement
                )

    else:

        st.info(
            "Keep playing to unlock achievements."
        )

    # --------------------------------------------------------
    # ACTIONS
    # --------------------------------------------------------

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button(
            "⚔️ PLAY AGAIN",
            use_container_width=True
        ):

            start_game()

            st.rerun()

    with c2:

        if st.button(
            "🏠 HOME",
            use_container_width=True
        ):

            st.session_state.screen = "home"

            st.rerun()

    with c3:

        if st.button(
            "👤 PROFILE",
            use_container_width=True
        ):

            st.session_state.screen = "profile"

            st.rerun()

    # --------------------------------------------------------
    # RECENT RUNS
    # --------------------------------------------------------

    st.markdown("---")

    st.markdown("### 📜 Recent Runs")

    if not st.session_state.history:

        st.caption(
            "No previous runs."
        )

    else:

        for match in st.session_state.history[:10]:

            icon = {
                "victory": "🏆",
                "defeat": "💀",
                "draw": "🤝"
            }.get(
                match["result"],
                "⚔️"
            )

            st.write(
                f"{icon} "
                f"{match['time']} • "
                f"{match['mode']} • "
                f"{match['difficulty']} • "
                f"Round {match['round']} • "
                f"{match['p1']} {match['p1_score']}"
            )


# ============================================================
# PROFILE SCREEN
# ============================================================

def profile_screen():

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                👤 PLAYER PROFILE
            </div>

            <div class="hero-title">
                ARENA PROFILE
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"### 🧙 {st.session_state.player1_name}"
    )

    level = get_level(
        st.session_state.p1_xp
    )

    progress = get_level_progress(
        st.session_state.p1_xp
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "LEVEL",
            level
        )

    with c2:

        st.metric(
            "TOTAL SCORE",
            st.session_state.p1_score
        )

    with c3:

        st.metric(
            "BEST COMBO",
            st.session_state.p1_best_combo
        )

    with c4:

        st.metric(
            "🪙 COINS",
            st.session_state.p1_coins
        )

    st.markdown("### ⭐ XP Progress")

    st.progress(
        min(
            1.0,
            progress / 100
        )
    )

    st.caption(
        f"{progress}/100 XP toward next level"
    )

    st.markdown("### 🏆 Achievements")

    if st.session_state.achievements:

        for achievement in st.session_state.achievements:

            st.success(
                achievement
            )

    else:

        st.info(
            "Play battles to unlock achievements."
        )

    st.markdown("### 📊 Lifetime Session Stats")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Wins",
            st.session_state.total_wins
        )

    with c2:

        st.metric(
            "Losses",
            st.session_state.total_losses
        )

    with c3:

        st.metric(
            "Matches",
            len(st.session_state.history)
        )

    st.markdown("")

    if st.button(
        "🏠 BACK TO HOME",
        use_container_width=True
    ):

        st.session_state.screen = "home"

        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

def sidebar():

    with st.sidebar:

        st.markdown(
            "## ⚔️ Maths Arena Pro"
        )

        st.caption(
            "Think fast. Attack smart."
        )

        st.divider()

        if st.session_state.screen != "battle":

            if st.button(
                "🏠 Home",
                use_container_width=True
            ):

                st.session_state.screen = "home"

                st.rerun()

            if st.button(
                "👤 Profile",
                use_container_width=True
            ):

                st.session_state.screen = "profile"

                st.rerun()

        else:

            st.markdown(
                f"**PLAYER:** "
                f"{get_current_player_name()}"
            )

            st.markdown(
                f"**MODE:** "
                f"{st.session_state.mode}"
            )

            st.markdown(
                f"**DIFFICULTY:** "
                f"{st.session_state.difficulty}"
            )

            st.markdown(
                f"**ROUND:** "
                f"{st.session_state.round}"
            )

            st.markdown(
                f"**COMBO:** "
                f"🔥 {get_current_combo()}"
            )

            st.divider()

            if st.button(
                "🏳️ End Run",
                use_container_width=True
            ):

                finish_game("defeat")

                st.rerun()


# ============================================================
# MAIN ROUTER
# ============================================================

sidebar()

if st.session_state.screen == "home":

    home_screen()

elif st.session_state.screen == "battle":

    battle_screen()

elif st.session_state.screen == "result":

    result_screen()

elif st.session_state.screen == "profile":

    profile_screen()

else:

    st.session_state.screen = "home"

    st.rerun()
