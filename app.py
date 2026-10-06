import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_faiss import FAISS


# -----------------------------
# Page
# -----------------------------







with st.sidebar:
    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("""
    ### How it works

    1. 📄 Add a transcript
    2. 🧩 Split into chunks
    3. 🧠 Create embeddings
    4. 🔎 Retrieve relevant content
    5. 🤖 Generate an answer

    ### Tech Stack

    Gemini • LangChain • FAISS • Streamlit
    """)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🎥 YouTube RAG Assistant")
st.caption("Ask questions about a YouTube video's transcript")


# -----------------------------
# API Key
# -----------------------------

api_key = st.text_input(
    "Google Gemini API Key",
    type="password"
)

if not api_key:
    st.info("Enter your Gemini API key to continue.")
    st.stop()


# -----------------------------
# Transcript
# -----------------------------

transcript = st.text_area(
    "Paste the YouTube transcript here",
    height=300,
    placeholder="Paste your transcript..."
)


# -----------------------------
# Process transcript
# -----------------------------

if st.button("Process Transcript"):

    if not transcript.strip():
        st.error("Please paste a transcript.")
        st.stop()

    with st.spinner("Processing transcript..."):

        documents = [
            Document(page_content=transcript)
        ]

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=api_key
        )

        vector_store = FAISS.from_documents(
            chunks,
            embeddings
        )

        llm = ChatGoogleGenerativeAI(
            model="gemini-3.6-flash",
            google_api_key=api_key
        )

        retriever= vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

        st.session_state.vector_store = vector_store
        st.session_state.retriever = retriever
        st.session_state.llm = llm
        st.session_state.processed = True

    st.success(f"✅ Transcript processed into {len(chunks)} chunks!")


# -----------------------------
# Question answering
# -----------------------------

# -----------------------------
# Question answering
# -----------------------------

if st.session_state.get("processed", False):

    st.divider()

    st.subheader("💬 Ask about the video")

    # Display previous chat messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    question = st.chat_input(
        "Ask something about the video..."
    )

    if question:

        # Show user's question
        with st.chat_message("user"):
            st.write(question)

        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        # Retrieve relevant transcript chunks
        with st.spinner("🔎 Searching the transcript..."):

            retrieved_docs = st.session_state.retriever.invoke(
                question
            )

            context = "\n\n".join(
                doc.page_content
                for doc in retrieved_docs
            )

        # Create conversation history
        chat_history = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in st.session_state.messages[:-1]
        )

        # RAG prompt
        prompt = f"""
You are a helpful YouTube transcript assistant.

Your job is to answer questions using the transcript
context provided below.

IMPORTANT RULES:
1. Use the transcript context as the primary source.
2. Do not invent information.
3. If the answer cannot be found in the transcript,
   say:
   "I couldn't find that information in the video."
4. Use the previous conversation to understand
   follow-up questions.
5. Answer clearly and naturally.

PREVIOUS CONVERSATION:
{chat_history}

TRANSCRIPT CONTEXT:
{context}

CURRENT QUESTION:
{question}

Answer the current question:
"""

        # Generate answer
        with st.spinner("🤖 Generating answer..."):

            response = st.session_state.llm.invoke(
                prompt
            )

            answer = response.content

        # Display answer
        with st.chat_message("assistant"):
            st.write(answer)

        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
