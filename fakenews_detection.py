#!/usr/bin/env python
# coding: utf-8

# In[16]:


import streamlit as st
import pickle
filename = 'fakeNews.pkl'
pickle_in = open(filename, 'rb')
loaded_model = pickle.load(pickle_in)
vectfilename = 'vect.pkl'
pickle_in = open(vectfilename, 'rb')
loaded_vect = pickle.load(pickle_in)


# In[18]:


# txt="""Ever get the feeling your life circles the roundabout rather than heads in a straight line toward the intended destination?

# Hillary Clinton remains the big woman on campus in leafy, liberal Wellesley, Massachusetts. Everywhere else votes her most likely to don her inauguration dress for the remainder of her days the way Miss Havisham forever wore that wedding dress."""
def checkNews(txt):
    if(txt!=''):
        vectTxt = loaded_vect.transform([txt])
        if(loaded_model.predict(vectTxt)):
            st.write('Fake News!')
        else:
            st.write("Authentic News!")


# In[19]:


news = st.text_area('Enter news:')
checkNews(news)

