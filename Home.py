import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/mephoto.jpg", width=600)

with col2:
    st.title("Dylan Beddo")
    content = """
    Hi! I am Dylan! I graduated from the University of Central Missouri in 2013 with a degree in Computer Information Systems.
    Currently I am a Data Analyst at Veterans United Home Loans on the Consumer Research & Development team.
    """

    st.info(content)

content2 = """
        Below you can find some of the apps I have built in Python. Feel free to contact me!
        """

st.info(content2)

col3, empty_col, col4 = st.columns([1.5, .5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")