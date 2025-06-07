# In response_generator.py
from features.chat_react.helpers.prompt_builder import build_prompt
from utils.chat_cleaner import clean_reply

def generate_response(viewer_input, model, base_template, style_instructions, category):
    """
    Generates a response based on input, templates, and the message category.
    """

    # Build the prompt
    prompt = build_prompt(
        viewer_input=viewer_input,
        category=category,
        base_template=base_template,
        style_instructions=style_instructions
    )

    # Set temperature based on category
    temperature = 1.0 if category == "Insult" else 0.8

    # Generate model output
    response = model(
        prompt,
        temperature=temperature,
        top_p=0.9,
        top_k=50,
        repetition_penalty=1.1,
        max_new_tokens=80,
        stop=["YOUR RESPONSE:", "Viewer message:", "<|endofprompt|>"],
        stream=False
    )

    # Clean and validate the response
    reply = clean_reply(response.strip())

    # Basic validation check
    if len(reply.split()) < 2 or len(reply.split()) > 120 or '\n' in reply:
        print("🔁 Reply too short/long or has newlines. Regenerating...")
        return generate_response(viewer_input, model, base_template, style_instructions, category)

    return reply
