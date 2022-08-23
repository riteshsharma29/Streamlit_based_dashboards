import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Box Plot Demo", page_icon="📈")

st.sidebar.success("# A Box Plot is the visual representation of the statistical five number summary of a given data set. "
                    "A Five Number Summary includes: "
                    "Minimum, First Quartile, Median (Second Quartile),Third Quartile, Maximum")


st.sidebar.markdown("# Box Plot  📈️")

df = px.data.tips()
fig = px.box(df, x="day", y="total_bill", color="smoker")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default

code = """
import plotly.express as px

df = px.data.tips()
fig = px.box(df, x="day", y="total_bill", color="smoker")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.show()
"""

st.title("Box Plot")
st.plotly_chart(fig)
st.title("Box Plot code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df.head(5))

