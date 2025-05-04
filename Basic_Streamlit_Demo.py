import streamlit as st
import pandas as pd
st.title('Basic Streamlit Demo')
user_name=st.text_input('Enter your name:')
if user_name:
    st.write(f'Hello,{user_name}!')
age = st.slider('Select your age:',0 ,100, 25)
st.write(f'You are {age} years old.')
agree = st.checkbox('I agree')
if agree:
    st.write('Thank you for agreeing!')

if st.button('Click me'):
    st.write('Button clicked!')

option = st.radio(
    "What's your favorite color?",
    ('Red',"Green",'Blue'))

if option:
    st.write(f'Your favorite color is {option}.')

selected_option = st.selectbox(
    'Select a number',
    [1,2,3,4,5])

st.write(f'You selected:{selectbox_option}')

data = {
    'Coloumn 1' : [1,2,3,4],
    'Coloumn 2' : [10,20,30,40]
}

df = pd.DataFrame(data)

st.write('Here is a sample dataframe:')

st.write(df)

st.Dataframe(df)

st.table(df)

st.linechart(df)

st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fauth0.com%2Fblog%2Fintroduction-to-streamlit-and-streamlit-components%2F&psig=AOvVaw38qK7HC6eoI1VBDYYlcXP-&ust=1746433234006000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCODCvfqwiY0DFQAAAAAdAAAAABAE')

st.markdown('This is **Markdown** text.')