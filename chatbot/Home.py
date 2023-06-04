import streamlit as st

st.set_page_config(page_title="CHATBOT USING STREAMLIT")

st.markdown("<h3 style='text-align: center; color:BLUE;'>CHATBOT USING PYTHON STREAMLIT FRAMEWORK</h3>",unsafe_allow_html=True)

help_1, help_2 = st.columns(2)
with help_1:
    with st.expander("README/ABOUT-app"):
        st.markdown('''
        - A simple ChatBot example using Python Streamlit Framework.
        - No Chatbot module OR library used. Q&A is handled through dictionary of Questions and Answers.  
        - For demoying have used Python based Questions and Answers.
        - This is just a proof of concept with regards to building a chatbot without any additional module so might not anwser all questions.
        - Type in the user input box to initiate the bot.
        - Type exit or quit in the user input box to terminate the bot.
        ''')

with help_2:
    with st.expander("MY CONTACT"):
        st.markdown('''
        - LinkedIn : https://www.linkedin.com/in/ritesh-sharma5/
        - YouTube Channel : https://www.youtube.com/@goautomation            
        ''')


st.markdown("""
<style>
     [data-testid=stSidebar] {
             background-color: #D3D3D3    
     }
</style>
""",unsafe_allow_html=True)
