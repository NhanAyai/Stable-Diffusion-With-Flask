import torch
from diffusers import StableDiffusionPipeline

# Parameters
random_seed = torch.manual_seed(42)  # Create a random seed in PyTorch
inference_steps = 25
guidance_scale = 7.5
height = 512  # The original model train dataset images 512x512.
width = 512

# List of models
model_list = [
    "nota-ai/bk-sdm-small",  # https://huggingface.co/nota-ai/bk-sdm-small
    "CompVis/stable-diffusion-v1-4",  # https://huggingface.co/CompVis/stable-diffusion-v1-4
    "runwayml/stable-diffusion-v1-5",  # https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5
    "prompthero/openjourney",  # https://huggingface.co/prompthero/openjourney
    "hakurei/waifu-diffusion",  # https://huggingface.co/hakurei/waifu-diffusion
    "stabilityai/stable-diffusion-2-1",  # https://huggingface.co/stabilityai/stable-diffusion-2-1
    "dreamlike-art/dreamlike-photoreal-2.0"  # https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0
]

def create_pipeline(model_name=model_list[6]):
    if torch.cuda.is_available():
        print("Using GPU")
        pipeline = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            use_safetensors=True
        ).to("cuda")
    else:
        print("Using CPU")
        pipeline = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            use_safetensors=True
        )
    return pipeline

def text2img(prompt, pipeline):
    images = pipeline(
        prompt,
        num_inference_steps=inference_steps,
        guidance_scale=guidance_scale,
        generator=random_seed,
        num_images_per_prompt=1,
        height=height,
        width=width
    ).images
    return images[0]