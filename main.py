import streamlit as st
import pandas

st.set_page_config(layout='wide')


st.header('The Best Company')
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod mauris non velit tristique, eget mollis augue dapibus. Sed pharetra nisl nec malesuada bibendum. Fusce in arcu quis diam malesuada varius. Sed maximus ante sed lacus eleifend, eget malesuada arcu interdum. Sed commodo, tortor ac hendrerit tristique, metus ligula commodo turpis, id ullamcorper purus odio ac metus. Praesent aliquet vel purus ac tristique. Morbi quis ante id velit commodo congue. Nunc rutrum purus quis risus imperdiet, sit amet cursus enim bibendum. Suspendisse ut quam sodales, consequat tortor ut, tincidunt ex. Aliquam mollis ipsum non nisl euismod, nec euismod nulla faucibus. Aenean scelerisque lorem et nunc efficitur, vel bibendum nibh convallis. Vivamus luctus lacus nec erat bibendum, a finibus eros faucibus')
st.header('Our Team')

col1, empty_col1, col2, empty_column2, col3 = st.columns(5)
data = pandas.read_csv('data.csv')

with col1:
    for index, rows in data[:4].iterrows():
        st.header(f"{rows['first name'].capitalize()} {rows['last name'].capitalize()}")
        st.write(rows['role'])
        st.image("images/" + rows['image'])

with col2:
    for index, rows in data[4:8].iterrows():
        st.header(f"{rows['first name'].capitalize()} {rows['last name'].capitalize()}")
        st.write(rows['role'])
        st.image("images/" + rows['image'])

with col3:
    for index, rows in data[8:12].iterrows():
        st.header(f"{rows['first name'].capitalize()} {rows['last name'].capitalize()}")
        st.write(rows['role'])
        st.image("images/" + rows['image'])


