# xkcd-Explainer

## Overview

The xkcd-explainer project works in a similar manner to the [alt-text-generator](../alt-text-generator), but on an image pulled from a website.

The code fetches a random [xkcd cartoon](https://xkcd.com/), then asks the [Llava](https://llava-vl.github.io/) LLM model to explain the joke.

This is a particularly challenging task for the LLM, since it requires several related interpretive steps. 
