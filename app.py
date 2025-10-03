import streamlit as st
from questionario import carregar_faq, responder
from huggingface_qa import responder_com_qa
from previnabot_ist import analisar_imagem

def responder_com_modelo(pergunta, faq):
    alvo = None
    for doenca in faq.keys():
        if doenca.lower() in pergunta.lower():
            alvo = doenca
            break

    if alvo:
        contexto = faq[alvo]
        return responder_com_qa(pergunta, contexto)
    else:
        return "Desculpe, não encontrei informações específicas sobre isso."

st.set_page_config(page_title="PrevinaBot - ISTs", layout="centered")
faq = carregar_faq()
if "ultima_doenca" not in st.session_state:
    st.session_state.ultima_doenca = None

st.markdown("<h2 style='text-align:center; color:#5A2D82;'>PrevinaBot - Chatbot Medicinal<br>para Análise de Casos de IST's</h2>", unsafe_allow_html=True)
st.write("Olá! Seja bem-vindo(a) ao PrevinaBot, seu assistente virtual sobre Infecções Sexualmente Transmissíveis.")

col1, col2 = st.columns(2)
with col1:
    if st.button("QUEM SOU EU?"):
        st.info("Eu sou o PrevinaBot, um chatbot educativo para orientar sobre ISTs. Não substituo avaliação médica.")

with col2:
    if st.button("Principais ISTs"):
        st.info("**Principais ISTs:** HIV, HPV, Sífilis, Gonorreia, Candidíase e Tricomoníase.")

st.subheader("Converse com o PrevinaBot")
pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if pergunta:
        resposta, st.session_state.ultima_doenca = responder(pergunta, faq, st.session_state.ultima_doenca)

        if resposta.startswith("Desculpe") or "Não encontrei" in resposta:
            resposta = responder_com_modelo(pergunta, faq)

        st.markdown(f"**Você:** {pergunta}")
        st.markdown(f"**PrevinaBot:** {resposta}")

st.subheader("Análise de Imagem (Protótipo)")
uploaded_file = st.file_uploader("Envie uma imagem para análise", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resultado = analisar_imagem("temp.jpg")
    st.success(f"**PrevinaBot:** {resultado}")
