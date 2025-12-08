import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, root_mean_squared_error
import streamlit as st

# st.title('Marks Prediction')
# st.info('Predicting Marks for students based on their time spent')
# st.write('Hello world!')

pickle_in = open("marks_pred.pkl", "rb")
lin_model = pickle.load(pickle_in)

def predict_authentication(time_study):
  prediction=lin_model([[time_study]])
  return prediction

def main():
    st.title("Marks Prediction")
    st.info('Predicting Marks for students based on their time spent(hours)')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Marks Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    time_study = st.number_input("Time spent on study(in hrs)",min_value=0, step=1)
    result=""
    if st.button("Predict my Marks"):
        result=predict_authentication(time_study)
    st.success('You may get Marks:{}, if you study {}hours'.format(result, time_study))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
        
if __name__=='__main__':
    main()
    
