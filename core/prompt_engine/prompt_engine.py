import os
import json

class PromptEngine:
    def __init__(self, base_prompt_dir="prompts"):
        self.base_prompt_dir = base_prompt_dir

    def load_persona(self):
        persona_path = os.path.join(self.base_prompt_dir, "persona.txt")
        if os.path.exists(persona_path):
            with open(persona_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        return ""

    def load_generic(self, feature):
        feature_dir = os.path.join(self.base_prompt_dir, feature)
        generic_path = os.path.join(feature_dir, "generic.txt")
        if os.path.exists(generic_path):
            with open(generic_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        return ""

    def load_detailed(self, feature):
        feature_dir = os.path.join(self.base_prompt_dir, feature)
        detailed_json = os.path.join(feature_dir, "detailed.json")
        detailed_txt = os.path.join(feature_dir, "detailed.txt")
        if os.path.exists(detailed_json):
            with open(detailed_json, "r", encoding="utf-8") as f:
                return json.load(f)
        elif os.path.exists(detailed_txt):
            with open(detailed_txt, "r", encoding="utf-8") as f:
                return f.read().strip()
        return None

    def get_prompt(self, feature, context=None, **kwargs):
        """
        Builds a full prompt for a given feature.
        - For .json detailed files: uses context as key
        - For .txt detailed files: fills in kwargs if provided
        """
        persona = self.load_persona()
        generic = self.load_generic(feature)
        detailed = self.load_detailed(feature)

        detailed_part = ""
        # If it's a dict (json): use context as a key, fallback to "Other"
        if isinstance(detailed, dict):
            detailed_part = detailed.get(context, detailed.get("Other", ""))
            # Support for parameterized instructions (optional, advanced)
            if kwargs and "{" in detailed_part:
                try:
                    detailed_part = detailed_part.format(**kwargs)
                except KeyError:
                    pass  # If missing kwarg, leave blank as is
        # If it's a string (txt): fill in kwargs if present
        elif isinstance(detailed, str):
            if kwargs and "{" in detailed:
                try:
                    detailed_part = detailed.format(**kwargs)
                except KeyError:
                    detailed_part = detailed  # If not all blanks filled, return template
            else:
                detailed_part = detailed

        # Compose the final prompt (remove empty parts)
        prompt_parts = [persona, generic, detailed_part]
        return "\n\n".join([part for part in prompt_parts if part])

# --- End of PromptEngine ---
