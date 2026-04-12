# Projeto Agente IA: Assistente Web Multimodal

Este projeto e um ecossistema de inteligencia artificial desenvolvido em Python, integrando o **Google Gemini (LLM)** com uma interface web interativa. O sistema foi otimizado para oferecer uma experiencia fluida de chat com sintese de voz automatica no navegador.

## 🛠️ Stack Tecnologica & Arquitetura

* **LLM (Large Language Model):** Google Gemini 1.5 Flash.
* **Frontend Web:** Streamlit.
* **Text-to-Speech (Voz):** gTTS (Google Text-to-Speech).
* **Estado/Memoria:** Gestao de contexto via `st.session_state`.
* **Ambiente DevOps:** Rocky Linux, VS Code, Git.

## 📂 Estrutura

* `app.py`: Interface Web moderna com baloes de chat e saida de audio.
* `historico`: Memoria de sessao ativa durante a execucao.

## 🎙️ Memoria e Audio

* **Possui Voz?** Sim. As respostas sao convertidas em audio automaticamente.
* **Armazena Memoria?** Sim. Mantem o contexto enquanto a aba estiver aberta.
* **Persistencia Local:** Nao. Versao focada em performance web.

## 📋 Diario de Troubleshooting (DevOps Mindset)

Durante o desenvolvimento, superei desafios criticos:
1. **API Management:** Logica dinamica para listagem de modelos (Erro 404).
2. **Web Audio:** Injeção HTML5 para autoplay de audio no navegador.
3. **Cota de Requisicoes:** Tratamento de excessoes para Erro 429.
4. **Ambiente:** Correcao de dependencias via terminal (gTTS).

## ⚙️ Como Executar

1. **Dependencias:** `pip install streamlit google-generativeai gTTS`
2. **Chave:** Insira sua API Key na variavel `minha_chave` no codigo.
3. **Executar:** `streamlit run app.py`
