from views.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINE_API_KEY"] = PINECONE_API_KEY

extract_data = load_pdf(data = 'medical_data/')
text_chunks = text_split(extract_data)
embeddings = download_hugging_face_embeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medassist"

pc.create_index(
    name = index_name,
    dimension = 384, # Replace with your model dimensions
    metric = "cosine", # Replace with your model metric
    spec = ServerlessSpec(
        cloud = "aws",
        region = "us-east-1"
    ) 
)

# Create a Pinecone vector store from LangChain
docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,  # List of text chunks
    index_name = index_name,  # Pinecone index name
    embedding = embeddings,    # Embedding model
)