import json

def load_usernames(file_path):
    usernames = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            usernames.append(data["username"])
    return usernames
