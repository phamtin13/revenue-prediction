import streamlit as st
import requirements.txt
model = pickle.load(open('model.pickle', "rb"))
st.title("Revenue Prediction")
a = st.number_input('Input Temperature')
if st.button('Predict'):
  result = model.predict(a)
  st.success(str(result))
