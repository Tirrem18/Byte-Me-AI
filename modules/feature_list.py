from modules.chat_reacts.chat_reacts import chat_react_run

from modules.story_time.story_time import story_time_run

# Add more as needed

FEATURES = {
    "chat-react": chat_react_run,
    "story-time": story_time_run,
    # etc.
}
