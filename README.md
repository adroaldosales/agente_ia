# 🎙️  Projeto Agente IA: Assistente de Voz com Memória Permanente

Este projeto é um ecossistema de inteligência artificial desenvolvido em Python, integrando o **Google Gemini (LLM)** com interfaces de voz e web. O sistema possui memória persistente via JSON, permitindo continuidade nas interações.

## 🛠️  Stack Tecnológica & Arquitetura
* **LLM (Large Language Model):** Google Gemini 1.5 Flash.
* **Frontend Web:** Streamlit.
* **Speech-to-Text:** SpeechRecognition (Google API).
* **Text-to-Speech:** PyTTsx3.
* **Persistência:** Banco de dados documental em JSON.
* **Ambiente DevOps:** Rocky Linux (VM via SSH), VS Code, Git.

## 📂 Estrutura
* `app.py`: Interface Web moderna com balões de chat.
* `assistente.py`: Versão leve para execução via Terminal.
* `historico_memoria.json`: Memória local do agente.

## 📋 Diário de Troubleshooting (DevOps Mindset)
Durante o desenvolvimento, superamos desafios críticos de ambiente:
1. **Versionamento:** Ajuste do Python 3.14 para 3.13 para compatibilidade de drivers de áudio.
2. **Hardware:** Implementação de limpeza de buffer de voz para evitar travamento de microfone no Windows/Linux.
3. **Estado:** Gestão de memória persistente com `st.session_state`.

## ⚙️ Como Executar
1. Instale as dependências: `pip install streamlit google-generativeai speechrecognition pyttsx3 pyaudio`
2. Execute a versão Web: `streamlit run app.py`# Agente_IA
Agente de IA multimodal utilizando LLM Gemini, com interface Web e assistente de voz com memória permanente.

