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

st.title('Fake News Detection System')

news = st.text_area('Enter news:')
checkNews(news)

from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="red",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in ",
        image('https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e181828ba9f9e92b6ebc6e7_RGB_Logomark_Color_Light_Bg.png',
              width=px(25), height=px(25)),
        " with ❤️ by imt-02",
        # link("https://twitter.com/ChristianKlose3", "@ChristianKlose3"),
        br(),
        link("https://buymeacoffee.com/chrischross", image('https://github.com/alooperalta/Fake-News-Detection-System/blob/main/gitLogo.png')),
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()

