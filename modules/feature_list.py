from modules.chat_reacts.chat_reacts import chat_react_run
from modules.story_time.story_time import story_time_run

FEATURES = {
    "chat-react": {
        "func": chat_react_run,
        "params": ["username", "chat"]
    },
    "story-time": {
        "func": story_time_run,
        "params": []
    },
    # etc.
}
