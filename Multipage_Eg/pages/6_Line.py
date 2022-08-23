import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Line Plot Demo", page_icon="📈")

st.sidebar.success("# A line plot is a graph that displays data with the help of symbols above a number line showing the frequency of each value. "
                    "It is used to organize the data in a simple way and is very easy to interpret. ")

st.sidebar.markdown("# Line Plot  📈️")


df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

code = """
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()

"""

st.title("Line Plot")
st.plotly_chart(fig)
st.title("Line Plot code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df.head(5))

