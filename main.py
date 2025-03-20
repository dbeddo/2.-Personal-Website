import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dylan Beddo")
    content = """
    Hi! I am Dylan! I am a Data Analyst at Veterans United Home Loans.
    """

    st.info(content)