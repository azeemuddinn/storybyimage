from transformers import pipeline, set_seed

# Load once at top level
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def generate_story(description, mood=None):
    return f"A story about: {description}. Mood: {mood or 'default'}."
    prompt = f"Here is  a short 100-word {mood + ' ' if mood else ''}story about: {description}"
    output = generator(prompt, max_length=120, num_return_sequences=1)[0]['generated_text']
    
    # Trim after first ~100 words
    words = output.split()
    story = ' '.join(words[:100])
    return story
