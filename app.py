import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import json
import os

# 1. Configuração Básica
st.set_page_config(page_title="Assistente Adroaldo")
st.title("🎙️ Assistente de Voz Web")

# 2. Configuração IA
genai.configure(api_key="Sua chave aqui")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- ESTE BLOCO TEM QUE APARECER ---
st.subheader("Interaja aqui:")
texto_usuario = st.text_input("Digite sua mensagem e dê ENTER")
botao_falar = st.button("🎤 Ativar Microfone")

if texto_usuario:
    st.write(f"Você digitou: {texto_usuario}")
    # Aqui vai a lógica de enviar para o Gemini depois que o campo aparecer
# ----------------------------------

st.divider()
st.info("O histórico aparecerá abaixo assim que você enviar uma mensagem.")