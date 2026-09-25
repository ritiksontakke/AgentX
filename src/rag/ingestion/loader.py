from langchain_community.document_loaders import PyMuPDFLoader

def load_pdf(file_Path:str):

    loader = PyMuPDFLoader(
        file_Path
    )

    document = loader.load()

    return document