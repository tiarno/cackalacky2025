Notes:

    - use an api and save on monthly subscriptions.
    - checkout openrouter
    - sites: huggingface/leaderboard
    - chub?
    - merging models (censored and not, coding with txt generation, etc)

To view the slides as they were presented at CackalackyCon2025 (along with video clips),
see https://tiarno.github.io/cackalacky2025_presentation/


To use the code in this repo, make sure you install the necessary libraries.
You can use 
```python
   pip install -r requirements.txt
```
The files are as follows:

   - chainlit_ollama (get a web interface for your ollama service running locally)
   - pdf_to_rag.py (parse/chunk/vectorize a collection of PDFs into a vector database)
   - chainlit_runpod.py (get a web interface for a model running on runpod)
   - chainlit_rag_runpod.py (use your vectorized db from your pdfs to support querying a model on runpod)

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

1. Download and install (https://ollama.com/)
2. In a terminal, execute ``ollama run huihui_ai/phi4-mini-abliterated``
3. Ollama will download this uncensored model, run it, and display a prompt in the terminal
4. Interact with the local LLM: your conversation is local and private
5. When you're finished, end the ollama process with ``\\bye``

Once ollama has downloaded a model, you can use it any time afterwards.
See your downloaded models with ``ollama list`` . When you ``run`` a model
that's already downloaded it's much faster to start.

## Local LLM Chat Interface with Chainlit and Ollama

When you start up that ollama as in the last step, you have an interactive prompt
waiting in the terminal. That's great and it has no overhead for those with small
machines. If you're only using a CPU and no GPU, you should probably stick with that.
On the other hand, it's nice to have a web interface even if it eats a little memory.

This is for those who would like that web interface (it will also get used later on).

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
   
- Open your web browser and navigate to http://localhost:8000
- You should see a chat interface where you can interact with the local LLM

How It Works

- The script creates a web interface using Chainlit
- When you send a message, it's processed by the local Phi-4 model running through Ollama
- Responses are displayed in real-time in the chat interface


Notes

- Keep both terminals running (Ollama and Chainlit)
- First-time model download might take a few minutes 
- The interface is accessible only on your local machine


## Creating a RAG database 

With a Retrieval Augmented Generation (RAG) system,
you format your document(s) so the LLM can understand them (into a vector database).
Wnen you query the LLM, the system first does a search through that datab ase 
which are sent, along with the query, to provide context for the model.
The model can then respond with information it already knows from its training and
from your document database. Using this method, you can make sure the model has
up-to-date information by periodically updating your database.


## ``pdf_to_rag.py``
This file does just what it says: you create a directory ``pdfs`` in which you place one or more
pdf documents. Also create a subdirectory  `embeddings`` to hold the database that will result. Execute this program and your pdfs are parsed, chunked, and vectorized. Then that info is saved into Chroma vector
database. You can use that database in later queries to get targeted answers from your model, whether
runing locally (with ollama, say) or remotely (runpod).

## Create Personal Assistant on Cloud big machines (RunPod) ``chainlit_runpod.py``

- make an account on runpod.io, add some money to your account.
- deploy:
  + pick some hardware to use (I used RTX 4090 for the talk).
  + pick a model (I used cognitivecomputations/dolphin-2.9-llama3-8b)
  + pick a template (I used vllm-latest) I used these options:
    ``--host 0.0.0.0 --port 8000`` 
    ``--model cognitivecomputations/dolphin-2.9-llama3-8b --dtype bfloat16``
    `` --enforce-eager --gpu-memory-utilization 0.95``
  + depending on what model you pick, you may need to add HF_TOKEN as a environment variable.
    it should contain your HUGGINGFACE api key, which you get when you sign up for it on huggingface.
  + start the pod
- make sure you can connect the pod once it has started (from runpod, "http connect") and copy that url to your chainlit code.
- edit chainlit_runpod.py
  + make sure the ``model`` variable has your model name exactly
  + make sure the ``base_url`` has the url for your pod instance.
- run chainlit run chainlit_runpod.py



## Using Our Local RAG with our Cloud LLM ``chainlit_rag_runpod.py``

Once you've created your database of documents (running pdf_to_rag.py), you
can use that database over and over. Make the model/url changes to the file
``chainlit_rag_runpod.py`` just as in the last step. In that step we interact
directly with the model through chainlit. This step is just like that except that
we also add context for the model by searching for relevant info from the document
database first. That's the power of a RAG system.

