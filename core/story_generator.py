import requests
import os

def generate_story(prompt, mood="neutral"):
    api_url = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-125M"  # Light model
    headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

    payload = {
        "inputs": f"Write a {mood} story about: {prompt}",
        "options": {"wait_for_model": True}
    }

    response = requests.post(api_url, headers=headers, json=payload)
    result = response.json()

    try:
        return result[0]['generated_text']
    except Exception:
        return "Oops! Couldn't generate story right now."
