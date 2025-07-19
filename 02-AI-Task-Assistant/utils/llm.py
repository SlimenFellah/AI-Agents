from langchain.llms import Ollama

llm = Ollama(model="llama2")

def call_llm(prompt: str) -> str:
    return llm(prompt).strip()
