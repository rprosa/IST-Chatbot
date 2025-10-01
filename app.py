from questionario import carregar_faq, responder
from huggingface_qa import responder_com_qa
from previnabot_ist import analisar_imagem

print("=== PrevinaBot - Chatbot sobre ISTs ===")
print("Olá! Seja bem-vindo(a) ao PrevinaBot, seu assistente virtual sobre Infecções Sexualmente Transmissíveis\n")

faq = carregar_faq()
ultima_doenca = None

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

while True:
    pergunta = input("Você: ").lower()

    if pergunta in ["sair", "exit", "quit"]:
        print("PrevinaBot: Obrigado por conversar! Procure sempre orientação médica quando necessário.")

        resposta = input("Você gostaria de enviar uma imagem para análise? (sim/não): ").lower()
        if resposta == "sim":
            caminho = input("Digite o caminho da imagem (ex: C:/Users/.../foto.jpg): ").strip()
            resultado = analisar_imagem(caminho)
            print("PrevinaBot:", resultado)
        break

    resposta, ultima_doenca = responder(pergunta, faq, ultima_doenca)

    if resposta.startswith("Desculpe") or "Não encontrei" in resposta:
        print("PrevinaBot: Tentando responder com IA (Hugging Face)...\n")
        resposta = responder_com_modelo(pergunta, faq)

    print("PrevinaBot:", resposta, "\n")
