import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Bubble Plot Demo", page_icon="📈")

st.sidebar.success("# A bubble plot is a scatterplot where a third dimension is added: "
                    "the value of an additional numeric variable is represented through the size of the dots. "
                    "You need 3 numerical variables as input: one is represented by the X axis, one by the Y axis, "
                    "and one by the dot size.")


st.sidebar.markdown("# Bubble Plot  📈️")

df = px.data.gapminder()
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)

code = """
import plotly.express as px

df = px.data.gapminder()
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
fig.show()
"""

st.title("Bubble Plot")
st.plotly_chart(fig)
st.title("Bubble Plot code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df)
