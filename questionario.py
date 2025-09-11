import json

# Carrega as informações do FAQ
def carregar_faq(caminho="data/faq.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

# Busca resposta no FAQ
def responder(pergunta, faq):
    for chave, resposta in faq.items():
        if chave in pergunta:
            return resposta
    return "Desculpe, não entendi. Pode reformular?"
