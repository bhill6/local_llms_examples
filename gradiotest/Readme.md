# Gradio Chat

## Overview

This example provides a relatively complete web-based Chat interface, and uses streaming output from the model. 
The streaming output will print the next word as soon as the LLM chooses it. 

In addition, the interface provides chat history, as well as a way to modify the system prompt dynamically. NOTE: if you
change the system prompt, you should also probably clear the chat history, lest the LLM get confused by previous messages
generated with a different system prompt.

