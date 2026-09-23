import random
from datetime import datetime

import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Maths Arena Pro",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GAME CONFIG
# ============================================================

DIFFICULTIES = {
    "Basic": {
        "player_hp": 120,
        "enemy_hp": 90,
        "base_damage": 24,
        "mistake_damage": 12,
        "xp": 8,
        "coins": 2,
    },
    "Medium": {
        "player_hp": 110,
        "enemy_hp": 125,
        "base_damage": 28,
        "mistake_damage": 16,
        "xp": 12,
        "coins": 3,
    },
    "Pro": {
        "player_hp": 100,
        "enemy_hp": 165,
        "base_damage": 32,
        "mistake_damage": 20,
        "xp": 17,
        "coins": 4,
    },
    "Master": {
        "player_hp": 95,
        "enemy_hp": 210,
        "base_damage": 37,
        "mistake_damage": 25,
        "xp": 22,
        "coins": 5,
    },
}


ENEMIES = {
    "Basic": [
        ("👹", "Number Goblin"),
        ("🤖", "Digit Droid"),
        ("🐲", "Sum Beast"),
        ("⚡", "Quick Calculator"),
    ],
    "Medium": [
        ("👻", "Fraction Phantom"),
        ("🤖", "Equation Raider"),
        ("🧠", "Logic Droid"),
        ("🏹", "Algebra Hunter"),
    ],
    "Pro": [
        ("💀", "Formula Reaper"),
        ("⚔️", "Algebra Knight"),
        ("☠️", "Prime Destroyer"),
        ("🤖", "Matrix Warrior"),
    ],
    "Master": [
        ("👑", "Infinity Lord"),
        ("☠️", "Zero King"),
        ("🔥", "Formula Titan"),
        ("💀", "Math Overlord"),
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
    "battle_type": "Endless Arena",
    "difficulty": "Basic",

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
    "turn_count": 1,

    "question": "",
    "correct_answer": 0,
    "options": [],

    "enemy_name": "Number Goblin",
    "enemy_icon": "👹",
    "is_boss": False,

    "shield": False,
    "double_damage": False,

    "p1_shield": False,
    "p2_shield": False,

    "message": "",
    "message_type": "info",

    "battle_log": [],

    "game_started": False,
    "result": None,

    "total_matches": 0,
    "wins": 0,
    "losses": 0,

    "achievements": [],

    "history": [],

    "used_questions": [],

    "fever": False,
}


for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def add_log(message):
    st.session_state.battle_log.insert(0, message)
    st.session_state.battle_log = st.session_state.battle_log[:12]


def player_level(xp):
    return max(1, int(xp // 100) + 1)


def xp_to_next_level(xp):
    level = player_level(xp)
    return level * 100


def accuracy(correct, attempts):
    if attempts == 0:
        return 0
    return round((correct / attempts) * 100)


def safe_int(value):
    try:
        return int(value)
    except Exception:
        return 0


# ============================================================
# QUESTION ENGINE
# ============================================================

def make_question(difficulty):
    """
    Returns:
        question_text, answer
    """

    if difficulty == "Basic":
        operation = random.choice(["+", "-", "*"])

        if operation == "+":
            a = random.randint(5, 50)
            b = random.randint(5, 50)
            return f"{a} + {b}", a + b

        if operation == "-":
            a = random.randint(20, 80)
            b = random.randint(5, a)
            return f"{a} − {b}", a - b

        a = random.randint(2, 12)
        b = random.randint(2, 12)
        return f"{a} × {b}", a * b


    if difficulty == "Medium":
        operation = random.choice(["+", "-", "*", "/"])

        if operation == "+":
            a = random.randint(20, 150)
            b = random.randint(20, 150)
            return f"{a} + {b}", a + b

        if operation == "-":
            a = random.randint(50, 200)
            b = random.randint(10, a)
            return f"{a} − {b}", a - b

        if operation == "*":
            a = random.randint(8, 25)
            b = random.randint(5, 20)
            return f"{a} × {b}", a * b

        b = random.randint(2, 12)
        answer = random.randint(2, 15)
        a = b * answer
        return f"{a} ÷ {b}", answer


    if difficulty == "Pro":
        operation = random.choice(
            ["+", "-", "*", "/", "square", "percentage"]
        )

        if operation == "+":
            a = random.randint(100, 900)
            b = random.randint(100, 900)
            return f"{a} + {b}", a + b

        if operation == "-":
            a = random.randint(300, 1500)
            b = random.randint(100, a)
            return f"{a} − {b}", a - b

        if operation == "*":
            a = random.randint(15, 60)
            b = random.randint(10, 35)
            return f"{a} × {b}", a * b

        if operation == "/":
            b = random.randint(3, 20)
            answer = random.randint(5, 40)
            a = b * answer
            return f"{a} ÷ {b}", answer

        if operation == "square":
            a = random.randint(8, 35)
            return f"{a}²", a * a

        a = random.choice([10, 20, 25, 50])
        number = random.randint(20, 500)
        return f"{a}% of {number}", (a * number) // 100


    # MASTER
    operation = random.choice(
        ["square", "cube", "power", "mixed", "percentage", "division"]
    )

    if operation == "square":
        a = random.randint(15, 60)
        return f"{a}²", a * a

    if operation == "cube":
        a = random.randint(3, 12)
        return f"{a}³", a ** 3

    if operation == "power":
        a = random.randint(2, 8)
        b = random.randint(2, 4)
        return f"{a}^{b}", a ** b

    if operation == "percentage":
        percent = random.choice([12, 15, 20, 25, 30, 40, 50])
        number = random.choice(
            [40, 60, 80, 100, 120, 150, 200, 240, 300, 400]
        )
        return f"{percent}% of {number}", (percent * number) // 100

    if operation == "division":
        divisor = random.randint(4, 30)
        answer = random.randint(10, 80)
        dividend = divisor * answer
        return f"{dividend} ÷ {divisor}", answer

    a = random.randint(10, 80)
    b = random.randint(5, 50)
    c = random.randint(2, 12)
    return f"({a} + {b}) × {c}", (a + b) * c


def generate_options(correct):
    """
    GUARANTEE:
    The correct answer is ALWAYS inside the options.
    """

    correct = safe_int(correct)

    values = {correct}

    deltas = [
        1, -1,
        2, -2,
        3, -3,
        4, -4,
        5, -5,
        7, -7,
        10, -10,
        12, -12,
        15, -15,
        20, -20,
        25, -25,
    ]

    for delta in deltas:
        candidate = correct + delta

        if candidate >= 0:
            values.add(candidate)

        if len(values) >= 4:
            break

    while len(values) < 4:
        candidate = max(0, correct + random.randint(-50, 50))
        values.add(candidate)

    options = list(values)
    random.shuffle(options)

    # Final safety check
    if correct not in options:
        options[0] = correct

    return options[:4]


def new_question():
    difficulty = st.session_state.difficulty

    for _ in range(50):
        question, answer = make_question(difficulty)
        signature = f"{question}|{answer}"

        if signature not in st.session_state.used_questions:
            st.session_state.used_questions.append(signature)

            if len(st.session_state.used_questions) > 100:
                st.session_state.used_questions.pop(0)

            options = generate_options(answer)

            # Absolute safety
            if answer not in options:
                options[0] = answer

            st.session_state.question = question
            st.session_state.correct_answer = answer
            st.session_state.options = options
            return

    question, answer = make_question(difficulty)

    st.session_state.question = question
    st.session_state.correct_answer = answer
    st.session_state.options = generate_options(answer)


# ============================================================
# ENEMY SYSTEM
# ============================================================

def create_enemy():
    difficulty = st.session_state.difficulty
    round_number = st.session_state.round
    config = DIFFICULTIES[difficulty]

    is_boss = (
        st.session_state.mode == "1 Player"
        and round_number % 5 == 0
    )

    if is_boss:
        icon, name = BOSSES[
            ((round_number // 5) - 1) % len(BOSSES)
        ]

        multiplier = 1 + ((round_number // 5) - 1) * 0.15
        hp = int(config["enemy_hp"] * 2.2 * multiplier)

    else:
        icon, name = random.choice(ENEMIES[difficulty])

        multiplier = 1 + ((round_number - 1) * 0.08)
        hp = int(config["enemy_hp"] * multiplier)

    st.session_state.enemy_icon = icon
    st.session_state.enemy_name = name
    st.session_state.enemy_max_hp = hp
    st.session_state.enemy_hp = hp
    st.session_state.is_boss = is_boss


# ============================================================
# RESET / START
# ============================================================

def reset_game():
    for key, value in DEFAULTS.items():
        if key in st.session_state:
            st.session_state[key] = value


def start_game():
    mode = st.session_state.mode

    # If player 2 is empty, automatically switch to 1 player.
    if mode == "2 Players":
        if not st.session_state.player2_name.strip():
            st.session_state.mode = "1 Player"
            mode = "1 Player"
            st.session_state.player2_name = "Player 2"

    difficulty = st.session_state.difficulty
    config = DIFFICULTIES[difficulty]

    st.session_state.p1_max_hp = config["player_hp"]
    st.session_state.p1_hp = config["player_hp"]

    st.session_state.p2_max_hp = config["player_hp"]
    st.session_state.p2_hp = config["player_hp"]

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
    st.session_state.turn_count = 1

    st.session_state.current_player = 1

    st.session_state.battle_log = []
    st.session_state.used_questions = []

    st.session_state.result = None
    st.session_state.game_started = True
    st.session_state.screen = "battle"

    st.session_state.shield = False
    st.session_state.double_damage = False
    st.session_state.p1_shield = False
    st.session_state.p2_shield = False

    st.session_state.fever = False

    if mode == "1 Player":
        create_enemy()

    new_question()

    add_log("⚔️ Battle started!")


# ============================================================
# DAMAGE / ANSWER SYSTEM
# ============================================================

def get_damage(player):
    difficulty = st.session_state.difficulty
    config = DIFFICULTIES[difficulty]

    combo = (
        st.session_state.p1_combo
        if player == 1
        else st.session_state.p2_combo
    )

    damage = config["base_damage"]

    combo_bonus = min(combo * 4, 24)
    damage += combo_bonus

    critical = random.random() < 0.15

    if critical:
        damage *= 2

    double_damage = (
        st.session_state.double_damage
        if player == 1
        else False
    )

    if player == 2:
        double_damage = False

    if double_damage:
        damage *= 2

        if player == 1:
            st.session_state.double_damage = False

    return int(damage), critical


def reward_correct(player):
    difficulty = st.session_state.difficulty
    config = DIFFICULTIES[difficulty]

    if player == 1:
        st.session_state.p1_correct += 1
        st.session_state.p1_attempts += 1
        st.session_state.p1_combo += 1

        if st.session_state.p1_combo > st.session_state.p1_best_combo:
            st.session_state.p1_best_combo = st.session_state.p1_combo

        st.session_state.p1_score += 100 + (
            st.session_state.p1_combo * 15
        )

        st.session_state.p1_xp += config["xp"]
        st.session_state.p1_coins += config["coins"]

        if st.session_state.p1_combo >= 5:
            st.session_state.fever = True

    else:
        st.session_state.p2_correct += 1
        st.session_state.p2_attempts += 1
        st.session_state.p2_combo += 1

        if st.session_state.p2_combo > st.session_state.p2_best_combo:
            st.session_state.p2_best_combo = st.session_state.p2_combo

        st.session_state.p2_score += 100 + (
            st.session_state.p2_combo * 15
        )

        st.session_state.p2_xp += config["xp"]
        st.session_state.p2_coins += config["coins"]


def reward_wrong(player):
    if player == 1:
        st.session_state.p1_attempts += 1
        st.session_state.p1_combo = 0
        st.session_state.fever = False
    else:
        st.session_state.p2_attempts += 1
        st.session_state.p2_combo = 0


def answer_question(selected_answer):
    correct = st.session_state.correct_answer
    player = st.session_state.current_player

    selected_answer = safe_int(selected_answer)
    correct = safe_int(correct)

    is_correct = selected_answer == correct

    if st.session_state.mode == "1 Player":
        handle_single_player_answer(player, is_correct)

    else:
        handle_two_player_answer(player, is_correct)

    check_achievements()

    if st.session_state.game_started:
        new_question()

    st.rerun()


# ============================================================
# SINGLE PLAYER
# ============================================================

def handle_single_player_answer(player, is_correct):

    config = DIFFICULTIES[st.session_state.difficulty]

    if is_correct:

        reward_correct(1)

        damage, critical = get_damage(1)

        st.session_state.enemy_hp = max(
            0,
            st.session_state.enemy_hp - damage
        )

        if critical:
            st.session_state.message = (
                f"💥 CRITICAL HIT! {damage} damage!"
            )
            st.session_state.message_type = "success"
            add_log(f"💥 Critical hit for {damage} damage!")
        else:
            st.session_state.message = (
                f"⚔️ Correct! You dealt {damage} damage."
            )
            st.session_state.message_type = "success"
            add_log(f"⚔️ Player attacked for {damage} damage.")

        if st.session_state.enemy_hp <= 0:
            defeat_enemy()

    else:

        reward_wrong(1)

        damage = config["mistake_damage"]

        if st.session_state.p1_shield:
            damage = 0
            st.session_state.p1_shield = False
            add_log("🛡️ Shield blocked the enemy attack!")
            st.session_state.message = "🛡️ Your shield blocked the damage!"
            st.session_state.message_type = "info"

        else:
            st.session_state.p1_hp = max(
                0,
                st.session_state.p1_hp - damage
            )

            st.session_state.message = (
                f"❌ Wrong! {st.session_state.enemy_name} dealt "
                f"{damage} damage."
            )

            st.session_state.message_type = "error"

            add_log(
                f"💥 Enemy attacked you for {damage} damage."
            )

        if st.session_state.p1_hp <= 0:
            finish_game("loss")


def defeat_enemy():

    bonus_coins = 5
    bonus_xp = 20

    st.session_state.p1_coins += bonus_coins
    st.session_state.p1_xp += bonus_xp

    add_log(
        f"🏆 {st.session_state.enemy_name} defeated!"
    )

    st.session_state.message = (
        f"🏆 ENEMY DEFEATED! +{bonus_coins} 🪙 +{bonus_xp} XP"
    )

    st.session_state.message_type = "success"

    if st.session_state.battle_type == "Quick Battle":

        if st.session_state.round >= 5:
            finish_game("win")
            return

    st.session_state.round += 1
    create_enemy()


# ============================================================
# TWO PLAYER
# ============================================================

def handle_two_player_answer(player, is_correct):

    config = DIFFICULTIES[st.session_state.difficulty]

    attacker_name = (
        st.session_state.player1_name
        if player == 1
        else st.session_state.player2_name
    )

    defender = 2 if player == 1 else 1

    defender_name = (
        st.session_state.player1_name
        if defender == 1
        else st.session_state.player2_name
    )

    if is_correct:

        reward_correct(player)

        damage, critical = get_damage(player)

        if defender == 1:
            if st.session_state.p1_shield:
                damage = 0
                st.session_state.p1_shield = False

                st.session_state.message = (
                    f"🛡️ {defender_name}'s shield blocked the attack!"
                )
                st.session_state.message_type = "info"

                add_log(
                    f"🛡️ {defender_name} blocked the attack."
                )

            else:
                st.session_state.p1_hp = max(
                    0,
                    st.session_state.p1_hp - damage
                )

        else:
            if st.session_state.p2_shield:
                damage = 0
                st.session_state.p2_shield = False

                st.session_state.message = (
                    f"🛡️ {defender_name}'s shield blocked the attack!"
                )
                st.session_state.message_type = "info"

                add_log(
                    f"🛡️ {defender_name} blocked the attack."
                )

            else:
                st.session_state.p2_hp = max(
                    0,
                    st.session_state.p2_hp - damage
                )

        if damage > 0:

            if critical:
                st.session_state.message = (
                    f"💥 CRITICAL! {attacker_name} dealt "
                    f"{damage} damage to {defender_name}!"
                )
            else:
                st.session_state.message = (
                    f"⚔️ {attacker_name} dealt "
                    f"{damage} damage to {defender_name}!"
                )

            st.session_state.message_type = "success"

            add_log(
                f"⚔️ {attacker_name} → {defender_name}: "
                f"{damage} damage"
            )

    else:

        reward_wrong(player)

        self_damage = max(
            5,
            config["mistake_damage"] // 2
        )

        if player == 1:

            st.session_state.p1_hp = max(
                0,
                st.session_state.p1_hp - self_damage
            )

        else:

            st.session_state.p2_hp = max(
                0,
                st.session_state.p2_hp - self_damage
            )

        st.session_state.message = (
            f"❌ Wrong answer! {attacker_name} lost "
            f"{self_damage} HP."
        )

        st.session_state.message_type = "error"

        add_log(
            f"❌ {attacker_name} made a mistake."
        )

    # Check winner
    if st.session_state.p1_hp <= 0:
        finish_game("p2_win")
        return

    if st.session_state.p2_hp <= 0:
        finish_game("p1_win")
        return

    # Quick battle
    if (
        st.session_state.battle_type == "Quick Battle"
        and st.session_state.turn_count >= 10
    ):
        if st.session_state.p1_hp > st.session_state.p2_hp:
            finish_game("p1_win")
        elif st.session_state.p2_hp > st.session_state.p1_hp:
            finish_game("p2_win")
        else:
            finish_game("draw")

        return

    # Change turn
    if player == 1:
        st.session_state.current_player = 2
    else:
        st.session_state.current_player = 1
        st.session_state.round += 1

    st.session_state.turn_count += 1


# ============================================================
# POWER UPS
# ============================================================

def use_shield():

    player = st.session_state.current_player

    if player == 1:

        if st.session_state.p1_coins < 5:
            st.warning("You need 5 coins.")
            return

        st.session_state.p1_coins -= 5
        st.session_state.p1_shield = True

        add_log(
            f"🛡️ {st.session_state.player1_name} activated Shield."
        )

    else:

        if st.session_state.p2_coins < 5:
            st.warning("You need 5 coins.")
            return

        st.session_state.p2_coins -= 5
        st.session_state.p2_shield = True

        add_log(
            f"🛡️ {st.session_state.player2_name} activated Shield."
        )

    st.session_state.message = "🛡️ SHIELD ACTIVATED!"
    st.session_state.message_type = "info"

    st.rerun()


def use_double_damage():

    if st.session_state.mode != "1 Player":
        st.info("Double Damage is available in 1 Player mode.")
        return

    if st.session_state.p1_coins < 8:
        st.warning("You need 8 coins.")
        return

    st.session_state.p1_coins -= 8
    st.session_state.double_damage = True

    add_log("💥 Double Damage activated.")

    st.session_state.message = (
        "💥 NEXT ATTACK = DOUBLE DAMAGE!"
    )

    st.session_state.message_type = "success"

    st.rerun()


def use_heal():

    player = st.session_state.current_player

    if player == 1:

        if st.session_state.p1_coins < 10:
            st.warning("You need 10 coins.")
            return

        if st.session_state.p1_hp >= st.session_state.p1_max_hp:
            st.info("Your HP is already full.")
            return

        st.session_state.p1_coins -= 10

        heal = 25

        st.session_state.p1_hp = min(
            st.session_state.p1_max_hp,
            st.session_state.p1_hp + heal
        )

        add_log(
            f"❤️ {st.session_state.player1_name} healed +{heal} HP."
        )

    else:

        if st.session_state.p2_coins < 10:
            st.warning("You need 10 coins.")
            return

        if st.session_state.p2_hp >= st.session_state.p2_max_hp:
            st.info("Your HP is already full.")
            return

        st.session_state.p2_coins -= 10

        heal = 25

        st.session_state.p2_hp = min(
            st.session_state.p2_max_hp,
            st.session_state.p2_hp + heal
        )

        add_log(
            f"❤️ {st.session_state.player2_name} healed +{heal} HP."
        )

    st.session_state.message = "❤️ +25 HP!"
    st.session_state.message_type = "success"

    st.rerun()


# ============================================================
# ACHIEVEMENTS
# ============================================================

def check_achievements():

    achievements = st.session_state.achievements

    if st.session_state.mode == "1 Player":

        if (
            st.session_state.p1_best_combo >= 5
            and "🔥 Combo Master" not in achievements
        ):
            achievements.append("🔥 Combo Master")

        if (
            st.session_state.p1_correct >= 10
            and "🎯 Sharp Mind" not in achievements
        ):
            achievements.append("🎯 Sharp Mind")

        if (
            st.session_state.round >= 5
            and "👑 Boss Hunter" not in achievements
        ):
            achievements.append("👑 Boss Hunter")

        if (
            st.session_state.p1_score >= 2000
            and "💰 Score Machine" not in achievements
        ):
            achievements.append("💰 Score Machine")

    else:

        if (
            st.session_state.p1_best_combo >= 5
            and "🔥 P1 Combo Master" not in achievements
        ):
            achievements.append("🔥 P1 Combo Master")

        if (
            st.session_state.p2_best_combo >= 5
            and "🔥 P2 Combo Master" not in achievements
        ):
            achievements.append("🔥 P2 Combo Master")


# ============================================================
# FINISH GAME
# ============================================================

def finish_game(result):

    st.session_state.game_started = False
    st.session_state.result = result
    st.session_state.screen = "result"

    st.session_state.total_matches += 1

    if result == "win":
        st.session_state.wins += 1
    elif result == "loss":
        st.session_state.losses += 1

    timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")

    if st.session_state.mode == "1 Player":

        score = st.session_state.p1_score

        record = {
            "Date": timestamp,
            "Player": st.session_state.player1_name,
            "Mode": "1 Player",
            "Difficulty": st.session_state.difficulty,
            "Result": (
                "Victory"
                if result == "win"
                else "Defeat"
            ),
            "Score": score,
            "Best Combo": st.session_state.p1_best_combo,
        }

    else:

        if result == "p1_win":
            winner = st.session_state.player1_name
        elif result == "p2_win":
            winner = st.session_state.player2_name
        else:
            winner = "Draw"

        record = {
            "Date": timestamp,
            "Player": winner,
            "Mode": "2 Players",
            "Difficulty": st.session_state.difficulty,
            "Result": (
                "Draw"
                if result == "draw"
                else "Victory"
            ),
            "Score": max(
                st.session_state.p1_score,
                st.session_state.p2_score,
            ),
            "Best Combo": max(
                st.session_state.p1_best_combo,
                st.session_state.p2_best_combo,
            ),
        }

    st.session_state.history.insert(0, record)

    st.session_state.history = st.session_state.history[:20]


# ============================================================
# HOME SCREEN
# ============================================================

def show_home():

    st.title("⚔️ MATHS ARENA PRO")
    st.subheader("THINK FAST • ATTACK SMART • MASTER MATHEMATICS")

    st.info(
        "🎮 A mathematics battle game where every correct answer "
        "becomes an attack."
    )

    st.divider()

    st.header("🎮 Enter the Arena")

    col1, col2 = st.columns(2)

    with col1:

        player1 = st.text_input(
            "👤 Player 1",
            value=st.session_state.player1_name,
            max_chars=20,
        )

        mode = st.radio(
            "⚔️ Game Mode",
            ["1 Player", "2 Players"],
            horizontal=True,
        )

    with col2:

        if mode == "2 Players":

            player2 = st.text_input(
                "👤 Player 2",
                value=(
                    ""
                    if st.session_state.player2_name == "Player 2"
                    else st.session_state.player2_name
                ),
                max_chars=20,
                placeholder="Enter Player 2 name",
            )

            st.caption(
                "👥 Local 2-player battle: same device, alternating turns."
            )

        else:

            player2 = "Player 2"

            st.success(
                "🤖 You will fight the Arena AI."
            )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        battle_type = st.radio(
            "🏟️ Battle Type",
            ["Endless Arena", "Quick Battle"],
            horizontal=True,
        )

        if battle_type == "Endless Arena":
            st.caption(
                "Survive as many enemy rounds as possible."
            )
        else:
            st.caption(
                "Short battle designed for a quick session."
            )

    with col4:

        difficulty = st.select_slider(
            "🔥 Difficulty",
            options=[
                "Basic",
                "Medium",
                "Pro",
                "Master",
            ],
            value=st.session_state.difficulty,
        )

    st.divider()

    st.header("⚡ Game Systems")

    features = st.columns(4)

    with features[0]:
        st.metric("⚔️ Battle", "LIVE")
        st.caption("Solve → Attack")

    with features[1]:
        st.metric("🔥 Combo", "MULTIPLIER")
        st.caption("Keep answering")

    with features[2]:
        st.metric("💥 Power", "BOOST")
        st.caption("Use your coins")

    with features[3]:
        st.metric("👑 Boss", "ROUND 5+")
        st.caption("Big rewards")

    st.divider()

    if st.button(
        "⚔️ START BATTLE",
        type="primary",
        use_container_width=True,
    ):

        st.session_state.player1_name = (
            player1.strip() or "Player 1"
        )

        st.session_state.player2_name = (
            player2.strip() or "Player 2"
        )

        st.session_state.mode = mode
        st.session_state.battle_type = battle_type
        st.session_state.difficulty = difficulty

        start_game()
        st.rerun()


# ============================================================
# BATTLE SCREEN
# ============================================================

def show_battle():

    if not st.session_state.game_started:
        st.session_state.screen = "result"
        st.rerun()

    mode = st.session_state.mode

    st.title("⚔️ BATTLE ARENA")

    if mode == "1 Player":

        st.caption(
            f"Round {st.session_state.round} • "
            f"{st.session_state.difficulty} • "
            f"{st.session_state.battle_type}"
        )

    else:

        st.caption(
            f"Turn {st.session_state.turn_count} • "
            f"Round {st.session_state.round} • "
            f"{st.session_state.difficulty}"
        )

    # --------------------------------------------------------
    # SINGLE PLAYER HUD
    # --------------------------------------------------------

    if mode == "1 Player":

        player_col, enemy_col = st.columns(2)

        with player_col:

            st.subheader(
                f"🧑 {st.session_state.player1_name}"
            )

            st.metric(
                "❤️ HP",
                f"{st.session_state.p1_hp} / "
                f"{st.session_state.p1_max_hp}",
            )

            st.progress(
                st.session_state.p1_hp
                / st.session_state.p1_max_hp
            )

            p1_metrics = st.columns(3)

            with p1_metrics[0]:
                st.metric(
                    "🏆 Score",
                    st.session_state.p1_score,
                )

            with p1_metrics[1]:
                st.metric(
                    "🔥 Combo",
                    st.session_state.p1_combo,
                )

            with p1_metrics[2]:
                st.metric(
                    "🪙 Coins",
                    st.session_state.p1_coins,
                )

            if st.session_state.fever:
                st.success("🔥 FEVER MODE ACTIVE!")

        with enemy_col:

            boss_label = (
                "👑 BOSS"
                if st.session_state.is_boss
                else "👹 ENEMY"
            )

            st.subheader(
                f"{st.session_state.enemy_icon} "
                f"{st.session_state.enemy_name}"
            )

            st.caption(boss_label)

            st.metric(
                "❤️ HP",
                f"{st.session_state.enemy_hp} / "
                f"{st.session_state.enemy_max_hp}",
            )

            st.progress(
                st.session_state.enemy_hp
                / st.session_state.enemy_max_hp
            )

            st.write(
                f"🎯 Round {st.session_state.round}"
            )

            if st.session_state.is_boss:
                st.warning(
                    "👑 BOSS BATTLE — defeat the boss for bonus rewards!"
                )

    # --------------------------------------------------------
    # TWO PLAYER HUD
    # --------------------------------------------------------

    else:

        p1_col, vs_col, p2_col = st.columns([4, 1, 4])

        with p1_col:

            if st.session_state.current_player == 1:
                st.success(
                    f"⚡ {st.session_state.player1_name}'s TURN"
                )

            st.subheader(
                f"🧑 {st.session_state.player1_name}"
            )

            st.metric(
                "❤️ HP",
                f"{st.session_state.p1_hp} / "
                f"{st.session_state.p1_max_hp}",
            )

            st.progress(
                st.session_state.p1_hp
                / st.session_state.p1_max_hp
            )

            m = st.columns(3)

            with m[0]:
                st.metric(
                    "🏆 Score",
                    st.session_state.p1_score,
                )

            with m[1]:
                st.metric(
                    "🔥 Combo",
                    st.session_state.p1_combo,
                )

            with m[2]:
                st.metric(
                    "🪙 Coins",
                    st.session_state.p1_coins,
                )

            if st.session_state.p1_shield:
                st.info("🛡️ Shield ready")

        with vs_col:

            st.write("")
            st.write("")
            st.title("VS")

        with p2_col:

            if st.session_state.current_player == 2:
                st.success(
                    f"⚡ {st.session_state.player2_name}'s TURN"
                )

            st.subheader(
                f"🧑 {st.session_state.player2_name}"
            )

            st.metric(
                "❤️ HP",
                f"{st.session_state.p2_hp} / "
                f"{st.session_state.p2_max_hp}",
            )

            st.progress(
                st.session_state.p2_hp
                / st.session_state.p2_max_hp
            )

            m = st.columns(3)

            with m[0]:
                st.metric(
                    "🏆 Score",
                    st.session_state.p2_score,
                )

            with m[1]:
                st.metric(
                    "🔥 Combo",
                    st.session_state.p2_combo,
                )

            with m[2]:
                st.metric(
                    "🪙 Coins",
                    st.session_state.p2_coins,
                )

            if st.session_state.p2_shield:
                st.info("🛡️ Shield ready")

    st.divider()

    # --------------------------------------------------------
    # MESSAGE
    # --------------------------------------------------------

    if st.session_state.message:

        if st.session_state.message_type == "success":
            st.success(st.session_state.message)

        elif st.session_state.message_type == "error":
            st.error(st.session_state.message)

        else:
            st.info(st.session_state.message)

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.header("🎯 YOUR MOVE")

    current_player_name = (
        st.session_state.player1_name
        if st.session_state.current_player == 1
        else st.session_state.player2_name
    )

    st.info(
        f"⚡ {current_player_name}, solve this to attack!"
    )

    q_col1, q_col2, q_col3 = st.columns([1, 3, 1])

    with q_col2:

        st.subheader(
            f"🧮 {st.session_state.question} = ?"
        )

        st.caption(
            "Choose the correct answer."
        )

    st.write("")

    # --------------------------------------------------------
    # ANSWERS
    # --------------------------------------------------------

    options = st.session_state.options

    if (
        st.session_state.correct_answer not in options
        or len(options) != 4
    ):
        options = generate_options(
            st.session_state.correct_answer
        )
        st.session_state.options = options

    answer_cols = st.columns(4)

    for index, option in enumerate(options):

        with answer_cols[index]:

            if st.button(
                f"⚔️ {option}",
                key=(
                    f"answer_"
                    f"{st.session_state.turn_count}_"
                    f"{st.session_state.round}_"
                    f"{index}"
                ),
                use_container_width=True,
            ):
                answer_question(option)

    st.divider()

    # --------------------------------------------------------
    # POWER UPS
    # --------------------------------------------------------

    st.subheader("⚡ Power-Ups")

    power1, power2, power3 = st.columns(3)

    with power1:

        if st.button(
            "🛡️ Shield — 5 🪙",
            use_container_width=True,
        ):
            use_shield()

    with power2:

        if mode == "1 Player":

            if st.button(
                "💥 Double Damage — 8 🪙",
                use_container_width=True,
            ):
                use_double_damage()

        else:

            st.caption(
                "💥 Double Damage is for 1 Player."
            )

    with power3:

        if st.button(
            "❤️ Heal +25 — 10 🪙",
            use_container_width=True,
        ):
            use_heal()

    st.divider()

    # --------------------------------------------------------
    # BATTLE LOG
    # --------------------------------------------------------

    with st.expander("📜 Battle Log", expanded=False):

        if st.session_state.battle_log:

            for log in st.session_state.battle_log:
                st.write(log)

        else:
            st.caption("Battle events will appear here.")

    if st.button(
        "🏠 Leave Battle",
        use_container_width=True,
    ):

        st.session_state.game_started = False
        st.session_state.screen = "home"
        st.rerun()


# ============================================================
# RESULT SCREEN
# ============================================================

def show_result():

    result = st.session_state.result

    if result == "win":

        st.title("🏆 VICTORY!")

        st.success(
            f"{st.session_state.player1_name} conquered the Arena!"
        )

        score = st.session_state.p1_score
        combo = st.session_state.p1_best_combo
        xp = st.session_state.p1_xp
        coins = st.session_state.p1_coins

    elif result == "loss":

        st.title("💀 RUN OVER")

        st.warning(
            "The Arena defeated you this time. "
            "Start another run and beat your record."
        )

        score = st.session_state.p1_score
        combo = st.session_state.p1_best_combo
        xp = st.session_state.p1_xp
        coins = st.session_state.p1_coins

    elif result == "p1_win":

        st.title("🏆 PLAYER 1 WINS!")

        st.success(
            f"{st.session_state.player1_name} "
            f"defeated {st.session_state.player2_name}!"
        )

        score = st.session_state.p1_score
        combo = st.session_state.p1_best_combo
        xp = st.session_state.p1_xp
        coins = st.session_state.p1_coins

    elif result == "p2_win":

        st.title("🏆 PLAYER 2 WINS!")

        st.success(
            f"{st.session_state.player2_name} "
            f"defeated {st.session_state.player1_name}!"
        )

        score = st.session_state.p2_score
        combo = st.session_state.p2_best_combo
        xp = st.session_state.p2_xp
        coins = st.session_state.p2_coins

    else:

        st.title("🤝 DRAW!")

        st.info(
            "Both players survived the Quick Battle."
        )

        score = max(
            st.session_state.p1_score,
            st.session_state.p2_score,
        )

        combo = max(
            st.session_state.p1_best_combo,
            st.session_state.p2_best_combo,
        )

        xp = max(
            st.session_state.p1_xp,
            st.session_state.p2_xp,
        )

        coins = max(
            st.session_state.p1_coins,
            st.session_state.p2_coins,
        )

    st.divider()

    st.header("📊 Battle Results")

    stats = st.columns(4)

    with stats[0]:
        st.metric("🏆 Score", score)

    with stats[1]:
        st.metric("🔥 Best Combo", combo)

    with stats[2]:
        st.metric("⭐ XP", xp)

    with stats[3]:
        st.metric("🪙 Coins", coins)

    st.divider()

    if st.session_state.mode == "1 Player":

        stats2 = st.columns(4)

        with stats2[0]:
            st.metric(
                "🎯 Correct",
                st.session_state.p1_correct,
            )

        with stats2[1]:
            st.metric(
                "🧮 Attempts",
                st.session_state.p1_attempts,
            )

        with stats2[2]:
            st.metric(
                "📈 Accuracy",
                f"{accuracy(
                    st.session_state.p1_correct,
                    st.session_state.p1_attempts
                )}%",
            )

        with stats2[3]:
            st.metric(
                "👑 Level",
                player_level(
                    st.session_state.p1_xp
                ),
            )

    else:

        st.header("⚔️ Final Duel Stats")

        duel = st.columns(2)

        with duel[0]:

            st.subheader(
                f"🧑 {st.session_state.player1_name}"
            )

            st.metric(
                "Score",
                st.session_state.p1_score,
            )

            st.metric(
                "Best Combo",
                st.session_state.p1_best_combo,
            )

            st.metric(
                "Accuracy",
                f"{accuracy(
                    st.session_state.p1_correct,
                    st.session_state.p1_attempts
                )}%",
            )

        with duel[1]:

            st.subheader(
                f"🧑 {st.session_state.player2_name}"
            )

            st.metric(
                "Score",
                st.session_state.p2_score,
            )

            st.metric(
                "Best Combo",
                st.session_state.p2_best_combo,
            )

            st.metric(
                "Accuracy",
                f"{accuracy(
                    st.session_state.p2_correct,
                    st.session_state.p2_attempts
                )}%",
            )

    st.divider()

    st.header("🏅 Achievements")

    if st.session_state.achievements:

        achievement_cols = st.columns(
            min(4, len(st.session_state.achievements))
        )

        for i, achievement in enumerate(
            st.session_state.achievements
        ):

            with achievement_cols[
                i % len(achievement_cols)
            ]:

                st.success(achievement)

    else:

        st.info(
            "No achievements unlocked yet. "
            "Keep playing!"
        )

    st.divider()

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
            "🏠 MAIN MENU",
            use_container_width=True,
        ):

            reset_game()
            st.session_state.screen = "home"
            st.rerun()


# ============================================================
# PROFILE SCREEN
# ============================================================

def show_profile():

    st.title("👤 PLAYER PROFILE")

    st.subheader(
        f"🧑 {st.session_state.player1_name}"
    )

    p1_level = player_level(
        st.session_state.p1_xp
    )

    p1_next = xp_to_next_level(
        st.session_state.p1_xp
    )

    metrics = st.columns(4)

    with metrics[0]:
        st.metric("👑 Level", p1_level)

    with metrics[1]:
        st.metric("⭐ XP", st.session_state.p1_xp)

    with metrics[2]:
        st.metric("🪙 Coins", st.session_state.p1_coins)

    with metrics[3]:
        st.metric("🏆 Best Score", st.session_state.p1_score)

    st.progress(
        min(
            1.0,
            (st.session_state.p1_xp % 100) / 100,
        )
    )

    st.caption(
        f"Next level target: {p1_next} XP"
    )

    st.divider()

    stats = st.columns(4)

    with stats[0]:
        st.metric(
            "🔥 Best Combo",
            st.session_state.p1_best_combo,
        )

    with stats[1]:
        st.metric(
            "🎯 Correct",
            st.session_state.p1_correct,
        )

    with stats[2]:
        st.metric(
            "🧮 Attempts",
            st.session_state.p1_attempts,
        )

    with stats[3]:
        st.metric(
            "📈 Accuracy",
            f"{accuracy(
                st.session_state.p1_correct,
                st.session_state.p1_attempts
            )}%",
        )

    st.divider()

    st.header("🏅 Achievements")

    if st.session_state.achievements:

        for achievement in st.session_state.achievements:
            st.success(achievement)

    else:

        st.info(
            "Play battles to unlock achievements."
        )

    st.divider()

    if st.button(
        "🏠 Back to Arena",
        use_container_width=True,
    ):

        st.session_state.screen = "home"
        st.rerun()


# ============================================================
# HISTORY SCREEN
# ============================================================

def show_history():

    st.title("📜 MATCH HISTORY")

    if not st.session_state.history:

        st.info(
            "No matches yet. Your battles will appear here."
        )

    else:

        st.dataframe(
            st.session_state.history,
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    if st.button(
        "🏠 Back to Arena",
        use_container_width=True,
    ):

        st.session_state.screen = "home"
        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

def show_sidebar():

    with st.sidebar:

        st.title("⚔️ Arena")

        st.caption(
            "Maths Arena Pro"
        )

        st.divider()

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

        if st.button(
            "📜 Match History",
            use_container_width=True,
        ):

            st.session_state.screen = "history"
            st.rerun()

        st.divider()

        st.metric(
            "🏆 Matches",
            st.session_state.total_matches,
        )

        st.metric(
            "🥇 Wins",
            st.session_state.wins,
        )

        st.metric(
            "💀 Losses",
            st.session_state.losses,
        )

        st.divider()

        st.caption(
            "Solve mathematics. "
            "Build combos. "
            "Defeat the Arena."
        )


# ============================================================
# MAIN ROUTER
# ============================================================

show_sidebar()

if st.session_state.screen == "home":

    show_home()

elif st.session_state.screen == "battle":

    show_battle()

elif st.session_state.screen == "result":

    show_result()

elif st.session_state.screen == "profile":

    show_profile()

elif st.session_state.screen == "history":

    show_history()

else:

    st.session_state.screen = "home"
    show_home()
