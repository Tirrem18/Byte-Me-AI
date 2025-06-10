import os
from ctransformers import AutoModelForCausalLM

def load_model():
    model_path = os.getenv("MODEL_PATH")
    if not model_path:
        raise EnvironmentError("MODEL_PATH not found in .env")

    print(f"⏳ Loading GGUF model from {model_path}...")

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="mistral",
        gpu_layers=9999          
    )

    print("✅ Model Loaded Successfully")
    return model
