import streamlit as st 
st.header('Ramachandra College of Engineering')
a=st.number_input('Enter any value')
if st.button('HIT ME'):
  st.success(f'Your lucky number is {a}')
