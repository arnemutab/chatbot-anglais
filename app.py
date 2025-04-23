import streamlit as st
import os
st.set_page_config(page_title="Chatbot Anglais", page_icon="🇬🇧")
st.title(" Chatbot pour apprendre l’anglais ")

# Entrée utilisateur
def chatbot():
    st.write ("Bot: Bonjour,Je suis ton assisant virtuel,tape 'quit' pour quitter ")
    while True :
        user=st.text_input("vous:").lower()

        if user=="quit":
            st.write("Bot: À bientôt ! 👋")
            break
        elif "bonjour" in user:
            st.write("Bot: Bonjour à toi aussi")
        elif "Comment ça va" in user:
            st.write("Bot: Je vais bien, merci. Et toi ?")
        elif "ton nom" in user:
            st.write("Bot:je m'appelle botos")
        else :
            st.write("Bot: Désolé, je n'ai pas compris. 😕")

chatbot()



