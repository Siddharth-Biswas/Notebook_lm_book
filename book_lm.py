import streamlit as st
import requests

st.title("My Notebook LM App for Story Telling")

notebook_lm_link = "https://notebooklm.google.com/notebook/e217b31f-bf1a-481c-868c-91e5fe353826?_gl=1*mjn46j*_ga*MjQ4MTA3MzQwLjE3NDUxNjU4MzA.*_ga_W0LDH41ZCB*MTc0NTE2NTgyOS4xLjAuMTc0NTE2NTgyOS42MC4wLjA.&original_referer=https:%2F%2Fnotebooklm.google%23&pli=1&authuser=8"

user_input = st.text_input("Enter your query:")

if st.button("Get Answer"):
    response = requests.get(notebook_lm_link, params={"query": user_input})
    if response.status_code == 200:
        st.write("Answer:", response.text)
    else:
        st.write("Error:", response.status_code)
