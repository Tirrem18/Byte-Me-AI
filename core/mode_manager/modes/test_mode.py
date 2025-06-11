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

        # Collect params dynamically
        params_needed = FEATURES[choice]["params"]
        inputs = []
        for param in params_needed:
            value = input(f"{param.capitalize()}: ")
            inputs.append(value)

        # Always pass model as the first argument, then params, then test_mode
        FEATURES[choice]["func"](model, *inputs, test_mode=True)
