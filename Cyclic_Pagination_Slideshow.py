import SessionState
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.sidebar.title('Streamlit Cyclic Presentation')
st.sidebar.markdown('** Last 5 olympics Top 10 Countries **')

st.sidebar.markdown("** Olympics 2004 **")
st.sidebar.markdown("** Olympics 2008 **")
st.sidebar.markdown("** Olympics 2012 **")
st.sidebar.markdown("** Olympics 2016 **")
st.sidebar.markdown("** Olympics 2020 **")

def generate_plot(olympicyear):
    medal_df = pd.read_excel(os.path.join("data","last_5_olympic.xlsx"),sheet_name=str(olympicyear))
    fig = px.bar(medal_df.head(30), x="Country", y="count", color="medal",
                 color_discrete_sequence=['yellow', 'silver', 'rgb(173, 138, 86)'],
                 title="Olympics " + str(olympicyear), width=800, height=600)
    fig.update_layout(xaxis_tickangle=60, font=dict(family="Courier New, monospace", size=20, color="#ff0000"))
    st.plotly_chart(fig)

# Number of entries per screen
N = 1

# A variable to keep track of which item we are currently displaying
session_state = SessionState.get(page_number=0)

data = ('2004','2008','2012','2016','2020')
last_page = len(data) - 1 // N

# Add a next button and a previous button

prev, _, next = st.columns([2, 10, 2])
_, c3 = st.columns([2, 100])

if next.button("Next"):

    if session_state.page_number + 1 > last_page:
        session_state.page_number = 0
    else:
        session_state.page_number += 1

if prev.button("Previous"):

    if session_state.page_number - 1 < 0:
        session_state.page_number = last_page
    else:
        session_state.page_number -= 1

# Get start and end indices of the next page of the dataframe
start_idx = session_state.page_number * N
end_idx = (1 + session_state.page_number) * N

try:
    # st.text_area("out", data[start_idx])
    with c3:
        generate_plot(data[start_idx])
except:
    # st.text_area("out", data[start_idx - 1])
    with c3:
        generate_plot(data[start_idx - 1])

