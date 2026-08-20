# 🎥 YouTube RAG Assistant

An AI-powered YouTube RAG (Retrieval-Augmented Generation) Assistant that allows users to ask questions about a YouTube video's transcript and get intelligent, context-aware answers.

## 🚀 Features

- 📺 Ask questions about YouTube video transcripts
- ✂️ Splits transcripts into smaller chunks
- 🧠 Generates vector embeddings
- 🔎 Retrieves relevant transcript content
- 🤖 Uses Google Gemini to generate answers
- 💬 Interactive Streamlit interface
- 🔐 API key is entered securely and `.env` is excluded from GitHub

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- LangChain
- FAISS
- YouTube Transcript API
- Python-dotenv

## 🔄 How It Works

```text
YouTube Video
     ↓
Transcript Extraction
     ↓
Text Chunking
     ↓
Vector Embeddings
     ↓
FAISS Vector Search
     ↓
Relevant Context
     ↓
Google Gemini
     ↓
AI Answer
