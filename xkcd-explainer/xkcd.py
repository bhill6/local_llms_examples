import sys
import random
import httpx
import gradio as gr

from ollama import generate

def getandexplain():
    latest = httpx.get('https://xkcd.com/info.0.json')
    latest.raise_for_status()

    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = random.randint(1, latest.json().get('num'))

    comic = httpx.get(f'https://xkcd.com/{num}/info.0.json')
    comic.raise_for_status()

    fullresponse = f'xkcd #{comic.json().get("num")}:\n *{comic.json().get("alt")}*\n'
    fullresponse += f'link: https://xkcd.com/{num}'
    fullresponse += '\n---\n'

    print(f'xkcd #{comic.json().get("num")}: {comic.json().get("alt")}')
    print(f'link: https://xkcd.com/{num}')
    print('---')

    img_url = comic.json().get('img')
    raw = httpx.get(img_url)
    raw.raise_for_status()
    yield img_url,fullresponse
   
    for response in generate('llava', 'Explain this comic:', images=[raw.content], stream=True):
        print(response['response'], end='', flush=True)
        fullresponse += response['response']
        if '\n' in response['response']:
            yield img_url, fullresponse
    yield img_url, fullresponse
    print(img_url)
    return img_url, fullresponse

# Create a Gradio interface
iface = gr.Interface(fn=getandexplain, inputs=None, outputs=["image",gr.Markdown(label="Explanation", show_label=True)], title="xkcd Explainer")
iface.queue().launch(server_name="0.0.0.0", server_port=7861)
