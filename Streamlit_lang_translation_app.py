import streamlit as st
from mtranslate import translate
import pandas as pd
import os

# read language dataset
df = pd.read_excel(os.path.join('data', 'language.xlsx'),sheet_name='wiki')
df.dropna(inplace=True)
lang = df['name'].to_list()
langlist=tuple(lang)
langcode = df['iso'].to_list()

# create dictionary of language and 2 letter langcode
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# layout
st.title("Language Translation app")
st.markdown("In < 40 lines of Python 🐍 code with Streamlit ! (https://www.streamlit.io/)")
st.markdown("Languages are pulled from language.xlsx dynamically !!")
inputtext = st.text_area("INPUT",height=200)

choice = st.sidebar.radio('SELECT LANGUAGE',langlist)
# I/O
if len(inputtext) > 0 :
    try:
        output = translate(inputtext,lang_array[choice])
        st.text_area("TRANSLATED TEXT",output,height=200)
    except Exception as e:
        st.error(e)

