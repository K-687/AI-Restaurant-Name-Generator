import streamlit as st
import  langchain_helper

st.set_page_config(
    page_title="Langchain_Resturant_app",
    layout="wide",
)

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine",( "Italian", "Japanese", "Indian", "Chinese", "MiddleEastern", "Greek", "Mexican", "French", "Thai", "Spanish", "Turkish", "Indonesian"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"].content.strip())
    menu_items = response["menu_items"].content.strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
