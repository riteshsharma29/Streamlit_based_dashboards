import streamlit as st
import pyautogui
import pandas as pd
import plotly.express as px
import os

st.title('Slide Show Presentation')
st.markdown('Last 5 olympics Top 10 Countries')
st.markdown("In Python 🐍 Streamlit ! (https://www.streamlit.io/) with flavors of Plotly (https://plotly.com/)")

def generate_plot(olympicyear):
    medal_df = pd.read_excel(os.path.join("data","last_5_olympic.xlsx"),sheet_name=str(olympicyear))
    fig = px.bar(medal_df.head(30), x="Country", y="count", color="medal",
                 color_discrete_sequence=['yellow', 'silver', 'rgb(173, 138, 86)'],
                 title="Olympics " + str(olympicyear), width=700, height=600)
    fig.update_layout(xaxis_tickangle=60, font=dict(family="Courier New, monospace", size=20, color="#ff0000"))
    st.plotly_chart(fig)

# create a button in the side bar that will move to the next page/radio button choice
next = st.sidebar.button('NEXT SLIDE')

choice = st.sidebar.radio("GO TO", ('2020','2016','2012','2008','2004'))

if next:
    pyautogui.press("tab")
    pyautogui.press("down")
else:
    # finally get to whats on each page
    if choice == '2020':
        generate_plot("2020")
    elif choice == '2016':
        generate_plot("2016")
    elif choice == '2012':
        generate_plot("2012")
    elif choice == '2008':
        generate_plot("2008")
    elif choice == '2004':
        generate_plot("2004")

