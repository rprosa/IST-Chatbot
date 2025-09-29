from questionario import carregar_faq, responder
from pesquisa import pesquisar_duckduckgo
from huggingface_qa import responder_com_qa

print("=== PrevinaBot - Chatbot sobre ISTs ===")
print("Este chatbot NÃO substitui uma consulta médica.\nDigite 'sair' para encerrar.\n")

faq = carregar_faq()
ultima_doenca = None

while True:
    pergunta = input("Você: ").lower()

    if pergunta in ["sair", "exit", "quit"]:
        print("PrevinaBot: Obrigado por conversar! Procure sempre orientação médica quando necessário.")
        break

    resposta, ultima_doenca = responder(pergunta, faq, ultima_doenca)

    if resposta.startswith("Desculpe"):
        print("PrevinaBot: Não encontrei no banco local, pesquisando na web...\n")
        resposta = pesquisar_duckduckgo(pergunta)

    if "Não encontrei" in resposta or "Desculpe" in resposta:
        print("PrevinaBot: Tentando responder com IA (Hugging Face)...\n")
        contexto = " ".join(faq.values())
        resposta = responder_com_qa(pergunta, contexto)

    print("PrevinaBot:", resposta, "\n")
