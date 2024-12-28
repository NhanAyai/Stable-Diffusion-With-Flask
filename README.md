text2image.py
This script handles the core functionality of image generation using Stable Diffusion models from the HuggingFace library. It includes:

A list of pre-trained models.

Functions to create a pipeline and generate images from text prompts.

server_model.py
This script acts as the server-side component powered by Flask. It:

Handles user requests (GET and POST).

Generates images using the selected model.

Saves the generated image to the static folder and displays it on the webpage.

index.html
The frontend interface for the web app. It includes:

A text area for entering prompts.

A dropdown menu for selecting models.

A section to display the generated image and prompt history.

static/
The folder where generated images are saved. The Flask app serves images from this folder.
