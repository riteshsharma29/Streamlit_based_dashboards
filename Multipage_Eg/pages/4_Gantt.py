import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Gantt Chart Demo", page_icon="📈")

st.sidebar.success("# A Gantt chart, commonly used in project management, "
                    "is one of the most popular and useful ways of showing activities (tasks or events) "
                    "displayed against time. On the left of the chart is a list of the activities and "
                    "along the top is a suitable time scale. Each activity is represented by a bar; the "
                    "position and length of the bar reflects the start date, duration and end date of the "
                    "activity. This allows you to see at a glance:")

st.sidebar.markdown("# Gantt Chart  📈️")

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
fig.update_yaxes(autorange="reversed")

code = """
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
fig.update_yaxes(autorange="reversed")
fig.show()
"""

st.title("Gantt Chart")
st.plotly_chart(fig)
st.title("Gantt Chart code")
st.code(code, language='python')
st.title("Dataframe")
st.table(df)
