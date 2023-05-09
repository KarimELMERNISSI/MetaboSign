import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

img_content = requests.get("https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/metabosign_icon.png?raw=true").content
img = Image.open(BytesIO(img_content))

univ_img_content = requests.get("https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/up-metabosign.png?raw=true").content
univ_img = Image.open(BytesIO(univ_img_content))

st.set_page_config(
    page_title="Contactez-nous",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define contact form HTML
contact_form_html = """
<div class="form-container">
    <h2>Contactez-nous</h2>
    <p>Remplissez le formulaire ci-dessous pour nous envoyer un message.</p>
    <form action="https://formsubmit.co/KARIM.EVASION@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Votre nom" required>
        <input type="email" name="email" placeholder="Votre email" required>
        <textarea name="message" placeholder="Votre message"></textarea>
        <input type="submit" value="Envoyer">
    </form>
</div>      
"""

# Define CSS styling
st.markdown("""
<style>
h1 {
    font-family: 'Arial Black', sans-serif;
    font-size: 3em;
    color: #1F618D;
    margin-bottom: 30px;
    text-align: center;
}

p {
    font-size: 1.2em;
    color: #2C3E50;
    margin-bottom: 30px;
    text-align: center;
}

psidebar {
    font-size: 1.1em;
    color: #2C3E50;
    margin-bottom: 30px;
    text-align: left;
}

.form-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 30px;
    background-color: #f5f5f5;
    border-radius: 10px;
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
}

.form-container h2 {
    font-size: 32px;
    margin-bottom: 20px;
    text-align: center;
}

.form-container p {
    font-size: 18px;
    margin-bottom: 30px;
    text-align: center;
}

.form-container input[type=text],
.form-container input[type=email],
.form-container textarea {
    display: block;
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    background-color: #f9f9f9;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.form-container input[type=submit] {
    display: block;
    width: 100%;
    padding: 10px;
    margin-top: 30px;
    font-size: 18px;
    font-weight: bold;
    color: #fff;
    background-color: #3f51b5;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.form-container input[type=submit]:hover {
    background-color: #2c3e50;
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
""", unsafe_allow_html=True)

st.markdown("""<h1>Vous avez des suggestions - Accès réservé aux étudiants du DU d'IA appliquée en santé</h1>""", unsafe_allow_html=True)

with open('./configs/config.yaml') as file:
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

    # Display contact form
    st.markdown(contact_form_html, unsafe_allow_html=True)

#st.sidebar.header("MetaboSign")
st.sidebar.image(univ_img,use_column_width='auto')
st.sidebar.markdown(
"""
<psidebar>
Ce dispositif médical est en cours de développement dans le cadre d'un projet de recherche du DU d'intelligence artificielle appliquée et n'a fait l'objet d'aucune évaluation clinique, ni réglementaire, ni juridique et son usage est exclusivement confidentiel. <br>
Son utilisation, quelle qu'en soit sa nature, ne peut engager la responsabilité de ses créateurs. <br>
Cet outil est la propriété intellectuelle des auteurs. <br>
Toute contrefaçon, plagiat, reproduction illicite est interdite. <br>
L'Université de Paris Cité n'entend donner aucune approbation ou improbation à cette production qui doit être considérée comme propre à leurs auteurs.
</psidebar>
""",unsafe_allow_html=True)

