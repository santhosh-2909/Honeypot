from fastapi import FastAPI, Depends
from app.auth import verify_api_key
from app.detector import detect_scam
from app.agent import agent_reply
from app.memory import store_message
from fastapi import Header, HTTPException
import os

app = FastAPI()

@app.post("/honeypot/message")
def handle_message(payload: dict, _: str = Depends(verify_api_key)):
    session_id = payload["sessionId"]
    message = payload["message"]
    history = payload.get("conversationHistory", [])

    store_message(session_id, message)

    scam_detected = detect_scam(message["text"])

    if scam_detected:
        reply = agent_reply(session_id, history)
    else:
        reply = "Okay, noted."

    return {
        "status": "success",
        "reply": reply
    }
