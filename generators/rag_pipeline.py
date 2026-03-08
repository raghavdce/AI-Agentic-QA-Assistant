# rag_pipeline.py

import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Loaders
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader, UnstructuredWordDocumentLoader

def prepare_rag_pipeline(data_folder="./data", persist_dir="./chroma_db", chunk_size=1000, chunk_overlap=100):
    """
    Prepares the RAG pipeline:
    - Loads documents from PDFs, Word docs, and text files
    - Splits into chunks
    - Builds a Chroma vectorstore and retriever
    """

    docs = []

    # Loop through all files in the data folder
    for file_name in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file_name)

        try:
            if file_name.lower().endswith(".pdf"):
                loader = PyPDFLoader(file_path)
                loaded_docs = loader.load()
            elif file_name.lower().endswith(".docx"):
                loader = UnstructuredWordDocumentLoader(file_path)
                loaded_docs = loader.load()
            elif file_name.lower().endswith(".txt"):
                loader = TextLoader(file_path, encoding="utf-8")
                loaded_docs = loader.load()
            else:
                print(f"Skipping unsupported file type: {file_name}")
                continue

            docs.extend(loaded_docs)
            print(f"Loaded {len(loaded_docs)} documents from {file_name}")

        except Exception as e:
            print(f"Skipping invalid file {file_name}, reason: {e}")

    if not docs:
        raise ValueError("No valid documents found in the data folder!")

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    docs_split = text_splitter.split_documents(docs)
    print(f"Total document chunks created: {len(docs_split)}")

    # Create embeddings
    embeddings = OpenAIEmbeddings()

    # Build Chroma vectorstore
    vectorstore = Chroma.from_documents(
        docs_split,
        embeddings,
        persist_directory=persist_dir
    )

    # Persist the vectorstore
    vectorstore.persist()
    print(f"Vectorstore persisted at: {persist_dir}")

    # Create retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return vectorstore, retriever