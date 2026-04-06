import streamlit as st

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

st.set_page_config(page_title="Simple Math Demo", page_icon="🧮")
st.title("🧮 Simple Math Calculator")
st.markdown("Enter two numbers and choose an operation.")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("First number", value=0.0, step=0.1)
with col2:
    num2 = st.number_input("Second number", value=0.0, step=0.1)

operation = st.selectbox("Operation", ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"])

if st.button("Calculate", type="primary"):
    if operation == "Add (+)":
        result = add(num1, num2)
        symbol = "+"
    elif operation == "Subtract (-)":
        result = subtract(num1, num2)
        symbol = "-"
    elif operation == "Multiply (*)":
        result = multiply(num1, num2)
        symbol = "*"
    else:
        result = divide(num1, num2)
        symbol = "/"
    
    st.success(f"**{num1} {symbol} {num2} = {result}**")

st.caption("Push to GitHub and share — runs locally or on Streamlit Cloud")