#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
from pickle import load
import pandas as pd 
from sklearn.svm import SVC
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[9]:


model= pickle.load(open(r"C:\Users\Admin\Downloads\LR_model.sav" ,'rb'))


# In[10]:


def Bankruptcy_Prevention(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Buisness show Bankruptcy'
    else:
      return 'Buisness show Non Bankruptcy'
  


# In[11]:


def main():
    
    st.title('Bankruptcy Prevention System')
    # getting the input data from the user
    
    industrial_risk = st.sidebar.selectbox('industrial_risk',('0','0.5','1'))
    management_risk = st.sidebar.selectbox('management_risk',('0','0.5','1'))
    financial_flexibility = st.sidebar.selectbox('financial flexibility',('0','0.5','1'))
    credibility = st.sidebar.selectbox('credibility',('0','0.5','1'))
    competitiveness = st.sidebar.selectbox('competitiveness',('0','0.5','1'))
    operating_risk = st.sidebar.selectbox('operating risk',('0','0.5','1'))
   

    # code for Prediction
    Conclusion = ''
    
    # creating a button for Prediction
    
    if st.button('Analyze'):
        
         Conclusion = Bankruptcy_Prevention ([industrial_risk, management_risk, financial_flexibility, credibility, competitiveness ,operating_risk])
        
        
    st.success(Conclusion)
    
    
    
    
    
if __name__ == '__main__':
    main()


# In[ ]:




