import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import json
import os

# Configuração da Página
st.set_page_config(page_title="Assistente Adroaldo", page_icon="🎙️")
st.title("🎙️ Assistente de Voz Web")

# Configuração IA
genai.configure(api_key="AIzaSyB-U_Q3Y3kje9nA5iWI7KWjX3V2VLp8fS0")
model = genai.GenerativeModel('gemini-1.5-flash')

# Memória
ARQUIVO_HISTORICO = "historico_memoria.json"

if "chat" not in st.session_state:
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            historico = json.load(f)
    else:
        historico = []
    st.session_state.chat = model.start_chat(history=historico)

# Interface
for msg in st.session_state.chat.history:
    with st.chat_message("user" if msg.role == "user" else "assistant"):
        st.write(msg.parts[0].text)

if st.button("🎤 Falar agora"):
    rec = sr.Recognizer()
    with sr.Microphone() as fonte:
        st.toast("Ouvindo...")
        try:
            audio = rec.listen(fonte, timeout=5)
            pergunta = rec.recognize_google(audio, language="pt-BR")
            st.chat_message("user").write(pergunta)
            
            response = st.session_state.chat.send_message(pergunta)
            with st.chat_message("assistant"):
                st.write(response.text)
                
            # Salvar Memória
            with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
                json.dump(st.session_state.chat.history, f, ensure_ascii=False, indent=4)
        except:
            st.error("Não ouvi nada ou erro de conexão.")