import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = []
corpus_path = "corpus/"

for file in os.listdir(corpus_path):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(corpus_path, file), encoding="utf-8")
        docs = loader.load()
        documents.extend(docs)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
split_docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(split_docs, embedding_model)
vectorstore.save_local("vectorstore")
