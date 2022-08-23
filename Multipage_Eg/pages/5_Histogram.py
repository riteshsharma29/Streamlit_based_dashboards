import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(page_title="Histogram Demo", page_icon="📈")

st.sidebar.success("# A histogram is one of the most commonly used graphs to show the frequency distribution. "
                    "As we know that the frequency distribution defines how often each different value occurs in the data set. "
                    "The histogram looks more similar to the bar graph, but there is a difference between them. ")

st.sidebar.markdown("# Histogram Plot  📈️")

x = ["Apples","Apples","Apples","Oranges", "Bananas"]
y = ["5","10","3","10","5"]
df = pd.DataFrame({"Fruit":x,"Quantity":y})
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name="sum"))
fig.show()

code = """
import plotly.graph_objects as go

x = ["Apples","Apples","Apples","Oranges", "Bananas"]
y = ["5","10","3","10","5"]
df = pandas.DataFrame({"Fruit":x,"Quantity":y})
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name="sum"))
fig.show()

"""

st.title("Histogram Plot")
st.plotly_chart(fig)
st.title("Histogram code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df)

