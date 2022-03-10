# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 05:09:57 2022

@author: osman volkan
"""

import streamlit as st
import pandas as pd
import seaborn as sns


st.title("datacan")
st.subheader("Data Analysis Using Python & Streamlit")

#Upload Dataset
upload=st.file_uploader("Please upload you file(in csv format)")
if upload is not None:
    data=pd.read_csv(upload)
    
#3.Show Dataset
if upload is not None:
   if st.checkbox("Preview Dataset"):
      if st.button("Head"):
        st.write(data.head())
      if st.button("Tail"):
        st.write(data.tail())
        
#4.Check Data type of Each Columns
if upload is not None:
    if st.checkbox("Data Type of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes.astype(str))
        
        
# 5. Find Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    data_shape=st.radio("Which Dimension Do You Want To Check?",('Rows',
                                                                'Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
    if data_shape=="Columns":
        st.text("Number of Columns")
        st.write(data.shape[1])    
    
        
# 6. Find Null Values in The Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!!,No Missing Values")
        

# 7. Find Duplicate Values in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
    
# 8. Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe())#(include='all'))


# 9. About Section

if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks to Priyang Bhatt")


# 10. By
if st.checkbox("By"):
    st.success("Osman Volkan")


#download updated file

if st.button('Save DataFrame'):
   # open('data_streamlit.csv','w').write(data.to_csv())
    st.text("Saved To local Drive")


