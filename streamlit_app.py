import numpy as np
import pickle
import pandas as pd
import streamlit as st 

# from PIL import Image


pickle_in = open("marks.pkl","rb")
lin_model=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_authentication(time_study):   
    prediction=lin_model.predict([[time_study]])
    return prediction



def main():
    # st.title("Marks Prediction")
    html_temp = """
    <div style="background-color:transparent;margin:auto">
    <h2 style="color:tomato;text-align:center;">Streamlit 'Marks Prediction' ML App </h2>
    <p style="color:olive; text-align:center;">Project 1️⃣<br>
    This is my 1<sup>st</sup> project. This app analysis the marks based on your study time</p>
    </div>
    <br>
    <br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    time_study = st.number_input("Time spent on study(in hrs)",min_value=0.0,max_value=16.0, step=0.1)
    result=""
    if st.button("Predict my Marks"):
        result=predict_authentication(time_study)
    st.success('You may get Marks:{}, if you study {}hours'.format(result, time_study))
    #if st.button("About"):
    #    st.text("Lets Learn")
    #    st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
