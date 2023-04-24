import streamlit as st

st.set_page_config(
    page_title="Contactez-nous",
    page_icon=":mailbox_with_mail:",
    layout="wide"
)

# Define contact form HTML
contact_form_html = """
<h1>Contactez-nous</h1>
<div class="form-container">
    <h2>Prise de contact</h2>
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
</style>
""", unsafe_allow_html=True)

# Display contact form
st.markdown(contact_form_html, unsafe_allow_html=True)
