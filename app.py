import streamlit as st

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }
table = st.table(data)
st.write(table)
st.write(data)
