from fuzzywuzzy import process
import json

def carregar_faq(caminho="data/faq.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def responder(pergunta, faq):
    melhor_match, score = process.extractOne(pergunta, faq.keys())
    if score > 60:
        return faq[melhor_match]
    return "Desculpe, não entendi. Pode reformular?"
