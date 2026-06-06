from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

loader = PyPDFLoader("pdfs/notes.pdf")

docs = loader.load()

vectorstore = Chroma.from_documents(
    docs,
    OllamaEmbeddings(model="nomic-embed-text"),
    persist_directory="db"
)

print("PDF indexed successfully")