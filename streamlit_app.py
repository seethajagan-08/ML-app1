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
    time_options = [i/4 for i in range(0, 69)]
    time_study = st.selectbox("Time spent on study (in hrs)",time_options)
    result=""
    if st.button("Predict my Marks"):
        result=predict_authentication(time_study)
    st.success('You may get Marks: {},\n if you study {} hrs'.format(result, time_study))
    if st.button("About Me"):
        st.text("I'm Seetha Jagan")
        st.text("Follow me on 👇")
        st.markdown(
                    "<a href='https://www.linkedin.com/in/seethajagan' target='_blank' style='color:royalblue; text-decoration:none; font-size:18px;'>Linked In</a>",
            unsafe_allow_html=True
        )

if __name__=='__main__':
    main()


#'''hours = st.slider(
#    "Time spent on study (in hrs)",
#    min_value=0.0,
#    max_value=24.0,
#    value=1.0,
#    step=0.1
#)'''

#'''time_study = st.number_input(
#    "Time spent on study(in hrs)",
#    min_value=0.0,
#    max_value=16.0,
#    step=0.1
#) '''

#time_options = [i/2 for i in range(0, 49)]  # 0.0 to 24.0 in 0.5-hour steps
#hours = st.selectbox(
#   "Time spent on study (in hrs)",
#    time_options
#)

