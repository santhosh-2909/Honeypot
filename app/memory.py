memory = {}

def store_message(session_id, message):
    memory.setdefault(session_id, []).append(message)

def get_conversation(session_id):
    return memory.get(session_id, [])
