🎨 Stable Diffusion Text-to-Image Web App
🌟 Transform Text into Stunning Images with AI!
This project is a web application that generates images from text prompts using Stable Diffusion models from HuggingFace. Built with Flask for the backend and integrated with the HuggingFace diffusers library, this app brings your imagination to life!

🚀 Features
Text-to-Image Generation: Create unique images from text prompts using state-of-the-art Stable Diffusion models.

Model Selection: Choose from a variety of pre-trained models to customize your image generation.

Prompt History: Keep track of your creative journey with a history of previously used prompts.

Responsive UI: Enjoy a clean, user-friendly interface designed for seamless interaction.

🛠️ Files Overview
File/Folder	Description
text2image.py	Core logic for image generation using Stable Diffusion models.
server_model.py	Flask server to handle requests, generate images, and display results.
templates/index.html	Frontend interface with a text input, model dropdown, and image display.
static/	Folder for storing generated images (e.g., output.jpg).
README.md	Project documentation (you're here!).
🧰 Setup Instructions
Prerequisites
Clone the repository:

bash
Copy
git clone https://github.com/your-username/stable-diffusion-web-app.git
Install Python 3.8 or higher.

Install required libraries:

bash
Copy
pip install -r setup.txt
Running the App
Start the Flask server:

bash
Copy
python server_model.py
Open your browser and navigate to http://127.0.0.1:5000/.

Enter a text prompt, select a model, and click Generate Image!

🖼️ How to Use
Enter a Prompt: Type your creative text prompt in the text area.

Select a Model: Choose a Stable Diffusion model from the dropdown menu.

Note: Larger models may take longer to load and generate images.

Generate Image: Click the Generate Image button to create your masterpiece.

View Results:

The generated image will be displayed on the webpage.

Your prompt will be added to the Prompt History section.

🧠 Supported Models
The app supports the following Stable Diffusion models:

stabilityai/stable-diffusion-2-1

CompVis/stable-diffusion-v1-4

runwayml/stable-diffusion-v1-5

prompthero/openjourney

hakurei/waifu-diffusion

dreamlike-art/dreamlike-photoreal-2.0

nota-ai/bk-sdm-small

📂 Folder Structure
Copy
stable-diffusion-web-app/
├── text2image.py            # Core image generation logic
├── server_model.py          # Flask server
├── templates/
│   └── index.html           # Frontend HTML template
├── static/                  # Folder for generated images
│   └── output.jpg
└── README.md                # Project documentation
📚 References
Video Tutorial: Stable Diffusion Tutorial
This video helped me understand the basics of Stable Diffusion and how to implement it in Python.

🌱 What I Have Learned
Through this project, I gained hands-on experience in:

Loading Models from HuggingFace: Using the diffusers library to load pre-trained Stable Diffusion models.

Configuring Hyperparameters: Adjusting inference_steps, guidance_scale, and image dimensions for optimal results.

Building a Flask App: Creating a web application with Flask to handle user inputs and display results dynamically.

Frontend-Backend Integration: Connecting HTML/CSS with Flask for a seamless user experience.

Local Server Deployment: Hosting the app locally using Flask and making it accessible via a web browser.

🎉 Get Started
Ready to unleash your creativity? Clone the repo, follow the setup instructions, and start generating stunning images today!

bash
Copy
git clone https://github.com/your-username/stable-diffusion-web-app.git
cd stable-diffusion-web-app
pip install -r setup.txt
python server_model.py
