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

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Menu", ["Main Menu","Page 2","Page 3", "Page 4"], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
  
# 2. horizontal menu
selected = option_menu(None, ["Main Menu", "Page 2", "Page 3", "Page 4"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# 3. CSS style definitions
selected = option_menu(None, ["Main Menu", "Page 2", "Page 3", "Page 4"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

page_names_to_funcs[selected]()