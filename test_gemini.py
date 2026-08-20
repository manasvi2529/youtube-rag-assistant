import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("API key found:", bool(api_key))

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
    temperature=0
)

response = llm.invoke("Say hello in one sentence.")

print(response.content)