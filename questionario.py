import json
from fuzzywuzzy import process

IST_LISTA = ["clamidia", "gonorreia", "sifilis", "hpv", "hiv"]

INTENCOES = {
    "sintomas": ["sintomas", "sinais", "quais sintomas", "o que causa"],
    "transmissao": ["transmissao", "transmitida", "como pega", "como transmite", "como passa"],
    "tratamento": ["tratamento", "cura", "remedio", "como tratar"],
    "medico": ["medico", "doutor", "quem trata"],
    "prevencao": ["prevenir", "evitar", "proteger"]
}

def carregar_faq(caminho="data/faq.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def identificar_doenca(pergunta: str):
    for d in IST_LISTA:
        if d in pergunta:
            return d
    return None

def identificar_intencao(pergunta: str):
    for chave, termos in INTENCOES.items():
        for termo in termos:
            if termo in pergunta:
                return chave
    return None

def responder(pergunta: str, faq: dict, ultima_doenca=None):
    pergunta = pergunta.lower()


    doenca = identificar_doenca(pergunta)
    if doenca:
        ultima_doenca = doenca
    else:
        doenca = ultima_doenca

    intencao = identificar_intencao(pergunta)

    if doenca and intencao:
        chave = f"{doenca} {intencao}"
        if chave in faq:
            return faq[chave], ultima_doenca

    melhor_match, score = process.extractOne(pergunta, faq.keys())
    if score > 70:
        return faq[melhor_match], ultima_doenca

    return "Desculpe, não encontrei informações específicas sobre isso.", ultima_doenca
