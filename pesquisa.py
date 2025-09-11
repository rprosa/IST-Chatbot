import requests

def pesquisar_duckduckgo(query: str) -> str:
    """
    Faz uma busca simples no DuckDuckGo e retorna um resumo.
    """
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        # Retorna o resumo se existir
        if dados.get("AbstractText"):
            return dados["AbstractText"]

        # Se não houver resumo, tenta pegar o primeiro tópico relacionado
        if dados.get("RelatedTopics"):
            for item in dados["RelatedTopics"]:
                if "Text" in item:
                    return item["Text"]

        return "Não encontrei informações relevantes sobre isso."
    
    except Exception as e:
        return f"Ocorreu um erro na pesquisa: {e}"
