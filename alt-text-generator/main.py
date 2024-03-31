import gradio as gr
import base64
from io import BytesIO
from ollama import generate
from transformers import BlipProcessor, BlipForConditionalGeneration

# Create Blip model for BLIP captions
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")


# converts image to base 64 format (required for Ollama API)
def image_to_base64_str(pil_image):
    byte_arr = BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))


# Define a function to encode the image with base64
def encode_image(image):
    global processor, model

    # Encode the image with base64
    blip_caption = "This is a BLIP caption"
    full_response = "### Processing llava model description...\n\n"

    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=40)
    blip_caption = processor.decode(out[0], skip_special_tokens=True)
    print(blip_caption)

    yield blip_caption, full_response

    for response in generate('llava', 'Please describe this image:', images=[image_to_base64_str(image)], stream=True):
        response_text = response['response']
        print(response_text, end='', flush=True)
        full_response += response_text
        if '\n' in response_text:
            yield blip_caption, full_response

    yield blip_caption, full_response

    return blip_caption, full_response


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            imageArea = gr.Image(label="Upload image", type="pil")
            blipArea = gr.TextArea(label="BLIP")
        with gr.Column():
            llavaArea = gr.Markdown("### Llava model output...\n\n")
    with gr.Row():
        submitButton = gr.Button(value="Describe")
        gr.ClearButton(components=[imageArea,blipArea,llavaArea])
    
    submitButton.click(encode_image, imageArea, [blipArea,llavaArea])

# Launch the interface server
demo.queue().launch(server_name="0.0.0.0", server_port=7861)
