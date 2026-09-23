import streamlit as st
import random
import math
import html

# ============================================================
# MATHS ARENA PRO
# Real-time Maths Battle Game
# No database required
# ============================================================

st.set_page_config(
    page_title="Maths Arena Pro",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# PREMIUM CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(89, 0, 255, 0.18), transparent 28%),
        radial-gradient(circle at 85% 20%, rgba(0, 217, 255, 0.13), transparent 25%),
        radial-gradient(circle at 50% 100%, rgba(255, 0, 128, 0.10), transparent 35%),
        #05060b;
    color: #ffffff;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main headings */
h1, h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.10);
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.025)
    );
    color: white;
    font-weight: 800;
    font-size: 1rem;
    transition: all 0.18s ease;
    box-shadow: 0 8px 25px rgba(0,0,0,0.22);
}

.stButton > button:hover {
    transform: translateY(-3px);
    border-color: rgba(0, 220, 255, 0.60);
    box-shadow:
        0 10px 35px rgba(0, 200, 255, 0.18),
        0 0 18px rgba(0, 200, 255, 0.08);
}

.stButton > button:active {
    transform: scale(0.98);
}

/* Inputs */
.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.045) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    color: white !important;
    border-radius: 12px !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.07);
    padding: 12px;
    border-radius: 15px;
}

/* Progress */
.stProgress > div > div > div > div {
    border-radius: 20px;
}

/* Cards */
.arena-card {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025)
        );
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 24px;
    padding: 24px;
    box-shadow:
        0 20px 60px rgba(0,0,0,0.28),
        inset 0 1px 0 rgba(255,255,255,0.04);
}

.hero {
    text-align: center;
    padding: 50px 20px 35px 20px;
}

.logo {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(2rem, 6vw, 4.5rem);
    font-weight: 900;
    letter-spacing: 3px;
    background: linear-gradient(
        90deg,
        #ffffff,
        #61e7ff,
        #9d70ff,
        #ffffff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline {
    color: #8f9bad;
    font-size: 1rem;
    letter-spacing: 3px;
    margin-top: 8px;
}

.big-number {
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    font-weight: 900;
}

.enemy-name {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
}

.question-box {
    text-align: center;
    padding: 30px 15px;
    margin: 15px 0;
    border-radius: 22px;
    background:
        radial-gradient(
            circle at center,
            rgba(0, 200, 255, 0.10),
            rgba(255,255,255,0.025)
        );
    border: 1px solid rgba(0, 220, 255, 0.14);
}

.question-label {
    color: #7f8da5;
    font-size: 0.8rem;
    letter-spacing: 3px;
    font-weight: 800;
}

.question-text {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(1.7rem, 4vw, 3rem);
    font-weight: 900;
    margin-top: 10px;
}

.boss {
    background:
        radial-gradient(
            circle at center,
            rgba(255, 0, 70, 0.18),
            rgba(255,255,255,0.025)
        );
    border: 1px solid rgba(255, 50, 80, 0.35);
}

.combo {
    text-align: center;
    padding: 15px;
    border-radius: 18px;
    background: rgba(255, 140, 0, 0.08);
    border: 1px solid rgba(255, 140, 0, 0.20);
}

.combo-number {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.2rem;
    font-weight: 900;
    color: #ffb347;
}

.powerup {
    text-align: center;
    padding: 12px;
    border-radius: 15px;
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.07);
}

.small-muted {
    color: #7f8da5;
    font-size: 0.85rem;
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: 1px;
}

.result-win {
    text-align: center;
    padding: 45px 20px;
    border-radius: 25px;
    background:
        radial-gradient(
            circle at center,
            rgba(0,255,170,0.14),
            rgba(255,255,255,0.025)
        );
    border: 1px solid rgba(0,255,170,0.20);
}

.result-loss {
    text-align: center;
    padding: 45px 20px;
    border-radius: 25px;
    background:
        radial-gradient(
            circle at center,
            rgba(255,40,70,0.14),
            rgba(255,255,255,0.025)
        );
    border: 1px solid rgba(255,40,70,0.20);
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    margin: 4px;
    border-radius: 999px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    font-size: 0.8rem;
    font-weight: 700;
}

.footer-text {
    text-align: center;
    color: #566174;
    margin-top: 40px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# GAME CONFIG
# ============================================================

DIFFICULTIES = {
    "Basic": {
        "player_hp": 110,
        "enemy_hp": 90,
        "base_damage": 24,
        "enemy_damage": 12,
        "xp": 8,
        "coins": 2,
    },
    "Medium": {
        "player_hp": 105,
        "enemy_hp": 120,
        "base_damage": 25,
        "enemy_damage": 16,
        "xp": 11,
        "coins": 3,
    },
    "Pro": {
        "player_hp": 100,
        "enemy_hp": 155,
        "base_damage": 27,
        "enemy_damage": 20,
        "xp": 15,
        "coins": 4,
    },
    "Master": {
        "player_hp": 95,
        "enemy_hp": 190,
        "base_damage": 30,
        "enemy_damage": 25,
        "xp": 20,
        "coins": 5,
    },
}

ENEMIES = {
    "Basic": [
        ("🔢 Number Goblin", "Goblin"),
        ("➕ Sum Beast", "Beast"),
        ("🧮 Digit Drone", "Drone"),
        ("⚡ Quick Calculator", "Calculator"),
    ],
    "Medium": [
        ("🧟 Equation Raider", "Raider"),
        ("👻 Fraction Phantom", "Phantom"),
        ("🤖 Logic Droid", "Droid"),
        ("⚔️ Algebra Hunter", "Hunter"),
    ],
    "Pro": [
        ("🔥 Prime Destroyer", "Destroyer"),
        ("🧙 Algebra Knight", "Knight"),
        ("💀 Formula Reaper", "Reaper"),
        ("⚡ Matrix Warrior", "Warrior"),
    ],
    "Master": [
        ("👑 Infinity Lord", "Lord"),
        ("☠️ Zero King", "King"),
        ("🌀 Formula Titan", "Titan"),
        ("🌌 Mathematics Overlord", "Overlord"),
    ],
}

BOSSES = [
    ("👑 THE CALCULATOR", "The Calculator"),
    ("☠️ THE ZERO KING", "The Zero King"),
    ("🔥 MATH TITAN", "Math Titan"),
    ("🌌 INFINITY LORD", "Infinity Lord"),
]


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "page": "home",
    "player_name": "",
    "difficulty": "Basic",
    "game_mode": "Endless Arena",

    "player_hp": 100,
    "max_hp": 100,

    "enemy_hp": 100,
    "enemy_max_hp": 100,
    "enemy_name": "Number Goblin",
    "enemy_is_boss": False,

    "round": 1,
    "score": 0,
    "combo": 0,
    "best_combo": 0,

    "xp": 0,
    "coins": 0,

    "total_correct": 0,
    "total_attempts": 0,

    "shield_charges": 0,
    "crit_charges": 0,
    "overdrive_charges": 0,

    "crit_ready": False,
    "overdrive_ready": False,

    "question": "",
    "correct_answer": 0,
    "options": [],

    "used_questions": [],

    "message": "ENTER THE ARENA",
    "message_type": "info",

    "run_history": [],

    "total_runs": 0,
    "wins": 0,
    "losses": 0,

    "achievement_list": [],

    "powerup_awards": [],

    "round_target": 0,

    "last_damage": 0,
    "last_player_damage": 0,

    "result_reason": "",
}


for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def clean_name(name):
    name = str(name).strip()
    if not name:
        return "PLAYER"

    return name[:18]


def format_number(value):
    if isinstance(value, float):
        if value.is_integer():
            return str(int(value))
        return f"{value:.2f}".rstrip("0").rstrip(".")

    return str(value)


def unique_options(correct, candidates):
    values = []

    def add_value(v):
        try:
            if isinstance(v, float):
                v = round(v, 2)

            if v not in values:
                values.append(v)
        except Exception:
            pass

    add_value(correct)

    for candidate in candidates:
        add_value(candidate)

    return values


def make_options(correct):
    candidates = []

    if isinstance(correct, float) and not correct.is_integer():
        correct = round(correct, 2)

        candidates.extend(
            [
                round(correct + 0.5, 2),
                round(correct - 0.5, 2),
                round(correct + 1, 2),
                round(correct - 1, 2),
                round(correct + 2, 2),
                round(correct - 2, 2),
                round(correct + 5, 2),
                round(correct - 5, 2),
            ]
        )

    else:
        correct = int(correct)

        magnitude = max(abs(correct), 5)

        offsets = [
            1,
            -1,
            2,
            -2,
            3,
            -3,
            5,
            -5,
            7,
            -7,
            10,
            -10,
            max(2, magnitude // 2),
            -max(2, magnitude // 2),
        ]

        candidates.extend(correct + x for x in offsets)

    values = unique_options(correct, candidates)

    values = [v for v in values if v != correct][:]

    random.shuffle(values)

    result = [correct]

    for value in values:
        if value != correct and len(result) < 4:
            result.append(value)

    while len(result) < 4:
        if isinstance(correct, float):
            candidate = round(correct + random.uniform(-10, 10), 2)
        else:
            candidate = correct + random.randint(-20, 20)

        if candidate not in result:
            result.append(candidate)

    random.shuffle(result)

    return result


# ============================================================
# QUESTION ENGINE
# ============================================================

def generate_question(difficulty):
    category = random.choice(
        [
            "addition",
            "subtraction",
            "multiplication",
            "division",
            "square",
            "percentage",
            "mixed",
            "equation",
        ]
    )

    if difficulty == "Basic":

        if category == "addition":
            a = random.randint(5, 40)
            b = random.randint(5, 40)

            text = f"{a} + {b}"
            answer = a + b

        elif category == "subtraction":
            a = random.randint(20, 80)
            b = random.randint(5, a)

            text = f"{a} − {b}"
            answer = a - b

        elif category == "multiplication":
            a = random.randint(2, 12)
            b = random.randint(2, 12)

            text = f"{a} × {b}"
            answer = a * b

        elif category == "division":
            b = random.randint(2, 12)
            answer = random.randint(2, 12)
            a = b * answer

            text = f"{a} ÷ {b}"

        elif category == "square":
            a = random.randint(2, 15)

            text = f"{a}²"
            answer = a * a

        else:
            a = random.randint(2, 20)
            b = random.randint(2, 12)

            text = f"{a} × {b} + {random.randint(1, 10)}"
            answer = a * b + int(text.split("+")[1])

    elif difficulty == "Medium":

        if category == "addition":
            a = random.randint(30, 150)
            b = random.randint(20, 150)

            text = f"{a} + {b}"
            answer = a + b

        elif category == "subtraction":
            a = random.randint(100, 400)
            b = random.randint(20, a)

            text = f"{a} − {b}"
            answer = a - b

        elif category == "multiplication":
            a = random.randint(8, 25)
            b = random.randint(5, 20)

            text = f"{a} × {b}"
            answer = a * b

        elif category == "division":
            b = random.randint(3, 20)
            answer = random.randint(4, 30)
            a = b * answer

            text = f"{a} ÷ {b}"

        elif category == "square":
            a = random.randint(8, 25)

            text = f"{a}²"
            answer = a * a

        elif category == "percentage":
            percent = random.choice([10, 20, 25, 30, 50])
            base = random.choice([40, 60, 80, 100, 120, 200])

            text = f"{percent}% of {base}"
            answer = base * percent / 100

        else:
            a = random.randint(5, 30)
            b = random.randint(3, 15)
            c = random.randint(1, 20)

            text = f"{a} × {b} − {c}"
            answer = a * b - c

    elif difficulty == "Pro":

        if category == "addition":
            a = random.randint(100, 500)
            b = random.randint(100, 500)

            text = f"{a} + {b}"
            answer = a + b

        elif category == "subtraction":
            a = random.randint(300, 1000)
            b = random.randint(50, a)

            text = f"{a} − {b}"
            answer = a - b

        elif category == "multiplication":
            a = random.randint(12, 40)
            b = random.randint(10, 35)

            text = f"{a} × {b}"
            answer = a * b

        elif category == "division":
            b = random.randint(5, 30)
            answer = random.randint(10, 50)
            a = b * answer

            text = f"{a} ÷ {b}"

        elif category == "square":
            a = random.randint(15, 40)

            text = f"{a}²"
            answer = a * a

        elif category == "percentage":
            percent = random.choice([12.5, 15, 20, 25, 30, 40])
            base = random.choice([80, 120, 160, 200, 240, 400])

            text = f"{percent}% of {base}"
            answer = round(base * percent / 100, 2)

        else:
            a = random.randint(10, 40)
            b = random.randint(5, 20)
            c = random.randint(5, 30)

            text = f"({a} + {b}) × {c}"
            answer = (a + b) * c

    else:

        if category == "addition":
            a = random.randint(300, 1500)
            b = random.randint(300, 1500)

            text = f"{a} + {b}"
            answer = a + b

        elif category == "subtraction":
            a = random.randint(800, 3000)
            b = random.randint(100, a)

            text = f"{a} − {b}"
            answer = a - b

        elif category == "multiplication":
            a = random.randint(20, 60)
            b = random.randint(15, 50)

            text = f"{a} × {b}"
            answer = a * b

        elif category == "division":
            b = random.randint(8, 40)
            answer = random.randint(20, 100)
            a = b * answer

            text = f"{a} ÷ {b}"

        elif category == "square":
            a = random.randint(25, 70)

            text = f"{a}²"
            answer = a * a

        elif category == "percentage":
            percent = random.choice([12.5, 15, 17.5, 22.5, 25, 35])
            base = random.choice([160, 240, 320, 400, 480, 800])

            text = f"{percent}% of {base}"
            answer = round(base * percent / 100, 2)

        elif category == "equation":
            x = random.randint(5, 30)
            a = random.randint(2, 9)
            b = random.randint(5, 30)

            total = a * x + b

            text = f"{a}x + {b} = {total}"
            answer = x

        else:
            a = random.randint(10, 50)
            b = random.randint(5, 25)
            c = random.randint(2, 10)

            text = f"({a} + {b}) × {c} − {random.randint(5, 25)}"

            minus = int(text.split("−")[1])

            answer = (a + b) * c - minus

    return text, answer


def create_new_question():
    difficulty = st.session_state.difficulty

    attempts = 0

    while attempts < 100:
        question, answer = generate_question(difficulty)

        identifier = f"{question}|{answer}"

        if identifier not in st.session_state.used_questions:
            st.session_state.used_questions.append(identifier)

            if len(st.session_state.used_questions) > 100:
                st.session_state.used_questions.pop(0)

            st.session_state.question = question
            st.session_state.correct_answer = answer
            st.session_state.options = make_options(answer)

            return

        attempts += 1

    # Emergency fallback
    question, answer = generate_question(difficulty)

    st.session_state.question = question
    st.session_state.correct_answer = answer
    st.session_state.options = make_options(answer)


# ============================================================
# ENEMY SYSTEM
# ============================================================

def setup_enemy():
    difficulty = st.session_state.difficulty
    config = DIFFICULTIES[difficulty]

    round_number = st.session_state.round

    is_boss = round_number % 5 == 0

    st.session_state.enemy_is_boss = is_boss

    if is_boss:
        boss = random.choice(BOSSES)

        st.session_state.enemy_name = boss[0]

        multiplier = 2.25 + ((round_number // 5) - 1) * 0.25

        hp = int(config["enemy_hp"] * multiplier)

    else:
        enemy = random.choice(ENEMIES[difficulty])

        st.session_state.enemy_name = enemy[0]

        scaling = 1 + max(0, round_number - 1) * 0.08

        hp = int(config["enemy_hp"] * scaling)

    st.session_state.enemy_max_hp = hp
    st.session_state.enemy_hp = hp

    create_new_question()


# ============================================================
# GAME START
# ============================================================

def start_game():
    name = clean_name(st.session_state.player_name)

    st.session_state.player_name = name

    difficulty = st.session_state.difficulty
    config = DIFFICULTIES[difficulty]

    st.session_state.player_hp = config["player_hp"]
    st.session_state.max_hp = config["player_hp"]

    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.combo = 0
    st.session_state.best_combo = 0

    st.session_state.xp = 0
    st.session_state.coins = 0

    st.session_state.total_correct = 0
    st.session_state.total_attempts = 0

    st.session_state.shield_charges = 0
    st.session_state.crit_charges = 0
    st.session_state.overdrive_charges = 0

    st.session_state.crit_ready = False
    st.session_state.overdrive_ready = False

    st.session_state.used_questions = []
    st.session_state.powerup_awards = []

    st.session_state.last_damage = 0
    st.session_state.last_player_damage = 0

    if st.session_state.game_mode == "Quick Battle":
        st.session_state.round_target = 5
    else:
        st.session_state.round_target = 0

    st.session_state.message = "BATTLE START!"
    st.session_state.message_type = "success"

    setup_enemy()

    st.session_state.page = "battle"


# ============================================================
# COMBO SYSTEM
# ============================================================

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


# ============================================================
# POWERUP SYSTEM
# ============================================================

def check_powerups():
    combo = st.session_state.combo

    awards = st.session_state.powerup_awards

    if combo >= 3 and "shield3" not in awards:
        st.session_state.shield_charges += 1
        awards.append("shield3")

    if combo >= 5 and "crit5" not in awards:
        st.session_state.crit_charges += 1
        awards.append("crit5")

    if combo >= 8 and "overdrive8" not in awards:
        st.session_state.overdrive_charges += 1
        awards.append("overdrive8")


def activate_shield():
    if st.session_state.shield_charges > 0:
        st.session_state.shield_charges -= 1
        st.session_state.message = "🛡️ SHIELD ACTIVATED!"
        st.session_state.message_type = "success"
        st.rerun()


def activate_crit():
    if st.session_state.crit_charges > 0:
        st.session_state.crit_charges -= 1
        st.session_state.crit_ready = True
        st.session_state.message = "💥 CRITICAL ATTACK READY!"
        st.session_state.message_type = "success"
        st.rerun()


def activate_overdrive():
    if st.session_state.overdrive_charges > 0:
        st.session_state.overdrive_charges -= 1
        st.session_state.overdrive_ready = True
        st.session_state.message = "⚡ OVERDRIVE READY!"
        st.session_state.message_type = "success"
        st.rerun()


def heal_player():
    cost = 5

    if st.session_state.coins < cost:
        st.session_state.message = "❌ NOT ENOUGH COINS"
        st.session_state.message_type = "error"
        st.rerun()

    if st.session_state.player_hp >= st.session_state.max_hp:
        st.session_state.message = "❤️ HP IS ALREADY FULL"
        st.session_state.message_type = "info"
        st.rerun()

    st.session_state.coins -= cost

    st.session_state.player_hp = min(
        st.session_state.max_hp,
        st.session_state.player_hp + 25,
    )

    st.session_state.message = "❤️ +25 HP"
    st.session_state.message_type = "success"

    st.rerun()


# ============================================================
# ACHIEVEMENTS
# ============================================================

def get_achievements():
    achievements = []

    if st.session_state.total_correct >= 1:
        achievements.append("🎯 First Hit")

    if st.session_state.best_combo >= 3:
        achievements.append("🔥 Combo Starter")

    if st.session_state.best_combo >= 5:
        achievements.append("🔥 Combo Hunter")

    if st.session_state.best_combo >= 10:
        achievements.append("👑 Combo Master")

    if st.session_state.score >= 500:
        achievements.append("💰 Score Grinder")

    if st.session_state.score >= 1500:
        achievements.append("⚡ Math Machine")

    if st.session_state.round >= 5:
        achievements.append("🛡️ Arena Survivor")

    if st.session_state.round >= 10:
        achievements.append("💀 Elite Fighter")

    if st.session_state.total_correct >= 25:
        achievements.append("🧠 Brain Power")

    return achievements


# ============================================================
# FINISH RUN
# ============================================================

def finish_run(victory, reason):
    achievements = get_achievements()

    st.session_state.achievement_list = achievements

    if victory:
        st.session_state.wins += 1
    else:
        st.session_state.losses += 1

    st.session_state.total_runs += 1

    record = {
        "player": st.session_state.player_name,
        "score": st.session_state.score,
        "difficulty": st.session_state.difficulty,
        "mode": st.session_state.game_mode,
        "round": st.session_state.round,
        "combo": st.session_state.best_combo,
        "correct": st.session_state.total_correct,
        "result": "VICTORY" if victory else "DEFEATED",
    }

    st.session_state.run_history.append(record)

    if len(st.session_state.run_history) > 20:
        st.session_state.run_history = st.session_state.run_history[-20:]

    st.session_state.result_reason = reason

    st.session_state.page = "result"


# ============================================================
# ANSWER ENGINE
# ============================================================

def answer_question(selected):
    correct = st.session_state.correct_answer

    st.session_state.total_attempts += 1

    if selected == correct:

        st.session_state.total_correct += 1

        st.session_state.combo += 1

        st.session_state.best_combo = max(
            st.session_state.best_combo,
            st.session_state.combo,
        )

        check_powerups()

        config = DIFFICULTIES[st.session_state.difficulty]

        multiplier = combo_multiplier(st.session_state.combo)

        damage = int(config["base_damage"] * multiplier)

        critical_used = False
        overdrive_used = False

        if st.session_state.crit_ready:
            damage *= 2
            st.session_state.crit_ready = False
            critical_used = True

        if st.session_state.overdrive_ready:
            damage *= 3
            st.session_state.overdrive_ready = False
            overdrive_used = True

        if st.session_state.enemy_is_boss:
            damage = int(damage * 0.92)

        damage = max(1, damage)

        st.session_state.enemy_hp -= damage

        st.session_state.last_damage = damage
        st.session_state.last_player_damage = 0

        xp_gain = config["xp"]

        coin_gain = config["coins"]

        combo_bonus = max(0, st.session_state.combo - 2)

        xp_gain += combo_bonus

        coin_gain += combo_bonus // 3

        if critical_used:
            coin_gain += 2

        if overdrive_used:
            coin_gain += 5

        if st.session_state.enemy_is_boss:
            xp_gain *= 3
            coin_gain *= 3

        st.session_state.xp += xp_gain
        st.session_state.coins += coin_gain

        st.session_state.score += damage * 10

        if overdrive_used:
            st.session_state.message = (
                f"⚡ OVERDRIVE! {damage} DAMAGE!"
            )

        elif critical_used:
            st.session_state.message = (
                f"💥 CRITICAL HIT! {damage} DAMAGE!"
            )

        elif st.session_state.combo >= 8:
            st.session_state.message = (
                f"🔥 FEVER ATTACK! {damage} DAMAGE!"
            )

        else:
            st.session_state.message = (
                f"⚔️ HIT! -{damage} HP"
            )

        st.session_state.message_type = "success"

        # Enemy defeated
        if st.session_state.enemy_hp <= 0:

            boss_defeated = st.session_state.enemy_is_boss

            reward = 100 if boss_defeated else 25

            st.session_state.score += reward

            st.session_state.coins += reward // 5

            if boss_defeated:
                st.session_state.message = (
                    f"👑 BOSS DEFEATED! +{reward} SCORE"
                )
            else:
                st.session_state.message = (
                    f"💀 ENEMY DEFEATED! +{reward} SCORE"
                )

            # Quick Battle completed
            if (
                st.session_state.game_mode == "Quick Battle"
                and st.session_state.round >= st.session_state.round_target
            ):
                finish_run(
                    True,
                    "You cleared all five battles.",
                )
                return

            # Next enemy
            st.session_state.round += 1

            setup_enemy()

            return

        create_new_question()

    else:

        st.session_state.combo = 0

        config = DIFFICULTIES[st.session_state.difficulty]

        damage = config["enemy_damage"]

        if st.session_state.enemy_is_boss:
            damage = int(damage * 1.25)

        # Shield blocks the attack
        if st.session_state.shield_charges > 0:

            st.session_state.shield_charges -= 1

            st.session_state.last_player_damage = 0

            st.session_state.message = (
                "🛡️ SHIELD BLOCKED THE ATTACK!"
            )

            st.session_state.message_type = "success"

        else:

            st.session_state.player_hp -= damage

            st.session_state.last_player_damage = damage

            st.session_state.message = (
                f"💀 WRONG! ENEMY HITS YOU -{damage} HP"
            )

            st.session_state.message_type = "error"

        if st.session_state.player_hp <= 0:

            st.session_state.player_hp = 0

            finish_run(
                False,
                "Your HP reached zero.",
            )

            return

        create_new_question()


# ============================================================
# HOME SCREEN
# ============================================================

def show_home():

    st.markdown(
        """
        <div class="hero">
            <div class="logo">⚔️ MATHS ARENA PRO</div>
            <div class="tagline">
                THINK FAST • ATTACK SMART • MASTER MATHEMATICS
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="arena-card">
            <h2 style="text-align:center;">
                🏟️ WELCOME TO THE ARENA
            </h2>

            <p style="text-align:center;color:#8f9bad;">
                This isn't a boring maths test.
                Every correct answer becomes an attack.
                Build combos, defeat enemies, unlock power-ups
                and survive the arena.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    left, center, right = st.columns([1, 1.4, 1])

    with center:

        st.markdown("### 👤 PLAYER")

        name = st.text_input(
            "Your fighter name",
            value=st.session_state.player_name,
            max_chars=18,
            placeholder="Enter your name...",
            label_visibility="collapsed",
        )

        st.session_state.player_name = clean_name(name)

        st.write("")

        st.markdown("### 🎮 GAME MODE")

        mode = st.selectbox(
            "Mode",
            [
                "Endless Arena",
                "Quick Battle",
            ],
            index=0 if st.session_state.game_mode == "Endless Arena" else 1,
            label_visibility="collapsed",
        )

        st.session_state.game_mode = mode

        st.write("")

        st.markdown("### ⚔️ DIFFICULTY")

        difficulty = st.selectbox(
            "Difficulty",
            [
                "Basic",
                "Medium",
                "Pro",
                "Master",
            ],
            index=[
                "Basic",
                "Medium",
                "Pro",
                "Master",
            ].index(st.session_state.difficulty),
            label_visibility="collapsed",
        )

        st.session_state.difficulty = difficulty

        st.write("")

        if st.button(
            "⚔️ ENTER THE ARENA",
            type="primary",
            use_container_width=True,
        ):
            start_game()
            st.rerun()

    st.write("")
    st.write("")

    st.markdown(
        "### 🎮 WHAT'S INSIDE",
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="powerup">
                <div style="font-size:2rem;">🔥</div>
                <b>COMBOS</b>
                <div class="small-muted">
                    Chain correct answers
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="powerup">
                <div style="font-size:2rem;">👑</div>
                <b>BOSSES</b>
                <div class="small-muted">
                    Every 5th round
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="powerup">
                <div style="font-size:2rem;">⚡</div>
                <b>POWER-UPS</b>
                <div class="small-muted">
                    Fight smarter
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            """
            <div class="powerup">
                <div style="font-size:2rem;">🏆</div>
                <b>XP + COINS</b>
                <div class="small-muted">
                    Build your run
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    if st.session_state.run_history:

        st.markdown("### 🏆 LOCAL HALL OF FAME")

        sorted_runs = sorted(
            st.session_state.run_history,
            key=lambda x: x["score"],
            reverse=True,
        )[:5]

        for index, run in enumerate(sorted_runs, 1):

            medal = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"][index - 1]

            st.markdown(
                f"""
                <div class="arena-card" style="margin-bottom:8px;padding:14px 18px;">
                    <b>{medal} {html.escape(str(run["player"]))}</b>
                    &nbsp;&nbsp;
                    <span style="color:#61e7ff;">
                        {run["score"]} XP-SCORE
                    </span>
                    &nbsp;&nbsp;
                    <span class="small-muted">
                        {run["difficulty"]} • {run["result"]}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="footer-text">
            MATHS ARENA PRO • Built for brains that love challenges ⚔️
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BATTLE SCREEN
# ============================================================

def show_battle():

    # Top navigation
    nav1, nav2, nav3, nav4, nav5 = st.columns(
        [1.5, 1, 1, 1, 1]
    )

    with nav1:
        st.markdown(
            "### ⚔️ MATHS ARENA"
        )

    with nav2:
        st.metric(
            "ROUND",
            st.session_state.round,
        )

    with nav3:
        st.metric(
            "SCORE",
            st.session_state.score,
        )

    with nav4:
        st.metric(
            "COINS",
            f"🪙 {st.session_state.coins}",
        )

    with nav5:
        st.metric(
            "XP",
            st.session_state.xp,
        )

    st.write("")

    # --------------------------------------------------------
    # Player / Enemy HUD
    # --------------------------------------------------------

    player_col, vs_col, enemy_col = st.columns(
        [1, 0.35, 1]
    )

    with player_col:

        st.markdown(
            f"""
            <div class="arena-card">
                <div class="small-muted">YOUR FIGHTER</div>
                <div class="enemy-name">
                    🧑 {html.escape(st.session_state.player_name)}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        hp_percent = (
            st.session_state.player_hp
            / st.session_state.max_hp
        )

        hp_percent = max(0.0, min(1.0, hp_percent))

        st.progress(
            hp_percent,
            text=f"❤️ HP {st.session_state.player_hp}/{st.session_state.max_hp}",
        )

    with vs_col:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding-top:35px;
                font-family:Orbitron;
                font-size:1.4rem;
                font-weight:900;
            ">
                VS
            </div>
            """,
            unsafe_allow_html=True,
        )

    with enemy_col:

        enemy_class = (
            "boss"
            if st.session_state.enemy_is_boss
            else ""
        )

        st.markdown(
            f"""
            <div class="arena-card {enemy_class}">
                <div class="small-muted">
                    {"👑 BOSS BATTLE" if st.session_state.enemy_is_boss else "ENEMY"}
                </div>

                <div class="enemy-name">
                    {st.session_state.enemy_name}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        enemy_percent = (
            st.session_state.enemy_hp
            / st.session_state.enemy_max_hp
        )

        enemy_percent = max(0.0, min(1.0, enemy_percent))

        st.progress(
            enemy_percent,
            text=f"💀 HP {st.session_state.enemy_hp}/{st.session_state.enemy_max_hp}",
        )

    st.write("")

    # --------------------------------------------------------
    # Combo HUD
    # --------------------------------------------------------

    combo_col, fever_col = st.columns([1, 2])

    with combo_col:

        st.markdown(
            f"""
            <div class="combo">
                <div class="small-muted">CURRENT COMBO</div>
                <div class="combo-number">
                    🔥 {st.session_state.combo}
                </div>
                <div class="small-muted">
                    Best: {st.session_state.best_combo}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with fever_col:

        multiplier = combo_multiplier(
            st.session_state.combo
        )

        st.markdown(
            f"""
            <div class="arena-card">
                <b>🔥 COMBAT MULTIPLIER</b>
                <div style="
                    font-family:Orbitron;
                    font-size:1.7rem;
                    margin-top:8px;
                ">
                    x{multiplier}
                </div>

                <div class="small-muted">
                    {
                        "🔥 FEVER MODE ACTIVE"
                        if st.session_state.combo >= 8
                        else "Keep answering correctly to increase damage."
                    }
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # --------------------------------------------------------
    # Message
    # --------------------------------------------------------

    if st.session_state.message_type == "success":
        st.success(
            st.session_state.message
        )

    elif st.session_state.message_type == "error":
        st.error(
            st.session_state.message
        )

    else:
        st.info(
            st.session_state.message
        )

    # --------------------------------------------------------
    # Question
    # --------------------------------------------------------

    question_class = (
        "question-box boss"
        if st.session_state.enemy_is_boss
        else "question-box"
    )

    st.markdown(
        f"""
        <div class="{question_class}">
            <div class="question-label">
                ⚔️ CHOOSE YOUR ATTACK
            </div>

            <div class="question-text">
                {html.escape(str(st.session_state.question))}
                = ?
            </div>

            <div class="small-muted" style="margin-top:12px;">
                Solve the equation to damage the enemy.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # --------------------------------------------------------
    # Answer buttons
    # --------------------------------------------------------

    options = st.session_state.options

    col1, col2 = st.columns(2)

    for index, option in enumerate(options):

        target_col = col1 if index % 2 == 0 else col2

        with target_col:

            label = f"⚔️  {format_number(option)}"

            if st.button(
                label,
                key=f"answer_{st.session_state.round}_{index}_{st.session_state.total_attempts}",
                use_container_width=True,
            ):
                answer_question(option)
                st.rerun()

    st.write("")

    # --------------------------------------------------------
    # Powerups
    # --------------------------------------------------------

    st.markdown(
        "### ⚡ POWER-UPS"
    )

    p1, p2, p3, p4 = st.columns(4)

    with p1:

        st.markdown(
            f"""
            <div class="powerup">
                🛡️ <b>SHIELD</b><br>
                <span class="small-muted">
                    Charges: {st.session_state.shield_charges}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Activate Shield",
            key="shield_button",
            disabled=st.session_state.shield_charges <= 0,
        ):
            activate_shield()

    with p2:

        st.markdown(
            f"""
            <div class="powerup">
                💥 <b>CRIT</b><br>
                <span class="small-muted">
                    Charges: {st.session_state.crit_charges}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Prepare Crit",
            key="crit_button",
            disabled=(
                st.session_state.crit_charges <= 0
                or st.session_state.crit_ready
            ),
        ):
            activate_crit()

    with p3:

        st.markdown(
            f"""
            <div class="powerup">
                ⚡ <b>OVERDRIVE</b><br>
                <span class="small-muted">
                    Charges: {st.session_state.overdrive_charges}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Prepare Overdrive",
            key="overdrive_button",
            disabled=(
                st.session_state.overdrive_charges <= 0
                or st.session_state.overdrive_ready
            ),
        ):
            activate_overdrive()

    with p4:

        st.markdown(
            """
            <div class="powerup">
                ❤️ <b>HEAL</b><br>
                <span class="small-muted">
                    Costs 5 coins • +25 HP
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Heal",
            key="heal_button",
            disabled=(
                st.session_state.coins < 5
                or st.session_state.player_hp >= st.session_state.max_hp
            ),
        ):
            heal_player()

    st.write("")

    # --------------------------------------------------------
    # Active buffs
    # --------------------------------------------------------

    active = []

    if st.session_state.crit_ready:
        active.append("💥 CRIT READY")

    if st.session_state.overdrive_ready:
        active.append("⚡ OVERDRIVE READY")

    if st.session_state.shield_charges:
        active.append(
            f"🛡️ {st.session_state.shield_charges} SHIELD"
        )

    if active:

        st.markdown(
            " ".join(
                f'<span class="badge">{html.escape(x)}</span>'
                for x in active
            ),
            unsafe_allow_html=True,
        )

    st.write("")

    # --------------------------------------------------------
    # Game controls
    # --------------------------------------------------------

    c1, c2, c3 = st.columns([1, 1, 1])

    with c2:

        if st.button(
            "🏳️ END RUN",
            key="end_run",
            use_container_width=True,
        ):
            finish_run(
                False,
                "You ended the run manually.",
            )
            st.rerun()


# ============================================================
# RESULT SCREEN
# ============================================================

def show_result():

    victory = (
        st.session_state.result_reason
        == "You cleared all five battles."
    )

    if victory:

        st.markdown(
            """
            <div class="result-win">
                <div style="font-size:4rem;">🏆</div>

                <h1>ARENA CLEARED</h1>

                <p style="color:#8f9bad;">
                    You defeated every enemy in the Quick Battle.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            """
            <div class="result-loss">
                <div style="font-size:4rem;">💀</div>

                <h1>RUN OVER</h1>

                <p style="color:#8f9bad;">
                    The arena defeated you this time.
                    Your next run starts from zero.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "SCORE",
            st.session_state.score,
        )

    with c2:
        st.metric(
            "BEST COMBO",
            st.session_state.best_combo,
        )

    with c3:
        st.metric(
            "CORRECT",
            st.session_state.total_correct,
        )

    with c4:
        st.metric(
            "COINS",
            f"🪙 {st.session_state.coins}",
        )

    st.write("")

    st.markdown(
        "### 🏅 ACHIEVEMENTS"
    )

    achievements = st.session_state.achievement_list

    if achievements:

        badges = " ".join(
            f'<span class="badge">{html.escape(x)}</span>'
            for x in achievements
        )

        st.markdown(
            badges,
            unsafe_allow_html=True,
        )

    else:

        st.info(
            "No achievements yet. Start another run!"
        )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⚔️ PLAY AGAIN",
            type="primary",
            use_container_width=True,
        ):
            start_game()
            st.rerun()

    with col2:

        if st.button(
            "🏠 BACK TO HOME",
            use_container_width=True,
        ):
            st.session_state.page = "home"
            st.rerun()

    st.write("")

    # --------------------------------------------------------
    # Recent Runs
    # --------------------------------------------------------

    st.markdown(
        "### 📜 RECENT RUNS"
    )

    if st.session_state.run_history:

        recent = list(
            reversed(
                st.session_state.run_history[-8:]
            )
        )

        for run in recent:

            result_icon = (
                "🏆"
                if run["result"] == "VICTORY"
                else "💀"
            )

            st.markdown(
                f"""
                <div class="arena-card" style="
                    margin-bottom:10px;
                    padding:15px;
                ">
                    <b>
                        {result_icon}
                        {html.escape(str(run["player"]))}
                    </b>

                    <span class="small-muted">
                        &nbsp; {run["difficulty"]}
                        &nbsp; • &nbsp; {run["mode"]}
                        &nbsp; • &nbsp; Round {run["round"]}
                    </span>

                    <br>

                    <span style="color:#61e7ff;">
                        Score: {run["score"]}
                    </span>

                    &nbsp;&nbsp;

                    <span style="color:#ffb347;">
                        Combo: {run["combo"]}
                    </span>

                    &nbsp;&nbsp;

                    <span class="small-muted">
                        Correct: {run["correct"]}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# PROFILE / STATS
# ============================================================

def show_profile():

    st.markdown(
        "## 👤 PLAYER PROFILE"
    )

    name = st.session_state.player_name or "PLAYER"

    total_runs = st.session_state.total_runs

    win_rate = (
        (st.session_state.wins / total_runs) * 100
        if total_runs > 0
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "PLAYER",
            name,
        )

    with c2:
        st.metric(
            "RUNS",
            total_runs,
        )

    with c3:
        st.metric(
            "VICTORIES",
            st.session_state.wins,
        )

    with c4:
        st.metric(
            "WIN RATE",
            f"{win_rate:.0f}%",
        )

    st.write("")

    st.markdown(
        """
        <div class="arena-card">
            <h3>🎮 CURRENT SESSION</h3>
            <p class="small-muted">
                Your statistics are stored in this browser session.
                This version intentionally doesn't use SQLite,
                so you don't get the old database-schema errors.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "🏠 BACK HOME",
        use_container_width=True,
    ):
        st.session_state.page = "home"
        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## ⚔️ MATHS ARENA PRO"
    )

    st.caption(
        "Turn mathematics into combat."
    )

    if st.session_state.page == "battle":

        st.write("")

        st.markdown(
            f"""
            **Player:** {st.session_state.player_name}

            **Difficulty:** {st.session_state.difficulty}

            **Mode:** {st.session_state.game_mode}

            **Round:** {st.session_state.round}

            **Score:** {st.session_state.score}

            **Combo:** 🔥 {st.session_state.combo}

            **Coins:** 🪙 {st.session_state.coins}
            """
        )

        st.write("")

        if st.button(
            "🏳️ End Current Run",
            use_container_width=True,
        ):
            finish_run(
                False,
                "You ended the run from the menu.",
            )
            st.rerun()

    else:

        if st.button(
            "🏠 Home",
            use_container_width=True,
        ):
            st.session_state.page = "home"
            st.rerun()

        if st.button(
            "👤 Profile",
            use_container_width=True,
        ):
            st.session_state.page = "profile"
            st.rerun()


# ============================================================
# PAGE ROUTER
# ============================================================

if st.session_state.page == "home":

    show_home()

elif st.session_state.page == "battle":

    show_battle()

elif st.session_state.page == "result":

    show_result()

elif st.session_state.page == "profile":

    show_profile()

else:

    st.session_state.page = "home"
    st.rerun()
