# In a new file or in response_generator.py if it fits
def generate_story_response(prompt, model, max_tokens=500):
    """
    Generates long-form story output using raw prompt.
    No style templates, categories, or formatting enforcement.
    """

    response = model(
        prompt,
        temperature=0.9,
        top_p=0.95,
        top_k=40,
        repetition_penalty=1.05,
        max_new_tokens=max_tokens,
        stop=["<|endofprompt|>"],
        stream=False
    )

    return response.strip()
