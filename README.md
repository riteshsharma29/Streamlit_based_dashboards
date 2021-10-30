# Streamlit_based_dashboards

DOCUMENTATION : https://streamlit.io/
REFERENCES : https://discuss.streamlit.io/t/wide-layout-left-aligned-with-padding/7938

ALL DEPENDECIES CAN BE INSTALLED USING pip.

To run streamlit app use this cmd : streamlit run <python file name>

All modules/dependencies can be installed using pip.

To run any app : Goto the path where script and data folder is downloaded and kept. Then run this command streamlit run <script>

Streamlit based data apps and dashboards

1. <simple_data_dashboard.py> Simplest data apps / dashboard for olympic 2016 dataset. To launch the app run this command in cmd : streamlit run simple_data_dashboard.py
2. <olympic.py> Live Olympics Tokyo 2020 Dashboard in Python 🐍 Streamlit! (https://www.streamlit.io/) & Plotly (https://plotly.com/)
3. <dash_cert_report.py> Certificate validation report 
4. <advanced_filter.py> Advanced filter reporting Dashboard.
5. <slide_presentation_1.py> - Last 5 olympics Top 10 Countries using Python 🐍 Streamlit ! (https://www.streamlit.io/) with flavors of Plotly (https://plotly.com/). Have created last_5_olympic.xlsx by copying table from wiki for each olympic respectively then pasting it to raw.xlsx ==> running create_olypicdataset_top10.py ==> output then pasted to last_5_olympic.xlsx dataset. Done slight manual changes as well.
6. <NLP.py> - Streamlit "Natural Language Processing" app: Created Streamlit "Natural Language Processing" app to perform NLTK functions.Requires gensim==3.8.3.
7. <lang_translation_app.py> - Streamlit Translation. Layout input is driven from data/language.xlsx.
8. <latex.py> - Streamlit app to parse LaTex .tex files.
9. <Streamlit_Scientific_calc.py> - Streamlit - Kalker Scientific Calculator app
10. <Streamlit_lang_translation_speech_app.py> - Streamlit Language Translation with text-to-speech converter. Layout input is driven from data/language.xlsx.
  
11. ######################################################## <Multilingual_NLP.py>  ######################################################## start
  
  #This script is demonstartion of Multilingual Natural Language Processing app using Stanza,Streamlit mainly.

Documentation link for Stanza: https://stanfordnlp.github.io/stanza/

# Depencies can be installed using below commands :

pip install streamlit==1.1.0
pip install stanza==1.3.0
pip install mtranslate==1.8
pip install PyAutoGUI==0.9.53
pip install pandas==1.2.4
pip install nltk==3.6.2

The windows path for language downloaded models is :
C:\Users\<username>\stanza_resources

Refer Supported_Languages sheet in stanza_supported_languages.xlsx and check for the languages you want to download.

#command prompt Sample code to download the language model is as follows :

>>> import stanza
>>> # to download language model for Afrikaans
>>> stanza.download('af')
>>> # to download language model for German
>>> stanza.download('de')
>>> # to download multilingual model 
>>> stanza.download("multilingual")

Update langtable sheet in stanza_supported_languages.xlsx if you wish to add OR delete languages. Mostly nlp_langid	are transid same however google around for transid.

11. ######################################################## <Multilingual_NLP.py>  ######################################################## End
 
