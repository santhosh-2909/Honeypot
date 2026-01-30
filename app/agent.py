# app/agent.py

def agent_reply(message, conversation_history=None, metadata=None):
    """
    Autonomous honeypot agent reply
    """

    # Touch variables so linters know they are intentional
    conversation_history = conversation_history or []
    metadata = metadata or {}

    text = message.get("text", "").lower()

    if any(word in text for word in ["blocked", "verify", "account", "upi", "bank"]):
        reply = "I just got this message. What exactly do I need to do?"
    else:
        reply = "Can you please explain? I don’t understand."

    return {
        "status": "success",
        "reply": reply
    }
