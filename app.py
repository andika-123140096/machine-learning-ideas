import pandas as pd
import streamlit as st

st.title("Machine Learning Ideas")
df = pd.read_excel("data.xlsx")
st.dataframe(df)
