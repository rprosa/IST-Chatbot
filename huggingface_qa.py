from transformers import pipeline

qa_model = pipeline(
    "question-answering",
    model="pierreguillou/bert-base-cased-squad-v1.1-portuguese",
    tokenizer="pierreguillou/bert-base-cased-squad-v1.1-portuguese"
)

def responder_com_qa(pergunta: str, contexto: str) -> str:
    """
    Usa o modelo Hugging Face para responder com base em um contexto.
    """
    try:
        resposta = qa_model(question=pergunta, context=contexto)
        return resposta["answer"]
    except Exception as e:
        return f"Erro ao usar modelo Hugging Face: {e}"
