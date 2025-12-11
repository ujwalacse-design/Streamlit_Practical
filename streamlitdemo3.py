import streamlit as st
import pandas as pd
st.title("Upload CSV File")
st.write("Please upload a CSV file to see its contents.")
myfile = st.file_uploader("Upload,type=['csv'])")
if myfile is not None:
    df = pd.DataFrame(pd.read_csv(myfile))
    st.write(df)
else:
    st.write("No File Uploaded")
