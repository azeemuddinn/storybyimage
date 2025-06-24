import requests
import os
from PIL import Image
import base64
from io import BytesIO

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_caption(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

    response = requests.post(API_URL, headers=headers, files={"file": img_bytes})
    try:
        result = response.json()
        return result[0]["generated_text"]
    except Exception:
        return "Unable to generate caption right now."
