import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
st.set_page_config(page_title="Chatbot Anglais", page_icon="🇬🇧")
st.title(" Chatbot pour apprendre l’anglais ")

# Entrée utilisateur
question = st.text_input("Pose ta question sur la grammaire, le vocabulaire ou les expressions anglaises :")
# Chargement de la clé OpenAI (via secrets)
openai_api_key = st.secrets["OPENAI_API_KEY"]

# LangChain - LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_api_key)

# Prompt LangChain
prompt = PromptTemplate(
    input_variables=["question"],
    template="Tu es un professeur d’anglais patient et sympathique. Réponds à cette question : {question}"
)

# Chaîne LangChain
chain = LLMChain(llm=llm, prompt=prompt)

# Exécution
if question:
    with st.spinner("Le professeur réfléchit... 🧠"):
        response = chain.run(question)
        st.write("✏️ Réponse :", response)



