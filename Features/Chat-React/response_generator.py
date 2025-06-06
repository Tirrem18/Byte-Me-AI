from classifiers.precheck import precheck_classify
from classifiers.ai_classifier import classify_message_ai
from prompting.prompter import build_prompt
from utils.cleaner import clean_reply

def generate_response(viewer_input, model):
    category = precheck_classify(viewer_input)

    if category is None:
        print("🧠 No precheck match, asking AI classifier...")
        category = classify_message_ai(viewer_input, model)  # remove tokenizer
    else:
        print(f"🛡️ Prechecked and classified as: {category}")

    prompt = build_prompt(viewer_input, category)

    temperature = 1.0 if category == "Insult" else 0.8

    # ⚡ Generate directly
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


    reply = response.strip()
    reply = clean_reply(reply)

    if len(reply.split()) < 2 or len(reply.split()) > 120 or '\n' in reply:
        print("🔁 Reply too short/long or has newlines. Regenerating...")
        return generate_response(viewer_input, model)  # no tokenizer anymore!

    return reply
