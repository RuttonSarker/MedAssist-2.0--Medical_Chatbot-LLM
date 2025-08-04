import streamlit as st
import re  # Import the regular expression module
from dotenv import load_dotenv
import os
from views.open_ai import initialize_pinecone_and_chain
import time
import string
from fuzzywuzzy import fuzz

# Load environment variables from the .env file
load_dotenv()

# Cache Pinecone and RAG initialization to avoid reloading every time
@st.cache_resource
def initialize_pinecone_and_chain_cached():
    docsearch, rag_chain = initialize_pinecone_and_chain()
    return docsearch, rag_chain

# Function to validate email format
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

# Normalize the text by converting it to lowercase and removing punctuation
def normalize_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Fuzzy matching for user input to handle typos or minor variations
def fuzzy_match(query, user_input, threshold=80):
    score = fuzz.partial_ratio(query, user_input)
    return score >= threshold  # Return True if the match is above the threshold

def login():
    st.subheader("🔐 Login")
    email = st.text_input("Email Address", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if not email and not password:
            st.error("Both email and password fields must be filled!")
        elif not email:
            st.error("Please enter an email address.")
        elif not password:
            st.error("Please enter a password.")
        elif not is_valid_email(email):
            st.error("Please enter a valid email address (e.g., example@gmail.com).")
        else:
            # Load the emails and passwords from .env
            emails = os.getenv("USER_EMAILS").split(",")  # Split the emails into a list
            passwords = os.getenv("USER_PASSWORDS").split(",")  # Split the passwords into a list

            # Check if email exists in the list and password matches the same index
            if email in emails:
                email_index = emails.index(email)
                if password == passwords[email_index]:
                    st.session_state.logged_in = True
                    st.success("Login successful!")
                    st.rerun()  # Redirect to chatbot page
                else:
                    st.session_state.logged_in = False
                    st.error("Invalid credentials")
            else:
                st.session_state.logged_in = False
                st.error("Invalid email address")

    st.markdown("Note: For testing purpose only, selected users can log in. Register will be available soon.")

def show_login():
    login()

def chatbot():
    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        show_login()
        return

    st.title("֎ MedAssist 2.0")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'initialized' not in st.session_state:
        st.session_state.initialized = False

    with st.spinner("Vector DB is loading..."):
        docsearch, rag_chain = initialize_pinecone_and_chain_cached()
        st.session_state.rag_chain = rag_chain

    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.chat_message(message['role']).markdown(f"<div style='background-color: #2774DE; padding: 10px; border-radius: 5px;'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.chat_message(message['role']).markdown(f"<div style='text-align: justify;'>{message['content']}</div>", unsafe_allow_html=True)

    prompt = st.chat_input("Ask your medical query here")

    greetings = ["hi", "hello", "how are you", "hey", "good morning", "good evening"]
    farewells = ["goodbye", "bye", "thank you", "see you", "take care", "later"]
    assistant_queries = ["who are you", "tell me about yourself"]

    if prompt:
        user_input = normalize_text(prompt)

        st.chat_message('user').markdown(f"<div style='background-color: #2774DE; padding: 10px; border-radius: 5px;'>{prompt}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        # Check if the user input contains any greeting using fuzzy matching
        if any(fuzzy_match(normalize_text(greeting), user_input) for greeting in greetings):
            response = "Hello! How can I assist you today?"
            st.session_state.messages.append({'role': 'assistant', 'content': response})
            st.chat_message('assistant').markdown(f"<div style='text-align: justify;'>{response}</div>", unsafe_allow_html=True)
        
        # Check if the user input contains any farewell using fuzzy matching
        elif any(fuzzy_match(normalize_text(farewell), user_input) for farewell in farewells):
            response = "Take care and feel free to come back anytime."
            st.session_state.messages.append({'role': 'assistant', 'content': response})
            st.chat_message('assistant').markdown(f"<div style='text-align: justify;'>{response}</div>", unsafe_allow_html=True)
        
        # Check if the user input is about the assistant using fuzzy matching
        elif any(fuzzy_match(normalize_text(query), user_input) for query in assistant_queries):
            response = "I am MedAssist, an AI assistant here to help you with medical-related queries. How can I assist you today?"
            st.session_state.messages.append({'role': 'assistant', 'content': response})
            st.chat_message('assistant').markdown(f"<div style='text-align: justify;'>{response}</div>", unsafe_allow_html=True)
        
        else:
            start_time = time.time()
            with st.spinner("Thinking..."):
                response = st.session_state.rag_chain.invoke({"input": prompt})

                answer = response.get("answer", None)

                if not answer or answer.strip() == "":
                    answer = "Sorry, I couldn't find an answer for that."

                response_time = round(time.time() - start_time, 2)

                st.session_state.messages.append({'role': 'assistant', 'content': answer + f"\n\nResponse time: {response_time} seconds"})

            st.chat_message('assistant').markdown(f"<div style='text-align: justify;'>{answer} <br> <small>Response Time: {response_time} seconds</small></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    chatbot()