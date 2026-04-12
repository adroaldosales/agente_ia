import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64
from io import BytesIO

# 1. Configuração Visual
st.set_page_config(page_title="Assistente Adroaldo", page_icon="🎙️")
st.title("🎙️ Assistente Adroaldo")

# Função para a Voz funcionar no Navegador
def falar(texto):
    try:
        tts = gTTS(text=texto, lang='pt', tld='com.br')
        fp = BytesIO()
        tts.write_to_fp(fp)
        b64 = base64.b64encode(fp.getvalue()).decode()
        md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# 2. Configuração da API (Corrigida e Unificada)
minha_chave = "SUA CHAVE AQUI" # Sua chave aqui

try:
    genai.configure(api_key=minha_chave)
    
    # Busca os modelos disponíveis para evitar o Erro 404
    modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    nome_modelo = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in modelos else modelos[0]
    
    model = genai.GenerativeModel(nome_modelo)
    # st.success(f"Conectado ao modelo: {nome_modelo}") # Opcional: mostra que conectou
except Exception as e:
    st.error(f"Erro na conexão: {e}")

# 3. Memória do Chat
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# 4. Entrada de texto
entrada = st.chat_input("Diga algo para a IA, Adroaldo...")

if entrada:
    st.session_state.mensagens.append({"role": "user", "content": entrada})
    with st.chat_message("user"):
        st.write(entrada)

    try:
        response = model.generate_content(entrada)
        resposta_final = response.text
        
        st.session_state.mensagens.append({"role": "assistant", "content": resposta_final})
        with st.chat_message("assistant"):
            st.write(resposta_final)
        
        # Faz o robô falar!
        falar(resposta_final)
        
    except Exception as e:
        if "429" in str(e):
            st.error("Cota cheia! Aguarde 1 minuto e tente de novo.")
        else:
            st.error(f"Erro: {e}")