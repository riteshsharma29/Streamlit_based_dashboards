import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Bar Plot Demo", page_icon="📈")

st.sidebar.success("# A barplot (or barchart) shows the relationship between a numeric and a categoric variable."
                    "Each entity of the categoric variable is represented as a bar. "
                    "The size of the bar represents its numeric value.")

st.sidebar.markdown("# Bar Plot  📈️")


df = px.data.medals_long()
fig = px.bar(df, x="nation", y="count", color="medal", title="Long-Form Input")

code = """
import plotly.express as px

long_df = px.data.medals_long()
fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
fig.show()
"""


st.title("Bar Plot")
st.plotly_chart(fig)
st.title("Bar Plot code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df)

