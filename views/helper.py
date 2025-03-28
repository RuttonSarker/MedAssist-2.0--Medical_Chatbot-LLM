from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


# Extract Data from the PDF file
def load_pdf(data):
    loader = DirectoryLoader(data,
                             glob = "*.pdf",
                             loader_cls = PyPDFLoader)
    documents = loader.load()

    return documents

# split the data text chunks
def text_split(extract_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extract_data)
    return text_chunks

# Download the Embedding from Hugging Face
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    return embeddings