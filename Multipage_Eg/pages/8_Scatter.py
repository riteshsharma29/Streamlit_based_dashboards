import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Scatter Plot Demo", page_icon="📈")

st.sidebar.success("# Scatter plots are used to plot data points on a horizontal and a vertical "
            "axis in the attempt to show how much one variable is affected by another. "
            "Each row in the data table is represented by a marker whose position depends on its values in the columns set on the X and Y axes. "
            "❄️")

st.sidebar.markdown("# Scatter Plot  📈️")

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])

code = """
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()                
"""

st.title("Scatter Plot")
st.plotly_chart(fig)
st.title("Scatter Plot code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df.head(5))

