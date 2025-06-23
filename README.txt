# 🖼️ Story by Image — Generative AI with Django & Hugging Face

This is a simple Django web application that demonstrates how to combine **Computer Vision** and **Natural Language Generation** using open-source AI models.

Users can:
- Upload an image
- Automatically generate a **description** using a Vision model (BLIP)
- Choose a **mood** (like funny, mysterious, sad)
- Get a 100-word fictional **story** written by an AI language model (GPT-2)

---

## 🚀 Technologies Used

- **Django** (Python web framework)
- **Hugging Face Transformers**
  - `Salesforce/blip-image-captioning-base` for image descriptions
  - `gpt2` for story generation
- **Pillow** (image handling)
- **Torch** (for model inference)

---

## 📸 Demo Flow

1. Upload an image (JPEG, PNG)
2. Select an optional mood (funny, mysterious, sad, etc.)
3. AI generates:
   - A caption based on the image
   - A 100-word short story matching the mood
4. View the result and upload another

---
 