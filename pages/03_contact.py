# Contents of ~/WEBAPP/streamlit_app.py
import streamlit as st
from streamlit_option_menu import option_menu

def main_page():
    st.markdown("# Accueil 🎈")
    st.sidebar.markdown("# Accueil 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def page4():
    st.markdown("# Page 4 ")
    st.sidebar.markdown("# Page 4 ")

page_names_to_funcs = {
    "Main Menu": main_page,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4
}