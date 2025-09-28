from questionario import carregar_faq, responder
from pesquisa import pesquisar_duckduckgo
from huggingface_qa import responder_com_qa

# Lista de ISTs conhecidas (pode expandir)
IST_LISTA = ["gonorreia", "clamidia", "sifilis", "hpv", "hiv"]

print("=== PrevinaBot - Chatbot sobre ISTs ===")
print("Este chatbot NÃO substitui uma consulta médica.\nDigite 'sair' para encerrar.\n")

faq = carregar_faq()
ultima_doenca = None  # memória simples

while True:
    pergunta = input("Você: ").lower()

    if pergunta in ["sair", "exit", "quit"]:
        print("PrevinaBot: Obrigado por conversar! Procure sempre orientação médica quando necessário.")
        break

    for doenca in IST_LISTA:
        if doenca in pergunta:
            ultima_doenca = doenca
            break

    if ultima_doenca and not any(d in pergunta for d in IST_LISTA):
        pergunta = f"{ultima_doenca} {pergunta}"

    resposta = responder(pergunta, faq)

    # 2️⃣ Se não achou, pesquisa na web
    if resposta.startswith("Desculpe"):
        print("PrevinaBot: Não encontrei no banco local, pesquisando na web...\n")
        resposta = pesquisar_duckduckgo(pergunta)

    # 3️⃣ Se ainda não resolveu, tenta Hugging Face
    if "Não encontrei" in resposta or "Desculpe" in resposta:
        print("PrevinaBot: Tentando responder com IA (Hugging Face)...\n")
        contexto = " ".join(faq.values())  # por enquanto, todo FAQ
        resposta = responder_com_qa(pergunta, contexto)

    print("PrevinaBot:", resposta, "\n")
