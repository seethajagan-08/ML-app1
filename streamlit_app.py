import pandas as pd
import numpy as np
import pickle
import streamlit as st

st.title('Marks Prediction')
st.info('Predicting Marks for students based on their time spent')
# st.write('Hello world!')

pickle_in = open("marks_pred.pkl", "rb")
lin_mod = pickle.load(pickle_in)

def predict_authntication('time_study'):
  prediction=lin_mod([[time_study]])
  return prediction
