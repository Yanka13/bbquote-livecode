import streamlit as st

from bbquote.api import get_quote


st.title("Welcome to our website!")
result = get_quote()  # assuming the function returns an author and a quote

st.write(result)
