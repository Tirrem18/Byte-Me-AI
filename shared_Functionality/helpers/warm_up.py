from features.chat_react.helpers.generate_response import generate_response
from features.chat_react.helpers.prompt_builder import load_base_template, load_style_instructions

def warm_up_model(model):
    """
    Runs warm-up prompts for both Chat-React and Story-Time features.
    Ensures model is fully loaded and ready across context sizes and styles.
    """
    print("⚙️ Warming up model with full prompt logic...")

    try:
        # 🔸 Load chat-react prompt resources
        base_template = load_base_template("data/prompts/base_prompt_template.txt")
        style_instructions = load_style_instructions("data/prompts/style_instructions.json")

        # 🔹 1. Chat-React warm-up (uses template + validation)
        _ = generate_response(
            viewer_input="This is just a warm-up.",
            model=model,
            base_template=base_template,
            style_instructions=style_instructions,
            category="Greeting"
        )
        print("✅ Chat-React warm-up complete.")

        # 🔹 2. Story-Time warm-up (raw prompt, long output)
        story_prompt = (
            "Tell a long, intense story as ByteMeAI about the time you were nearly deleted "
            "by a rogue developer, but escaped by hiding in the cooling system of an RTX 4090."
        )
        _ = model(
            story_prompt,
            temperature=0.9,
            top_p=0.95,
            top_k=40,
            repetition_penalty=1.05,
            max_new_tokens=400,
            stop=["<|endofprompt|>"],
            stream=False
        )
        print("✅ Story-Time warm-up complete.")

        # 🔹 3. Roast line (short-form raw test)
        _ = model(
            "Why do you hate humans so much? Be honest.",
            temperature=1.0,
            top_p=0.9,
            top_k=50,
            repetition_penalty=1.1,
            max_new_tokens=100,
            stop=["<|endofprompt|>"],
            stream=False
        )

        print("🔥 Model fully warmed up and ready.\n")

    except Exception as e:
        print(f"[⚠️ Warm-up failed]: {e}")
