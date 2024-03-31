# Just Curl

## Overview
This example just contains a shell script that calls the Ollama OpenAI compatible endpoint using curl.

The request contains a short message history that includes a system prompt. The system prompt tells the LLM to assume
the role of a storyteller, and the user's prompt asks the LLM to tell it a story. 

It will usually generate short fairy-tale type story.

This usually takes about 7-10 seconds on an Apple Macbook with an M1 CPU and 32 GB of RAM.
