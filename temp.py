# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 12:52:48 2025

@author: User
"""

import numpy as np
import pickle
import streamlit as st

load_model =pickle.load(open("C:/Users/User/Desktop/UOC Lectures/IS 4007/Week 2/trained_model.sav",'rb'))
input_data = (0,66,4.6,45,4.1,4.2,0.9,2.8,2.34,0.6,90)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction =load_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
elif(prediction[0] == 1):
  print('The person is pre diabetic')
else :
    print('The person is diabetic')