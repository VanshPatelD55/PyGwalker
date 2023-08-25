import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Pygwalker",
    layout="wide"
)
 
# Add Title
st.title("Pygwalker")
 
# Import your data
st.session_state.df = None
if st.session_state.df is None:
    uploaded_file = st.file_uploader(
        "Choose a CSV file. This should be in long format (one datapoint per row).",
        type="csv",
    )
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
 


with st.form("demo"):
    submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner():
            pyg_html = pyg.walk(st.session_state.df, return_html=True)
            components.html(pyg_html, height=1000, scrolling=True)

