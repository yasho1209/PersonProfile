import streamlit as st
import pandas as pd
import wikipedia as wiki
import pyttsx3 as py

def summary(val):
    sum = wiki.summary(selected_person, sentences=3)
    sum = str(sum)
    py.speak(sum)


st.header("psuedo-wiki")

selected_person = st.text_input(
    'Enter the name of the person'
)


button = st.button("Submit")

if button:
    st.write(wiki.summary(selected_person, sentences=3))
    summary(selected_person) 