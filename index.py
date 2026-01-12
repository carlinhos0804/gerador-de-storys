import streamlit as st
import google.generativeai as genai

# Configuração da página para parecer um App de celular
st.set_page_config(page_title="Gemini App", page_icon="🤖")

st.title("📱 Meu Gemini Nativo")

# Configurar a chave API (vamos usar o 'Secrets' do Streamlit depois)
if "API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["API_KEY"])
else:
    st.error("Chave API não configurada nos Secrets do Streamlit.")

model = genai.GenerativeModel('gemini-1.5-flash')

# Histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada
if prompt := st.chat_input("Como posso ajudar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta do Gemini
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
