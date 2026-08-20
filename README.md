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

## 📂 Project Structure

youtube-rag-assistant/
│
├── app.py
├── test_gemini.py
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ Installation

### Clone the repository

git clone https://github.com/manasvi2529/youtube-rag-assistant.git

cd youtube-rag-assistant

### Install dependencies

pip install -r requirements.txt

## 🔑 Gemini API Key

This project uses the Google Gemini API.

1. Get a Gemini API key from Google AI Studio.
2. Run the application.
3. Enter your API key when prompted.

⚠️ Never upload your API key to GitHub.

## 💡 Example Use Cases

- 📚 Summarize educational YouTube videos
- 💻 Ask questions about programming tutorials
- 🧠 Understand long technical videos
- 🔍 Find specific information from a video
- 💬 Interact with video content using natural language

## 🚀 Future Improvements

- 🔗 Direct YouTube URL input
- 🧠 Conversation memory
- ⏱️ Timestamp-based answers
- 🎥 Multiple video support
- 📚 Source citations
- ☁️ Streamlit Cloud deployment

## 👩‍💻 Author

**Manasvi Bhargava**

GitHub: https://github.com/manasvi2529
