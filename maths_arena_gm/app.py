import random
import streamlit as st

# ============================================================
# MATHS ARENA PRO
# Complete single-file game
# No database
# No API
# No JavaScript
# ============================================================

st.set_page_config(
    page_title="Maths Arena Pro",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS - ONLY FOR THEME / VISUAL POLISH
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(87, 45, 255, .16), transparent 28%),
            radial-gradient(circle at 90% 15%, rgba(0, 210, 255, .10), transparent 25%),
            radial-gradient(circle at 50% 100%, rgba(255, 0, 120, .08), transparent 35%),
            #06070c;
        color: white;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
    }

    .arena-title {
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(2rem, 6vw, 4.5rem);
        font-weight: 900;
        letter-spacing: 3px;
        margin-top: 15px;
        background: linear-gradient(
            90deg,
            #ffffff,
            #66e8ff,
            #a57cff,
            #ffffff
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .arena-subtitle {
        text-align: center;
        color: #8b96a8;
        letter-spacing: 3px;
        font-size: .85rem;
        margin-bottom: 35px;
    }

    .game-card {
        padding: 24px;
        border-radius: 22px;
        border: 1px solid rgba(255,255,255,.09);
        background: rgba(255,255,255,.035);
        box-shadow: 0 18px 50px rgba(0,0,0,.25);
        margin-bottom: 15px;
    }

    .battle-question {
        text-align: center;
        padding: 28px 15px;
        border-radius: 22px;
        border: 1px solid rgba(0,220,255,.15);
        background:
            radial-gradient(
                circle,
                rgba(0,210,255,.09),
                rgba(255,255,255,.02)
            );
        margin: 18px 0;
    }

    .question-label {
        color: #8490a5;
        font-size: .75rem;
        font-weight: 800;
        letter-spacing: 3px;
    }

    .question-number {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 900;
        margin-top: 10px;
    }

    .boss-card {
        border: 1px solid rgba(255,55,80,.35);
        background:
            radial-gradient(
                circle,
                rgba(255,35,70,.14),
                rgba(255,255,255,.02)
            );
    }

    .win-card {
        text-align: center;
        padding: 40px 20px;
        border-radius: 25px;
        border: 1px solid rgba(0,255,170,.25);
        background: rgba(0,255,170,.05);
    }

    .lose-card {
        text-align: center;
        padding: 40px 20px;
        border-radius: 25px;
        border: 1px solid rgba(255,40,70,.25);
        background: rgba(255,40,70,.05);
    }

    .small-text {
        color: #818ca0;
        font-size: .85rem;
    }

    .big-combo {
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        font-weight: 900;
    }

    .section-label {
        font-family: 'Orbitron', sans-serif;
        font-weight: 800;
        letter-spacing: 1px;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# CONFIG
# ============================================================

DIFFICULTY = {
    "Basic": {
        "hp": 110,
        "enemy_hp": 90,
        "damage": 24,
        "enemy_damage": 12,
        "xp": 8,
        "coins": 2,
    },
    "Medium": {
        "hp": 105,
        "enemy_hp": 120,
        "damage": 26,
        "enemy_damage": 16,
        "xp": 11,
        "coins": 3,
    },
    "Pro": {
        "hp": 100,
        "enemy_hp": 155,
        "damage": 29,
        "enemy_damage": 20,
        "xp": 15,
        "coins": 4,
    },
    "Master": {
        "hp": 95,
        "enemy_hp": 190,
        "damage": 32,
        "enemy_damage": 25,
        "xp": 20,
        "coins": 5,
    },
}

NORMAL_ENEMIES = {
    "Basic": [
        "🔢 Number Goblin",
        "➕ Sum Beast",
        "🤖 Digit Drone",
        "⚡ Quick Calculator",
    ],
    "Medium": [
        "👻 Fraction Phantom",
        "⚔️ Equation Raider",
        "🤖 Logic Droid",
        "🔥 Algebra Hunter",
    ],
    "Pro": [
        "💀 Formula Reaper",
        "⚔️ Algebra Knight",
        "🔥 Prime Destroyer",
        "⚡ Matrix Warrior",
    ],
    "Master": [
        "👑 Infinity Lord",
        "☠️ Zero King",
        "🌀 Formula Titan",
        "🌌 Math Overlord",
    ],
}

BOSSES = [
    "👑 THE CALCULATOR",
    "☠️ THE ZERO KING",
    "🔥 MATH TITAN",
    "🌌 INFINITY LORD",
]

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "screen": "home",

    "name": "Dilshad",
    "difficulty": "Medium",
    "mode": "Endless Arena",

    "player_hp": 100,
    "max_hp": 100,

    "enemy_hp": 100,
    "enemy_max_hp": 100,
    "enemy_name": "Number Goblin",
    "boss": False,

    "round": 1,

    "score": 0,
    "xp": 0,
    "coins": 0,

    "combo": 0,
    "best_combo": 0,

    "correct": 0,
    "attempts": 0,

    "question": "",
    "answer": 0,
    "options": [],

    "shield": 0,
    "crit": 0,
    "overdrive": 0,

    "crit_ready": False,
    "overdrive_ready": False,

    "used_questions": [],

    "message": "",
    "message_kind": "info",

    "history": [],

    "wins": 0,
    "losses": 0,

    "result": "",

    "achievements": [],
}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# QUESTION GENERATOR
# ============================================================

def make_question(difficulty):

    kind = random.choice([
        "addition",
        "subtraction",
        "multiplication",
        "division",
        "square",
        "percentage",
        "mixed",
        "equation",
    ])

    if difficulty == "Basic":

        if kind == "addition":

            a = random.randint(5, 40)
            b = random.randint(5, 40)

            return f"{a} + {b}", a + b

        if kind == "subtraction":

            a = random.randint(20, 80)
            b = random.randint(5, a)

            return f"{a} − {b}", a - b

        if kind == "multiplication":

            a = random.randint(2, 12)
            b = random.randint(2, 12)

            return f"{a} × {b}", a * b

        if kind == "division":

            b = random.randint(2, 12)
            answer = random.randint(2, 12)
            a = b * answer

            return f"{a} ÷ {b}", answer

        if kind == "square":

            a = random.randint(2, 15)

            return f"{a}²", a * a

        a = random.randint(2, 15)
        b = random.randint(2, 10)
        c = random.randint(1, 10)

        return f"{a} × {b} + {c}", a * b + c

    if difficulty == "Medium":

        if kind == "addition":

            a = random.randint(30, 200)
            b = random.randint(30, 200)

            return f"{a} + {b}", a + b

        if kind == "subtraction":

            a = random.randint(100, 500)
            b = random.randint(20, a)

            return f"{a} − {b}", a - b

        if kind == "multiplication":

            a = random.randint(5, 25)
            b = random.randint(5, 20)

            return f"{a} × {b}", a * b

        if kind == "division":

            b = random.randint(3, 20)
            answer = random.randint(4, 30)
            a = b * answer

            return f"{a} ÷ {b}", answer

        if kind == "square":

            a = random.randint(8, 25)

            return f"{a}²", a * a

        if kind == "percentage":

            percentage = random.choice(
                [10, 20, 25, 30, 50]
            )

            base = random.choice(
                [40, 60, 80, 100, 120, 200]
            )

            answer = base * percentage / 100

            return (
                f"{percentage}% of {base}",
                answer,
            )

        a = random.randint(5, 30)
        b = random.randint(3, 15)
        c = random.randint(1, 20)

        return (
            f"{a} × {b} − {c}",
            a * b - c,
        )

    if difficulty == "Pro":

        if kind == "addition":

            a = random.randint(100, 700)
            b = random.randint(100, 700)

            return f"{a} + {b}", a + b

        if kind == "subtraction":

            a = random.randint(400, 1500)
            b = random.randint(50, a)

            return f"{a} − {b}", a - b

        if kind == "multiplication":

            a = random.randint(12, 40)
            b = random.randint(10, 35)

            return f"{a} × {b}", a * b

        if kind == "division":

            b = random.randint(5, 30)
            answer = random.randint(10, 50)
            a = b * answer

            return f"{a} ÷ {b}", answer

        if kind == "square":

            a = random.randint(15, 40)

            return f"{a}²", a * a

        if kind == "percentage":

            percentage = random.choice(
                [12.5, 15, 20, 25, 30, 40]
            )

            base = random.choice(
                [80, 120, 160, 200, 240, 400]
            )

            answer = round(
                base * percentage / 100,
                2,
            )

            return (
                f"{percentage}% of {base}",
                answer,
            )

        a = random.randint(10, 40)
        b = random.randint(5, 20)
        c = random.randint(5, 30)

        return (
            f"({a} + {b}) × {c}",
            (a + b) * c,
        )

    # MASTER

    if kind == "addition":

        a = random.randint(300, 1500)
        b = random.randint(300, 1500)

        return f"{a} + {b}", a + b

    if kind == "subtraction":

        a = random.randint(800, 3000)
        b = random.randint(100, a)

        return f"{a} − {b}", a - b

    if kind == "multiplication":

        a = random.randint(20, 60)
        b = random.randint(15, 50)

        return f"{a} × {b}", a * b

    if kind == "division":

        b = random.randint(8, 40)
        answer = random.randint(20, 100)
        a = b * answer

        return f"{a} ÷ {b}", answer

    if kind == "square":

        a = random.randint(25, 70)

        return f"{a}²", a * a

    if kind == "percentage":

        percentage = random.choice(
            [12.5, 15, 17.5, 22.5, 25, 35]
        )

        base = random.choice(
            [160, 240, 320, 400, 480, 800]
        )

        answer = round(
            base * percentage / 100,
            2,
        )

        return (
            f"{percentage}% of {base}",
            answer,
        )

    if kind == "equation":

        x = random.randint(5, 30)
        a = random.randint(2, 9)
        b = random.randint(5, 30)

        total = a * x + b

        return (
            f"{a}x + {b} = {total}",
            x,
        )

    a = random.randint(10, 50)
    b = random.randint(5, 25)
    c = random.randint(2, 10)
    d = random.randint(5, 25)

    return (
        f"({a} + {b}) × {c} − {d}",
        (a + b) * c - d,
    )


# ============================================================
# ANSWER OPTIONS
# ============================================================

def build_options(correct):

    options = [correct]

    if isinstance(correct, float):

        offsets = [
            .5,
            -.5,
            1,
            -1,
            2,
            -2,
            5,
            -5,
        ]

        for offset in offsets:

            value = round(
                correct + offset,
                2,
            )

            if value not in options:
                options.append(value)

    else:

        magnitude = max(
            abs(int(correct)),
            5,
        )

        offsets = [
            1,
            -1,
            2,
            -2,
            3,
            -3,
            5,
            -5,
            10,
            -10,
            max(2, magnitude // 2),
            -max(2, magnitude // 2),
        ]

        for offset in offsets:

            value = int(correct) + offset

            if value not in options:
                options.append(value)

    random.shuffle(options)

    return options[:4]


def format_answer(value):

    if isinstance(value, float):

        if value.is_integer():

            return str(int(value))

        return f"{value:.2f}".rstrip("0").rstrip(".")

    return str(value)


# ============================================================
# NEW QUESTION
# ============================================================

def new_question():

    for _ in range(100):

        question, answer = make_question(
            st.session_state.difficulty
        )

        identifier = f"{question}|{answer}"

        if identifier not in st.session_state.used_questions:

            st.session_state.used_questions.append(
                identifier
            )

            st.session_state.question = question
            st.session_state.answer = answer
            st.session_state.options = build_options(
                answer
            )

            return

    question, answer = make_question(
        st.session_state.difficulty
    )

    st.session_state.question = question
    st.session_state.answer = answer
    st.session_state.options = build_options(
        answer
    )


# ============================================================
# ENEMY
# ============================================================

def create_enemy():

    difficulty = st.session_state.difficulty
    config = DIFFICULTY[difficulty]

    round_number = st.session_state.round

    boss = (
        round_number % 5 == 0
    )

    st.session_state.boss = boss

    if boss:

        st.session_state.enemy_name = random.choice(
            BOSSES
        )

        multiplier = (
            2.2
            + ((round_number // 5) - 1) * .25
        )

        hp = int(
            config["enemy_hp"] * multiplier
        )

    else:

        st.session_state.enemy_name = random.choice(
            NORMAL_ENEMIES[difficulty]
        )

        scaling = (
            1
            + max(0, round_number - 1) * .08
        )

        hp = int(
            config["enemy_hp"] * scaling
        )

    st.session_state.enemy_max_hp = hp
    st.session_state.enemy_hp = hp

    new_question()


# ============================================================
# START GAME
# ============================================================

def start_game():

    config = DIFFICULTY[
        st.session_state.difficulty
    ]

    st.session_state.player_hp = config["hp"]
    st.session_state.max_hp = config["hp"]

    st.session_state.round = 1

    st.session_state.score = 0
    st.session_state.xp = 0
    st.session_state.coins = 0

    st.session_state.combo = 0
    st.session_state.best_combo = 0

    st.session_state.correct = 0
    st.session_state.attempts = 0

    st.session_state.shield = 0
    st.session_state.crit = 0
    st.session_state.overdrive = 0

    st.session_state.crit_ready = False
    st.session_state.overdrive_ready = False

    st.session_state.used_questions = []

    st.session_state.message = (
        "⚔️ BATTLE START!"
    )

    st.session_state.message_kind = "success"

    create_enemy()

    st.session_state.screen = "battle"


# ============================================================
# COMBO MULTIPLIER
# ============================================================

def get_multiplier():

    combo = st.session_state.combo

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
# ACHIEVEMENTS
# ============================================================

def calculate_achievements():

    achievements = []

    if st.session_state.correct >= 1:
        achievements.append(
            "🎯 First Hit"
        )

    if st.session_state.best_combo >= 3:
        achievements.append(
            "🔥 Combo Starter"
        )

    if st.session_state.best_combo >= 5:
        achievements.append(
            "🔥 Combo Hunter"
        )

    if st.session_state.best_combo >= 10:
        achievements.append(
            "👑 Combo Master"
        )

    if st.session_state.score >= 500:
        achievements.append(
            "💰 Score Grinder"
        )

    if st.session_state.score >= 1500:
        achievements.append(
            "⚡ Math Machine"
        )

    if st.session_state.round >= 5:
        achievements.append(
            "🛡️ Arena Survivor"
        )

    if st.session_state.round >= 10:
        achievements.append(
            "💀 Elite Fighter"
        )

    if st.session_state.correct >= 25:
        achievements.append(
            "🧠 Brain Power"
        )

    return achievements


# ============================================================
# FINISH GAME
# ============================================================

def finish_game(result, reason):

    st.session_state.result = result

    st.session_state.achievements = (
        calculate_achievements()
    )

    if result == "VICTORY":

        st.session_state.wins += 1

    else:

        st.session_state.losses += 1

    record = {
        "player": st.session_state.name,
        "score": st.session_state.score,
        "difficulty": st.session_state.difficulty,
        "mode": st.session_state.mode,
        "round": st.session_state.round,
        "combo": st.session_state.best_combo,
        "correct": st.session_state.correct,
        "result": result,
    }

    st.session_state.history.append(
        record
    )

    if len(st.session_state.history) > 15:

        st.session_state.history = (
            st.session_state.history[-15:]
        )

    st.session_state.message = reason

    st.session_state.screen = "result"


# ============================================================
# USE POWERUPS
# ============================================================

def use_shield():

    if st.session_state.shield <= 0:
        return

    st.session_state.shield -= 1

    st.session_state.message = (
        "🛡️ SHIELD READY — YOUR NEXT MISTAKE IS BLOCKED!"
    )

    st.session_state.message_kind = "success"

    st.rerun()


def use_crit():

    if st.session_state.crit <= 0:
        return

    st.session_state.crit -= 1
    st.session_state.crit_ready = True

    st.session_state.message = (
        "💥 CRITICAL ATTACK READY!"
    )

    st.session_state.message_kind = "success"

    st.rerun()


def use_overdrive():

    if st.session_state.overdrive <= 0:
        return

    st.session_state.overdrive -= 1
    st.session_state.overdrive_ready = True

    st.session_state.message = (
        "⚡ OVERDRIVE READY — NEXT HIT x3!"
    )

    st.session_state.message_kind = "success"

    st.rerun()


def heal():

    if st.session_state.coins < 5:

        st.session_state.message = (
            "❌ You need 5 coins."
        )

        st.session_state.message_kind = "error"

        st.rerun()

    if (
        st.session_state.player_hp
        >= st.session_state.max_hp
    ):

        st.session_state.message = (
            "❤️ Your HP is already full."
        )

        st.session_state.message_kind = "info"

        st.rerun()

    st.session_state.coins -= 5

    st.session_state.player_hp = min(
        st.session_state.max_hp,
        st.session_state.player_hp + 25,
    )

    st.session_state.message = (
        "❤️ +25 HP"
    )

    st.session_state.message_kind = "success"

    st.rerun()


# ============================================================
# ANSWER
# ============================================================

def submit_answer(selected):

    st.session_state.attempts += 1

    correct_answer = (
        st.session_state.answer
    )

    # --------------------------------------------------------
    # CORRECT
    # --------------------------------------------------------

    if selected == correct_answer:

        st.session_state.correct += 1

        st.session_state.combo += 1

        st.session_state.best_combo = max(
            st.session_state.best_combo,
            st.session_state.combo,
        )

        config = DIFFICULTY[
            st.session_state.difficulty
        ]

        multiplier = get_multiplier()

        damage = int(
            config["damage"]
            * multiplier
        )

        # Critical
        if st.session_state.crit_ready:

            damage *= 2

            st.session_state.crit_ready = False

            st.session_state.message = (
                f"💥 CRITICAL HIT! -{damage} HP"
            )

        # Overdrive
        elif st.session_state.overdrive_ready:

            damage *= 3

            st.session_state.overdrive_ready = False

            st.session_state.message = (
                f"⚡ OVERDRIVE! -{damage} HP"
            )

        elif st.session_state.combo >= 8:

            st.session_state.message = (
                f"🔥 FEVER ATTACK! -{damage} HP"
            )

        else:

            st.session_state.message = (
                f"⚔️ HIT! -{damage} HP"
            )

        st.session_state.message_kind = "success"

        st.session_state.enemy_hp -= damage

        st.session_state.score += (
            damage * 10
        )

        st.session_state.xp += (
            config["xp"]
            + st.session_state.combo
        )

        st.session_state.coins += (
            config["coins"]
        )

        # Powerups
        if (
            st.session_state.combo >= 3
            and st.session_state.shield == 0
        ):

            st.session_state.shield += 1

        if (
            st.session_state.combo >= 5
            and st.session_state.crit == 0
            and not st.session_state.crit_ready
        ):

            st.session_state.crit += 1

        if (
            st.session_state.combo >= 8
            and st.session_state.overdrive == 0
            and not st.session_state.overdrive_ready
        ):

            st.session_state.overdrive += 1

        # ----------------------------------------------------
        # ENEMY DEFEATED
        # ----------------------------------------------------

        if st.session_state.enemy_hp <= 0:

            boss_defeated = (
                st.session_state.boss
            )

            if boss_defeated:

                st.session_state.score += 250
                st.session_state.coins += 10
                st.session_state.xp += 50

                st.session_state.message = (
                    "👑 BOSS DESTROYED! +250 SCORE"
                )

            else:

                st.session_state.score += 50
                st.session_state.coins += 3

                st.session_state.message = (
                    "💀 ENEMY DEFEATED! +50 SCORE"
                )

            # Quick battle
            if (
                st.session_state.mode
                == "Quick Battle"
                and st.session_state.round >= 5
            ):

                finish_game(
                    "VICTORY",
                    "🏆 You cleared all five battles!",
                )

                return

            st.session_state.round += 1

            create_enemy()

            return

        new_question()

    # --------------------------------------------------------
    # WRONG
    # --------------------------------------------------------

    else:

        st.session_state.combo = 0

        config = DIFFICULTY[
            st.session_state.difficulty
        ]

        damage = config["enemy_damage"]

        if st.session_state.boss:

            damage = int(
                damage * 1.25
            )

        # Shield
        if st.session_state.shield > 0:

            st.session_state.shield -= 1

            st.session_state.message = (
                "🛡️ SHIELD BLOCKED THE ATTACK!"
            )

            st.session_state.message_kind = (
                "success"
            )

        else:

            st.session_state.player_hp -= damage

            st.session_state.message = (
                f"💀 WRONG ANSWER! -{damage} HP"
            )

            st.session_state.message_kind = (
                "error"
            )

        if st.session_state.player_hp <= 0:

            st.session_state.player_hp = 0

            finish_game(
                "DEFEAT",
                "💀 Your HP reached zero.",
            )

            return

        new_question()


# ============================================================
# HOME SCREEN
# ============================================================

def home_screen():

    st.markdown(
        '<div class="arena-title">⚔️ MATHS ARENA PRO</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="arena-subtitle">THINK FAST • ATTACK SMART • MASTER MATHEMATICS</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ## 🏟️ Welcome to the Arena

        This is **not a maths exam**.

        Every correct answer becomes an attack.
        Build combos, unlock power-ups, destroy enemies
        and survive increasingly difficult rounds.
        """
    )

    st.divider()

    left, center, right = st.columns(
        [1, 1.4, 1]
    )

    with center:

        st.markdown(
            "### 👤 YOUR FIGHTER"
        )

        name = st.text_input(
            "Fighter name",
            value=st.session_state.name,
            max_chars=18,
            placeholder="Enter your name",
        )

        if name.strip():

            st.session_state.name = (
                name.strip()[:18]
            )

        st.write("")

        st.markdown(
            "### 🎮 GAME MODE"
        )

        mode = st.radio(
            "Choose mode",
            [
                "Endless Arena",
                "Quick Battle",
            ],
            horizontal=True,
        )

        st.session_state.mode = mode

        st.write("")

        st.markdown(
            "### ⚔️ DIFFICULTY"
        )

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
            ].index(
                st.session_state.difficulty
            ),
        )

        st.session_state.difficulty = (
            difficulty
        )

        st.write("")

        if st.button(
            "⚔️ ENTER THE ARENA",
            type="primary",
            use_container_width=True,
        ):

            start_game()

            st.rerun()

    st.write("")
    st.divider()

    st.markdown(
        "### 🎮 GAME FEATURES"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.info(
            "🔥 **COMBOS**\n\n"
            "Keep answering correctly "
            "to increase your damage."
        )

    with c2:

        st.info(
            "👑 **BOSSES**\n\n"
            "Every 5th round brings "
            "a stronger enemy."
        )

    with c3:

        st.info(
            "⚡ **POWER-UPS**\n\n"
            "Shield, Critical, Overdrive "
            "and Heal."
        )

    with c4:

        st.info(
            "🏆 **REWARDS**\n\n"
            "Earn score, XP and coins "
            "during your run."
        )

    if st.session_state.history:

        st.write("")
        st.divider()

        st.markdown(
            "### 🏆 LOCAL HALL OF FAME"
        )

        best = sorted(
            st.session_state.history,
            key=lambda x: x["score"],
            reverse=True,
        )[:5]

        for position, run in enumerate(
            best,
            start=1,
        ):

            icon = {
                1: "🥇",
                2: "🥈",
                3: "🥉",
                4: "4️⃣",
                5: "5️⃣",
            }[position]

            st.write(
                f"{icon} **{run['player']}**  "
                f"— Score: **{run['score']}**  "
                f"— Combo: **🔥 {run['combo']}**  "
                f"— {run['difficulty']}"
            )


# ============================================================
# BATTLE SCREEN
# ============================================================

def battle_screen():

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        '<div class="arena-title">⚔️ BATTLE ARENA</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="arena-subtitle">'
        f'ROUND {st.session_state.round} • '
        f'{st.session_state.difficulty.upper()} • '
        f'{st.session_state.mode.upper()}'
        f'</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # TOP STATS
    # --------------------------------------------------------

    a, b, c, d, e = st.columns(5)

    with a:

        st.metric(
            "❤️ HP",
            f"{st.session_state.player_hp}/{st.session_state.max_hp}",
        )

    with b:

        st.metric(
            "💀 ENEMY HP",
            f"{st.session_state.enemy_hp}/{st.session_state.enemy_max_hp}",
        )

    with c:

        st.metric(
            "🔥 COMBO",
            st.session_state.combo,
        )

    with d:

        st.metric(
            "🏆 SCORE",
            st.session_state.score,
        )

    with e:

        st.metric(
            "🪙 COINS",
            st.session_state.coins,
        )

    # --------------------------------------------------------
    # HP BARS
    # --------------------------------------------------------

    st.progress(
        max(
            0.0,
            min(
                1.0,
                st.session_state.player_hp
                / st.session_state.max_hp,
            ),
        ),
        text="❤️ YOUR HEALTH",
    )

    st.progress(
        max(
            0.0,
            min(
                1.0,
                st.session_state.enemy_hp
                / st.session_state.enemy_max_hp,
            ),
        ),
        text=(
            "👑 BOSS HEALTH"
            if st.session_state.boss
            else "💀 ENEMY HEALTH"
        ),
    )

    st.write("")

    # --------------------------------------------------------
    # FIGHTERS
    # --------------------------------------------------------

    player_col, vs_col, enemy_col = st.columns(
        [1, .35, 1]
    )

    with player_col:

        st.markdown(
            "### 🧑 YOUR FIGHTER"
        )

        st.markdown(
            f"## {st.session_state.name}"
        )

        st.caption(
            f"XP: {st.session_state.xp}"
        )

    with vs_col:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-family:Orbitron;
                font-size:1.5rem;
                padding-top:35px;
            ">
            VS
            </div>
            """,
            unsafe_allow_html=True,
        )

    with enemy_col:

        if st.session_state.boss:

            st.error(
                f"👑 BOSS\n\n"
                f"{st.session_state.enemy_name}"
            )

        else:

            st.warning(
                f"💀 ENEMY\n\n"
                f"{st.session_state.enemy_name}"
            )

    # --------------------------------------------------------
    # COMBO
    # --------------------------------------------------------

    multiplier = get_multiplier()

    st.markdown(
        "### 🔥 COMBAT STATUS"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Combo",
            f"🔥 {st.session_state.combo}",
        )

    with c2:

        st.metric(
            "Damage Multiplier",
            f"x{multiplier}",
        )

    with c3:

        if st.session_state.combo >= 8:

            st.success(
                "🔥 FEVER MODE"
            )

        elif st.session_state.combo >= 5:

            st.info(
                "⚡ POWER MODE"
            )

        else:

            st.caption(
                "Build your combo!"
            )

    # --------------------------------------------------------
    # MESSAGE
    # --------------------------------------------------------

    if st.session_state.message:

        if (
            st.session_state.message_kind
            == "success"
        ):

            st.success(
                st.session_state.message
            )

        elif (
            st.session_state.message_kind
            == "error"
        ):

            st.error(
                st.session_state.message
            )

        else:

            st.info(
                st.session_state.message
            )

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="battle-question">
            <div class="question-label">
                ⚔️ SOLVE TO ATTACK
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="
            text-align:center;
            font-family:Orbitron;
            font-size:clamp(2rem,5vw,3.5rem);
            font-weight:900;
            padding:10px;
        ">
        {st.session_state.question} = ?
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Choose the correct answer to damage your enemy."
    )

    # --------------------------------------------------------
    # ANSWERS
    # --------------------------------------------------------

    options = st.session_state.options

    col1, col2 = st.columns(2)

    for index, option in enumerate(options):

        target = (
            col1
            if index % 2 == 0
            else col2
        )

        with target:

            if st.button(
                f"⚔️  {format_answer(option)}",
                key=f"answer_{st.session_state.round}_{st.session_state.attempts}_{index}",
                use_container_width=True,
            ):

                submit_answer(option)

                st.rerun()

    st.write("")

    # --------------------------------------------------------
    # POWERUPS
    # --------------------------------------------------------

    st.markdown(
        "### ⚡ POWER-UPS"
    )

    p1, p2, p3, p4 = st.columns(4)

    with p1:

        st.metric(
            "🛡️ Shield",
            st.session_state.shield,
        )

        if st.button(
            "Use Shield",
            disabled=(
                st.session_state.shield <= 0
            ),
            key="use_shield",
            use_container_width=True,
        ):

            use_shield()

    with p2:

        st.metric(
            "💥 Critical",
            st.session_state.crit,
        )

        if st.button(
            "Use Critical",
            disabled=(
                st.session_state.crit <= 0
                or st.session_state.crit_ready
            ),
            key="use_crit",
            use_container_width=True,
        ):

            use_crit()

    with p3:

        st.metric(
            "⚡ Overdrive",
            st.session_state.overdrive,
        )

        if st.button(
            "Use Overdrive",
            disabled=(
                st.session_state.overdrive <= 0
                or st.session_state.overdrive_ready
            ),
            key="use_overdrive",
            use_container_width=True,
        ):

            use_overdrive()

    with p4:

        st.metric(
            "❤️ Heal",
            "5 🪙",
        )

        if st.button(
            "Heal +25 HP",
            disabled=(
                st.session_state.coins < 5
                or st.session_state.player_hp
                >= st.session_state.max_hp
            ),
            key="heal",
            use_container_width=True,
        ):

            heal()

    # --------------------------------------------------------
    # ACTIVE EFFECTS
    # --------------------------------------------------------

    active = []

    if st.session_state.crit_ready:

        active.append(
            "💥 CRITICAL READY"
        )

    if st.session_state.overdrive_ready:

        active.append(
            "⚡ OVERDRIVE READY"
        )

    if active:

        st.write("")

        st.info(
            "   |   ".join(active)
        )

    # --------------------------------------------------------
    # END RUN
    # --------------------------------------------------------

    st.write("")
    st.divider()

    if st.button(
        "🏳️ END RUN",
        use_container_width=True,
    ):

        finish_game(
            "DEFEAT",
            "You ended the run.",
        )

        st.rerun()


# ============================================================
# RESULT SCREEN
# ============================================================

def result_screen():

    if st.session_state.result == "VICTORY":

        st.success(
            "🏆 ARENA CLEARED!"
        )

        st.markdown(
            "# 🏆 VICTORY"
        )

        st.write(
            "You defeated the arena. "
            "That was a strong run."
        )

    else:

        st.error(
            "💀 RUN OVER"
        )

        st.markdown(
            "# 💀 GAME OVER"
        )

        st.write(
            st.session_state.message
        )

    st.divider()

    # --------------------------------------------------------
    # FINAL STATS
    # --------------------------------------------------------

    st.markdown(
        "### 📊 FINAL STATS"
    )

    a, b, c, d = st.columns(4)

    with a:

        st.metric(
            "🏆 SCORE",
            st.session_state.score,
        )

    with b:

        st.metric(
            "🔥 BEST COMBO",
            st.session_state.best_combo,
        )

    with c:

        st.metric(
            "🎯 CORRECT",
            st.session_state.correct,
        )

    with d:

        st.metric(
            "🪙 COINS",
            st.session_state.coins,
        )

    st.write("")

    # --------------------------------------------------------
    # ACCURACY
    # --------------------------------------------------------

    accuracy = 0

    if st.session_state.attempts > 0:

        accuracy = (
            st.session_state.correct
            / st.session_state.attempts
            * 100
        )

    st.markdown(
        "### 🎯 PERFORMANCE"
    )

    p1, p2, p3 = st.columns(3)

    with p1:

        st.metric(
            "Accuracy",
            f"{accuracy:.0f}%",
        )

    with p2:

        st.metric(
            "Round",
            st.session_state.round,
        )

    with p3:

        st.metric(
            "Difficulty",
            st.session_state.difficulty,
        )

    st.write("")

    # --------------------------------------------------------
    # ACHIEVEMENTS
    # --------------------------------------------------------

    st.markdown(
        "### 🏅 ACHIEVEMENTS"
    )

    if st.session_state.achievements:

        cols = st.columns(
            min(
                3,
                len(
                    st.session_state.achievements
                ),
            )
        )

        for index, achievement in enumerate(
            st.session_state.achievements
        ):

            with cols[
                index % len(cols)
            ]:

                st.success(
                    achievement
                )

    else:

        st.info(
            "No achievements unlocked yet."
        )

    st.write("")

    # --------------------------------------------------------
    # ACTIONS
    # --------------------------------------------------------

    st.markdown(
        "### ⚔️ READY?"
    )

    a1, a2 = st.columns(2)

    with a1:

        if st.button(
            "⚔️ PLAY AGAIN",
            type="primary",
            use_container_width=True,
        ):

            start_game()

            st.rerun()

    with a2:

        if st.button(
            "🏠 BACK TO HOME",
            use_container_width=True,
        ):

            st.session_state.screen = "home"

            st.rerun()

    # --------------------------------------------------------
    # RECENT RUNS
    # --------------------------------------------------------

    st.write("")
    st.divider()

    st.markdown(
        "### 📜 RECENT RUNS"
    )

    if not st.session_state.history:

        st.info(
            "No previous runs."
        )

    else:

        for number, run in enumerate(
            reversed(
                st.session_state.history
            ),
            start=1,
        ):

            icon = (
                "🏆"
                if run["result"] == "VICTORY"
                else "💀"
            )

            st.markdown(
                f"#### {icon} {run['player']}"
            )

            c1, c2, c3, c4, c5 = st.columns(5)

            with c1:

                st.metric(
                    "Score",
                    run["score"],
                )

            with c2:

                st.metric(
                    "Combo",
                    f"🔥 {run['combo']}",
                )

            with c3:

                st.metric(
                    "Correct",
                    run["correct"],
                )

            with c4:

                st.metric(
                    "Difficulty",
                    run["difficulty"],
                )

            with c5:

                st.metric(
                    "Result",
                    run["result"],
                )

            if number < len(
                st.session_state.history
            ):

                st.divider()


# ============================================================
# PROFILE SCREEN
# ============================================================

def profile_screen():

    st.markdown(
        "# 👤 PLAYER PROFILE"
    )

    total_runs = (
        st.session_state.wins
        + st.session_state.losses
    )

    if total_runs:

        win_rate = (
            st.session_state.wins
            / total_runs
            * 100
        )

    else:

        win_rate = 0

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "PLAYER",
            st.session_state.name,
        )

    with c2:

        st.metric(
            "RUNS",
            total_runs,
        )

    with c3:

        st.metric(
            "WINS",
            st.session_state.wins,
        )

    with c4:

        st.metric(
            "WIN RATE",
            f"{win_rate:.0f}%",
        )

    st.divider()

    st.markdown(
        "### 🎮 ABOUT THIS VERSION"
    )

    st.info(
        "Your gameplay data is kept in the current "
        "Streamlit session. This version intentionally "
        "does not use SQLite or an external API."
    )

    st.write("")

    if st.button(
        "🏠 BACK HOME",
        use_container_width=True,
    ):

        st.session_state.screen = "home"

        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## ⚔️ MATHS ARENA"
    )

    st.caption(
        "Think fast. Attack smart."
    )

    st.divider()

    if st.session_state.screen == "battle":

        st.write(
            f"👤 **{st.session_state.name}**"
        )

        st.write(
            f"🎮 **{st.session_state.mode}**"
        )

        st.write(
            f"⚔️ **{st.session_state.difficulty}**"
        )

        st.write(
            f"🏟️ **Round {st.session_state.round}**"
        )

        st.write(
            f"🔥 **Combo {st.session_state.combo}**"
        )

        st.write(
            f"🏆 **{st.session_state.score} Score**"
        )

        st.divider()

        if st.button(
            "🏳️ End Run",
            use_container_width=True,
        ):

            finish_game(
                "DEFEAT",
                "You ended the run.",
            )

            st.rerun()

    else:

        if st.button(
            "🏠 Home",
            use_container_width=True,
        ):

            st.session_state.screen = "home"

            st.rerun()

        if st.button(
            "👤 Profile",
            use_container_width=True,
        ):

            st.session_state.screen = "profile"

            st.rerun()


# ============================================================
# ROUTER
# ============================================================

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
