# Alt-Text Generator

## Overview
The alt-text-generator project demonstrates how to submit an image to a multi-model LLM for analysis. In this case, 
we'll ask the model to provide a description of the image. We'll use the LlaVa model to do this.

To provide a contrast, we'll also use a simpler BLIP caption model to generate a shorter description for the image 
using a BLIP model. 

## How does this work?
The multi-modal model includes a vision encoder that creates a tokenized representation of the image, based on the 
images it's been trained with. This tokenized description is then passed to the LLM to summarize the tokens and 
generate a text description of the image.

The BLIP model also creates a tokenized representation of the image, based on the images it was trained with, but
the tokenized description is converted to text and output, instead of it being summarized by an LLM.