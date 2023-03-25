import streamlit as st
st.title("BMI calculator")
st.text_input("Name:","")
st.radio("Select gender:",('Male', 'Female'))
st.number_input('Age:')
st.text_input("Address:","")
st.text("Hobbies:")
st.checkbox("Reading Novel")
st.checkbox("Dance ")
st.checkbox("Gardening")
h= st.number_input('Weight(kg):')
W= st.number_input('Height(cm):')
if(h>0 and W>0):
     bmi=((W/h)/h)*10000
else:
     bmi=0
st.write('BMI is:',bmi)
