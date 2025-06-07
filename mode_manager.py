
import os  # Access environment variables
import sys  # For clean system exit
from features.chat_react import chat_react  # Import chat-react feature
from features.story_time import story_time  # Import story-time feature
from shared_Functionality.helpers.model_loader import load_model
from dotenv import load_dotenv
load_dotenv()

def run_mode_manager():
    """
    Main controller that decides which ByteMeAI mode and feature to run.
    """

    # Load mode and feature from environment variables
    mode = os.getenv("MODE", "Production")
    feature = os.getenv("FEATURE", "Chat-React")

    print(f"Mode: {mode} | Feature: {feature}")

    # Load the model ONCE here
    model = load_model()

    # Mapping of feature names to their run() functions
    feature_funcs = {
        "chat-react": chat_react.run,
        "story-time": story_time.run,
        # Add more features here later
    }

    # List of features that are READY for testing
    testable_features = {"chat-react"}  # Only Chat-React is ready for test mode

    # Find the function for the selected feature
    feature_func = feature_funcs.get(feature.lower())

    if not feature_func:
        print(f"[ERROR] Unknown feature '{feature}'. Exiting.")
        sys.exit(1)

    if mode.lower() == "production":
        print("[TODO] Production logic not implemented yet.")
    elif mode.lower() == "test":
        if feature.lower() in testable_features:
            feature_func(model, test_mode=True)  # <-- Pass model here
        else:
            print(f"[TODO] Test mode for feature '{feature}' is not implemented yet.")
    else:
        print(f"[ERROR] Unknown mode '{mode}'. Exiting.")
        sys.exit(1)