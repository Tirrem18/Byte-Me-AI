import os  # Access environment variables
import sys  # For clean system exit
from features.chat_react import chat_react  # Import chat-react feature
from features.story_time import story_time  # Import story-time feature

def run_mode_manager():
    """
    Main controller that decides which ByteMeAI mode and feature to run.
    """

    # Load mode and feature from environment variables; set defaults if not defined
    mode = os.getenv("MODE", "Production")
    feature = os.getenv("FEATURE", "Chat-React")

    print(f"Mode: {mode} | Feature: {feature}")

    # Mapping of feature names to their run() functions
    feature_funcs = {
        "chat-react": chat_react.run,
        "story-time": story_time.run,
        # ➕ Add more features here later
    }

    # List of features that are READY for testing
    testable_features = {"chat-react"}  # Only Chat-React is ready for test mode

    # Find the function for the selected feature
    feature_func = feature_funcs.get(feature.lower())

    if not feature_func:
        print(f"[ERROR] Unknown feature '{feature}'. Exiting.")
        sys.exit(1)

    if mode.lower() == "production":
        # Production Mode — Main runtime logic goes here (not yet implemented)
        print("[TODO] Production logic not implemented yet.")
    elif mode.lower() == "test":
        if feature.lower() in testable_features:
            feature_func(test_mode=True)  # Run feature in test mode
        else:
            print(f"[TODO] Test mode for feature '{feature}' is not implemented yet.")
    else:
        print(f"[ERROR] Unknown mode '{mode}'. Exiting.")
        sys.exit(1)
