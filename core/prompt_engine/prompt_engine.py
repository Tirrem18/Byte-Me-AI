import os
import json

class PromptEngine:
    def __init__(self, base_prompt_dir="prompts"):
        self.base_prompt_dir = base_prompt_dir

    def load_persona(self):
        # Load the universal persona prompt
        persona_path = os.path.join(self.base_prompt_dir, "persona.txt")
        with open(persona_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    def load_feature_prompt(self, feature_name):
        # Try to load feature-specific prompt (supports .json or .txt)
        feature_dir = os.path.join(self.base_prompt_dir, feature_name)
        for filename in ["persona.txt", "tailored_response.json", "prompt.txt"]:
            file_path = os.path.join(feature_dir, filename)
            if os.path.exists(file_path):
                if filename.endswith(".json"):
                    with open(file_path, "r", encoding="utf-8") as f:
                        return json.load(f)  # Might be dict
                else:
                    with open(file_path, "r", encoding="utf-8") as f:
                        return f.read().strip()
        return ""

    def load_style_instructions(self, feature_name, style=None):
        # Optionally load style/extra instructions
        style_file = os.path.join(self.base_prompt_dir, feature_name, "styles.json")
        if style and os.path.exists(style_file):
            with open(style_file, "r", encoding="utf-8") as f:
                styles = json.load(f)
                return styles.get(style, "")
        return ""

    def build_prompt(self, feature_name, style=None):
        # Compose the full prompt in order: persona > feature > style
        parts = [
            self.load_persona(),
            self.load_feature_prompt(feature_name),
            self.load_style_instructions(feature_name, style)
        ]
        # If any part is a dict (from JSON), flatten to string as needed:
        return "\n\n".join([p if isinstance(p, str) else json.dumps(p, indent=2) for p in parts if p])

# Usage:
# engine = PromptEngine()
# prompt = engine.build_prompt("chat-response", style="insult")
# print(prompt)
