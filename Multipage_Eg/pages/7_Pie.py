import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Pie Chart Demo", page_icon="📈")

st.sidebar.success("# A pie chart is a pictorial representation of data in the form of a circular chart "
                    "or pie where the slices of the pie show the size of the data. "
                    "A list of numerical variables along with categorical "
                    "variables is needed to represent data in the form of a pie chart. "
                    "The arc length of each slice and consequently "
                    "the area and central angle it forms in a pie chart is proportional to the quantity it represents.")

st.sidebar.markdown("# Pie Chart  📈️")

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')

code = """
import plotly.express as px

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()
"""

st.title("Pie Chart")
st.plotly_chart(fig)
st.title("Pie Chart code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df.head(5))
