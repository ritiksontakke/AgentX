from src.utils.llm import AiModel

def genrate_ans(
        query : str,
        documents : list,
):

    context = "\n\n".join(
        document["content"]
        for document in documents
        if document.get("content")
    )

    prompt = f"""
You are a company knowledge assistant.

Answer the user's question using ONLY
the provided context.

If the answer is not present in the
context, say that the information is
not available in the company documents.

Context:

{context}

Question:

{query}

Answer:
"""

    model = AiModel()
    response = model.invoke(prompt)
    return response.content