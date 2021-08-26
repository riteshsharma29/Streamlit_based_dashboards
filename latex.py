import streamlit as st
from TexSoup import TexSoup
import os
from glob import glob


# list all .tex files in the below path
PATH = os.path.join(os.getcwd(),"inputfiles")
EXT = "*.tex"
all_tex_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]


st.title('Latex Extractor')
st.markdown("**Extracted all Physics and Mathematical equations from the .tex latex files**")

# Select Box
file = st.selectbox('Select Latex File',all_tex_files)

# parse .tex files and extract only latex equation
soup = TexSoup(open(file, 'r'))
equations = soup.find_all("\\begin{equation}")
for equation in equations:
    equation = str(equation).replace("\\begin{equation}","")\
        .replace("\\end{equation}","").replace("\\label","").replace("\\mathds","").replace("\Hat","")
    try :
        href = "**" + equation + "**"
        st.markdown(href)
        st.latex(equation)
    except Exception as e:
        st.error(e)