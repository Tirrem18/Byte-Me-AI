import json

# Load template and styles from files
def load_base_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_style_instructions(style_path):
    with open(style_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_prompt(viewer_input, category, base_template, style_instructions):
    style_instruction = style_instructions.get(category, style_instructions.get("Other", ""))
    return base_template.format(style_instruction=style_instruction, viewer_input=viewer_input)
