import streamlit as st
import pickle
filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))
st.title("Revenue Prediction")
a = st.number_input('Input Temperature')
a = a.reshape(-1,1)
if st.button('Predict'):
  result = model.predict(a)
  st.caption('Revenue Prediction')
  st.success(str(result))
