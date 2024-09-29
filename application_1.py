#!/usr/bin/env python
# coding: utf-8

# In[12]:


# STREAMLIT 


# In[13]:





# In[14]:


import streamlit as st


# In[15]:


st.title("Welcome to Raj's First App")
st.write("Hello  Geeks")


# In[16]:


number =st.number_input("insert a number : ")
st.write(f"entered : {number}")


# In[17]:





# In[18]:


name=st.text_input("enter your name: ")
st.write(f"your entered name is {name}")


# In[19]:


age=st.slider("your age: ",0,100,25)
st.write(f"your entered age is {age}")


# In[ ]:




