# generators/data_loader.py
from langchain.document_loaders import TextLoader, PyPDFLoader

def load_capstone_data():
    """
    Loads all documents (TXT, PDF) from capstone_data/docs/
    Returns a list of LangChain Document objects
    """
    docs = []

    # Load text files
    txt_loader = TextLoader("capstone_data/docs/requirement_doc.txt")
    docs.extend(txt_loader.load())

    # Load PDF files
    pdf_loader = PyPDFLoader("capstone_data/docs/project_guidelines.pdf")
    docs.extend(pdf_loader.load())

    return docs