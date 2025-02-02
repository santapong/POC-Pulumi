from fastapi import FastAPI
from langchain_ollama import ChatOllama


app = FastAPI()

@app.get("/infer")
def chat(question):

    return {"msg":question}