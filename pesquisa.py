import requests

def pesquisar_duckduckgo(query: str) -> str:
    url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        if dados.get("AbstractText"):
            return dados["AbstractText"]

        if dados.get("RelatedTopics"):
            for item in dados["RelatedTopics"]:
                if "Text" in item and "FirstURL" in item:
                    return f"{item['Text']} (Fonte: {item['FirstURL']})"

        return "Não encontrei informações relevantes sobre isso."
    
    except Exception as e:
        return f"Ocorreu um erro na pesquisa: {e}"
