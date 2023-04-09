import streamlit as st
from send_mail import send_email
import pandas


st.header('Contact Us')
data = pandas.read_csv('topics.csv')
print(data)


with st.form(key='form'):
    email = st.text_input('Your Email Address')

        #st.selectbox('What topic do you want to discuss?', rows['topic'])
    topic = st.selectbox('What topic do you want to discuss?', data['topic'])
    st.write('You have selected:', topic)
    message = st.text_area('Text')
    button = st.form_submit_button('Submit')

    if button:
        send_email(message)
        st.info('Email Submitted Successfully')



