use an api and save on monthly subscriptions.
openrouter! openai, runpod, notebookllm
sites: huggingface/yeahhub/ollama/runpod/leaderboard
chub?
merging models (censored and not, coding with txt generation, etc)


# The Uncensored Underground: Using Uncensored AI Models to Create a Hacking Assistant

## Creating Your Own Programming Assistant with NotebookLLM

Learn how to build a personalized programming assistant using NotebookLLM and free programming resources.

### Quick Setup Guide

1. Obtain Learning Materials
- Visit [YeahHub's hacking books collection] and find the "Top 100 Hacking & Security E-Books"
    https://www.yeahhub.com/biggest-hacking-security-ebooks-collection-free-download/
    or
    https://github.com/yeahhub/Hacking-Security-Ebooks?tab=readme-ov-file
  
- Download the ZIP file
- Extract the ZIP file to a local directory on your computer

2. Set Up NotebookLLM
- Navigate to [NotebookLLM](https://notebookllm.com)
- Create a new account if you haven't already
- Click "New Project" to create a fresh workspace

3. Import Learning Materials
- In your new NotebookLLM project, click "Upload Files"
- Select approximately 50 PDFs from your extracted hacking books
- Wait for the upload and processing to complete

4. Start Learning
- Use the chat interface to ask programming and hacking-related questions
- The AI will reference the uploaded materials to provide contextual answers
- Example questions you can ask:
  - "How do I set up a basic penetration testing environment?"
  - "Explain the concept of buffer overflow"
  - "What are common web application vulnerabilities?"


## Chat with LLM locally

1. Download ollama (https://ollama.com/)
2. In a terminal, execute ``ollama run huihui_ai/phi4-mini-abliterated``
3. Ollama will download this uncensored model, run it, and display a prompt in the terminal
4. Interact with the local LLM: your conversation is local and private
5. When you're finished, end the ollama process with ``\\bye``

## Local LLM Chat Interface with Chainlit and Ollama

Create a simple but powerful chat interface for local LLMs using Chainlit and Ollama.

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Ollama installed on your system (https://ollama.com/)

## Setup Instructions

### 1. Install Required Packages
```bash
pip install chainlit langchain
```

Create or download the python program `chainlit_ollama.py`
```python
import chainlit as cl
from langchain_ollama import OllamaLLM

@cl.on_message
async def main(message: cl.Message):
    llm = OllamaLLM(model="huihui_ai/phi4-mini-abliterated")
    response = llm.invoke(message.content)
    await cl.Message(content=response).send()
```
Open a terminal and run ollama:
```bash
ollama run huihui_ai/phi4-mini-abliterated
```

Keep that teminal running. 
In another, run the chainlit python program:

```bash
chainlit run chainlit_ollama.py
```

5. Start Chatting
   
    Open your web browser and navigate to http://localhost:8000

    You should see a chat interface where you can interact with the local LLM

How It Works

    The script creates a web interface using Chainlit

    When you send a message, it's processed by the local Phi-4 model running through Ollama

    Responses are displayed in real-time in the chat interface


Notes

    Keep both terminals running (Ollama and Chainlit)

    First-time model download might take a few minutes

    The interface is accessible only on your local machine


## Creating a RAG database 

## How RAG works

## ``pdf_to_rag.py``

## Create Personal Assistant on Cloud big machines (RunPod) ``chainlit_runpod.py``

## Using Our Local RAG with our Cloud LLM ``chainlit_rag_runpod.py``



