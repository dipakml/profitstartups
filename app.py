# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author: Dipak Argade
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 5 22:50:04 2022

@author: Dipak Argade
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("lm.pkl","rb")
lm=pickle.load(pickle_in)  

def predict(RD,Administration,MS,Florida,NewYork):
    
    """
    
    ---
    parameters:  
      - name: RD
        in: query
        type: number
        required: true
      - name: Administration
        in: query
        type: number
        required: true
      - name: MS	
        in: query
        type: number
        required: true
      - name: Florida
        in: query
        type: number
        required: true
      - name: NewYork
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=lm.predict([[RD,Administration,MS,Florida,NewYork]])
    print(prediction)
    return prediction



def main():
    header_container = st.container()
    st.image('logo.jpeg')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Profit Prediction of start-ups in USA </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    RD = st.text_input("RD","Type Here")
    Administration = st.text_input("Administration","Type Here")
    MS	 = st.text_input("MS","Type Here")
    Florida = st.text_input("Florida","Type Here")
    NewYork = st.text_input("NewYork","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(RD,Administration,MS,Florida,NewYork)
    st.success('The predicted profit is {}'.format(result))
    if st.button("About"):
        st.text("Created by PWS")

if __name__=='__main__':
    main()
    
    
    