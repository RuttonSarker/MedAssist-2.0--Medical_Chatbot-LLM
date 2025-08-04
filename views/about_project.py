import streamlit as st

def about_project():
    st.title("📘 About MedAssist 2.0")

    st.header("🔍 Project Overview")

    st.markdown("""
MedAssist 2.0 is an AI-powered medical chatbot developed using **OpenAI’s GPT models** (like **GPT-4o**) 
via the ChatGPT API. It is integrated with a cloud-based **semantic retrieval system** to provide real-time,
reliable medical responses to users. Unlike traditional LLMs like **BioGPT** or **BioBERT**, this project utilizes
**ChatGPT's general-purpose fluency** combined with **vector-based document search** to ensure both relevance and 
accuracy. The system is built using modern **cloud technologies** and **NLP libraries** to ensure speed, scalability, 
and responsiveness.

The chatbot is designed to:

- Provide instant, natural-language responses to health-related queries  
- Help reduce patient wait times  
- Support doctors by answering common medical questions  
- Scale globally through cloud deployment  
""")
    
    st.header("🧰 Tools & Technologies")

    st.subheader("🔤 Language & Frameworks")
    st.markdown("""
- **Programming Language**: Python
- **Web Interface**: Streamlit (`streamlit==1.40.1`)
    """)

    st.subheader("🧠 LLM & NLP")
    st.markdown("""
- **ChatGPT API** via OpenAI (`langchain_openai==0.3.10`)
- **LangChain Framework** (`langchain==0.3.21`)
- **Hugging Face Integration** (`langchain_huggingface==0.1.2`)
- **Sentence Embeddings** via `sentence-transformers==3.4.1`
- **Fuzzy Matching** using `fuzzywuzzy==0.18.0`
    """)

    st.subheader("📦 Vector Search & RAG")
    st.markdown("""
- **Pinecone Vector DB** (`langchain_pinecone==0.2.3`)
- **LangChain Retriever Chain** for RAG logic
- **dotenv config** (`python-dotenv==0.21.0`)
    """)

    st.subheader("☁️ Cloud Infrastructure")
    st.markdown("""
- **Docker** for containerization
- **AWS EC2 / ECR / Lambda** for scalable deployment
    """)

    st.header("⚙️ How It Works")

    with st.expander("📖 Phase 1: Data Embedding"):
        st.markdown("""
- Medical content is chunked and converted into embeddings using Sentence Transformers
- Stored in **Pinecone** for fast vector search
        """)

    with st.expander("🔍 Phase 2: Semantic Retrieval"):
        st.markdown("""
- User input is embedded and matched against the Pinecone index
- Top 3 similar documents are selected as context
        """)

    with st.expander("💬 Phase 3: Response Generation (GPT-4o)"):
        st.markdown("""
- Retrieved context + user query is sent to **ChatGPT (GPT-4o)**
- The model generates a concise, patient-friendly response
        """)

    with st.expander("☁️ Cloud Deployment"):
        st.markdown("""
- Code is containerized via Docker
- Hosted on **AWS EC2**
- Uses **Lambda** for auto-scaling and background tasks
- Accessible globally via public endpoint
        """)

    st.header("📈 Results & Benefits")
    st.markdown("""
- ✅ AI-powered assistant with real medical context  
- ✅ Fast, accurate, and natural responses  
- ✅ Easy to deploy and scale  
- ✅ Continuously improving via vector updates and model enhancements  
    """)

    st.caption("Built by Rutton Chandra Sarker 👩🏻‍💻 using OpenAI, LangChain, Pinecone, and Streamlit")

# 🔥 CALL the function to display content
about_project()