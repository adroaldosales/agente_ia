import streamlit as st
import google.generativeai as genai

# Configuração simples
st.set_page_config(page_title="Assistente Adroaldo")
st.title("🎙️ Assistente de Voz Web")

# Configura IA
genai.configure(api_key="Sua chave aqui")
model = genai.GenerativeModel('gemini-1.5-flash')

# BARRA DE TEXTO - Se isso não aparecer, o arquivo não salvou!
texto = st.chat_input("Digite aqui, Adroaldo!")

if texto:
    with st.chat_message("user"):
        st.write(texto)
    
    response = model.generate_content(texto)
    
    with st.chat_message("assistant"):
        st.write(response.text)