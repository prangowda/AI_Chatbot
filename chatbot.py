import random
import spacy
from transformers import pipeline

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, how about you?", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you soon!", "Take care!"],
    "default": ["I'm not sure how to respond.", "Can you rephrase?", "Let me think..."]
}

# AI-based response using GPT-2
gpt_model = pipeline("text-generation", model="gpt2")

# Function to process user input
def chatbot_response(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)

    # Check for predefined responses
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])

    # Generate AI-based response
    ai_response = gpt_model(user_input, max_length=50, num_return_sequences=1)
    return ai_response[0]['generated_text']
