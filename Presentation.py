import SessionState
import streamlit as st
import pandas as pd
import os
import re

st.sidebar.title('Streamlit Multi Topic Presentation Dashboard')
st.sidebar.markdown('** [Bidirectional Paging Functionality Concept] **')

# function to create list of images
def Module_ImgDir(img_dir):
    pd_img=os.listdir(os.path.join(img_dir))
    final_output = [ str(i)+".jpg" for i in sorted([ int(num.split('.')[0]) for num in pd_img])]
    new_list = [img_dir + "\\" + x for x in final_output]
    return tuple(new_list)

# Bidirectional Paging function
def Screen(data_list):
    # Number of entries per screen
    N = 1
    # A variable to keep track of which item we are currently displaying
    session_state = SessionState.get(page_number=0)
    last_page = len(data_list) - 1 // N
    # Add a next button and a previous button
    prev, _, next = st.columns([2, 10, 2])
    _, c3 = st.columns([2, 100])
    if next.button("Next"):
        if session_state.page_number + 1 > last_page:
            session_state.page_number = 0
        else:
            session_state.page_number += 1
    if prev.button("Previous"):
        if session_state.page_number - 1 < 0:
            session_state.page_number = last_page
        else:
            session_state.page_number -= 1
    # Get start and end indices of the next page of the dataframe
    start_idx = session_state.page_number * N
    # end_idx = (1 + session_state.page_number) * N
    try:
        with c3:
            slideno = data_list[start_idx]
            slideno = re.sub(r"\D", "", slideno)
            st.markdown("SLIDE : " + slideno)
            st.image(data_list[start_idx])
    except:
        with c3:
            slideno = data_list[len(data_list) - 1]
            slideno = re.sub(r"\D", "", slideno)
            st.markdown("SLIDE : " + slideno)
            st.image(data_list[len(data_list) - 1])

# creating Module Tuple list
Module_list = (
    "Streamlit",
    "######################################",
    "Pandas",
    "######################################",
    "Numpy",
    "######################################",
    "Matplotlib",
    "######################################",
    "Seaborn"
)

# TOPIC Selection List
choice = st.sidebar.radio('SELECT TOPIC',Module_list)
if choice == "Streamlit":
    data = Module_ImgDir("images\\st_imgs")
    Screen(data)
elif choice == "Pandas":
    data = Module_ImgDir("images\\pd_imgs")
    Screen(data)
elif choice == "Numpy":
    data = Module_ImgDir("images\\np_imgs")
    Screen(data)
elif choice == "Matplotlib":
    data = Module_ImgDir("images\\mp_imgs")
    Screen(data)
elif choice == "Seaborn":
    data = Module_ImgDir("images\\sb_imgs")
    Screen(data)
else:
    data = []






