from questionario import carregar_faq, responder
from pesquisa import pesquisar_duckduckgo

print("=== PrevinaBot - Chatbot sobre ISTs ===")
print("Este chatbot NÃO substitui uma consulta médica.\nDigite 'sair' para encerrar.\n")

faq = carregar_faq()

while True:
    pergunta = input("Você: ").lower()
    
    if pergunta in ["sair", "exit", "quit"]:
        print("PrevinaBot: Obrigado por conversar! Procure sempre orientação médica quando necessário.")
        break
    
    resposta = responder(pergunta, faq)
    
    if resposta.startswith("Desculpe"):
        print("PrevinaBot: Não encontrei no banco local, pesquisando na web...\n")
        resposta = pesquisar_duckduckgo(pergunta)
    
    print("PrevinaBot:", resposta, "\n")