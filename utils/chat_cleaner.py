import re

def clean_reply(reply):
    reply = reply.strip()
    reply = re.sub(r'\([^)]*\)', '', reply)
    reply = re.sub(r'\[[^]]*\]', '', reply)
    reply = re.sub(r'<[^>]*>', '', reply)
    reply = re.sub(r'#\S+', '', reply)
    reply = re.sub(r'(Chat Log|User\d+|Viewer\w*|ByteMeAI)', '', reply, flags=re.IGNORECASE)
    reply = re.sub(r'[^a-zA-Z0-9\s.,!?\'\"-]', '', reply)
    reply = re.sub(r'\s+', ' ', reply).strip()

    if not reply.endswith(('.', '!', '?')):
        reply += '.'

    return reply
