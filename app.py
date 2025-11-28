import streamlit as st
st.write('# Streamlit calculator')
number1= st.number_input('number 1')
number2 = st.number_input('number 2')
number3 = st.number_input('number 3')
num3 = number1+number2+number3
st.write('# Answer is ',num3)
