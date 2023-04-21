import streamlit as st

st.set_page_config(
   page_title="Détection de malignité dans les tumeurs de la corticosurénale",
   page_icon=":pill:",
   layout="wide",
   initial_sidebar_state="expanded"
)

# Define some custom CSS styling
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
</style>
""",
unsafe_allow_html=True)

# Create a dictionary to hold the team members' information
team = {
    "Fidéline Bonnet-Serrano": {
        "title": "Cofounder & Med",
        "photo": "https://t4.ftcdn.net/jpg/01/84/92/75/240_F_184927527_K7Q1PFVoQ3QFgRkXGJuAuvYGhbbhaDmk.jpg",
        "bio": "TBD"
    },
    "Christelle Cahen": {
        "title": "Founder & Med",
        "photo": "https://t4.ftcdn.net/jpg/01/84/92/75/240_F_184927527_K7Q1PFVoQ3QFgRkXGJuAuvYGhbbhaDmk.jpg",
        "bio": "TBD"
    },
    "Mathilde Chanut": {
        "title": "Founder & Med",
        "photo": "https://t4.ftcdn.net/jpg/01/84/92/75/240_F_184927527_K7Q1PFVoQ3QFgRkXGJuAuvYGhbbhaDmk.jpg",
        "bio": "TBD"
    },
    "Delphine Cozzone": {
        "title": "Founder & Marketing",
        "photo": "https://t4.ftcdn.net/jpg/01/84/92/75/240_F_184927527_K7Q1PFVoQ3QFgRkXGJuAuvYGhbbhaDmk.jpg",
        "bio": "TDB"
    },
    "Karim El Mernissi": {
        "title": "Founder & Tech",
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


# Create the Streamlit app
def main():
    # Set the page title and header
    #st.set_page_config(page_title="About Us", page_icon=":smiley:")
    st.write("<h1>À propos de Nous</h1><p>Notre équipe:</p>", unsafe_allow_html=True)
    
    # Display a personal card for each team member
    for name in team:
        personal_card(name)

if __name__ == "__main__":
    main()