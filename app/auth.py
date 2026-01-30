import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("HONEY_POT_API_KEY")

def verify_api_key(x_api_key: str = Header(...)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key
