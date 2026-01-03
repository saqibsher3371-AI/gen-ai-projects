from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    document = loader.load()
    textsplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = textsplitter.split_documents(document)
    return docs
