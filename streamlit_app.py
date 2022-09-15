import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast FAvorites')

streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text('🥗 Kale, spinach and rocket smoothie')
streamlit.text('🐔 Hard boiled free-range egg')
streamlit.text('🥑🍞 Advokado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
