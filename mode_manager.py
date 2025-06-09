import os
import sys
from dotenv import load_dotenv

from features.chat_react import chat_react
from features.story_time import story_time
from shared_Functionality.helpers.model_loader import load_model
from shared_Functionality.helpers.warm_up import warm_up_model  # ✅ Import warm-up

load_dotenv()

def run_mode_manager():
    """
    ByteMeAI controller – loads model once, warms up, and lets user switch features dynamically in test mode.
    """

    mode = os.getenv("MODE", "Test")
    print(f"Mode: {mode}")

    # Load the model ONCE
    print("⏳ Loading GGUF model...")
    model = load_model()
    print("✅ Model Loaded Successfully")

    # ✅ Silent warm-up using real pipeline logic
    warm_up_model(model)

    # Feature map
    feature_funcs = {
        "chat-react": chat_react.run,
        "story-time": story_time.run,
        # Add more features here
    }

    testable_features = {"chat-react", "story-time"}

    if mode.lower() == "production":
        print("[TODO] Production logic not implemented yet.")
        return

    elif mode.lower() == "test":
        while True:
            print("\n🎮 Available features:")
            for name in feature_funcs:
                print(f" - {name}")

            choice = input("\nEnter feature to run (or 'exit' to quit): ").strip().lower()
            if choice == "exit":
                print("👋 Exiting ByteMeAI.")
                break

            feature_func = feature_funcs.get(choice)
            if not feature_func:
                print(f"[ERROR] Feature '{choice}' not recognized.")
                continue

            if choice not in testable_features:
                print(f"[TODO] Feature '{choice}' not yet available in test mode.")
                continue

            print(f"\n🧪 Running feature: {choice}")
            feature_func(model, test_mode=True)

    else:
        print(f"[ERROR] Unknown mode '{mode}'. Exiting.")
        sys.exit(1)
