import streamlit as st
import pandas as pd
import os

#https://medium.com/streamlit/paginating-dataframes-with-streamlit-2da29b080920

st.set_page_config(layout="centered")

st.title('Data Search-Filter with Pagination')

@st.cache_data(show_spinner=False)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df

dataset = pd.read_csv(os.path.join('data', 'customer.csv'))
# extract unique list for below
Customer = dataset['year'].to_list()
Customer = list(set(Customer))
Product = dataset['discipline'].to_list()
Product = list(set(Product))
top_menu = st.columns(2)
with top_menu[0]:
    Category = st.selectbox('Select Category', ["year", "discipline"])
    with top_menu[1]:
        if Category == "year":
            Subcategory = st.selectbox('Select year', Customer)
        elif Category == "discipline":
            Subcategory = st.selectbox('Select discipline', Product)
        result = dataset[dataset[Category] == Subcategory]
        dataset = result.sort_values(
            by=Category, ignore_index=True
        )
pagination = st.container()
bottom_menu = st.columns((4, 1, 1))
with bottom_menu[2]:
    batch_size = st.selectbox("Page Size", options=[25, 50, 100])
with bottom_menu[1]:
    total_pages = (
        int(len(result) / batch_size) if int(len(result) / batch_size) > 0 else 1
    )
    current_page = st.number_input(
        "Page", min_value=1, max_value=total_pages, step=1
    )
with bottom_menu[0]:
    st.markdown(f"Page **{current_page}** of **{total_pages}** ")

pages = split_frame(result, batch_size)
pagination.dataframe(data=pages[current_page - 1], use_container_width=True)
