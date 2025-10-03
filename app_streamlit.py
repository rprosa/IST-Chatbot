import streamlit as st
from questionario import carregar_faq, responder
from huggingface_qa import responder_com_qa
from previnabot_ist import analisar_imagem
import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.markdown("<div class='main-box'><h2>PrevinaBot - Chatbot Medicinal<br>para Análise de Casos de IST's</h2></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='card'>👤 QUEM SOU EU?</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>📖 Principais ISTs</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'>🖼️ Análise de Imagens</div>", unsafe_allow_html=True)


st.set_page_config(page_title="PrevinaBot", page_icon="🧑‍⚕️", layout="centered")

st.title(" PrevinaBot - Chatbot sobre ISTs ")
st.write("Olá! Seja bem-vindo(a) ao PrevinaBot, seu assistente virtual sobre Infecções Sexualmente Transmissíveis")

faq = carregar_faq()
ultima_doenca = None

st.subheader("💬 Diga suas duvidas sobre ISTs:")

if "historico" not in st.session_state:
    st.session_state.historico = []

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    resposta, ultima_doenca = responder(pergunta, faq, ultima_doenca)

    if resposta.startswith("Desculpe") or "Não encontrei" in resposta:
        contexto = " ".join(faq.values())
        resposta = responder_com_qa(pergunta, contexto)

    st.session_state.historico.append((pergunta, resposta))

for p, r in st.session_state.historico:
    st.markdown(f"**Você:** {p}")
    st.markdown(f"**PrevinaBot:** {r}")

st.subheader("Análise de Imagem")
imagem = st.file_uploader("Envie uma imagem para análise", type=["jpg", "jpeg", "png"])

if imagem:
    with open("upload.jpg", "wb") as f:
        f.write(imagem.read())
    resultado = analisar_imagem("upload.jpg")
    st.success("Análise concluída!")
    st.write(resultado)