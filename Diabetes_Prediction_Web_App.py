# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 12:58:08 2025

@author: User
"""

import numpy as np
import pickle
import streamlit as st

load_model =pickle.load(open("C:/Users/User/Desktop/UOC Lectures/IS 4007/Week 2/trained_model.sav",'rb'))

#Creating a function for prediction
def diabetes_prediction(input_data):
     input_data = (0,66,4.6,45,4.1,4.2,0.9,2.8,2.34,0.6,90)

     # changing the input_data to numpy array
     input_data_as_numpy_array = np.asarray(input_data)

     # reshape the array as we are predicting for one instance
     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

     prediction =load_model.predict(input_data_reshaped)
     print(prediction)

     if (prediction[0] == 0):
       return 'The person is not diabetic'
     elif(prediction[0] == 1):
       return 'The person is pre diabetic'
     else :
         return 'The person is diabetic'
     
        
def main():
    
    #Giving a title
    st.title("Diabetes prediction web app")
    
    #getting input values from user 
    
       
    Gender = st.text_input("Gender ")
    AGE = st.text_input("Age ")
    Urea = st.text_input("Urea ")
    Cr = st.text_input("Level of Creatinine ")
    HbA1c = st.text_input("HbA1c level ")
    Chol = st.text_input("Cholesterol level ")
    TG = st.text_input("TG level ")
    HDL = st.text_input("Level of HDL ")
    LDL = st.text_input("Level of LDL ")
    VLDL = st.text_input("Level of VLDL ")
    BMI = st.text_input("Level of BMI ")
    
    #code for prediction
    diagnosis = ' '
    
    #creating a button for prediction
    if st.button("Diabetes test result "):
        diagnosis = diabetes_prediction([Gender,AGE,Urea,Cr,HbA1c,Chol,TG,HDL,LDL,VLDL,BMI])


    st.success(diagnosis)
   
if __name__ == '__main__':
    main()