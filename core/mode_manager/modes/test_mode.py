from modules.chat_reacts import chat_react
from modules.story_time import story_time

def run_test_mode(model):
    feature_funcs = {
        "chat-react": chat_react.run,
        "story-time": story_time.run,
    }

    print("\n🧪 Entering Test Mode.")
    while True:
        print("\n🎮 Available Features:")
        for name in feature_funcs:
            print(f" - {name}")

        choice = input("Enter a feature name (or 'exit'): ").strip().lower()
        if choice == "exit":
            print("👋 Exiting Test Mode.")
            break
        elif choice not in feature_funcs:
            print(f"[ERROR] '{choice}' not found.")
            continue

        print(f"\n▶ Running: {choice}")
        feature_funcs[choice](model, test_mode=True)
