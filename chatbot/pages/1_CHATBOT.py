import streamlit as st

st.markdown("""
<style>
     [data-testid=stAppViewContainer] {
                 background-color: #87CEFA    
     }
</style>
""",unsafe_allow_html=True)


input_text = st.text_input("User: ",key=str(0))
input_text = input_text.lower().strip()

mydict = {
    ("hi","hello"):"Hi, I am bot how can I help you ? will try to answer your python queries.",
    ("python","python language"):"Python is a high-level, general-purpose programming language.\nIts design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.\nPython is dynamically typed and garbage-collected. ",
    ("web","web development","web development framework"):"Django https://www.djangoproject.com/ is best web development framework in Python.\nFlask https://flask.palletsprojects.com/ is second best",
    ("modules","pypi","module","library"):"Search for any module here https://pypi.org/",
    ("pip","what is pip"):"pip is python package manager",
    ("data analysis","pandas","data"): "Best Python data analysis library : https://pandas.pydata.org/",
    ("ml","machine learning"):"Best Python ML library/module is Scikit-learn https://scikit-learn.org/stable/",
    ("plots","graph","visualization","plot","charts","chart"):"https://python-charts.com/ - One the best resource avaialble to learn Python data visualization",
    ("inventor","python inventor","python creator","creator"):"Guido van Rossum best known as the creator of the Python programming language !",
    ("automation","browser automation","test"): "selenium : https://selenium-python.readthedocs.io/\nRobot Framework : https://robotframework.org/\nPytest : https://docs.pytest.org/en/7.3.x/"
}

def get_dict_value_by_key(kwd):
    for keys, v in mydict.items():
        if kwd in keys:
            return v

counter = 100
counter_2 = 1

while (input_text != "") and (input_text != "exit") or (input_text == "bye") or (input_text == "quit"):
    try:
        if get_dict_value_by_key(input_text) != None:
            output = st.text_area("bot", get_dict_value_by_key(input_text), key=str(counter_2),height=125)
            input_text = st.text_input("User: ", key=str(counter))
            input_text = input_text.lower().strip()
        else:
            output = st.text_area("bot", "Keyword not found !!! Search with appropriate keyword", key=str(counter_2),height=125)
            input_text = st.text_input("User: ", key=str(counter))
            input_text = input_text.lower().strip()
    except:
        output = st.text_area("bot", "Keyword not found !!! Search with appropriate keyword", key=str(counter_2),height=125)
        input_text = st.text_input("User: ", key=str(counter))
        input_text = input_text.lower().strip()

    if (input_text == "exit") or (input_text == "bye") or (input_text == "quit"):
        output = st.text_area("bot", "Thank you for using me ! Goodbye have a nice day ahead.", key=str(counter_2))
        break

    counter += 100
    counter_2 += 1



















