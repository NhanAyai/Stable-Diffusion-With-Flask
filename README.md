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
1. Clone the repository or download the files.
2. Python 3.8 or higher.
3.. Install the required libraries:
   ```bash
   pip install -r setup.txt

## **Usage**
1. Run the Flask app:
    ```bash
   python server_model.py
    
2. **Enter a Prompt**:
   - Type your text prompt in the text area.

3. **Select a Model**:
   - Choose a Stable Diffusion model from the dropdown menu. Note: Top models may take longer to load and generate images.

4. **Generate Image**:
   - Click the “Generate Image” button to create an image from the prompt.

5. **View Results**:
   - The generated image will be displayed on the webpage.
   - The prompt will be added to the history section.

## **Model List**

The app supports the following Stable Diffusion models:
1. `stabilityai/stable-diffusion-2-1`
2. `CompVis/stable-diffusion-v1-4`
3. `runwayml/stable-diffusion-v1-5`
4. `prompthero/openjourney`
5. `hakurei/waifu-diffusion`
6. `dreamlike-art/dreamlike-photoreal-2.0`
7. `nota-ai/bk-sdm-small`

---

## **Folder Structure**
```
project/
│
├── text2image.py # Core image generation logic
├── server_model.py # Flask server
├── templates/
│ └── index.html # Frontend HTML template
├── static/ # Folder for generated images
│ └── output.jpg
└── README.md # Project documentation
```

## **Reference**

- **Video Tutorial**: [Stable Diffusion Tutorial](https://www.youtube.com/watch?v=vDAgIokDQ4Q&t=2197s)  
  This video helped me understand the basics of Stable Diffusion and how to implement it in Python.

- **Code Reference**: [MIAI_GAN_EuroSat GitHub Repository](https://github.com/thangnch/MIAI_GAN_EuroSat/)  
  This repository provided a foundation for building the Flask app and integrating Stable Diffusion models.

---

## **What I Have Learned**

Through this project, I gained hands-on experience in several key areas:
1. **Loading Models from HuggingFace**: I learned how to load pre-trained Stable Diffusion models from HuggingFace using the `diffusers` library.
2. **Configuring Hyperparameters**: I explored how to configure basic hyperparameters such as `inference_steps`, `guidance_scale`, and image dimensions to control the image generation process.
3. **Building a Flask App**: I developed a web application using Flask to provide a user-friendly interface for text-to-image generation. This included handling user inputs, processing requests, and displaying results dynamically.
4. **Integrating Frontend and Backend**: I learned how to connect the frontend (HTML/CSS) with the backend (Flask) to create a seamless user experience.
5. **Deploying a Local Server**: I set up a local server using Flask to host the application and make it accessible via a web browser.
