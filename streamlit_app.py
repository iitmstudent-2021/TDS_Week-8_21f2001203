import streamlit as st

st.write('# Find the largest among three numbers')

number1 = st.number_input('Enter number 1')
number2 = st.number_input('Enter number 2')
number3 = st.number_input('Enter number 3')

largest = max(number1, number2, number3)

st.write('The largest number among', number1, ',', number2, ', and', number3, 'is:', largest)
