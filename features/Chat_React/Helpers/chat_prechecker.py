import re
import json

def load_phrases(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load all phrases
GREETING_PHRASES = load_phrases('data/data_sets/phrases/greetings.json')["greetings"]
OPINION_PHRASES = load_phrases('data/data_sets/phrases/opinions.json')["opinions"]
INSULT_PHRASES = load_phrases('data/data_sets/phrases/insults.json')["insults"]
QUESTION_PHRASES = load_phrases('data/data_sets/phrases/questions.json')["questions"]
STREAM_PHRASES = load_phrases('data/data_sets/phrases/streams.json')["streams"]

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text.strip())  # Remove extra spaces
    return text

def contains_phrase(phrases, text):
    for phrase in phrases:
        pattern = r'\b' + re.escape(phrase) + r'\b'
        if re.search(pattern, text):
            return phrase
    return None

def precheck_classify(viewer_input):
    viewer_input_clean = normalize_text(viewer_input)

    match = contains_phrase(OPINION_PHRASES, viewer_input_clean)
    if match:
        print(f"🛡️ Precheck: Detected as Opinion (matched phrase: '{match}')")
        return "Opinion", match

    match = contains_phrase(INSULT_PHRASES, viewer_input_clean)
    if match:
        print(f"🛡️ Precheck: Detected as Insult (matched phrase: '{match}')")
        return "Insult", match

    if viewer_input_clean.endswith("?"):
        print(f"🛡️ Precheck: Detected as Question (matched by '?')")
        return "Question", "?"

    match = contains_phrase(QUESTION_PHRASES, viewer_input_clean)
    if match:
        print(f"🛡️ Precheck: Detected as Question (matched phrase: '{match}')")
        return "Question", match

    match = contains_phrase(GREETING_PHRASES, viewer_input_clean)
    if match:
        print(f"🛡️ Precheck: Detected as Greeting (matched phrase: '{match}')")
        return "Greeting", match

    match = contains_phrase(STREAM_PHRASES, viewer_input_clean)
    if match:
        print(f"🛡️ Precheck: Detected as Stream Related (matched phrase: '{match}')")
        return "StreamRelated", match

    return None, None
