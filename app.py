import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="centered")

st.title("🔬 Scientific Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display
st.text_input("Display", st.session_state.expression, key="display", disabled=True)

# Function to add value
def add_value(val):
    st.session_state.expression += str(val)

# Function to clear
def clear():
    st.session_state.expression = ""

# Calculate result
def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# Scientific functions
def apply_func(func):
    try:
        value = float(eval(st.session_state.expression))
        
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "sqrt":
            result = math.sqrt(value)
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "square":
            result = value ** 2

        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error"

# Button Layout

cols = st.columns(5)
buttons = ["7","8","9","/","sqrt"]

for i,b in enumerate(buttons):
    if cols[i].button(b):
        if b=="sqrt":
            apply_func("sqrt")
        else:
            add_value(b)

cols = st.columns(5)
buttons = ["4","5","6","*","square"]

for i,b in enumerate(buttons):
    if cols[i].button(b):
        if b=="square":
            apply_func("square")
        else:
            add_value(b)

cols = st.columns(5)
buttons = ["1","2","3","-","log"]

for i,b in enumerate(buttons):
    if cols[i].button(b):
        if b=="log":
            apply_func("log")
        else:
            add_value(b)

cols = st.columns(5)
buttons = ["0",".","+","=","ln"]

for i,b in enumerate(buttons):
    if cols[i].button(b):
        if b=="=":
            calculate()
        elif b=="ln":
            apply_func("ln")
        else:
            add_value(b)

cols = st.columns(5)
buttons = ["sin","cos","tan","π","C"]

for i,b in enumerate(buttons):
    if cols[i].button(b):
        if b=="sin":
            apply_func("sin")
        elif b=="cos":
            apply_func("cos")
        elif b=="tan":
            apply_func("tan")
        elif b=="π":
            add_value(math.pi)
        elif b=="C":
            clear()
