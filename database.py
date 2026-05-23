# ============================================================
# 📚 CYBER ARENA MASTER TEXTBOOK VAULT (`database.py`)
# ============================================================

# ------------------------------------------------------------
# PHASE 1: Baseline Questions (From your original app.py)
# ------------------------------------------------------------
PHASE_1_QUESTIONS = {
    "Class 1": {
        "Ch 1: Shapes & Space": [
            {"question": "NCERT Ex 1.1: A cat is sitting inside a basket and a puppy is playing outside. Where is the cat? Inside (1) or Outside (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "NCERT Ex 1.2: A sparrow sits on the top of a temple tree, and a snake crawls at the bottom ground. Where is the snake? Top (1) or Bottom (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 1: Rohan parks his bicycle near the school gate, but leaves his football far away. Which object is farther from the gate? Bicycle (1) or Football (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "NCERT Ex 1.3: Look at a giant festival elephant and a tiny garden ant. Which animal is strictly smaller? Elephant (1) or Ant (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 1: A round currency coin is placed next to a textbook. What geometric shape layout does the coin look like? Circle (1), Triangle (2), Square (3)?", "answer": 1, "options": [1, 2, 3, 4]}
        ],
        "Ch 2: Numbers 1 to 9": [
            {"question": "NCERT Ex 2.1: Count the total number of individual alphabetic letters spelling out the exact subject word 'MATHS'.", "answer": 5, "options": [3, 4, 5, 6]},
            {"question": "RS Aggarwal Ch 2: What fundamental standalone counting integer value follows directly after the number 7?", "answer": 8, "options": [6, 7, 8, 9]},
            {"question": "NCERT Ex 2.3: Identify the missing structural sequence number that completes this counting line: 3, 4, 5, __, 7.", "answer": 6, "options": [5, 6, 7, 8]},
            {"question": "RS Aggarwal Ch 2: Sana has 4 balloons. If Amit has a collection strictly GREATER than 4, which option could be his? 2, 3, 4, or 6?", "answer": 6, "options": [2, 3, 4, 6]}
        ]
    },
    "Class 2": {
        "Ch 2: Counting in Groups": [
            {"question": "NCERT Ex 2.1: Radha arranges matching pairs of earrings. If she has 6 complete pairs, how many individual earrings does she possess?", "answer": 12, "options": [6, 10, 12, 14]},
            {"question": "RS Aggarwal Ch 3: A bundle contains exactly 10 wooden sticks. If a farmer builds 4 full bundles and has 5 loose sticks left over, what is the net count?", "answer": 45, "options": [40, 45, 54, 50]}
        ],
        "Ch 7: Jugs and Mugs": [
            {"question": "NCERT Ex 7.2: A large cooking pot can hold exactly 15 mugs of soup fluid. If a small family jug holds 3 mugs, how many full jugs are needed to fill the pot?", "answer": 5, "options": [3, 4, 5, 6]},
            {"question": "RS Aggarwal Ch 8: A bucket contains 8 litres of water. If Ram removes 3 litres using a mug container, how many litres of water remain inside the bucket?", "answer": 5, "options": [4, 5, 6, 11]}
        ]
    },
    "Class 3": {
        "Ch 2: Fun with Numbers": [
            {"question": "NCERT Ex 2.2: Dhoni scored 96 runs in a cricket match. How many more runs did he require to complete a glorious century (100 runs)?", "answer": 4, "options": [2, 4, 6, 10]},
            {"question": "RS Aggarwal Ch 2: Read the place parameters: What is the true place value of the digit 6 inside the numeral integer 462?", "answer": 60, "options": [6, 60, 600, 2]}
        ],
        "Ch 4: Long and Short": [
            {"question": "NCERT Ex 4.1: A tailor uses a measuring tape layout. If a piece of silk cloth measures exactly 3 meters, express this distance metric in centimeters.", "answer": 300, "options": [30, 100, 300, 3000]},
            {"question": "RS Aggarwal Ch 9: An athlete ran a sprint distance of 2000 meters during a training camp. Express this track run distance cleanly in kilometers.", "answer": 2, "options": [2, 20, 200, 1]}
        ]
    },
    "Class 4": {
        "Ch 1: Building with Bricks": [
            {"question": "NCERT Ex 1.1: A brick merchant charges Rs. 2000 for exactly 1000 bricks. Find the purchasing price of a single structural brick unit.", "answer": 2, "options": [1, 2, 5, 10]},
            {"question": "RS Aggarwal Ch 1: A brick face layout shows regular boundary lines. How many faces does a standard solid 3D building brick possess?", "answer": 6, "options": [4, 6, 8, 12]}
        ],
        "Ch 4: Tick-Tick-Tick": [
            {"question": "NCERT Ex 4.2: A school sports drill starts at 08:15 AM and concludes at 10:45 AM. Calculate the absolute duration of the sports drill session in minutes.", "answer": 150, "options": [120, 130, 150, 180]},
            {"question": "RS Aggarwal Ch 15: An automated manufacturing conveyor belt runs for 3 hours and 20 minutes. Convert this complete operational run time into net minutes.", "answer": 200, "options": [180, 200, 220, 240]}
        ]
    },
    "Class 5": {
        "Ch 1: The Fish Tale": [
            {"question": "NCERT Ex 1.1: A fisherman log boat catches 20 kg of fish per trip. If the boat completes 7 successful trips, what is the grand total weight caught?", "answer": 140, "options": [120, 140, 160, 200]},
            {"question": "RS Aggarwal Ch 4: A fast motor boat travels at a uniform speed of 22 km per hour. How far will this boat travel in 3 hours of non-stop navigation?", "answer": 66, "options": [60, 64, 66, 72]}
        ],
        "Ch 11: Area and its Boundary": [
            {"question": "NCERT Ex 11.2: A rectangular school patch layout measures 15 meters in length and 10 meters in width. Compute its total square meter area.", "answer": 150, "options": [50, 150, 300, 250]},
            {"question": "RS Aggarwal Ch 18: Find the perimeter boundary line of a perfect square garden plot whose single outer edge fence measures 12 meters.", "answer": 48, "options": [24, 36, 48, 144]}
        ]
    },
    "Class 6": {
        "Ch 1: Knowing Our Numbers": [
            {"question": "NCERT Ex 1.2: A vessel contains 4 litres and 500 ml of fresh curd fluid. How many small dispensing glasses, each of 25 ml capacity, can be filled completely?", "answer": 180, "options": [150, 180, 200, 220]},
            {"question": "RS Aggarwal Ch 1: Find the absolute mathematical difference between the greatest 5-digit number and the smallest 5-digit number formable using all digits 9, 4, 3, 2, 1.", "answer": 83952, "options": [83952, 85000, 79999, 81240]}
        ],
        "Ch 3: Playing with Numbers": [
            {"question": "NCERT Ex 3.7: Three tankers contain 403 litres, 434 litres, and 465 litres of diesel respectively. Find the maximum capacity of a container that can measure the diesel of all three tankers an exact number of times (HCF).", "answer": 31, "options": [21, 31, 41, 51]},
            {"question": "RS Aggarwal Ch 2: Two traffic signals flash every 60 seconds and 90 seconds respectively. If they flash together at 8:00 AM, after how many seconds will they flash together again?", "answer": 180, "options": [120, 150, 180, 240]}
        ]
    },
    "Class 7": {
        "Ch 1: Integers": [
            {"question": "NCERT Ex 1.1: A research submarine cruises at a depth of -250 meters below sea level. It executes a dive command descending 120 meters further down. What is its new position coordinate?", "answer": -370, "options": [-130, -370, 370, -350]},
            {"question": "RS Aggarwal Ch 1: During a high-altitude weather simulation, the starting room temperature is 15°C. The cooling unit drops the temperature by 4°C every hour. What is the room temperature after 5 hours?", "answer": -5, "options": [5, 0, -5, -10]}
        ],
        "Ch 4: Simple Equations": [
            {"question": "NCERT Ex 4.1: Irfan states that he has 7 marbles more than five times the marbles Parmit has. If Irfan has 37 marbles in his collection, find how many marbles Parmit has.", "answer": 6, "options": [5, 6, 7, 8]},
            {"question": "RS Aggarwal Ch 4: Solve the structural balance expression to find the isolated coordinate matrix value of x: 3x - 8 = 13.", "answer": 7, "options": [5, 6, 7, 8]}
        ]
    },
    "Class 8": {
        "Ch 2: Linear Equations": [
            {"question": "NCERT Ex 2.2: The perimeter of a rectangular swimming pool is 154 m. Its length is 2 m more than twice its breadth. Determine the breadth of the pool.", "answer": 25, "options": [20, 25, 30, 35]},
            {"question": "RS Aggarwal Ch 8: Two numbers are in the ratio 5:3. If they differ from each other by exactly 18 units, determine the value of the larger structural number.", "answer": 45, "options": [27, 45, 54, 63]}
        ],
        "Ch 12: Exponents and Powers": [
            {"question": "NCERT Ex 12.1: Simplify the laws of exponents payload calculation string cleanly to find the integer answer token value: (3^-1 + 4^-1 + 5^-1)^0", "answer": 1, "options": [0, 1, 12, 60]},
            {"question": "RS Aggarwal Ch 2: Evaluate the computational component expression parameters to resolve the base power value: (2/3)^-2 multiplied by (2/3)^4. What is the final value over 9?", "answer": 4, "options": [2, 4, 6, 8]}
        ]
    }
}

# ------------------------------------------------------------
# 📝 PASTING ZONE: Paste your collected phases below!
# ------------------------------------------------------------

# ============================================================
# 📚 PHASE 2: VAULT EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_2_QUESTIONS = {
    "Class 1": {
        "Ch 3: Addition Drill": [
            {"question": "NCERT Ex 3.1: Three cows are grazing peacefully in a green field. Soon, 2 more cows walk over to join them. Count the total number of cows.", "answer": 5, "options": [4, 5, 6, 7]},
            {"question": "RS Aggarwal Ch 3: Rahul has 5 juicy red tomatoes in his basket. His mother drops 4 more yellow tomatoes into it. How many tomatoes does he have now?", "answer": 9, "options": [8, 9, 10, 11]},
            {"question": "NCERT Ex 3.4: There are 6 children playing on a slide. 2 more children run over to play with them. What is the total sum of children on the slide?", "answer": 8, "options": [6, 7, 8, 9]}
        ],
        "Ch 5: Numbers 10 to 20": [
            {"question": "NCERT Ex 5.2: You have a group bundle of 10 chocolates and 3 loose individual chocolates left over. What is the final numeral layout value?", "answer": 13, "options": [10, 12, 13, 31]},
            {"question": "RS Aggarwal Ch 5: Count backward from the number 20. What specific counting integer comes directly before 19?", "answer": 18, "options": [17, 18, 19, 20]}
        ]
    },
    "Class 2": {
        "Ch 4: Counting in Tens": [
            {"question": "NCERT Ex 4.1: Traki collects 35 chickens on her farm. She places exactly 10 chickens inside each wooden basket. How many baskets are completely filled?", "answer": 3, "options": [2, 3, 4, 5]},
            {"question": "RS Aggarwal Ch 4: A woodcutter makes bundles of 10 twigs each. If he completes 6 full bundles, how many twigs has he secured in total?", "answer": 60, "options": [50, 56, 60, 66]}
        ],
        "Ch 10: Add Our Points": [
            {"question": "NCERT Ex 10.2: In a boarding game, a smart lizard moves along a wall to eat insects. To score exactly 12 points, it takes a path through three nodes: 5, 4, and what missing number?", "answer": 3, "options": [2, 3, 4, 5]},
            {"question": "RS Aggarwal Ch 12: In a cricket match overview, Sachin scores 14 runs in his first over and 11 runs in his second over. Calculate his total combined score.", "answer": 25, "options": [23, 24, 25, 26]}
        ]
    },
    "Class 3": {
        "Ch 3: Give and Take": [
            {"question": "NCERT Ex 3.2: A merchant shopkeeper has 243 organic eggs on his display shelf. He sells away exactly 120 eggs to customers. How many eggs remain unsold?", "answer": 123, "options": [120, 123, 143, 223]},
            {"question": "RS Aggarwal Ch 4: A massive school library contains 650 storybooks. During the weekend, students check out 150 books. How many books are left on the shelves?", "answer": 500, "options": [450, 480, 500, 550]}
        ],
        "Ch 7: Time Goes On": [
            {"question": "NCERT Ex 7.1: If today's calendar date tracking falls exactly on a Monday, what specific day of the week was it precisely 2 days ago?", "answer": 6, "options": [5, 6, 7, 1]},  # Let Saturday = 6, Sunday = 7, Monday = 1
            {"question": "RS Aggarwal Ch 14: A clock hand points precisely to the number 3 for hours and number 12 for minutes. What exact time does this system configure?", "answer": 3, "options": [3, 6, 9, 12]}
        ]
    },
    "Class 4": {
        "Ch 2: Long and Short": [
            {"question": "NCERT Ex 2.3: A fitness coach tells Devi Prasad to run 2 kilometers every morning. He completes one full round around a square field with a side length of 500 meters. How many total meters did he run?", "answer": 2000, "options": [1000, 1500, 2000, 2500]},
            {"question": "RS Aggarwal Ch 8: The height of a classroom door is 2 meters and 15 centimeters. Express this complete architectural layout parameter in total centimeters.", "answer": 215, "options": [200, 215, 250, 2150]}
        ],
        "Ch 11: Tables and Shares": [
            {"question": "NCERT Ex 11.1: Ganu needs to pack 48 fragile glasses into shipping boxes. If each box can safely hold exactly 6 glasses, how many boxes does he require?", "answer": 8, "options": [6, 7, 8, 9]},
            {"question": "RS Aggarwal Ch 10: A group of 5 friends go out for lunch. The total bill amounts to Rs. 450. If they decide to split the share completely evenly, how much does each person pay?", "answer": 90, "options": [80, 85, 90, 95]}
        ]
    },
    "Class 5": {
        "Ch 2: Shapes and Angles": [
            {"question": "NCERT Ex 2.1: Look closely at the standard capital alphabet letter 'H'. How many perfect right angles (90 degrees) are formed inside its structural design lines?", "answer": 4, "options": [2, 4, 6, 8]},
            {"question": "RS Aggarwal Ch 13: An angle measures exactly 45 degrees on a protractor layout. How do you classify this specific angle archetype? Acute (1), Obtuse (2), Right (3)?", "answer": 1, "options": [1, 2, 3, 4]}
        ],
        "Ch 7: Can You See the Pattern?": [
            {"question": "NCERT Ex 7.2: Analyze the geometric sequence progression blueprint safely: 7, 14, 21, 28, __. Find the missing value coordinate.", "answer": 35, "options": [32, 34, 35, 42]},
            {"question": "RS Aggarwal Ch 20: A number pattern loops by multiplying by 2 each step: 3, 6, 12, 24, __. What value completes this sequence array?", "answer": 48, "options": [36, 40, 48, 50]}
        ]
    },
    "Class 6": {
        "Ch 2: Whole Numbers": [
            {"question": "NCERT Ex 2.2: Compute the sum using smart rearrangement properties to save system execution time: 234 + 197 + 66.", "answer": 497, "options": [434, 497, 500, 512]},
            {"question": "RS Aggarwal Ch 2: What is the true mathematical product identity element value when any whole number is multiplied by zero?", "answer": 0, "options": [0, 1, 10, -1]}
        ],
        "Ch 12: Ratio and Proportion": [
            {"question": "NCERT Ex 12.1: The cost of a dozen premium pens is Rs. 180, and the cost of 8 standard ball pens is Rs. 56. Find the simplified ratio of the cost of one premium pen to one ball pen.", "answer": 15, "options": [15, 7, 2, 5]}  # Ratio is 15:7, taking leading component for game mechanics
        ]
    },
    "Class 7": {
        "Ch 2: Fractions and Decimals": [
            {"question": "NCERT Ex 2.4: Lipika reads an educational textbook for 1.75 hours every day. She completely finishes reading the book in 6 days. Compute the total hours spent.", "answer": 10.5, "options": [9.5, 10.0, 10.5, 12.0]},
            {"question": "RS Aggarwal Ch 3: Convert the structural fraction 7/25 into a clean base-10 decimal format value.", "answer": 0.28, "options": [0.24, 0.28, 0.72, 2.5]}
        ],
        "Ch 8: Comparing Quantities": [
            {"question": "NCERT Ex 8.3: An investor buys an asset property system for Rs. 3,000,000. Next year, its market valuation climbs to Rs. 3,600,000. Find the percentage increase.", "answer": 20, "options": [10, 15, 20, 25]},
            {"question": "RS Aggarwal Ch 9: Out of 40 students in a computer class, 25% pass a programming challenge. Find the absolute number of students who cleared the benchmark.", "answer": 10, "options": [8, 10, 12, 15]}
        ]
    },
    "Class 8": {
        "Ch 1: Rational Numbers": [
            {"question": "NCERT Ex 1.1: Identify the true multiplicative inverse property token value for the negative rational fraction -13/19.", "answer": -1.46, "options": [-1.46, 1.46, -0.68, 1.0]},  # decimal conversion evaluation
            {"question": "RS Aggarwal Ch 1: Find a rational number exactly halfway between the fraction coordinates 1/4 and 1/2.", "answer": 0.375, "options": [0.35, 0.375, 0.45, 0.5]}
        ],
        "Ch 9: Algebraic Expressions": [
            {"question": "NCERT Ex 9.3: Multiply the linear binomial expressions completely: (x + 3)(x + 5). What is the value of the resulting coefficient of the middle 'x' term?", "answer": 8, "options": [3, 5, 8, 15]},
            {"question": "RS Aggarwal Ch 12: Evaluate the polynomial expression system mapping for x = 3: 2x^2 - 5x + 4. What value drops out?", "answer": 7, "options": [5, 7, 11, 13]}
        ]
    }
}

# ============================================================
# 📚 PHASE 3: MASTER VAULT EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_3_QUESTIONS = {
    "Class 1": {
        "Ch 4: Subtraction Drill": [
            {"question": "NCERT Ex 4.1: Six juicy mangoes are kept on a plate. Meera eats 2 of them completely. How many mangoes are left untouched on the plate?", "answer": 4, "options": [2, 3, 4, 5]},
            {"question": "RS Aggarwal Ch 4: A branch has 8 beautiful green leaves. A strong wind blows and 5 leaves fall to the ground. Count the remaining leaves on the branch.", "answer": 3, "options": [2, 3, 4, 5]},
            {"question": "NCERT Ex 4.3: There are 9 glass marbles in a cup. Rohit takes away 4 marbles to play a game. How many marbles stay inside the cup?", "answer": 5, "options": [4, 5, 6, 7]}
        ],
        "Ch 6: Time & Routine": [
            {"question": "NCERT Ex 6.1: Think about your daily schedule sequence. Which activity do you perform earliest in the day? Eating Dinner (1), Sleeping at Night (2), Brushing Teeth in Morning (3)?", "answer": 3, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 6: Which action takes strictly MORE time to complete? Blinking your eye once (1) or Writing a complete page in your notebook (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 2": {
        "Ch 5: Patterns Space": [
            {"question": "NCERT Ex 5.1: Look at the visual pattern sequence: One leaf pointing UP, one leaf pointing DOWN, one UP, one DOWN. What comes next? Leaf pointing UP (1) or Leaf pointing DOWN (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 6: Decode the leaping number logic sequence step-by-step: 2, 4, 6, 8, 10, __. Identify the missing coordinate.", "answer": 12, "options": [11, 12, 13, 14]}
        ],
        "Ch 11: Lines and Lines": [
            {"question": "NCERT Ex 11.3: If you draw a straight line along the flat edge of a standard rectangular ruler, what type of line do you get? Straight Line (1) or Curved Line (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 14: How many straight boundary lines are required to build a perfect geometric triangle layout on paper?", "answer": 3, "options": [2, 3, 4, 5]}
        ]
    },
    "Class 3": {
        "Ch 5: Shapes and Designs": [
            {"question": "NCERT Ex 5.2: Look closely at a standard square piece of paper. How many sharp corners (vertices) can you count along its perimeter?", "answer": 4, "options": [3, 4, 5, 6]},
            {"question": "RS Aggarwal Ch 10: A basic geometric triangle shape has exactly 3 sides. How many distinct corners does it possess?", "answer": 3, "options": [2, 3, 4, 5]}
        ],
        "Ch 11: Jugs and Mugs Deep": [
            {"question": "NCERT Ex 11.1: A large commercial bottle contains exactly 1 litre of mineral water. If Amina drinks 250 ml and her friend drinks 150 ml, how many millilitres of water are left?", "answer": 600, "options": [400, 500, 600, 750]},
            {"question": "RS Aggarwal Ch 16: A dairy bucket holds 5 litres of fresh milk. Express this identical fluid volume measurement completely in millilitres.", "answer": 5000, "options": [50, 500, 5000, 50000]}
        ]
    },
    "Class 4": {
        "Ch 3: A Trip to Bhopal": [
            {"question": "NCERT Ex 3.1: A school trip requires transport. Each school bus can carry exactly 50 children. If 210 children register for the trip, what is the minimum number of buses needed so no one is left out?", "answer": 5, "options": [4, 5, 6, 7]},
            {"question": "RS Aggarwal Ch 4: A group of travelers stops to buy wild bananas. If 1 dozen bananas cost Rs. 36, calculate the cost of purchasing exactly 5 individual bananas using the unitary method.", "answer": 15, "options": [12, 15, 18, 20]}
        ],
        "Ch 13: Fields and Fences": [
            {"question": "NCERT Ex 13.1: Rahmat intends to wire fence his square field layout. If one side of his square field measures exactly 21 meters, calculate the total length of fence wire he must buy.", "answer": 84, "options": [42, 63, 84, 441]},
            {"question": "RS Aggarwal Ch 17: A rectangular running track setup measures 40 meters long and 30 meters wide. An athlete runs exactly 1 full lap around the edge. Calculate the total distance covered.", "answer": 140, "options": [70, 120, 140, 200]}
        ]
    },
    "Class 5": {
        "Ch 3: How Many Squares?": [
            {"question": "NCERT Ex 3.2: A custom stamp layout template has a footprint measuring 3 cm long and 2 cm wide. How many such stamps can cleanly fit inside a larger rectangle of area 24 square cm?", "answer": 4, "options": [4, 6, 8, 12]},
            {"question": "RS Aggarwal Ch 19: The perimeter of a regular square cardboard cutout token is measured at 36 cm. Compute the absolute square area of this cardboard item.", "answer": 81, "options": [36, 64, 81, 144]}
        ],
        "Ch 13: Multiply & Divide Ways": [
            {"question": "NCERT Ex 13.1: A corporate firm pays a master technician a daily wage of Rs. 245. Calculate the total currency amount earned by the technician if he works continuously for 30 days.", "answer": 7350, "options": [7200, 7350, 7450, 7500]},
            {"question": "RS Aggarwal Ch 7: A warehouse clerk needs to pack 576 organic apples into matching wooden crates. If each crate holds 24 apples, how many crates will be packed completely full?", "answer": 24, "options": [20, 22, 24, 26]}
        ]
    },
    "Class 6": {
        "Ch 4: Basic Geometrical Ideas": [
            {"question": "NCERT Ex 4.2: Analyze standard polygon architecture definitions. What is the minimum number of straight line segments required to construct a closed geometric polygon shape?", "answer": 3, "options": [2, 3, 4, 5]},
            {"question": "RS Aggarwal Ch 12: Consider a standard multi-point layout circle blueprint. If the measured radius line segment equals 7 cm, find the absolute length of its longest internal chord (diameter).", "answer": 14, "options": [7, 11, 14, 21]}
        ],
        "Ch 7: Fractions Operations": [
            {"question": "NCERT Ex 7.4: Express the improper textbook fractional numerical expression 17/5 as a clean, properly formatted mixed fraction value footprint. Select the correct integer quotient identifier.", "answer": 3, "options": [2, 3, 4, 5]},
            {"question": "RS Aggarwal Ch 5: Simplify the rational fractional value layout expression to its lowest irreducible form: 48/72. Find the resulting value of the numerator component.", "answer": 2, "options": [2, 3, 4, 6]}
        ]
    },
    "Class 7": {
        "Ch 3: Data Handling Matrix": [
            {"question": "NCERT Ex 3.1: A batsman scores the following sequence of runs across five consecutive match innings: 40, 35, 61, 22, 52. Compute the exact arithmetic mean score.", "answer": 42, "options": [38, 40, 42, 45]},
            {"question": "RS Aggarwal Ch 21: Find the mathematical range parameter for the raw score statistical dataset: 12, 25, 45, 67, 8, 33, 19. (Range = Maximum - Minimum)", "answer": 59, "options": [55, 57, 59, 67]}
        ],
        "Ch 12: Algebraic Expressions": [
            {"question": "NCERT Ex 12.2: Simplify the variable polynomial expression framework by combining matching like terms: 12m^2 - 9m + 5m - 4m^2. Identify the coefficient of the resulting m^2 term.", "answer": 8, "options": [4, 6, 8, 16]},
            {"question": "RS Aggarwal Ch 11: Subtract the algebraic expression value block (3x - 4y) completely away from the expression block (7x + 2y). Find the coefficient of the y term in the final answer.", "answer": 6, "options": [2, 4, 6, 8]}
        ]
    },
    "Class 8": {
        "Ch 3: Quadrilaterals Geometry": [
            {"question": "NCERT Ex 3.1: Calculate the absolute interior angles summation constant value for a standard closed convex quadrilateral polygon template.", "answer": 360, "options": [180, 360, 540, 720]},
            {"question": "RS Aggarwal Ch 15: Three interior angles of a quadrilateral are measured at 80°, 110°, and 75° respectively. Find the measure of the missing fourth angle coordinate.", "answer": 95, "options": [85, 90, 95, 100]}
        ],
        "Ch 6: Squares and Square Roots": [
            {"question": "NCERT Ex 6.4: Use long division or prime factorization to discover the core square root extraction answer token value for the perfect square integer 729.", "answer": 27, "options": [23, 27, 33, 37]},
            {"question": "RS Aggarwal Ch 3: Find the least perfect square number that is completely and evenly divisible by each of the baseline analytical values 4, 9, and 10.", "answer": 900, "options": [180, 360, 900, 3600]}
        ]
    }
}
# ============================================================
# 📚 PHASE 4: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_4_QUESTIONS = {
    "Class 1": {
        "Ch 7: Measurement Drill": [
            {"question": "NCERT Ex 7.1: Look at a long bamboo stick and a short pencil lying on a desk. Which object is strictly LONGER? Bamboo stick (1) or Pencil (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 7: A heavy stone sitting in the garden is compared to a light plastic feather. Which object is HEAVIER? Stone (1) or Feather (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "NCERT Ex 7.4: A large clay pot is filled with water alongside a small glass cup. Which container has GREATER fluid capacity? Clay pot (1) or Glass cup (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ],
        "Ch 8: Numbers 21 to 50": [
            {"question": "NCERT Ex 8.2: If you count a structural sequence block containing 2 full tens bundles and 4 loose ones, what is the net numerical representation?", "answer": 24, "options": [20, 24, 42, 40]},
            {"question": "RS Aggarwal Ch 8: What specific sequential integer follows directly after the number 49?", "answer": 50, "options": [48, 49, 50, 51]}
        ]
    },
    "Class 2": {
        "Ch 8: Tens and Ones Currency": [
            {"question": "NCERT Ex 8.1: Aarav wants to purchase a notebook worth Rs. 25. He only has notes of Rs. 10 and coins of Rs. 1. How many Rs. 10 notes does he need to hand over?", "answer": 2, "options": [2, 3, 5, 25]},
            {"question": "RS Aggarwal Ch 9: If a collection contains exactly 5 notes of Rs. 10 each, calculate the total absolute currency value in rupees.", "answer": 50, "options": [15, 45, 50, 55]}
        ],
        "Ch 12: Give and Take Basics": [
            {"question": "NCERT Ex 12.3: Sonu has 16 glossy beads and Aarif has 24 beads. Find the total number of beads they have collected together.", "answer": 40, "options": [30, 38, 40, 42]},
            {"question": "RS Aggarwal Ch 13: A shopkeeper stocks 45 drawing charts. He sells 18 charts during the morning shift. Calculate the remaining charts on the counter shelf.", "answer": 27, "options": [23, 27, 33, 63]}
        ]
    },
    "Class 3": {
        "Ch 6: Fun with Give & Take": [
            {"question": "NCERT Ex 6.2: In a high-scoring T20 cricket match, India scored 324 runs. The opposing team has chased down 115 runs so far. How many more runs do they need to win the match?", "answer": 210, "options": [200, 209, 210, 215]},
            {"question": "RS Aggarwal Ch 5: Solve the standard subtraction equation layout cleanly to find the missing token balance value: 753 - 421 = ?", "answer": 332, "options": [322, 332, 342, 1174]}
        ],
        "Ch 9: How Many Times?": [
            {"question": "NCERT Ex 9.1: A set of 5 motorbikes are parked in a row. Each motorbike has exactly 2 wheels. Write the total wheel count using repeated multiplication logic.", "answer": 10, "options": [7, 8, 10, 12]},
            {"question": "RS Aggarwal Ch 7: A box contains 6 rows of premium chocolates, and each row holds exactly 10 pieces. Calculate the complete chocolate bundle volume.", "answer": 60, "options": [16, 50, 60, 70]}
        ]
    },
    "Class 4": {
        "Ch 5: The Way World Looks": [
            {"question": "NCERT Ex 5.1: Look at a standard kitchen cylinder gas pipe from directly above. What clean structural geometric shape outline do you see? Circle (1), Rectangle (2), Triangle (3)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 11: A toy train track box contains pieces to build shapes. If you connect elements to create a closed shape with 4 equal sides and 4 corners, what is it? Square (1) or Triangle (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ],
        "Ch 12: How Heavy? How Light?": [
            {"question": "NCERT Ex 12.2: A bag contains 2 kg of organic rice, 3 kg of wholesale dal, and 500 grams of pure sugar. Compute the total mass load of the bag in grams.", "answer": 5500, "options": [5000, 5500, 6000, 2500]},
            {"question": "RS Aggarwal Ch 19: A commercial delivery truck drops off a cargo load weighing exactly 4500 kilograms. Express this total physical mass weight metric in structural metric tonnes (1 tonne = 1000 kg).", "answer": 4.5, "options": [4.0, 4.5, 5.0, 45.0]}
        ]
    },
    "Class 5": {
        "Ch 4: Parts and Wholes": [
            {"question": "NCERT Ex 4.1: A standard national flag design grid is split horizontally into 3 equal stripes. If the top section is dyed saffron, what precise fractional portion of the flag is saffron?", "answer": 0.33, "options": [0.25, 0.33, 0.50, 0.66]},  # rounded representation
            {"question": "RS Aggarwal Ch 5: A student completes 15 mathematics home assignments out of a target workbook pool of 20 tasks. Reduce this status fraction to its simplest irreducible value.", "answer": 0.75, "options": [0.50, 0.60, 0.75, 0.80]}
        ],
        "Ch 12: Smart Charts Matrix": [
            {"question": "NCERT Ex 12.1: A student records a tally chart tracking passing vehicles. If one complete square block with a diagonal line cross represents 5 cars, what value do 4 complete blocks show?", "answer": 20, "options": [15, 20, 24, 25]},
            {"question": "RS Aggarwal Ch 22: A clean bar chart shows that 1 cm of vertical pillar height corresponds to exactly 20 families. If the pillar for the 'Car Owners' group measures 6 cm high, calculate the total family count.", "answer": 120, "options": [100, 110, 120, 140]}
        ]
    },
    "Class 6": {
        "Ch 6: Integers Grid": [
            {"question": "NCERT Ex 6.1: A shop trader logs a net business transaction loss of Rs. 700 during a market dip day. Represent this financial position change using a standard signed integer notation.", "answer": -700, "options": [700, -700, 0, -70]},
            {"question": "RS Aggarwal Ch 4: Evaluate the absolute signed integer calculation block precisely to determine the final system tracking position output: (-12) + (+5) - (-3) = ?", "answer": -4, "options": [-14, -10, -4, 4]}
        ],
        "Ch 8: Decimals Tracking": [
            {"question": "NCERT Ex 8.2: Write the following positional base-10 value layout block cleanly as a single combined decimal string: 200 + 30 + 5 + (2/10) + (9/100)", "answer": 235.29, "options": [235.29, 235.92, 253.29, 2352.9]},
            {"question": "RS Aggarwal Ch 6: Express a currency balance structural measurement value of 7 rupees and 5 paise completely inside a standardized unified decimal rupee notation system.", "answer": 7.05, "options": [7.50, 7.05, 75.0, 0.75]}
        ]
    },
    "Class 7": {
        "Ch 5: Lines and Angles Blueprint": [
            {"question": "NCERT Ex 5.1: Two geometric angles are defined as strictly complementary angles. If the measure of the first angle layout evaluates to 35°, compute the precise degree measure of its complement.", "answer": 55, "options": [45, 55, 65, 145]},
            {"question": "RS Aggarwal Ch 13: Find the value of a supplementary angle matching structural component element if the primary baseline angular orientation is measured at 110° on a grid.", "answer": 70, "options": [70, 80, 90, 180]}
        ],
        "Ch 9: Rational Numbers Calculus": [
            {"question": "NCERT Ex 9.1: Reduce the raw system fractional format token -36/54 into its standard minimal irreducible mathematical rational number format. Find the denominator component.", "answer": 3, "options": [2, 3, 4, 6]},
            {"question": "RS Aggarwal Ch 2: Sum the following multi-base fractional metrics across matching layouts cleanly: (5/4) + (-11/4). Find the net unified evaluation value string.", "answer": -1.5, "options": [-1.5, -2.0, 1.5, -0.75]}
        ]
    },
    "Class 8": {
        "Ch 5: Data Handling & Probabilities": [
            {"question": "NCERT Ex 5.3: A fair 6-sided playing die is rolled once on an open arena board canvas. Calculate the exact mathematical percentage probability of rolling a perfect prime number.", "answer": 50, "options": [16, 33, 50, 66]},
            {"question": "RS Aggarwal Ch 23: A group pie chart distribution indicates that a 90° sector block slice corresponds to the 'Engineering' student allocation bracket. What percentage of the overall student population does this represent?", "answer": 25, "options": [20, 25, 30, 33]}
        ],
        "Ch 7: Cubes and Cube Roots": [
            {"question": "NCERT Ex 7.2: Find the core base value integer code whose cubic geometric volumetric exponential expansion directly yields the total structural calculation product value 512.", "answer": 8, "options": [6, 8, 12, 16]},
            {"question": "RS Aggarwal Ch 4: Determine the smallest uniform whole number factor by which the integer 256 must be multiplied so that the final matching evaluation product transforms into a perfect cube.", "answer": 2, "options": [2, 3, 4, 6]}
        ]
    }
}

# ============================================================
# 📚 PHASE 5: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_5_QUESTIONS = {
    "Class 1": {
        "Ch 9: Data Handling Basics": [
            {"question": "NCERT Ex 9.1: Look at the word 'ELEMENT'. Count exactly how many times the letter 'E' appears in this string.", "answer": 3, "options": [2, 3, 4, 5]},
            {"question": "RS Aggarwal Ch 9: Count the total count of individual letters making up the system name 'AMIT'.", "answer": 4, "options": [3, 4, 5, 6]},
            {"question": "NCERT Ex 9.2: There are 3 triangles, 5 circles, and 2 squares drawn on a slate. Which geometric shape is present in the greatest quantity? Triangles (1), Circles (2), Squares (3)?", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 10: Pattern Strings": [
            {"question": "NCERT Ex 10.1: Analyze the repeating loop blueprint: 1, 2, 1, 2, 1, __. Identify the next coordinate value.", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 10: Decode this tracking sequence string: A, B, A, B, A, __. Select the correct letter code index: A (1) or B (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 2": {
        "Ch 13: Longest Step Units": [
            {"question": "NCERT Ex 13.2: Nitin measures a long wooden table with his handspans and counts exactly 8 spans. If his younger sister measures the same table, will her handspan count be more (1) or less (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 15: A teacher uses her foot steps to measure the classroom floor width and counts 15 steps. Express this baseline standard approach identifier type: Standard Unit (1) or Non-Standard Unit (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 14: Birds Come, Birds Go": [
            {"question": "NCERT Ex 14.1: There were 28 white swans swimming peacefully inside a lake. A group of 14 migration birds fly in to join them. Compute the final swan total count.", "answer": 42, "options": [32, 40, 42, 44]},
            {"question": "RS Aggarwal Ch 14: A massive flock of 53 crows settles down on an old oak tree. If 19 crows get startled and fly away, calculate the remaining bird count left on the branches.", "answer": 34, "options": [34, 36, 44, 46]}
        ]
    },
    "Class 3": {
        "Ch 10: Play with Patterns": [
            {"question": "NCERT Ex 10.3: Look closely at the changing alphabetical sequence layout: AA, BB, CC, DD, __. Identify the correct item pair index: EE (1), EF (2), FE (3).", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 18: Analyze the growing number pattern logic structure: 5, 10, 15, 20, 25, __. Find the next sequential integer token.", "answer": 30, "options": [26, 30, 35, 40]}
        ],
        "Ch 12: Can We Share?": [
            {"question": "NCERT Ex 12.2: A grandmother buys 24 delicious lollipops to distribute. She shares them completely evenly among her 4 grandchildren. How many items does each child get?", "answer": 6, "options": [4, 6, 8, 12]},
            {"question": "RS Aggarwal Ch 6: Divide a complete bundle set of 45 colorful stickers equally among 5 school classmates. Calculate the single share count allocated per head.", "answer": 9, "options": [7, 8, 9, 15]}
        ]
    },
    "Class 4": {
        "Ch 6: The Junk Seller Matrix": [
            {"question": "NCERT Ex 6.1: Kiran buys 1 kg of old plastic waste from collectors for Rs. 12 and sells it later to a big dealer for Rs. 15. Calculate her total net profit margin if she trades exactly 10 kg of plastic.", "answer": 30, "options": [20, 30, 40, 150]},
            {"question": "RS Aggarwal Ch 7: A retail shopkeeper purchases a bulk set of notebook bundles for Rs. 180 and marks them up to sell the bundle for Rs. 220. Compute his absolute financial gain amount.", "answer": 40, "options": [20, 30, 40, 50]}
        ],
        "Ch 7: Jugs and Mugs Math": [
            {"question": "NCERT Ex 7.3: A roadside tea vendor uses exactly 250 ml of pure fresh milk to prepare a single large pot of spiced tea. How many millilitres of milk will he consume to brew 4 identical pots?", "answer": 1000, "options": [500, 750, 1000, 1250]},
            {"question": "RS Aggarwal Ch 12: A water tank setup currently holds 12 litres and 500 ml of fluid. If a household usage drains away exactly 3 litres and 200 ml, compute the remaining water volume left inside.", "answer": 9300, "options": [9000, 9300, 9500, 15700]}
        ]
    },
    "Class 5": {
        "Ch 5: Does it Look Same?": [
            {"question": "NCERT Ex 5.1: If you rotate a perfectly symmetric capital letter 'H' block by a precise half-turn (180 degrees) around its center, does its final orientation look exactly the same? Yes (1) or No (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 14: Consider a standard regular geometric square tile structure template. How many unique axes of line symmetry can you cleanly drop across its footprint?", "answer": 4, "options": [2, 3, 4, 6]}
        ],
        "Ch 6: Multiples & Factors Grid": [
            {"question": "NCERT Ex 6.3: Find the absolute smallest common multiple (LCM) shared between the basic starting structural numbers 4 and 6.", "answer": 12, "options": [4, 6, 12, 24]},
            {"question": "RS Aggarwal Ch 3: Examine the total factoring array of the integer value 15. How many distinct whole number factors does the number 15 possess in total?", "answer": 4, "options": [2, 3, 4, 5]}
        ]
    },
    "Class 6": {
        "Ch 9: Data Handling Records": [
            {"question": "NCERT Ex 9.2: A school library tracker map shows a pictograph where one star symbol represents 10 books. If the science shelf row displays 5 complete star symbols, find the total book inventory.", "answer": 50, "options": [15, 45, 50, 55]},
            {"question": "RS Aggarwal Ch 23: A raw list of test grades reads: 7, 8, 5, 7, 6, 7, 9, 7, 8. Determine the absolute frequency count for the specific student score coordinate 7.", "answer": 4, "options": [2, 3, 4, 5]}
        ],
        "Ch 10: Mensuration Layouts": [
            {"question": "NCERT Ex 10.1: An equilateral triangle signpost layout has a total perimeter boundary measurement of 45 cm. Determine the physical length of any one of its single uniform edges.", "answer": 15, "options": [10, 15, 20, 135]},
            {"question": "RS Aggarwal Ch 16: A clean rectangular plot path configuration measures 20 meters in length and has a total area value of 240 square meters. Find the width dimension of this plot.", "answer": 12, "options": [10, 12, 14, 24]}
        ]
    },
    "Class 7": {
        "Ch 6: Triangles Properties": [
            {"question": "NCERT Ex 6.5: In a right-angled construction triangle matrix, the base floor measures 3 cm and the vertical side height measures 4 cm. Use the Pythagorean theorem to compute the hypotenuse.", "answer": 5, "options": [5, 6, 7, 25]},
            {"question": "RS Aggarwal Ch 15: In a geometric triangle layout framework, two internal angles are measured at 50 degrees and 60 degrees. Compute the precise degree measure of the third missing angle.", "answer": 70, "options": [60, 70, 80, 90]}
        ],
        "Ch 11: Perimeter & Area Calculus": [
            {"question": "NCERT Ex 11.2: Find the absolute area blueprint value of a parallelogram template system whose baseline measure equals 12 cm and corresponding height equals 8 cm.", "answer": 96, "options": [40, 48, 96, 100]},
            {"question": "RS Aggarwal Ch 16: A circular metal wheel disk has a radius measurement tracking line of 7 cm. Compute its total boundary circumference length using 22/7 for pi.", "answer": 44, "options": [22, 44, 154, 88]}
        ]
    },
    "Class 8": {
        "Ch 8: Comparing Quantities Complex": [
            {"question": "NCERT Ex 8.2: A fashionable winter jacket listing shows a baseline retail price tag of Rs. 2,000. It is sold at a special holiday discount markdown of 15 percent. Calculate the final net sale price.", "answer": 1700, "options": [1500, 1700, 1850, 1985]},
            {"question": "RS Aggarwal Ch 10: An item bought for Rs. 800 is resold on an auction forum platform for Rs. 1,000. Calculate the exact net profit percentage realized on this asset transaction.", "answer": 25, "options": [20, 25, 30, 200]}
        ],
        "Ch 11: Direct & Inverse Proportions": [
            {"question": "NCERT Ex 11.1: A modern industrial machine layout fills exactly 840 glass bottles across a clean runtime shift of 6 hours. How many bottles will it fill if left running for 5 hours straight?", "answer": 700, "options": [650, 700, 720, 800]},
            {"question": "RS Aggarwal Ch 13: If 15 workers can build a specific brick wall system layout in 48 hours, how many hours will it take 30 workers to complete the identical operational task at the same uniform rate?", "answer": 24, "options": [24, 36, 48, 96]}
        ]
    }
}

# ============================================================
# 📚 PHASE 6: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_6_QUESTIONS = {
    "Class 1": {
        "Ch 11: Numbers 51 to 100": [
            {"question": "NCERT Ex 11.1: If you assemble a grid containing 6 bundles of tens and 5 single loose sticks, what is the net sequence number?", "answer": 65, "options": [56, 60, 65, 75]},
            {"question": "RS Aggarwal Ch 11: Complete the counting sequence tracking line carefully: 87, 88, 89, __, 91.", "answer": 90, "options": [80, 90, 91, 92]},
            {"question": "NCERT Ex 11.4: What is the grand total count if you add 1 single unit to the greatest 2-digit baseline counting number 99?", "answer": 100, "options": [90, 99, 100, 101]}
        ],
        "Ch 12: Money Basics": [
            {"question": "NCERT Ex 12.1: Rehana wants to build a currency match. Which two coins can she combine together to make exactly a Rs. 5 value? Rs. 2 + Rs. 3 (1) or Rs. 2 + Rs. 2 + Rs. 1 (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 12: Look at a shiny Indian currency coin. If one face shows the Lion Capital emblem, what do we call that specific side? Heads (1) or Tails (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 2": {
        "Ch 9: My Funday Calendar": [
            {"question": "NCERT Ex 9.1: If school classes are held sequentially throughout the week, what specific calendar day falls directly after Friday?", "answer": 1, "options": [1, 2, 3, 4]},  # Let Saturday = 1, Sunday = 2, Monday = 3
            {"question": "RS Aggarwal Ch 11: Think about the calendar months layout. Which month follows immediately after the ending of July?", "answer": 2, "options": [1, 2, 3, 4]}  # Let June = 1, August = 2, September = 3
        ],
        "Ch 15: How Many Pigtails?": [
            {"question": "NCERT Ex 15.1: A teacher records names on a board: 'ANNA', 'BOB', 'CHRIS'. Count how many names in this specific array have exactly 4 letters.", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 24: In a small toy box, there are 4 blue cars, 3 red cars, and 5 green trucks. Calculate the total vehicular toy count.", "answer": 12, "options": [7, 9, 12, 15]}
        ]
    },
    "Class 3": {
        "Ch 13: Smart Charts Data": [
            {"question": "NCERT Ex 13.2: A tracking table logs favorite colors of students. If 8 kids choose Red, 12 choose Blue, and 5 choose Yellow, which color tracking node represents the absolute mode?", "answer": 2, "options": [1, 2, 3, 4]},  # Let Red=1, Blue=2, Yellow=3
            {"question": "RS Aggarwal Ch 22: In a clean playground tally chart, each slash marks 1 point. If a student marks two groups of 5 cross-slashes, what total number is logged?", "answer": 10, "options": [5, 8, 10, 12]}
        ],
        "Ch 14: Rupees and Paise Arithmetic": [
            {"question": "NCERT Ex 14.3: Ram buys a colorful kite for Rs. 5.50 and a sweet candy bar for Rs. 2.00. Calculate the total currency change handed over to the shopkeeper.", "answer": 7.50, "options": [7.00, 7.50, 8.00, 9.50]},
            {"question": "RS Aggarwal Ch 13: Convert an isolated currency value token of exactly 4 rupees completely into raw individual paise units.", "answer": 400, "options": [40, 400, 4000, 440]}
        ]
    },
    "Class 4": {
        "Ch 8: Carts and Wheels Geometry": [
            {"question": "NCERT Ex 8.1: A student uses a mechanical compass device to trace a perfect geometric circle on grid paper. What do we call the fixed center point tracking line to the outer rim? Radius (1) or Diameter (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 16: If a circular playground wheel configuration registers a total measured diameter line of 20 meters, find its true operational radius metric.", "answer": 10, "options": [5, 10, 15, 40]}
        ],
        "Ch 9: Halves and Quarters Fractions": [
            {"question": "NCERT Ex 9.2: A massive birthday cake is cut evenly into 4 matching slices. If Amit eats exactly 1 slice, express the remaining cake volume as a decimal metric fraction.", "answer": 0.75, "options": [0.25, 0.50, 0.75, 1.00]},
            {"question": "RS Aggarwal Ch 5: If you evaluate the simple fraction addition string payload cleanly, what value resolves out: (1/4) + (2/4) = ?", "answer": 0.75, "options": [0.25, 0.50, 0.75, 3.00]}
        ]
    },
    "Class 5": {
        "Ch 8: Mapping Your Way": [
            {"question": "NCERT Ex 8.1: On a tourist map route layout, a scale parameter dictates that 1 cm on paper equals 2 km on real ground. If the map track scales to 5 cm, compute the real distance.", "answer": 10, "options": [5, 7, 10, 20]},
            {"question": "RS Aggarwal Ch 14: If an architectural layout blue map indicates an absolute straight scale where 2 cm shifts match 100 meters, find the distance value for an 8 cm blueprint linespan.", "answer": 400, "options": [200, 300, 400, 800]}
        ],
        "Ch 9: Boxes and Sketches 3D": [
            {"question": "NCERT Ex 9.2: Think about the 3D spatial properties of a regular solid dice block cube container. How many flat outer faces can you count across its structure?", "answer": 6, "options": [4, 6, 8, 12]},
            {"question": "RS Aggarwal Ch 18: A classic solid brick module is structurally categorized as a cuboid layout matrix. How many sharp corner vertices does it possess?", "answer": 8, "options": [6, 8, 12, 16]}
        ]
    },
    "Class 6": {
        "Ch 11: Introduction to Algebra": [
            {"question": "NCERT Ex 11.1: A matchstick pattern builds separate houses in a row. If 1 house requires 6 sticks, write the variable rule to compute the total sticks for 'n' houses.", "answer": 6, "options": [1, 4, 6, 12]},  # checking coefficient factor
            {"question": "RS Aggarwal Ch 8: Translate the following English statement cleanly into a functional algebraic variable string: '15 subtracted from twice of variable x'. Find the constant numeric parameter.", "answer": -15, "options": [15, -15, 2, -2]}
        ],
        "Ch 13: Symmetry Dimensions": [
            {"question": "NCERT Ex 13.1: Look at the geometric construction architecture of a standard Equilateral Triangle tile. How many clean lines of reflective axis symmetry exist?", "answer": 3, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 17: Consider a perfectly balanced isosceles triangle blueprint. How many unique paths of structural balance folding symmetry lines can be mapped?", "answer": 1, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 7": {
        "Ch 7: Congruence of Triangles": [
            {"question": "NCERT Ex 7.1: Two geometric line segments are mathematically declared to be perfectly congruent systems. If line A measures 7.5 cm, what is the length of line B?", "answer": 7.5, "options": [5.0, 7.5, 15.0, 0.0]},
            {"question": "RS Aggarwal Ch 16: Identify the baseline congruence criteria symbol notation where matching parameters specify two sides and the completely enclosed interior angle layout: ASA (1), SAS (2), SSS (3)?", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 13: Exponents and Powers Calculus": [
            {"question": "NCERT Ex 13.2: Simplify the laws of exponents base operation to resolve the product token calculation value: (2^3) multiplied by (5^0). What integer drops out?", "answer": 8, "options": [0, 2, 8, 40]},
            {"question": "RS Aggarwal Ch 2: Evaluate the base-power evaluation string safely to discover the final configuration array numerical output: (-1)^1000 + (-1)^1001 = ?", "answer": 0, "options": [-2, -1, 0, 1]}
        ]
    },
    "Class 8": {
        "Ch 14: Factorisation Polynomials": [
            {"question": "NCERT Ex 14.1: Find the absolute Highest Common Factor (HCF) term value for the variable polynomial block array nodes: 12x^2y and 18xy^2. Identify the leading integer coefficient.", "answer": 6, "options": [2, 3, 6, 12]},
            {"question": "RS Aggarwal Ch 7: Factor the quadratic structural mathematical expression system completely: x^2 + 5x + 6. What is the value of the larger constant integer root factor?", "answer": 3, "options": [1, 2, 3, 6]}
        ],
        "Ch 15: Introduction to Graphs Grid": [
            {"question": "NCERT Ex 15.1: On a standardized Cartesian coordinate map layout plane, a target data coordinate point is locked at (4, 0). On which axis boundary line does this point sit? X-Axis (1) or Y-Axis (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 23: Find the distance metric from the geometric central absolute reference node origin (0,0) straight out to the tracking target grid coordinate point (0, 15).", "answer": 15, "options": [0, 5, 10, 15]}
        ]
    }
}

# ============================================================
# 📚 PHASE 7: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_7_QUESTIONS = {
    "Class 1": {
        "Ch 13: How Many Objects": [
            {"question": "NCERT Ex 13.1: A farmer ties sugarcanes into bundles of 10. If he has 3 complete bundles and 7 loose sugarcanes, what is his total stock count?", "answer": 37, "options": [30, 37, 43, 73]},
            {"question": "RS Aggarwal Ch 13: Look at a sketch of a standard house. If there are 4 windows on the front wall and 2 windows on the side wall, calculate the total window count.", "answer": 6, "options": [4, 5, 6, 8]},
            {"question": "NCERT Ex 13.3: In a village market, a banana seller has 10 single bananas left. How many full groups of tens can he make out of them?", "answer": 1, "options": [1, 2, 5, 10]}
        ],
        "Ch 14: Simple Math Review": [
            {"question": "NCERT Ex 14.1: If you have 5 clean sketch pens and your friend gifts you 5 more matching pens, what is the net sum of your collection?", "answer": 10, "options": [0, 5, 10, 15]},
            {"question": "RS Aggarwal Ch 15: A birdfeeder has 7 sparrows feeding on seeds. If all 7 sparrows get startled and fly away together, how many sparrows remain?", "answer": 0, "options": [0, 1, 7, 14]}
        ]
    },
    "Class 2": {
        "Ch 6: Footprints & Tracing": [
            {"question": "NCERT Ex 6.2: If you place a standard cylinder glass tumbler flat on a piece of paper and trace along its base, what clean geometric shape blueprint do you get? Circle (1), Square (2), Rectangle (3)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 7: An elephant walks across wet mud leaving deep footprints. Compare its footprint scale to a small forest rabbit. Which track layout footprint is strictly LARGER? Elephant (1) or Rabbit (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ],
        "Ch 7: Measuring Capacities": [
            {"question": "NCERT Ex 7.4: A kitchen jug can hold exactly 5 full glass cups of milk. If you want to fill 3 identical jugs completely for a recipe, how many glass cups do you need to pour?", "answer": 15, "options": [8, 12, 15, 18]},
            {"question": "RS Aggarwal Ch 16: A large cleaning bucket can be filled up completely by pouring 10 full mugs of water. If the bucket currently has 4 mugs inside, how many more mugs are needed to fill it to the brim?", "answer": 6, "options": [4, 6, 10, 14]}
        ]
    },
    "Class 3": {
        "Ch 8: Who is Heavier?": [
            {"question": "NCERT Ex 8.1: A merchant balances a scale. On one side sits a 1 kg block of iron weight, and on the other sits a large sack containing 1 kg of popcorn. Which side weighs MORE? Iron (1), Popcorn (2), Both are Equal (3)?", "answer": 3, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 11: A gas cylinder delivery truck brings a payload item weighing 14 kilograms. Express this identical physical weight value cleanly in standard grams.", "answer": 14000, "options": [140, 1400, 14000, 140000]}
        ],
        "Ch 15: How Many Ponytails Data": [
            {"question": "NCERT Ex 15.2: A classroom roster tracks hair styles. There are 12 girls with single ponytails, 8 girls with two ponytails, and 10 boys with short hair. Calculate the total student count logged in this dataset.", "answer": 30, "options": [20, 28, 30, 32]},
            {"question": "RS Aggarwal Ch 24: In a fruits catalog list, there are 5 apples, 9 mangoes, and 4 oranges. Which fruit item name represents the absolute mode value of this collection? Apples (1), Mangoes (2), Oranges (3)?", "answer": 2, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 4": {
        "Ch 10: Play with Patterns": [
            {"question": "NCERT Ex 10.2: A secret agent encryption rule maps letters directly to numbers where A=1, B=2, C=3, and so on. Decode the encrypted secret message word token '13-1-20-8-19'. What is the sum of these integers?", "answer": 51, "options": [41, 45, 51, 60]},
            {"question": "RS Aggarwal Ch 18: Analyze the growing numerical pattern tower layout: 1, 3, 6, 10, 15, __. Discover the next configuration node sequence integer.", "answer": 21, "options": [18, 20, 21, 25]}
        ],
        "Ch 14: Smart Charts Analytics": [
            {"question": "NCERT Ex 14.1: A school survey asks 40 kids about their favorite hobbies. A clean circular pie chart shows exactly half of the circle slice belongs to 'Playing Games'. How many kids chose games?", "answer": 20, "options": [10, 15, 20, 30]},
            {"question": "RS Aggarwal Ch 22: On a bar chart tracking rainwater levels, each 1 cm step on the grid represents 5 mm of rainfall. If the rainy Monday bar reaches a height of 7 cm, calculate the net rainfall in mm.", "answer": 35, "options": [25, 30, 35, 40]}
        ]
    },
    "Class 5": {
        "Ch 10: Tenths and Hundredths": [
            {"question": "NCERT Ex 10.1: A tiny garden frog measures exactly 2 cm and 4 mm in physical length. Express this biological layout metric cleanly as a unified decimal centimeter string.", "answer": 2.4, "options": [0.24, 2.04, 2.4, 24.0]},
            {"question": "RS Aggarwal Ch 6: A matchbox item costs exactly 75 paise at a wholesale store. Express this asset transaction price value using standard decimal rupee notation tokens.", "answer": 0.75, "options": [0.07, 0.75, 7.5, 75.0]}
        ],
        "Ch 14: How Big? How Heavy Volume": [
            {"question": "NCERT Ex 14.2: A solid mathematical cube toy has edge dimensions measuring exactly 5 cm along its sides. Compute its net 3D volumetric space capacity in cubic centimeters.", "answer": 125, "options": [25, 75, 125, 150]},
            {"question": "RS Aggarwal Ch 19: A rectangular shipping carton container measures 10 cm long, 6 cm wide, and 4 cm high. Compute the absolute cubic volume payload calculation for this box.", "answer": 240, "options": [100, 200, 240, 480]}
        ]
    },
    "Class 6": {
        "Ch 5: Understanding Shapes": [
            {"question": "NCERT Ex 5.4: An engineer uses a compass tool to inspect an structural angle that measures exactly 135 degrees on a protractor layout. Classify this angle category: Acute (1), Right (2), Obtuse (3), Reflex (4)?", "answer": 3, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 13: A clock setup shows exactly 6:00 PM on its display. What is the precise degree measurement of the angle formed directly between the hour hand and minute hand?", "answer": 180, "options": [45, 90, 180, 360]}
        ],
        "Ch 14: Practical Geometry Tools": [
            {"question": "NCERT Ex 14.2: A draftsman constructs a perfect circle matching layout using a standard ruler and a steel tip compass setup opened to a width of 4.5 cm. What is the total length of its diameter line?", "answer": 9.0, "options": [4.5, 9.0, 13.5, 18.0]},
            {"question": "RS Aggarwal Ch 19: If you construct a perpendicular bisector line across a baseline segment measuring exactly 12 cm, what is the length of each newly formed halved segment?", "answer": 6, "options": [3, 4, 6, 8]}
        ]
    },
    "Class 7": {
        "Ch 14: Rotational Symmetry Matrix": [
            {"question": "NCERT Ex 14.1: Consider the structural geometric symmetry mapping of a perfect square tile. What is the total order of rotational symmetry it possesses when spun around its center point?", "answer": 4, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 18: A standard capital alphabet letter block 'Z' is rotated complete turns on a flat table. Find the order of its rotational symmetry layout configuration.", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 15: Visualising Solid Shapes": [
            {"question": "NCERT Ex 15.2: If you cut a standard cylindrical wooden pipe with a straight horizontal cross-section slice, what 2D geometric shape face is exposed? Square (1), Circle (2), Triangle (3)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 19: A solid triangular pyramid structure template is checked for parameters. Count the total number of triangular faces making up this polyhedron system.", "answer": 4, "options": [3, 4, 5, 6]}
        ]
    },
    "Class 8": {
        "Ch 10: Visualising Solid Polyhedrons": [
            {"question": "NCERT Ex 10.3: Use Euler's Polyhedron Formula (Faces + Vertices - Edges = 2) to solve a puzzle. If a solid 3D shape has 6 faces and 8 vertices, compute its total count of straight edges.", "answer": 12, "options": [6, 10, 12, 14]},
            {"question": "RS Aggarwal Ch 19: A solid polyhedron structure possesses exactly 20 faces and 30 edges. Run Euler's computational formula calculation block to determine its total count of corner vertices.", "answer": 12, "options": [10, 12, 20, 50]}
        ],
        "Ch 16: Playing with Numbers Logic": [
            {"question": "NCERT Ex 16.1: In a crypto-arithmetic puzzle addition sum block, '31A' plus '1A3' equals '501'. Work out the single missing digit value that maps cleanly to variable A.", "answer": 8, "options": [5, 6, 7, 8]},
            {"question": "RS Aggarwal Ch 5: A three-digit generic number string is written as '4X2'. If this complete integer token is perfectly and evenly divisible by 9, find the missing single-digit value for variable X.", "answer": 3, "options": [2, 3, 4, 6]}
        ]
    }
}

# ============================================================
# 📚 PHASE 8: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_8_QUESTIONS = {
    "Class 1": {
        "Ch 15: Spatial Awareness Review": [
            {"question": "NCERT Ex 15.1: A small playful kitten is sitting safely under a sturdy wooden table. Where is the kitten located? Above the table (1) or Under the table (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 1: A big bright red balloon escapes and flies high up into the sky while a heavy toy truck sits flat on the grass. Which object is TOP? Balloon (1) or Truck (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "NCERT Ex 15.3: Look at a picture of a tree. A small bird is sitting inside a nest on a branch, and a dog is standing on the ground near the trunk. Which animal is at the BOTTOM? Bird (1) or Dog (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 16: Basic Sorting Data": [
            {"question": "NCERT Ex 16.2: You collect 4 red plastic buttons, 2 shiny blue buttons, and 4 round green buttons. Calculate the total button count inside your collection bag.", "answer": 10, "options": [6, 8, 10, 12]}
        ]
    },
    "Class 2": {
        "Ch 10: Weights and Balances": [
            {"question": "NCERT Ex 10.4: A heavy pumpkin and a light lemon are placed on a balancing seesaw scale. Which vegetable node drops down lower because it is HEAVIER? Pumpkin (1) or Lemon (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 18: A grocery store keeper sells a bag of loose sugar. Which standard tool metric does he use to measure the sugar mass load properly? Metre Scale (1) or Weighing Balance (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 11: Simple Adding Mechanics": [
            {"question": "NCERT Ex 11.5: In a small neighborhood garden patch, 37 red roses and 22 yellow marigolds bloom together. Compute the total flower count blooming in the patch.", "answer": 59, "options": [50, 55, 59, 61]}
        ]
    },
    "Class 3": {
        "Ch 6: Basic Array Multiplication": [
            {"question": "NCERT Ex 6.4: A smart farmer plants small apple saplings in neat arrays. If he creates 4 parallel rows and drops exactly 8 trees inside each row, what is his total sapling count?", "answer": 32, "options": [24, 28, 32, 36]},
            {"question": "RS Aggarwal Ch 8: A box has 3 compartments, and each compartment safely holds 12 farm-fresh eggs. Find the net egg capacity of the container setup.", "answer": 36, "options": [30, 32, 36, 48]}
        ],
        "Ch 7: Fluid Capacities Metric": [
            {"question": "NCERT Ex 7.5: A tea kettle contains 800 ml of herbal tea. If a host pours out 200 ml into a cup for a guest, how many millilitres of tea remain inside the kettle body?", "answer": 600, "options": [400, 500, 600, 700]}
        ]
    },
    "Class 4": {
        "Ch 4: Tick-Tick-Tick Time": [
            {"question": "NCERT Ex 4.2: A school sports assembly begins precisely at 08:15 AM and wraps up its routine at 09:00 AM on the dot. Calculate the absolute duration of the assembly in minutes.", "answer": 45, "options": [30, 40, 45, 60]},
            {"question": "RS Aggarwal Ch 15: An express train leaves a city station platform at 14:00 hours and reaches its final destination stop at 18:30 hours. Calculate the total travel time elapsed.", "answer": 4.5, "options": [3.5, 4.0, 4.5, 5.0]}
        ],
        "Ch 10: Building Smart Tables": [
            {"question": "NCERT Ex 10.4: If a local shopkeeper packs sets of handmade candles into boxes of 9, how many total boxes can he fill completely if he manufactures 72 candles?", "answer": 8, "options": [6, 7, 8, 9]}
        ]
    },
    "Class 5": {
        "Ch 6: Be My Multiple Geometry": [
            {"question": "NCERT Ex 6.2: List out the sequence factors for the integer value 12. Which number is a common factor shared cleanly between both 12 and 18? 5 (1), 6 (2), 7 (3), 8 (4)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 4: Find the absolute Lowest Common Multiple (LCM) tracking value for the baseline parameter pair 8 and 12.", "answer": 24, "options": [12, 16, 24, 48]}
        ],
        "Ch 11: Area Configurations": [
            {"question": "NCERT Ex 11.4: A classic rectangular hallway floor setup measures 8 meters in length and 5 meters in total width. Calculate the net flat surface floor area in square meters.", "answer": 40, "options": [26, 35, 40, 80]}
        ]
    },
    "Class 6": {
        "Ch 3: Playing with Numbers Core": [
            {"question": "NCERT Ex 3.3: Apply the standard divisibility test rules safely. Which single digit completes the empty space to make the number string '45_2' perfectly divisible by 3? 1 (1), 2 (2), 4 (3), 5 (4)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 2: Find the absolute Highest Common Factor (HCF) configuration value matching the integer dataset nodes 24 and 36.", "answer": 12, "options": [4, 6, 8, 12]}
        ],
        "Ch 7: Decimals and Money": [
            {"question": "NCERT Ex 7.5: Reena buys a geometry book asset for Rs. 45.50 and a drawing pen bundle for Rs. 15.25. Compute the total cash amount she spends at the store counter.", "answer": 60.75, "options": [55.50, 60.25, 60.75, 65.00]}
        ]
    },
    "Class 7": {
        "Ch 4: Simple Variable Equations": [
            {"question": "NCERT Ex 4.1: Solve the basic structural linear equation system cleanly to extract the true target variable value: 3x + 7 = 22. Find x.", "answer": 5, "options": [3, 4, 5, 6]},
            {"question": "RS Aggarwal Ch 7: Translate and compute the expression: If you add 10 to 4 times a secret integer variable y, the balance product yields 50. Discover y.", "answer": 10, "options": [8, 10, 12, 15]}
        ],
        "Ch 10: Percentage Conversion Calculus": [
            {"question": "NCERT Ex 10.3: Convert the standard fractional system tracking metric 3/4 cleanly into its corresponding unified percentage value layout token.", "answer": 75, "options": [25, 50, 75, 80]}
        ]
    },
    "Class 8": {
        "Ch 2: Linear Equations One Variable": [
            {"question": "NCERT Ex 2.2: Two whole numbers are locked in a structural ratio of 5:3. If their absolute mathematical difference equals 18, find the value of the larger number node.", "answer": 45, "options": [27, 36, 45, 54]},
            {"question": "RS Aggarwal Ch 8: Solve the single variable structural rational equation model securely for variable z: (z - 5) / 3 = (z - 3) / 5. Find the value of z.", "answer": 8, "options": [4, 6, 8, 12]}
        ],
        "Ch 12: Solid Mensuration Architecture": [
            {"question": "NCERT Ex 12.1: A cylindrical storage tank layout has a base floor radius of 7 meters and a total vertical chamber height of 10 meters. Compute its Total Surface Area in square meters using 22/7 for pi.", "answer": 748, "options": [154, 440, 548, 748]}
        ]
    }
}

# ============================================================
# 📚 PHASE 9: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_9_QUESTIONS = {
    "Class 1": {
        "Ch 17: Sizes and Shapes Review": [
            {"question": "NCERT Ex 17.1: Look at a massive basketball and a tiny table tennis ball side by side. Which object is strictly SMALLER? Basketball (1) or Table Tennis Ball (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 1: A playful puppy is sitting on top of a slide while a small kitten sits below on the grass. Which animal is at the bottom node? Puppy (1) or Kitten (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "NCERT Ex 17.4: Imagine a long train and a short bicycle parked at a station track. Which vehicle profile spans a LONGER length? Train (1) or Bicycle (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ],
        "Ch 18: Basic Sequence Logic": [
            {"question": "NCERT Ex 18.2: Trace the repeating color pattern chain code safely: Red, Blue, Red, Blue, __. What color token completes this cycle? Red (1) or Blue (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 2": {
        "Ch 16: Lines Types and Shapes": [
            {"question": "NCERT Ex 16.1: If you drop a heavy stone completely straight down using a tight string, what specific type of line axis does the string form? Standing Line (1) or Sleeping Line (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 14: Look at the roof line profile of a classic hut sketch. What type of lines form the slanted pitch design? Slanting Lines (1) or Straight Horizontal Lines (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ],
        "Ch 17: Multi-Digit Subtraction": [
            {"question": "NCERT Ex 17.3: An old tree trunk has 54 birds resting on its branches. A sudden loud noise scares away 25 birds. Calculate the remaining bird count on the tree.", "answer": 29, "options": [24, 29, 31, 39]}
        ]
    },
    "Class 3": {
        "Ch 16: Basic Fraction Shading": [
            {"question": "NCERT Ex 16.2: A round circular pizza chart is divided into 2 perfectly equal halves. If you eat 1 complete half, write the fraction value left over.", "answer": 0.5, "options": [0.25, 0.5, 0.75, 1.0]},
            {"question": "RS Aggarwal Ch 5: A long ribbon strip is cut cleanly into 3 equal pieces. If a tailor uses 1 piece for a dress, what fraction of the ribbon remains untouched?", "answer": 0.67, "options": [0.33, 0.5, 0.67, 0.75]}
        ],
        "Ch 17: Length Conversions Metric": [
            {"question": "NCERT Ex 17.5: An athlete completes a running drill over a track measuring exactly 3 meters in total length. Convert this metric length coordinate directly into centimeters.", "answer": 300, "options": [30, 300, 3000, 350]}
        ]
    },
    "Class 4": {
        "Ch 15: Perimeter Rules and Borders": [
            {"question": "NCERT Ex 15.1: A farmer maps out a regular triangular garden layout where each uniform side measures exactly 12 meters. Calculate the net perimeter boundary fence length.", "answer": 36, "options": [24, 36, 48, 144]},
            {"question": "RS Aggarwal Ch 17: A rectangular canvas frame footprint tracks at 15 cm long and 10 cm wide. Compute the total length of wooden borders required to frame the canvas.", "answer": 50, "options": [25, 40, 50, 150]}
        ],
        "Ch 16: Division Group Blocks": [
            {"question": "NCERT Ex 16.4: A warehouse clerk receives a bundle of 96 brand new books. If he stacks them evenly into piles of 8, calculate the total count of piles compiled.", "answer": 12, "options": [10, 11, 12, 14]}
        ]
    },
    "Class 5": {
        "Ch 15: Decimal Place Tracking": [
            {"question": "NCERT Ex 15.2: Look closely at the decimal numeral code coordinate 4.56. Identify the precise place value structural location of the digit 6. Tenths (1) or Hundredths (2)?", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 6: Evaluate the decimal math summary equation string cleanly to extract the final system tracking result: 1.25 + 2.50 = ?", "answer": 3.75, "options": [3.5, 3.75, 4.0, 4.25]}
        ],
        "Ch 16: Volume Tracking Math": [
            {"question": "NCERT Ex 16.5: A solid rectangular water container measures 4 cm in length, 3 cm in width, and 2 cm in total height. Calculate the cubic space volume inside.", "answer": 24, "options": [9, 12, 18, 24]}
        ]
    },
    "Class 6": {
        "Ch 15: Negative Integers Scale": [
            {"question": "NCERT Ex 15.1: A deep sea research submarine logs its navigation depth level at 450 meters below sea level. Represent this depth scale position using standard signed integer token layout.", "answer": -450, "options": [450, -450, 0, -45]},
            {"question": "RS Aggarwal Ch 4: Compare these two integer nodes on a baseline number line graph: -15 and -5. Which integer holds a strictly GREATER mathematical value? -15 (1) or -5 (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 16: Simplified Ratios Math": [
            {"question": "NCERT Ex 16.3: A computer classroom contains 20 desktop terminals and 10 printers. Find the simplified baseline ratio tracking parameter of computers to printers.", "answer": 2, "options": [1, 2, 3, 5]}  # Represented as 2:1 mapping evaluation
        ]
    },
    "Class 7": {
        "Ch 16: Exponent Laws Multiplication": [
            {"question": "NCERT Ex 16.2: Simplify the exponential mathematical expression system string logic to discover the output factor value: (3^2) * (3^1). What value drops out?", "answer": 27, "options": [9, 18, 27, 81]},
            {"question": "RS Aggarwal Ch 2: Evaluate the base exponential power configuration block securely for system tracking output: (2^4) / (2^2) = ?", "answer": 4, "options": [2, 4, 8, 16]}
        ],
        "Ch 17: Simple Equation Balance": [
            {"question": "NCERT Ex 17.4: Extract the true matching variable root calculation sequence coordinate for the equation layout model: 5y - 4 = 21. Find y.", "answer": 5, "options": [3, 4, 5, 6]}
        ]
    },
    "Class 8": {
        "Ch 17: Financial Interest Equations": [
            {"question": "NCERT Ex 17.2: An investor locks Rs. 10,000 inside a fixed deposit savings account running at a 10 percent Simple Interest rate per annum. Calculate the total interest currency accumulated over 2 years.", "answer": 2000, "options": [1000, 1500, 2000, 2500]},
            {"question": "RS Aggarwal Ch 11: A retail customer buys a smartphone appliance valued at Rs. 15,000. If the store charges a flat 12 percent sales tax (GST) markup, compute the final total billing price.", "answer": 16800, "options": [15000, 16200, 16800, 18000]}
        ],
        "Ch 18: Direct Variation Vectors": [
            {"question": "NCERT Ex 18.1: If the purchase cost of 5 identical heavy iron rods scales directly to Rs. 250, compute the total financial cost transaction required to buy 8 identical rods.", "answer": 400, "options": [300, 350, 400, 500]}
        ]
    }
}
# ============================================================
# 📚 PHASE 10: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_10_QUESTIONS = {
    "Class 1": {
        "Ch 19: Comparing Profiles": [
            {"question": "NCERT Ex 19.1: A tall wild giraffe stands right next to a short forest goat. Which animal profile reaches HIGHER into the trees? Giraffe (1) or Goat (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 2: You pick 3 crisp red apples from a branch and 3 bright green apples from another. Compute the total apple count in your basket.", "answer": 6, "options": [3, 5, 6, 9]},
            {"question": "NCERT Ex 19.4: A heavy iron anvil is placed on a scale next to a single dry tree leaf. Which object is strictly LIGHTER? Anvil (1) or Leaf (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ],
        "Ch 20: Space Geometry Introduction": [
            {"question": "NCERT Ex 20.1: Look at a standard round orange fruit. What structural shape blueprint does it resemble closest? Cube (1), Triangle (2), Sphere (3)?", "answer": 3, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 2": {
        "Ch 18: Weight Metrics Drill": [
            {"question": "NCERT Ex 18.2: A heavy wooden cricket bat is balanced on a playground scale against a tiny bird feather. Which side drops LOWER because it is heavier? Cricket Bat (1) or Feather (2)?", "answer": 1, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 12: A standard wall clock face maps out time intervals. How many main hourly number markings are printed around its perimeter?", "answer": 12, "options": [4, 6, 12, 24]}
        ],
        "Ch 19: Sequential Calendar Logic": [
            {"question": "NCERT Ex 19.5: If yesterday was completely a weekend Sunday, what specific weekday tracking node starts today? Monday (1) or Tuesday (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 3": {
        "Ch 18: Currency Change Math": [
            {"question": "NCERT Ex 18.1: Rohan hands over a crisp Rs. 20 note to purchase a cool drawing pencil that costs exactly Rs. 12. Calculate the currency token balance returned to him.", "answer": 8, "options": [6, 8, 10, 12]},
            {"question": "RS Aggarwal Ch 9: A teacher distributes a total bundle of 18 premium chocolates evenly among 3 top students. Calculate the single share count allocated per head.", "answer": 6, "options": [3, 4, 6, 8]}
        ],
        "Ch 19: Distribution Array Logic": [
            {"question": "NCERT Ex 19.4: A baker places 32 warm cookies onto large trays. If each tray holds exactly 8 cookies, how many trays are filled completely?", "answer": 4, "options": [2, 4, 6, 8]}
        ]
    },
    "Class 4": {
        "Ch 17: Pattern String Decoding": [
            {"question": "NCERT Ex 17.1: Discover the hidden arithmetic jumping logic tracking sequence parameter: 10, 20, 30, 40, __. Identify the missing coordinate integer.", "answer": 50, "options": [45, 50, 55, 60]},
            {"question": "RS Aggarwal Ch 13: Find the complete perimeter tracking line around a square bedroom layout if one uniform wall side length measures exactly 5 meters.", "answer": 20, "options": [10, 15, 20, 25]}
        ],
        "Ch 18: Time Duration Matrix": [
            {"question": "NCERT Ex 18.3: A system maintenance script runs from 11:30 AM continuous until 01:00 PM on the dot. Calculate the runtime duration in minutes.", "answer": 90, "options": [60, 75, 90, 120]}
        ]
    },
    "Class 5": {
        "Ch 17: Border Area Configurations": [
            {"question": "NCERT Ex 17.2: A rectangular neighborhood park has a total area footprint of 50 square meters. If its mapped length dimension equals 10 meters, find its width.", "answer": 5, "options": [4, 5, 8, 12]},
            {"question": "RS Aggarwal Ch 11: A standard clinical thermometer tracks physical heat metrics. What specific value represents the average baseline human body temperature in degrees Celsius?", "answer": 37, "options": [32, 35, 37, 40]}
        ],
        "Ch 18: Mapping Scale Vectors": [
            {"question": "NCERT Ex 18.5: An urban planning map scale shows that 1 cm on paper equals 500 meters of actual street grid. If a highway path measures 4 cm on the layout, find its real-world length in meters.", "answer": 2000, "options": [1000, 1500, 2000, 2500]}
        ]
    },
    "Class 6": {
        "Ch 17: Proportional Value Simplification": [
            {"question": "NCERT Ex 17.1: A storage bin contains 5 blue marble nodes and 15 white marble nodes. Express the simplified ratio mapping layout of blue to white marbles as 1:X. Find X.", "answer": 3, "options": [2, 3, 4, 5]},
            {"question": "RS Aggarwal Ch 15: Think about the structural geometry of a perfect regular pentagon tile template. How many distinct lines of reflective axis symmetry can be drawn?", "answer": 5, "options": [3, 4, 5, 6]}
        ],
        "Ch 18: Unitary Cost Analysis": [
            {"question": "NCERT Ex 18.4: If a logistics office pays Rs. 360 to purchase a pack of 12 standard logbooks, calculate the transaction cost required to buy exactly 5 logbooks.", "answer": 150, "options": [120, 150, 180, 200]}
        ]
    },
    "Class 7": {
        "Ch 18: Statistical Data Processing": [
            {"question": "NCERT Ex 18.2: Run a sorting and processing loop to find the clean statistical median coordinate value for the dataset sequence: 10, 12, 15, 20, 22.", "answer": 15, "options": [12, 15, 18, 20]},
            {"question": "RS Aggarwal Ch 8: Variable y scales in a direct proportion framework with variable x. If y evaluates to 20 when x is 4, compute the value of y when x transforms to 6.", "answer": 30, "options": [24, 25, 30, 40]}
        ],
        "Ch 19: Geometry Invariance Laws": [
            {"question": "NCERT Ex 19.3: An equilateral triangle structure is rotated smoothly around its center configuration hub. What is the lowest positive degree angle of rotation where the shape matches its original footprint perfectly?", "answer": 120, "options": [60, 90, 120, 180]}
        ]
    },
    "Class 8": {
        "Ch 19: Algebraic Division Operations": [
            {"question": "NCERT Ex 19.1: Divide the monolithic variable polynomial term 24x^3 completely by the linear term 8x. Identify the mathematical exponent power of variable x in the remaining quotient.", "answer": 2, "options": [1, 2, 3, 4]},
            {"question": "RS Aggarwal Ch 14: A massive solid cubical water reservoir tank has individual edge metrics measuring exactly 2 meters along each side. Compute its complete fluid holding capacity inside in liters (1 cubic meter = 1000 liters).", "answer": 8000, "options": [2000, 4000, 6000, 8000]}
        ],
        "Ch 20: Advanced Graphs Mapping": [
            {"question": "NCERT Ex 20.3: A data tracking coordinate dot is locked onto a Cartesian layout sheet at the position index point (0, 12). On which exact baseline chart axis framework line does this node rest? X-Axis (1) or Y-Axis (2)?", "answer": 2, "options": [1, 2, 3, 4]}
        ]
    }
}
# ============================================================
# 📚 PHASE 11: REPOSITORY EXPANSION (NCERT & RS AGGARWAL)
# ============================================================
PHASE_11_QUESTIONS = {
    "Class 1": {
        "Ch 21: Advanced Counting Blocks": [
            {"question": "NCERT Ex 21.1: You stack up 7 full wooden boxes containing 10 crayons each, and you have 2 extra loose crayons on the side. What is the total crayon count in your workshop inventory?", "answer": 72, "options": [27, 70, 72, 74]},
            {"question": "RS Aggarwal Ch 3: Count the total number of vowel characters present inside the system string token 'EDUCATION'.", "answer": 5, "options": [3, 4, 5, 6]},
            {"question": "NCERT Ex 21.3: If you take a collection of 19 glossy stickers and add exactly 1 single matching sticker to the pile, what clean round number do you get?", "answer": 20, "options": [10, 18, 20, 21]}
        ],
        "Ch 22: Visual Sorting Arrays": [
            {"question": "NCERT Ex 22.2: Look at a rectangular book cover page and a circular wall clock plate. Which specific object has sharp corners? Book Cover (1) or Wall Clock (2)?", "answer": 1, "options": [1, 2, 3, 4]}
        ]
    },
    "Class 2": {
        "Ch 20: Advanced Cash Tracking": [
            {"question": "NCERT Ex 20.2: Dev wants to settle a bill of Rs. 38 at a general store. He decides to pay using only Rs. 10 notes and Rs. 1 coins. How many individual Rs. 1 coins must he hand over?", "answer": 8, "options": [3, 5, 8, 38]},
            {"question": "RS Aggarwal Ch 13: A wallet contains exactly 3 notes of Rs. 20 value each. Calculate the complete absolute financial cash asset total in rupees.", "answer": 60, "options": [20, 40, 50, 60]}
        ],
        "Ch 21: Pattern String Generation": [
            {"question": "NCERT Ex 21.4: Decode the progressive numerical pattern jumping layout logic safely: 2, 4, 6, 8, 10, __. Identify the next step integer.", "answer": 12, "options": [11, 12, 14, 16]}
        ]
    },
    "Class 3": {
        "Ch 20: Multi-Digit Addition Drill": [
            {"question": "NCERT Ex 20.3: A dairy processing plant dispatches 415 milk packets during the early morning shift and 280 packets during the evening shift. Calculate the total packets dispatched.", "answer": 695, "options": [600, 685, 695, 700]},
            {"question": "RS Aggarwal Ch 4: Resolve the structural mathematics subtraction equation to clear out the missing placeholder variable node balance: 890 - 350 = ?", "answer": 540, "options": [500, 540, 550, 1240]}
        ],
        "Ch 21: Volumetric Fluid Tracking": [
            {"question": "NCERT Ex 21.5: A chef fills a large soup bowl by pouring in 4 complete full mugs of broth. If the mug capacity scales exactly to 250 ml, calculate the total volume of soup inside the bowl in millilitres.", "answer": 1000, "options": [500, 750, 1000, 2000]}
        ]
    },
    "Class 4": {
        "Ch 19: Heavy Scale Mass Conversions": [
            {"question": "NCERT Ex 19.2: A wholesale grocery sack holds 4 kilograms of organic wheat flour and 750 grams of baking powder. Compute the total combined mass weight load of the sack item in grams.", "answer": 4750, "options": [4000, 4500, 4750, 5000]},
            {"question": "RS Aggarwal Ch 20: A commercial construction truck unloads a heavy steel beam structure weighing 6500 kilograms. Express this absolute weight value metric in standardized structural metric tonnes.", "answer": 6.5, "options": [6.0, 6.5, 7.0, 65.0]}
        ],
        "Ch 20: Analytical Chart Processing": [
            {"question": "NCERT Ex 20.4: If a school attendance chart uses a single emoji icon block to represent a group of 4 students, how many icons are needed to visualize a block of 32 present students?", "answer": 8, "options": [6, 8, 12, 16]}
        ]
    },
    "Class 5": {
        "Ch 19: Percentage Foundation Nodes": [
            {"question": "NCERT Ex 19.1: A student scores exactly 45 marks out of a maximum target score pool of 50 points on an online coding mock test. Convert this ratio status cleanly into an absolute percentage representation string.", "answer": 90, "options": [80, 85, 90, 95]},
            {"question": "RS Aggarwal Ch 8: Reduce the raw system fractional model token 12/20 into its equivalent unified decimal scale configuration format parameter.", "answer": 0.6, "options": [0.5, 0.6, 0.75, 0.8]}
        ],
        "Ch 20: Perimeter Optimization Models": [
            {"question": "NCERT Ex 20.3: A square electronic display screen panel features a calculated total perimeter framing line measuring 36 cm. Calculate the individual physical side length dimension of the screen.", "answer": 9, "options": [4, 6, 9, 18]}
        ]
    },
    "Class 6": {
        "Ch 19: Advanced Multi-Variable Ratios": [
            {"question": "NCERT Ex 19.2: In a corporate web development agency team layout, there are 15 backend developers and 12 UI/UX designers. Express the simplified operational ratio of developers to designers.", "answer": 1.25, "options": [1.0, 1.2, 1.25, 1.5]},  # Evaluated as 5:4 float division
            {"question": "RS Aggarwal Ch 9: The variables A and B sit locked inside a direct ratio mapping of 3:5. If the value tracking node for variable A updates to 18, calculate the matching output value for variable B.", "answer": 30, "options": [24, 28, 30, 36]}
        ],
        "Ch 20: Spatial Angles Visuals": [
            {"question": "NCERT Ex 20.5: Examine the geometric interior configuration of a standard right-angled isosceles triangle tile. What is the precise degree measure of its smallest individual angular orientation?", "answer": 45, "options": [30, 45, 60, 90]}
        ]
    },
    "Class 7": {
        "Ch 20: Algebraic Expression Expansions": [
            {"question": "NCERT Ex 20.2: Run an algebraic compilation processing loop to expand and simplify the expression string layout: 4(x + 3) - 2x. Identify the clean resulting leading coefficient factor matching variable x.", "answer": 2, "options": [2, 4, -2, 6]},
            {"question": "RS Aggarwal Ch 6: Compute the true numerical evaluation balance output for the polynomial string structure 3a^2 - 2b when variable parameter a equals 3 and variable parameter b equals 4.", "answer": 19, "options": [10, 14, 19, 25]}
        ],
        "Ch 21: Advanced Probability Matrices": [
            {"question": "NCERT Ex 21.4: A closed opaque bag contains 3 bright red game tokens, 4 blue game tokens, and 5 green game tokens. Calculate the percentage probability of randomly drawing a blue token out of the bundle.", "answer": 33.33, "options": [25.0, 33.33, 41.66, 50.0]}
        ]
    },
    "Class 8": {
        "Ch 21: Compound Interest Compilations": [
            {"question": "NCERT Ex 21.2: A financial asset sum of Rs. 8,000 is locked inside a investment fund compound yield script tracking at a 10 percent interest rate per annum, compounded annually. Compute the total compound interest currency accumulated at the end of 2 years.", "answer": 16800, "options": [1600, 1680, 2000, 9680]},  # Final Amount calculated as 8000 * 1.21 = 9680 -> Net Interest = 1680
            {"question": "RS Aggarwal Ch 12: A high-end manufacturing machinery layout drops its asset valuation liquidity at a uniform depreciation rate parameter of 10 percent annually. If its initial purchase index was Rs. 50,000, find its net book value after 1 year.", "answer": 45000, "options": [40000, 45000, 48000, 49000]}
        ],
        "Ch 22: Spatial Coordinate Matrix Mapping": [
            {"question": "NCERT Ex 22.4: A core tracking point node is mapped onto a 2D Cartesian grid layout sheet precisely at the location coordinates (7, 7). Calculate its absolute perpendicular distance metric matching down to the horizontal X-axis line.", "answer": 7, "options": [0, 5, 7, 14]}
        ]
    }
}


# ============================================================
# ⚙️ THE AUTOMATED MERGE ENGINE (DO NOT TOUCH)
# ============================================================
# This script bundles every single phase together into the master lookup layout

TEXTBOOK_DB = {}

ALL_PHASES = [
    PHASE_1_QUESTIONS,
    PHASE_5_QUESTIONS,
    PHASE_6_QUESTIONS,
    PHASE_7_QUESTIONS,
    PHASE_8_QUESTIONS,
    PHASE_9_QUESTIONS,
    PHASE_10_QUESTIONS,
    PHASE_11_QUESTIONS
]

for phase in ALL_PHASES:
    # If a phase placeholder is empty, skip it gracefully
    if not phase:
        continue
        
    for class_level, chapters in phase.items():
        # If the Class block doesn't exist yet, initialize it
        if class_level not in TEXTBOOK_DB:
            TEXTBOOK_DB[class_level] = {}
            
        for chapter_name, questions in chapters.items():
            # If the Chapter doesn't exist yet under this Class, initialize it
            if chapter_name not in TEXTBOOK_DB[class_level]:
                TEXTBOOK_DB[class_level][chapter_name] = []
                
            # Append questions safely to prevent overwriting existing chapters
            TEXTBOOK_DB[class_level][chapter_name].extend(questions)
