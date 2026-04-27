import streamlit as st

# 1. The Header
st.title("🧮 Dilshad's Pro Calculator")
st.write("---")

# 2. The Inputs
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0)
with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# 3. The Operation Selection
operation = st.radio("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# 4. The Logic (CS50P Style)
def calculate(a, b, op):
    if op == "Add":
        return a + b
    elif op == "Subtract":
        return a - b
    elif op == "Multiply":
        return a * b
    elif op == "Divide":
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b

# 5. The Trigger
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"The result is: {result}")
