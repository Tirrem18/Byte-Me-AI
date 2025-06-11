from modules.chat_reacts.chat_reacts import chat_react_run
from modules.story_time.story_time import story_time_run

FEATURES = {
    "chat-react": {
        "func": chat_react_run,
        "params": [
            {"name": "username", "custom_prompt": "Enter username", "optional": True},
            {"name": "chat", "custom_prompt": "Enter chat message", "optional": True}
        ]
    },
    "story-time": {
        "func": story_time_run,
        "params": [
            {"name": "story_prompt", "custom_prompt": "Enter story prompt", "optional": True}
        ]
    }
}

