from dotenv import load_dotenv
from config.model_loader import load_model
from core.mode_manager.mode_manager import ModeManager 


def main():
    load_dotenv()
    print("ByteMeAI is starting...")

    # ✅ Load model once
    print("⏳ Loading model...")
    model = load_model()
    print("✅ Model loaded.")

    # 🧠 Pass model to mode manager
    manager = ModeManager(model)
    manager.run()

if __name__ == "__main__":
    main()
