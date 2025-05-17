import streamlit as st
import numpy as np
import pandas as pd

st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Vazir';
        src: url('Vazir-Regular.ttf') format('ttf');
    }
    html, body, [class*="css"] {
        font-family: 'Vazir', sans-serif;
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('لیست اسامی اعضا در سامانه سلامت ایرانیان')

@st.cache_data
def load_data():
    df = pd.read_excel('data-for-salamatnegar-ir.xlsx', engine="openpyxl")  
    return df
df = load_data()

st.write('تعداد کل اعضا:', len(df))
st.write("پیش‌نمایش داده‌ها:")
st.dataframe(df)

column_name = st.selectbox("ستونی که می‌خوای داخلش جستجو بشه:", df.columns)
search_value = st.text_input("مقداری که می‌خوای جستجو کنی:")

if search_value:
    result = df[df[column_name].astype(str).str.contains(search_value, case=False, na=False)]

    if not result.empty:
        st.success(f"{len(result)} نتیجه پیدا شد:")
        st.dataframe(result)
    else:
        st.warning("مقدار مورد نظر پیدا نشد.")
