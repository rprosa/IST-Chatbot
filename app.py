from questionario import carregar_faq, responder
from pesquisa import pesquisar_duckduckgo
from huggingface_qa import responder_com_qa
from previnabot_ist import analisar_imagem

print("=== PrevinaBot - Chatbot sobre ISTs ===")
print("Este chatbot NÃO substitui uma consulta médica.\nDigite 'sair' para encerrar.\n")

faq = carregar_faq()
ultima_doenca = None

while True:
    pergunta = input("Você: ").lower()

    if pergunta in ["sair", "exit", "quit"]:
        print("PrevinaBot: Obrigado por conversar! Procure sempre orientação médica quando necessário.")
        escolha = input("Você gostaria de enviar uma imagem para análise? (sim/não): ").lower()
        if escolha == "sim":
            caminho = input("Digite o caminho da imagem: ")
            resultado = analisar_imagem(caminho)
            print("PrevinaBot:", resultado)
        break

    resposta, ultima_doenca = responder(pergunta, faq, ultima_doenca)

    if resposta.startswith("Desculpe"):
        print("PrevinaBot: Não encontrei no banco local, pesquisando na web...\n")
        resposta = pesquisar_duckduckgo(pergunta)

    if "Não encontrei" in resposta or "Desculpe" in resposta:
        print("PrevinaBot: Tentando responder com Hugging Face...\n")
        contexto = " ".join(faq.values())
        resposta = responder_com_qa(pergunta, contexto)

    print("PrevinaBot:", resposta, "\n")
