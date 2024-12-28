# Stable Diffusion Text-to-Image Web App

This project is a web application that generates images from text prompts using Stable Diffusion models from HuggingFace. The app is built with Flask for the backend and integrates with the HuggingFace `diffusers` library for image generation.

---

## **Features**

- **Text-to-Image Generation**: Generate images from text prompts using Stable Diffusion models.
- **Model Selection**: Choose from a list of pre-trained Stable Diffusion models.
- **Prompt History**: View a history of previously used prompts.
- **Responsive UI**: User-friendly interface with a clean design.

---

## **Files Overview**

### **`text2image.py`**
This script handles the core functionality of image generation using Stable Diffusion models from the HuggingFace library. It includes:
- A list of pre-trained models.
- Functions to create a pipeline and generate images from text prompts.

### **`server_model.py`**
This script acts as the server-side component powered by Flask. It:
- Handles user requests (GET and POST).
- Generates images using the selected model.
- Saves the generated image to the `static` folder and displays it on the webpage.

### **`index.html`**
The frontend interface for the web app. It includes:
- A text area for entering prompts.
- A dropdown menu for selecting models.
- A section to display the generated image and prompt history.

### **`static/`**
The folder where generated images are saved. The Flask app serves images from this folder.

---

## **Setup Instructions**

### **Prerequisites**
1. Python 3.8 or higher.
2. Install the required libraries:
   ```bash
   pip install flask torch diffusers
# Setup Instructions
## Prerequisites
1. **Clone the repository or download the files.**
2. **Pip install the file setup.txt**
3. **Run the Flask app: python server_model.py**

## **Usage**

1. **Enter a Prompt**:
   - Type your text prompt in the text area.

2. **Select a Model**:
   - Choose a Stable Diffusion model from the dropdown menu. Note: Top models may take longer to load and generate images.

3. **Generate Image**:
   - Click the “Generate Image” button to create an image from the prompt.

4. **View Results**:
   - The generated image will be displayed on the webpage.
   - The prompt will be added to the history section.
