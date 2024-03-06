import streamlit as st
import helper
import pickle

model = pickle.load(open('D:\Quora_duplicate_project\model.pkl','rb'))
# st.image(logo_url, width=100)
# st.set_page_config(page_title="Duplicate Question Pairs", page_icon="🐙")
st.header('Duplicate-Question-Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')        
