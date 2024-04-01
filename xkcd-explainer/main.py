import sys
import random
import httpx
import gradio as gr

from ollama import generate


def getandexplain():
    # Fetch the latest cartoon information
    latest = httpx.get('https://xkcd.com/info.0.json')
    latest.raise_for_status()

    # You can specify a specific xkcd cartoon to interpret by passing it as a parameter on the command line
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = random.randint(1, latest.json().get('num'))

    # Fetch the information for the specified cartoon
    comic = httpx.get(f'https://xkcd.com/{num}/info.0.json')
    comic.raise_for_status()

    # begin building the output text, by setting up the comic header and alt-text
    fullresponse = f'xkcd #{comic.json().get("num")}:\n *{comic.json().get("alt")}*\n'
    fullresponse += f'link: https://xkcd.com/{num}'
    fullresponse += '\n---\n'

    print(f'xkcd #{comic.json().get("num")}: {comic.json().get("alt")}')
    print(f'link: https://xkcd.com/{num}')
    print('---')

    # Fetch the image from the xkcd website
    img_url = comic.json().get('img')
    raw = httpx.get(img_url)
    raw.raise_for_status()

    # draw the image as soon as it's received
    yield img_url, fullresponse

    # submit the image and the prompt into the LLM. The Ollama API will handle encoding it as appropriate
    # Also set the output to streaming.
    for response in generate('llava', 'Explain this comic:', images=[raw.content], stream=True):
        print(response['response'], end='', flush=True)
        fullresponse += response['response']
        # To speed up printing the output slightly, buffer the output by line
        if '\n' in response['response']:
            yield img_url, fullresponse

    # Update the image and the output on-screen
    yield img_url, fullresponse

    print(img_url)

    # return the image URL and completed output at the end
    return img_url, fullresponse


# Create a Gradio interface
iface = gr.Interface(fn=getandexplain,
                     inputs=None,
                     outputs=["image",gr.Markdown(label="Explanation", show_label=True)],
                     title="xkcd Explainer")
iface.queue().launch(server_name="0.0.0.0", server_port=7861)
