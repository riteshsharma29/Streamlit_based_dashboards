import pandas as pd
import streamlit as st
import plotly.graph_objects as go

#youtube link : https://www.youtube.com/watch?v=wXwrqVqbexc&t=3s

st.title('Live Olympics Tokyo 2020 Dashboard')
st.markdown("Dashboard in Python 🐍 Streamlit! (https://www.streamlit.io/) & Plotly (https://plotly.com/)")

base_df = pd.read_html("https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm?utm_campaign=dp_google")

# extracting olympic medal dataset
df = base_df[0]

# renaming dataframe columns
df.columns = ['Rank', 'Country', 'Gold', 'Silver', 'Bronze', 'Total','RankbyTotal', 'NOCCode']

# renaming country values to list
country = df['Country'].to_list()

# combo box
country_inp = st.selectbox('Select Country from the Dropdown below :', country)

# medal counts
gold_count = df[df['Country']==country_inp]['Gold'].values
silver_count = df[df['Country']==country_inp]['Silver'].values
bronze_count = df[df['Country']==country_inp]['Bronze'].values

res = df[df['Country']==country_inp]
res.set_index('Rank', inplace=True)

#  creating bar graph
fig = go.Figure(data=[go.Bar(name='Gold', x=['Gold'], y=gold_count,marker_color='gold'),
                      go.Bar(name='Silver', x=['Silver'], y=gold_count,marker_color='rgb(180, 180, 180)'),
                      go.Bar(name='Bronze', x=['Bronze'], y=bronze_count,marker_color='rgb(173, 138, 86)')]
                )

# creating layout

fig.update_layout(
    title=country_inp,
    xaxis_title="Medals",
    yaxis_title="Scale",
    legend_title="Medals Tally",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

try:
    st.table(res)
    st.plotly_chart(fig)
except Exception as e:
    st.error(e)



