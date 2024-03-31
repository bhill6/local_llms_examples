# Local LLMs Presentation Examples

## Overview

This repository contains the code examples described during the Local LLMs presntation at the UW Madison ITPC 2024.

## Examples
* **just-curl**
  * Just a simple `curl` command to get the LLM to write a story
  * Simple example of OpenAI-compatible Ollama API
* **simplest_chat**
  * Simple Javascript REST example
  * Demonstrates use of a System Prompt
  * Demonstrates some Model Parameters
* **simple_chat**
  * Demonstrates the use and maintenance of Chat History to provide ongoing context to the LLM
* **gradiotest**
  * Simple Chat web application
  * Demonstrates streaming output to make 'next word' predication a bit more obvious
  * Allows easy experimentation with System Prompts
* **rag-embed**
  * Demonstrates a very basic Retrieval Augmented Generation system
* **llama-index**
  * Demonstrates the use of the LlamaIndex library to implement a RAG system
* **alt-text-generator**
  * Demonstrates the use of both a BLIP caption model and a multi-model LLM model to generate image captions
* **xkcd-explainer**
  * Leverages a multi-model model to attempt to explain random [xkcd](https://xkcd.com) cartoons.

## Preparation & Requirements
* **Hardware**
  * 4-8 CPU cores
  * 8-32 GB RAM
  * 8GB+ GPU or Apple Silicon CPU (M1, M2, M3) recommended, but not required
* **Software**
  * Python 3.9.x - Some components of some examples may have trouble under 3.10 at the moment (3/2024).
  * Node 18.x
  * Ollama desktop application - Cross platform LLM manager. Available at [https://ollama.com](https://ollama.com)
  * Mistral:7B LLM model - Available through Ollama once installed
    * `ollama pull mistral:latest` 
  * LlaVa Multi-model model - Available through Ollama once installed
    * `ollama pull llava:latest`
  * Nomic embedding model - Available through Ollama once installed
    * `ollama pull nomic-embed-text`

## Running the examples

### Javascript Examples
1. Change to the directory of one of the javascript examples (`simple_chat` or `simplest_chat`).
2. Install the dependencies
   1. `npm install`
3. Run the script
   1. `node main.sh`

### Python Examples
For best results, I'd suggest creating a separate Python virtual environment in each example directory.
1. Change to the example directory
2. Create and activate a new python virtual environment
   1. `python -m venv .venv`
   2. `. .venv/bin/activate`
3. Install the requirements
   1. `pip install -r requirements.txt`
4. Run the script
   1. `python main.py`

For examples that provide a web interface, it will be available at [http://localhost:7861](http://localhost:7861)

