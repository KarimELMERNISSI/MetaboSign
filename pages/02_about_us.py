import streamlit as st
import requests
from io import BytesIO
from PIL import Image

img_content = requests.get("https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/metabosign_icon.png?raw=true").content
img = Image.open(BytesIO(img_content))

st.set_page_config(
   page_title="MetaboSign & Nous",
   page_icon=img,
   layout="wide",
   initial_sidebar_state="expanded"
)

# Define some custom CSS styling
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
    font-size: 2em;
    color: #1F618D;
    text-align: center;
}

p {
    font-size: 1.2em;
    color: #2C3E50;
    margin-bottom: 30px;
    text-align: center;
}

.personal-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.metabosign2-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: justify;
}

.metabosign2-card .image-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    text-align: center;
}

.metabosign2-card img {
    border-radius: 50%;
    max-width: 200px;
    display: block;
    margin: auto;
}

.metabosign-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: justify;
}

.metabosign-card img {
    border-radius: 50%;
    margin-bottom: 20px;
    max-width: 200px;
}

.metabosign2-card p {
    margin-bottom: 0;
    font-size: 1.2em;
    color: #2C3E50;
    text-align: justify;
}

.personal-card img {
    border-radius: 50%;
    margin-bottom: 20px;
    max-width: 200px;
}

.personal-card h2 {
    margin-top: 0;
    font-size: 1.5em;
    color: #1F618D;
}

.personal-card p {
    margin-bottom: 0;
    font-size: 1.2em;
    color: #2C3E50;
}

#MainMenu {
    visibility: hidden;
}

footer {
	visibility: hidden;
}
</style>
""",
unsafe_allow_html=True)

# Create a dictionary to hold the team members' information
team = {
    "Fidéline Bonnet-Serrano": {
        "title": "Co-founder & Med",
        "photo": "https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/Fideline.jpg?raw=true",
        "bio": "TBD"
    },
    "Christelle Cahen": {
        "title": "Co-Founder & industry",
        "photo": "https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/Christelle.jpg?raw=true",
        "bio": "TBD"
    },
    "Mathilde Chanut": {
        "title": "Co-Founder & Med",
        "photo": "https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/Mathilde.jpg?raw=true",
        "bio": "TBD"
    },
    "Delphine Cozzone": {
        "title": "Co-Founder & Industry",
        "photo": "https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/Delphine.jpg?raw=true",
        "bio": "TDB"
    },
    "Karim El Mernissi": {
        "title": "Co-Founder & Tech",
        "photo": "https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/linkedin_pic.jpg?raw=true",
        "bio": "TBD"
    }
}

def personal_card(name):
    # Get the team member's information from the dictionary
    title = team[name]['title']
    photo = team[name]['photo']
    bio = team[name]['bio']
    
    # Create a card to display the team member's information
    st.write(f"<div class='personal-card'><img src='{photo}'><h2>{name}</h2><p>{title}</p><p>{bio}</p></div>", unsafe_allow_html=True)

def company_card():
    # Get the team member's information from the dictionary
    photo1 = "https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/metabosign.jpg?raw=true"
    photo2 = "https://github.com/KarimELMERNISSI/MetaboSign/blob/main/images/UniversiteParisCite_logo_horizontal_couleur_RVB.jpg?raw=true"
    description = """
        MetaboSign est spécialisée dans l'identification de profil métabolomique sérique par LC-MS/MS et investit continuellement en R&D pour identifier d'autres applications suite à ce premier outil. 
        Le choix de notre modèle économique tient compte d'une part des perspectives de développement de MetaboSign, et d'autre part, du nombre restreint de clients potentiels pour l'outil diagnostic des corticosurrénalomes puisque l'on estime à une trentaine, le nombre de laboratoires équipés de LC-MS/MS en France."""
    
    # Create a card to display the team member's information
    #st.write(f"<div class='metabosign-card'><img src='{photo1}'><p>{description}</p></div>", unsafe_allow_html=True)
    st.write(f"""
    <div class='metabosign2-card'>
        <div class="image-container">
            <img src='{photo1}' alt="MetaboSign">
            <img src='{photo2}' alt="Université Paris-Cité">
        </div>
        <p>{description}</p>
    </div>""", unsafe_allow_html=True)

# Create the Streamlit app
def about_us():
    # Set the page title and header
    #st.set_page_config(page_title="About Us", page_icon=":smiley:")
    st.write("""
            <h1>À propos de Nous</h1>""", unsafe_allow_html=True)
    company_card()     
    st.write("""<h2>Notre équipe</h2>""", unsafe_allow_html=True)
    
    # Display a personal card for each team member
    for name in team:
        personal_card(name)

about_us()