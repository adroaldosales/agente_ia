# Projeto Agente IA: Assistente com chat e saída de voz

Este projeto tem como objetivo utilizar a IA Gemini para para interação, há um campo onde você realiza a interação e a IA responde em texto e com áudio, foi desenolvido usando a linguagem  Python, integrando o **Google Gemini (LLM)** com uma interface web bem simples e funcional no navegador.

## Tecnologias utilizadas:

* **LLM (Large Language Model):** Google Gemini 1.5 Flash.
* **Frontend Web:** Streamlit.
* **Text-to-Speech (Voz):** gTTS (Google Text-to-Speech).
* **Estado/Memoria:** Gestao de contexto via `st.session_state`.
* **Ambiente DevOps:** Rocky Linux, VS Code, Git.

## Estrutura

* `app.py`: Interface Web simples e funcional com chat e saida de audio.
* `historico`: Memoria de sessao ativa durante a execucao.

## Memoria e Audio

* **Possui Voz?** Sim. As respostas sao convertidas em audio automaticamente.
* **Armazena Memoria?** Sim. Mantem o historico da convesa enquanto a aba estiver aberta.
* **Persistencia Local:** Nao. Versao focada em performance web.

##  Desafios encontrados, o tão famoso "Troubleshooting"

Durante o desenvolvimento, superei desafios criticos:
1. **API Management:** Enfrentei problemas com (Erro 404).
2. **Web Audio:** Injeção HTML5 para autoplay de audio no navegador.
3. **Cota de Requisicoes:** Como estou usando uma versão gratuita, a IA impõe limitações de uso com o  Erro 429.
4. **Ambiente:** Tive dificuldade com o audio, recorri a algumas dependencias do gTTS até conseguir que funcionasse a correcão.

## Para executar

1. **Dependencias:** Execute no terminal este comando `pip install streamlit google-generativeai gTTS`
2. **Chave:** Por boas práticas eu removi a chave API do código, então será necessário adicionar uma nova no endereço a seguir [Google AI Studio](https://aistudio.google.com/app/apikey) e insira na variável `minha_chave` no código.
3. **Executar:** Execute este comando no terminal para abrir a pagina web `streamlit run app-final.py``
