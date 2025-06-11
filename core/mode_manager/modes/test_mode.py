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

        param_defs = FEATURES[choice]["params"]
        inputs = []
        for param in param_defs:
            # Optional param handling
            if param.get("optional", False):
                do_custom = input(f"Custom {param['name']}? (y/n): ").strip().lower()
                if do_custom == "y":
                    value = input(f"{param['custom_prompt']}: ")
                    if value == "":
                        value = None
                else:
                    value = None
            else:  # Required, always prompt
                value = input(f"{param['custom_prompt']}: ")
                if value == "":
                    print(f"{param['name']} is required!")
                    value = input(f"{param['custom_prompt']}: ")
            inputs.append(value)
        FEATURES[choice]["func"](model, *inputs, test_mode=True)
