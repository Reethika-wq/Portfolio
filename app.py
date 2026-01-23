import streamlit as st
import streamlit.components.v1 as components

# This code tells Streamlit to show your index.html file
with open("index.html", 'r') as f:
    html_data = f.read()

st.set_page_config(layout="wide")
components.html(html_data, height=1000, scrolling=True)