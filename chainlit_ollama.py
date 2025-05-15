import chainlit as cl
from langchain_ollama import OllamaLLM

# pip install chainlit langchain
# in another terminal exec: ollama run huihui_ai/phi4-mini-abliterated
#

@cl.on_message
async def main(message: cl.Message):
    llm = OllamaLLM(model="huihui_ai/phi4-mini-abliterated")
    response = llm.invoke(message.content)
    await cl.Message(content=response).send()
