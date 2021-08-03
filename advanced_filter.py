import pandas as pd
import streamlit as st
import base64
import os
import numpy as np

# read dataset
df = pd.read_excel(os.path.join('data', 'customer_products_data.xlsx'))
# convert all np.float64 to int64
df[['Gross Amount','GST','Total Amount']] = df[['Gross Amount','GST','Total Amount']].astype(np.int64)

# extract unique list for below
Customer = df['Customer Name'].to_list()
Customer = list(set(Customer))
Product = df['Product Name'].to_list()
Product = list(set(Product))

st.title('Advanced Search/Filter Dashboard')
st.markdown("In Python 🐍 Streamlit ! (https://www.streamlit.io/) & Pandas (https://pandas.pydata.org/)")

# Align 3 widgets in 3 column
left_column_1, center_column_1, right_column_1 = st.beta_columns(3)

with left_column_1:
    Category = st.selectbox('Select Category', ["Customer Name","Product Name"])

with center_column_1:
    if Category == "Customer Name":
        Subcategory = st.selectbox('Select Customer',Customer)
        total = df[df[Category] == Subcategory][['Gross Amount','GST','Total Amount']].sum()
        total = total.to_list()
        total_df = pd.DataFrame({"Customer":[Subcategory],"Gross Amount":[total[0]],"GST":[total[1]],"Total Amount":[total[2]]})
    elif Category == "Product Name":
        Subcategory = st.selectbox('Select Product', Product)
        total = df[df[Category] == Subcategory][['Gross Amount','GST','Total Amount']].sum()
        total = total.to_list()
        total_df = pd.DataFrame({"Product":[Subcategory],"Gross Amount":[total[0]],"GST":[total[1]],"Total Amount":[total[2]]})

with right_column_1:
    st.markdown('Click Search Button')
    search = st.button("search")

# rectifying Date format
df['NewDate'] = df['Date'].dt.date
df = df[['Customer Name', 'Invoice No.', 'NewDate', 'Product Name', 'Quantity','Rate', 'Gross Amount', 'GST', 'Total Amount']]
result = df[df[Category] == Subcategory]

try:
    if search:
        st.markdown(Category)
        st.table(total_df)
        st.dataframe(result)
        csv = result.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        st.markdown('### Download the selected result to a file **')
        href = f'<a href="data:file/excel;base64,{b64}" download="' + Category + '_' +  Subcategory + ".csv" + '">Download</a>'
        st.markdown(href, unsafe_allow_html=True)
except Exception as e:
    st.error(e)
