# Simplest Chat

## Overview
This extremely simple node program shows how to use the Ollama REST interface to use a LLM. 

The script collects user input from the command line, prepends it with a System Prompt to set the model's role, then 
sends it to the Ollama REST interface. The response is printed to the command line.

## System Prompts
When you run a model via code, versus using one of the official web-based chat sites, like ChatGPT, you have the ability to 
set the chat session's system prompt. 

A System Prompt is an initialization-type message that sets the conversational role of the LLM. This message is used by 
the LLM when generating the response to frame the language and apparent point of view of the answer. It can also be used 
to some extent to provide some guidelines to the LLM about how it should generate an answer, such as in a particular format. 
NOTE: You can provide some measure of constraint on how likely it will be that the LLM will 'lie', but it's not entirely 
effective.

## Model Parameters

temperature: 
Controls the algorithm's creativity.

num_ctx:
Number of tokens in the context window. Setting this to a value larger than the model's own context window may lead
to poor results, since the model will never be able to 'remember' the entire chat history. This also has a bearing on
memory use. 

top_k: 
Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a 
lower value (e.g. 10) will be more conservative. (Default: 40)

top_p: 
Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) 
will generate more focused and conservative text. (Default: 0.9)	

repeat_penalty:
Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a 
lower value (e.g., 0.9) will be more lenient. (Default: 1.1)	

repeat_last_n: 
Sets how far back for the model to look back to prevent repetition. (Default: 64, 0 = disabled, -1 = num_ctx)	


