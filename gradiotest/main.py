import os

from langchain_community.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import gradio as gr
from openai import OpenAI

# Initialize an OpenAI compatible client. the api_key is not used by ollama, but is required by the
# ChatOpenAI package.
client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)
base_system_prompt = "You are a helpful assistant. You only reply with facts that verify from training data."

def predict(message, history, system_prompt):
    # initialize the message history 
    history_langchain_format = [{"role": "system", "content": system_prompt}]
    
    # append all the previous messages to the message history
    for human, ai in history:
        history_langchain_format.append({"role": "user", "content": human})
        history_langchain_format.append({"role": "assistant", "content": ai})
    
    # append in latest question from the user    
    history_langchain_format.append({"role": "user", "content": message})
    # Send the current conversation, including the new question, to the Ollama server.
    # gpt_response = llm(history_langchain_format)
    response = client.chat.completions.create(
        model='mistral',
        messages=history_langchain_format,
        temperature=0.8,
        stream=True  # this time, we set stream=True
    )
    fullresponse = ''
    for chunk in response:
        if chunk.choices[0].finish_reason != True:
            fullresponse += chunk.choices[0].delta.content
        yield fullresponse

    return fullresponse

# launch the gradio interface on port 7860
gr.ChatInterface(predict,
                 additional_inputs=[
                     gr.Textbox(base_system_prompt, label="System Prompt")                 
                ]).launch(server_name="0.0.0.0", server_port=7861)


