from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from ollama import chat

db = Chroma(
    persist_directory="db",
    embedding_function=OllamaEmbeddings(
        model="nomic-embed-text"
    )
)

while True:

    question = input("Ask: ")

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [d.page_content for d in docs]
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {question}
    """

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(
        "\nAnswer:\n",
        response["message"]["content"]
    ) 
    