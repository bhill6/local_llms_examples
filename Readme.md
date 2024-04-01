# Local LLMs Presentation Examples

## Overview

This repository contains the code examples described during the Local LLMs presentation at the UW Madison ITPC 2024.
The aim of these examples is to build a hands-on understanding of how LLMs work, how they can be used and their
various limitations. All rely on freely available tools and data models that can be run locally on most developer's 
computers.

## Examples
* **[just-curl](just-curl/Readme.md)**
  * Just a simple `curl` command to get the LLM to write a story
  * Simple example of OpenAI-compatible Ollama API
* **[simplest_chat](simplest_chat/Readme.md)**
  * Simple Javascript REST example
  * Demonstrates use of a System Prompt
  * Demonstrates some Model Parameters
* **[simple_chat](simple_chat/Readme.md)**
  * Demonstrates the use and maintenance of Chat History to provide ongoing context to the LLM
* **[gradiotest](chat-ui/Readme.md)**
  * Simple Chat web application
  * Demonstrates streaming output to make 'next word' prediction a bit more obvious
  * Allows easy experimentation with System Prompts
* **[rag-embed](rag-embed/Readme.md)**
  * Demonstrates a very basic Retrieval Augmented Generation system
* **llama-index**
  * Demonstrates the use of the LlamaIndex library to implement a RAG system
* **[alt-text-generator](alt-text-generator/Readme.md)**
  * Demonstrates the use of both a BLIP caption model and a multi-modal LLM model to generate image captions
* **xkcd-explainer**
  * Leverages a multi-model model to attempt to explain random [xkcd](https://xkcd.com) cartoons.

## Preparation & Requirements
* **Hardware**
  * 4-8 CPU cores
  * 8-32 GB RAM
  * 8GB+ GPU or Apple Silicon CPU (M1, M2, M3) recommended, but not required
  * 20GB of disk space (or so, less might work)
* **Software**
  * Python 3.9.x - Some components of some examples may have trouble under 3.10 at the moment (3/2024).
  * Node 18.x
  * Ollama desktop application - Cross platform LLM manager. 
    * Free download at [https://ollama.com](https://ollama.com)
  * Mistral:7B LLM model - Available through Ollama once installed
    * `ollama pull mistral:latest` 
  * LlaVa Multi-model model - Available through Ollama once installed
    * `ollama pull llava:latest`
  * Nomic embedding model - Available through Ollama once installed
    * `ollama pull nomic-embed-text`

## Running the examples

### Javascript Examples
1. Ensure that you are using Node 18+ (older versions *may* work, but not tested)
   1. ` node -v`
2. Change to the directory of one of the javascript examples (`simple_chat` or `simplest_chat`).
3. Install the dependencies
   1. `npm install`
4. Run the script
   1. `node main.sh`

### Python Examples
For best results, I'd suggest creating a separate Python virtual environment in each example directory.
1. Ensure that you are using Python 3.9.x
   1. `python -V`
2. Change to the example directory
3. Create and activate a new python virtual environment
   1. `python -m venv .venv`
   2. `. .venv/bin/activate`
4. Install the requirements
   1. `pip install -r requirements.txt`
5. Run the script
   1. `python main.py`

For examples that provide a web interface, it will be available at [http://localhost:7861](http://localhost:7861)

NOTE: Some of the examples will need to download a relatively large model file (about 5 GB) upon first run. 