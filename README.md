# 🎨 Stable Diffusion Text-to-Image Web App

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.3.2-000000?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/HuggingFace-Diffusers-FFD21F?logo=huggingface" alt="HuggingFace">
  <img src="https://img.shields.io/github/last-commit/your-username/stable-diffusion-web-app?color=blue" alt="Last Commit">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</div>

<div align="center">
  <br>
  <p>Transform text into stunning AI-generated images with state-of-the-art diffusion models</p>
  <img width="75%" src="https://www.vectorlogo.zone/logos/huggingface/huggingface-ar21.svg" alt="HuggingFace Logo">
</div>

---

## ✨ Features

<div align="center">
  
| **Feature**               | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| 🖼️ Text-to-Image AI      | Generate high-quality images from text prompts using Stable Diffusion models    |
| 🧠 Multiple Models        | Choose from 7+ pretrained models including SD 2.1, OpenJourney, and Waifu       |
| ⏳ Prompt History         | Track your creative process with automatically saved generation history         |
| 🎨 Customizable Settings  | Adjust image dimensions, inference steps, and guidance scale for perfect output |
| 🌐 Web Interface          | Intuitive Flask-based UI with real-time preview and download capabilities       |

</div>

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Git (optional)

### Installation
```bash
# Clone repository
git clone https://github.com/your-username/stable-diffusion-web-app.git
cd stable-diffusion-web-app

# Install dependencies
pip install -r setup.txt

# Launch application
python server_model.py
```

## 🧩 Project Structure
stable-diffusion-web-app/
├── text2image.py            # Core generation logic
├── server_model.py          # Flask server configuration
├── templates/
│   ├── base.html            # Master template
│   └── index.html           # Main interface
├── static/
│   ├── css/                 # Custom styles
│   ├── js/                  # Interactive scripts
│   └── outputs/             # Generated images
├── models/                  # Local model cache
├── requirements.txt         # Dependency list
└── README.md                # Documentation

## 📚 Model Library
Model	Version	Specialization
stabilityai/stable-diffusion-2-1	2.1	General Purpose
CompVis/stable-diffusion-v1-4	1.4	Base Model
runwayml/stable-diffusion-v1-5	1.5	Enhanced Details
prompthero/openjourney	v4	Artistic Styles
hakurei/waifu-diffusion	1.3	Anime/Manga
dreamlike-art/dreamlike-photoreal-2.0	2.0	Photorealistic Images
nota-ai/bk-sdm-small	tiny	Mobile Optimization
