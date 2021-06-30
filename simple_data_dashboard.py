import pandas as pd
import streamlit as st
from copy import deepcopy
import os

df = pd.read_csv(os.path.join("data","olympics2016.csv"))

list_1 = df['Country'].to_list()
list_1 = list(set(list_1))
list_1 = sorted(list_1)

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
st.title('Olympics 2016 Medals Dashboard')
st.info('The fastest way to build and share data apps. Streamlit turns data scripts into shareable web apps in minutes. All in Python. All for free. No front-end experience required.')
country_inp = st.selectbox('Select Country', list_1)

try:
    final = df[df["Country"] == country_inp]
    final.set_index('Unnamed: 0', inplace=True)
    final.set_index('Country', inplace=True)
    if len(final) > 0:
        # final.drop_duplicates(inplace=True)
        # table = deepcopy(final)
        st.table(final)
except:
    st.error("No Data Found.")
# st.markdown("https://streamlit.io/")
