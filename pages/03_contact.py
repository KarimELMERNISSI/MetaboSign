
import streamlit as st  # pip install streamlit

st.header(":mailbox: Laissez nous un message")


contact_form = """
<form action="https://formsubmit.co/KARIM.EVASION@GMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Votre nom" required>
     <input type="email" name="email" placeholder="Votre email" required>
     <textarea name="message" placeholder="Votre message"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("./style/style.css")
