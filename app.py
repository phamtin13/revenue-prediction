import streamlit as st
import numpy as np
import pickle
filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))
st.title("Revenue Prediction")
A = []
a = st.number_input('Input Temperature')
A.append(a)
A = np.array(A)
A = A.reshape(-1,1)
if st.button('Predict'):
  result = model.predict(A)
  st.caption('Revenue Prediction')
  st.success(*result)
