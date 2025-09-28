from fuzzywuzzy import process
import json

def carregar_faq(caminho="data/faq.json"):
    """Carrega o FAQ em formato JSON"""
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def responder(pergunta, faq):
    """
    Busca a melhor resposta no FAQ usando fuzzy matching.
    Retorna resposta se confiança > 60, senão avisa que não entendeu.
    """
    melhor_match, score = process.extractOne(pergunta, faq.keys())
    
    if score > 60:
        return faq[melhor_match]
    
    return "Desculpe, não encontrei uma resposta clara para sua pergunta."
