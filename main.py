import streamlit as st
import altair as alt
import pandas as pd
import streamlit as st
import numpy as np 
from datetime import time, datetime

#3日目チャレンジ

st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.markdown(''':rainbow[Day 3]''')
st.markdown(''':gray[st.button]''')


st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

if st.button('Say Hello'):
    st.write('Well hello governor')
else:
    st.write('Good bye')





st.write('-----------------------------')

#5日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.markdown(''':rainbow[Day 5]''')

st.markdown(''':gray[st.write]''')

st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")



st.header('Display text:')
#テキスト・マークダウン形式のテキスト表示
st.write('Oh hello, *governor!* :smile:')


st.header('Display numbers')
st.write('1234')


st.header('Display DataFrame')
#df→pandasのDataFrame
airi = pd.DataFrame({
    'fisrt column': [1, 2, 3, 4, 5],
    'second column' : [10, 20, 30, 40, 50 ]
    #このデータフレームは2つの列（'fisrt column' と 'second column'）を持ち、
    # それぞれの列には整数値のデータが格納されています。
})

st.write(airi)
#Pandasを使用してデータを表形式で整理し、
# それをStreamlitアプリケーション内で表示するためのもの


st.header('Accept multiple arguments')
st.write('Below is a DataFrame', airi, 'Above is a dataframe')

airi2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])

airichart = alt.Chart(airi2).mark_circle().encode(
    x='a', y='b', size= 'c', color ='b', tooltip=['a', 'b', 'c'])
st.write(airichart)




st.write('-----------------------------')

#8日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 8]''')

st.markdown(''':gray[st.slider]''')


st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.subheader('Slider')
