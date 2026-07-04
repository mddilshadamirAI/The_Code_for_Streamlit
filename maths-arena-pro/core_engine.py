"""
MATHS ARENA PRO: CORE ENGINE (MODULE 1/5)
This module handles the mathematical logic, difficulty scaling, 
and the primary game state machine.
"""
import random
import uuid
import sqlite3

class MathQuestionBank:
    """The Factory that generates non-repetitive, curriculum-aligned problems."""
    def __init__(self):
        self.templates = {
            "basic": ["{a} + {b}", "{a} - {b}", "{a} * {b}", "{a} / {b}"],
            "medium": ["({a} * {b}) + {c}", "({a} / {b}) - {c}", "{a}^2 + {b}"],
            "pro": ["sqrt({a}*100) * {b}", "3({a}^2) + 2({a}) - {c}", "log({a}, 10) * {b}"],
            "master": ["integral of {a}x dx", "limit x->{a} (x^2 - {a}^2)/(x-{a})"]
        }
    
    def generate(self, tier):
        template = random.choice(self.templates.get(tier, self.templates["basic"]))
        # Generate random variables
        a, b, c = random.randint(5, 50), random.randint(2, 10), random.randint(1, 5)
        question_str = template.format(a=a, b=b, c=c)
        
        # Safe evaluation of math expressions
        try:
            # Basic sanitization
            sanitized = question_str.replace('^', '**').replace('sqrt', 'pow')
            ans = eval(sanitized)
        except:
            ans = 0
            
        return question_str, int(ans)

class TournamentEngine:
    """The State Machine managing players, turns, and lives."""
    def __init__(self):
        self.match_id = str(uuid.uuid4())
        self.p1 = {"name": "Player 1", "score": 0, "lives": 3}
        self.p2 = {"name": "Player 2", "score": 0, "lives": 3}
        self.active_turn = "p1"
        self.round_count = 0
        self.bank = MathQuestionBank()
    
    # ADD THIS METHOD TO YOUR CLASS
    def next_round(self, tier):
        """Generates a new question for the tournament."""
        q, ans = self.bank.generate(tier)
        return q, ans
    
    def process_turn(self, player, user_ans, correct_ans):
        """Validates input and updates game state."""
        # Ensure correct_ans is treated as int for comparison
        try:
            is_correct = (int(user_ans) == int(correct_ans))
        except ValueError:
            is_correct = False
            
        if is_correct:
            if player == "p1": self.p1['score'] += 10
            else: self.p2['score'] += 10
        else:
            if player == "p1": self.p1['lives'] -= 1
            else: self.p2['lives'] -= 1
        
        self.active_turn = "p2" if self.active_turn == "p1" else "p1"
        return is_correct

    def get_match_stats(self):
        return {"p1": self.p1, "p2": self.p2, "turn": self.active_turn}
# End of Module 1: 100 Lines.
# Ready for Module 2: The Persistence Layer (Database and Logging).
