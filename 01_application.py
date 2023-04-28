# Contents of ~/WEBAPP/streamlit_app.py
import json
import utils_transformers
from utils_transformers import *
import requests
import pickle
from streamlit_lottie import st_lottie
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.chart_container import chart_container
from streamlit_extras import add_vertical_space as avs
import pandas as pd
import streamlit as st
from streamlit.elements.data_editor import _apply_dataframe_edits
from streamlit import type_util
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from detect_delimiter import detect
from io import BytesIO
from PIL import Image

img_content = requests.get("https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/metabosign_icon.png?raw=true").content
img = Image.open(BytesIO(img_content))

 # state variable   
if "mdf" not in st.session_state:
    st.session_state.mdf = None
    #pd.DataFrame(columns=["id","sexe","age","label","cortisol","composé S","17OHP","Delta4A","Testostérone","Progestérone"])

st.set_page_config(
   page_title="Détection de malignité dans les tumeurs de la corticosurénale",
   page_icon=img,
   layout="wide",
   initial_sidebar_state="expanded"
)

st.markdown(
"""
<style>
h1 {
    font-family: 'Arial Black', sans-serif;
    font-size: 3em;
    color: #1F618D;
    margin-bottom: 30px;
    text-align: center;
}

h2 {
    margin-top: 0;
    font-size: 1.5em;
    color: #1F618D;
}

p {
    font-size: 1.2em;
    color: #2C3E50;
    margin-bottom: 30px;
    text-align: justify;
}

#MainMenu {
    visibility: hidden;
}

footer {
	visibility: hidden;
}

header {
	visibility: hidden;
}
</style>
""",
unsafe_allow_html=True)

# load animation from lottie url
url = requests.get("https://assets1.lottiefiles.com/packages/lf20_uwWgICKCxj.json")
url_json = dict()
if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in URL")

# load animation from lottie url
url_hib = requests.get("https://assets1.lottiefiles.com/packages/lf20_loGwzbI7N3.json")
url_hib_json = dict()
if url.status_code == 200:
    url_hib_json = url_hib.json()
else:
    print("Error in URL")

# load animation from lottie url
url_robot = requests.get("https://assets10.lottiefiles.com/packages/lf20_mLnvYR.json") #https://assets3.lottiefiles.com/packages/lf20_q7wkifyr.json
url_robot_json = dict()
if url.status_code == 200:
    url_robot_json = url_robot.json()
else:
    print("Error in URL")



# Présentation de l'app
def main_page():
    st.markdown("# Présentation de l'application")
    st.markdown("## Tutoriel vidéo")
    st.markdown("MetaboSign-Corticosurrénale est une solution bout en bout permettant d'accélérer le diagnostic de malignité des tumeurs de la corticosurrénale sur base de relevés sériques analysés en LC-MS/MS.")
    st.sidebar.markdown("# Présentation :medical_symbol:")
    st.video('https://youtu.be/ntRInkPfY7Y', start_time=0)
    st.markdown("## Rappels sur la glande surrénale")
    st.markdown("La glande surrénale sécrète plusieurs hormones indispensables à la survie du corps humain. En effet, elle synthétise les glucocorticoïdes, les minéralocorticoïdes, les androgènes et les catécholamines. En cas de dysfonctionnement, la production de ces hormones est perturbée et cela peut induire divers pathologies. Ainsi, dans notre contexte, il est possible d'identifier une \"signature hormonale\" caractéristique des tumeurs malignes de la corticosurrénale")
    st.video('https://www.youtube.com/watch?v=eiOWyPOCUCM', start_time=18)

    #st_lottie(url_json,reverse=True,height=None,width=None,speed=1.5,loop=True,quality='high',key='med_team' )
    

# Saisie manuelle
def saisie_manuelle():
    st.markdown("# Saisie manuelle")
    st.sidebar.markdown("# Saisie manuelle :writing_hand:")
    avs.add_vertical_space(4)
    col0, col1, col2, col4, col5, col6, col7, col8, col9= st.columns(9,gap="small") #col3,
    id= col0.text_input('id', help="string identifer")
    sexe = col1.text_input('sexe', help="F or M")
    age = col2.number_input('age',min_value=0,format='%i')
    #label = col3.text_input('label')
    cortisol = col4.number_input('cortisol',min_value=0.01)
    compose_s = col5.number_input('composé S',min_value=0.01)
    var_17OHP = col6.number_input('17OHP',min_value=0.01)
    delta4A = col7.number_input('Delta4A',min_value=0.01)
    testosterone = col8.number_input('Testostérone',min_value=0.01)
    progesterone = col9.number_input('Progestérone',min_value=0.01)

    run = st.button('Submit')
      
    if run:
        df_new = pd.DataFrame({'id': id, 
                            'sexe': sexe, 
                            'age': age, 
                            #'label': label, 
                            'cortisol': cortisol, 
                            'composé S': compose_s,
                            '17OHP': var_17OHP, 
                            'Delta4A': delta4A, 
                            'Testostérone': testosterone,
                            'Progestérone': progesterone}, index=[id])  
        if st.session_state.mdf is None:
            st.session_state.mdf = df_new
        else:
            st.session_state.mdf = pd.DataFrame(pd.concat([st.session_state.mdf, df_new], axis=0))
        st.dataframe(st.session_state.mdf)

    if st.session_state.mdf is not None:
        st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")
    else:
        st.write(f"Total Rows: 0")
    st_lottie(url_json,reverse=True,height=None,width=None,speed=1.5,loop=True,quality='high',key='med_team' )

# Upload
def upload():
    st.markdown("# Upload")
    st.sidebar.markdown("# Upload :floppy_disk:")
    uploaded_file = st.file_uploader(label="Choose a CSV file",type='csv') 
    if uploaded_file:
        separator = detect(uploaded_file.getvalue().decode("utf-8"))
        df = pd.read_csv(uploaded_file,sep=separator)
        success_notif = "Chargement des données du fichier \""+uploaded_file.name+"\" réussi"
        st.success(success_notif)
        st.session_state.mdf = pd.concat([st.session_state.mdf, df], axis=0)
        st.session_state.mdf = st.session_state.mdf.set_index(st.session_state.mdf['id'])
        st.dataframe(st.session_state.mdf)
    if st.session_state.mdf is not None:
        st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")
    else:
        st.write(f"Total Rows: 0")
    st_lottie(url_json,reverse=True,height=None,width=None,speed=1.5,loop=True,quality='high',key='med_team' )

def f():
    t = st.session_state['mdf']
    t = type_util.convert_anything_to_df(t)
    _apply_dataframe_edits(t, st.session_state['st_t'])

# Modification de données
def data_modification():
    st.markdown("# Modification des données")
    st.sidebar.markdown("# Modification des données :hammer_and_wrench:")
    #st.write(df)
    #df = st.session_state.mdf
    if st.session_state.mdf is not None:
        edited_df = st.experimental_data_editor(st.session_state.mdf, use_container_width=True,num_rows='dynamic',on_change=f, key='st_t')
        st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")
        if st.button('Nettoyer les données numériques'):
            st.session_state.mdf = utils_transformers.num_encoder(edited_df)
            st.success('Nettoyage effectué!')
    else:
        st_lottie(url_hib_json,reverse=True,height=None,width=None,speed=1,loop=True,quality='high',key='hib' )

# Exploration
def exploration():
    st.markdown("# Data Exploration")
    st.sidebar.markdown("# Data Exploration :see_no_evil:")
    if st.session_state.mdf is not None:
        filtered_df = dataframe_explorer(st.session_state.mdf)
        st.dataframe(filtered_df, use_container_width=True)
        if filtered_df is not None:
            st.write(f"Total Rows: {filtered_df.shape[0]}")
            with chart_container(filtered_df):
                columns = st.multiselect("Columns:",filtered_df.columns)
                st.area_chart(filtered_df[columns])
        else:
            st.write(f"Total Rows: 0")
    else:
        st_lottie(url_hib_json,reverse=True,height=None,width=None,speed=1,loop=True,quality='high',key='hib' )

# Diagnostic
#@st.cache
def diagnostic():
    st.markdown("# Diagnostic")
    st.sidebar.markdown("# Diagnostic :stethoscope:")
    
    model_choice = st.selectbox('Choix du modèle',
    ('Augmented Decision Tree', 'Augmented Features Agglomeration LR', 'Augmented XGB','Consensus'))
    if model_choice == 'Augmented Decision Tree':
        with open('predict_dtc.pkl', 'rb') as f:
            model_load = pickle.load(f)
    elif model_choice == 'Augmented Features Agglomeration LR':
        with open('predict_red.pkl', 'rb') as f:
            model_load = pickle.load(f)
    elif model_choice == 'Augmented XGB':
        with open('predict_xgb.pkl', 'rb') as f:
            model_load = pickle.load(f)
    elif model_choice == 'Consensus':
        with open('predict_xgb.pkl', 'rb') as f:
            model_xgb = pickle.load(f)
        with open('predict_red.pkl', 'rb') as f:
            model_red_lr = pickle.load(f)
        with open('predict_dtc.pkl', 'rb') as f:
            model_dt = pickle.load(f)
            
    if st.button('Diagnostiquer la tumeur :stethoscope:'):
        
        if st.session_state.mdf is not None:
            st.success('diagnostic réalisé !')
            malignance = pd.DataFrame(st.session_state.mdf['id'])
            if model_choice != 'Consensus':
                malignance['malignité'] = model_load.predict(st.session_state.mdf)
                malignance['probabilité de maliginité (%)'] = model_load.predict_proba(st.session_state.mdf)[:,1]*100
            else:
                malignance['score_consensus'] = model_dt.predict(st.session_state.mdf) + model_xgb.predict(st.session_state.mdf) + model_red_lr.predict(st.session_state.mdf)   
                malignance['malignité'] = malignance['score_consensus'].apply(lambda x: 'Benin' if x == 0  else 'Malin' if x == 3 else 'Examens complémentaires requis')
            st.dataframe(malignance, use_container_width=True)
    st_lottie(url_robot_json,reverse=True,height=None,width=None,speed=1.5,loop=True,quality='high',key='robot' )
    

page_names_to_funcs = {
    "Présentation": main_page,
    "Upload": upload,
    "Modification des données": data_modification,
    "Saisie manuelle": saisie_manuelle,
    "Data Exploration": exploration,
    "Diagnostic": diagnostic
}

# authentif hash
#hashed_passwords = stauth.Hasher(['karim', 'duia']).generate()
#st.write(hashed_passwords)
with open('configs/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


name, authentication_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Bienvenue *{st.session_state["name"]}*')
    # 1. as sidebar menu
    with st.sidebar:
        selected_page = option_menu("Menu", ["Présentation","Saisie manuelle","Upload","Modification des données","Data Exploration","Diagnostic"], 
            icons=['house','pencil-square','cloud-upload','input-cursor','search','robot'], menu_icon="cast", default_index=0)
            
    #selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

