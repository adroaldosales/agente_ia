import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import time
import json
import os

# 1. Configuração da API
genai.configure(api_key="AIzaSyB-U_Q3Y3kje9nA5iWI7KWjX3V2VLp8fS0")
modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
model = genai.GenerativeModel(modelos[0])

# --- ARQUIVO DE MEMÓRIA ---
ARQUIVO_HISTORICO = "historico_memoria.json"

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_historico(historico):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=4)

# Inicia o chat com o que estiver salvo no HD
historico_salvo = carregar_historico()
chat = model.start_chat(history=historico_salvo)

def falar(texto):
    print(f"Assistente: {texto}")
    texto_limpo = texto.replace('*', '').replace('-', '')
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    
    voices = engine.getProperty('voices')
    for voice in voices:
        if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(texto_limpo)
    engine.runAndWait()
    engine.stop()
    del engine 
    time.sleep(0.5)

def ouvir():
    rec = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("\nOuvindo...")
        rec.adjust_for_ambient_noise(fonte, duration=1)
        audio = rec.listen(fonte)
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except:
        return ""

falar("Olá Adroaldo, tudo bem? Em que posso ajudar?")

while True:
    comando = ouvir()
    if comando:
        if "sair" in comando.lower():
            falar("Até logo, Adroaldo!")
            break
        
        try:
            response = chat.send_message(comando)
            falar(response.text)
            
            # Atualiza o arquivo no HD após cada resposta
            salvar_historico(chat.history) 
            
        except Exception as e:
            print(f"Erro: {e}")