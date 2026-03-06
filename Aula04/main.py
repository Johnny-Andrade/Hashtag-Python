# Passo a passo

# Título
# Input do chat
    # Mostrar a mensagem que o usuario enviou
    # Pegar a pergunta e enviar para a IA
    # Exibir a resposta na IA na tela

# Usaremos Frameworks, que é um pacote de código com regras a serem seguidas.
# Algum dos principais são: Streamlit, Flask, Django, FastAPI (Usaremos Streamlit)

# No Streamlit, podemos apenas com Python criar o frontend e o backend
# a IA que será usada é: OpenAI (ChatGPT)
# pip install openai streamlit

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

st.write("Danonebot com IA")

texto_usuario = st.chat_input("Digite sua mensagem...")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content) 

if texto_usuario: #Se houver algum texto do usuario (para nao ficar enviando None)
    st.chat_message("user").write(texto_usuario) 
    #pode ser um nome, user(ícone de pessoal), assistant (ícone da IA)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )

    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

print(st.session_state["lista_mensagens"])