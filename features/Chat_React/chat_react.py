import time
from features.chat_react.helpers.generate_response import generate_response
from features.chat_react.helpers.prompt_builder import load_base_template, load_style_instructions
from features.chat_react.helpers.chat_prechecker import precheck_classify


def run(model, test_mode=False):
    """
    Run function for chat-react feature.
    Logs response latency during test mode.
    """
    if test_mode:
        print("[Chat-React] Running in test mode...")

        # Load the prompt templates
        base_template_path = "data/prompts/base_prompt_template.txt"
        style_instructions_path = "data/prompts/style_instructions.json"

        print(f"📄 Loading base template from: {base_template_path}")
        base_template = load_base_template(base_template_path)

        print(f"🎨 Loading style instructions from: {style_instructions_path}")
        style_instructions = load_style_instructions(style_instructions_path)

        print("[✅] Templates loaded successfully.")

        # Testing Loop
        print("\n[Chat-React] Enter viewer message (or 'exit' to quit):\n")
        while True:
            viewer_input = input("Viewer: ")
            if viewer_input.strip().lower() == "exit":
                print("👋 Exiting test mode.")
                break

            # Precheck classify
            category, match = precheck_classify(viewer_input)
            if not category:
                category = "Other"

            print(f"🧩 Message category: {category}")

            # Measure latency
            start_time = time.time()
            reply = generate_response(
                viewer_input=viewer_input,
                model=model,
                base_template=base_template,
                style_instructions=style_instructions,
                category=category
            )
            end_time = time.time()
            latency = end_time - start_time

            print(f"Bot: {reply}")
            print(f"⏱️ Response Time: {latency:.2f} seconds\n")

    else:
        print("[Chat-React] Running in normal (production) mode...")
        print("[TODO] Production deployment logic not yet implemented.")
