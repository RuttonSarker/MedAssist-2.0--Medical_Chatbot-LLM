from views.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Lazy initialization for Pinecone and RAG chain
def initialize_pinecone_and_chain():
    load_dotenv()
    PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    os.environ["PINE_API_KEY"] = PINECONE_API_KEY
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # Initialize Pinecone connection only once
    index_name = "medassist"
    
    # Load the embeddings (assuming you have this function)
    embeddings = download_hugging_face_embeddings()

    # Initialize Pinecone VectorStore
    docsearch = PineconeVectorStore.from_existing_index(
        index_name = index_name,
        embedding = embeddings
    )

    # Create retriever and RAG chain
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    llm = OpenAI(temperature=0.4, max_tokens=500)

    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise\n\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("human", "{input}")]
    )

    # Create the RAG chain
    questions_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, questions_answer_chain)

    return docsearch, rag_chain