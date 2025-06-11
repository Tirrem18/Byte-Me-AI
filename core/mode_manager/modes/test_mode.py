from modules.feature_list import FEATURES

def run_test_mode(model):
    while True:
        print("Available features:", list(FEATURES.keys()))
        choice = input("Enter feature name (or 'exit'): ").strip().lower()
        if choice == "exit":
            break
        if choice not in FEATURES:
            print("Not found")
            continue
        # Here you prompt for username/chat, then:
        username = input("Username: ")
        chat = input("Chat: ")
        FEATURES[choice](model, username, chat, test_mode=True)
