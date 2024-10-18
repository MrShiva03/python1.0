# streamlit run file-name

import streamlit as st 

st.title("calculater")
st.markdown("Welcome to my streamlit app")
c1, c2 = st.column(2)
fnum = c1.number_input("Enter first number", value=1)
num = c1.number_input("Enter second number", value=0)

options = ["Add", "Subtract", "Multiply", "Divide"]
choice = st.radio("select operation", options)