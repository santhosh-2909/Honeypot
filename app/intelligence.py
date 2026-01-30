import re

def extract_intelligence(text: str):
    return {
        "upiIds": re.findall(r"\b\w+@\w+\b", text),
        "phoneNumbers": re.findall(r"\+91\d{10}", text),
        "phishingLinks": re.findall(r"https?://\S+", text),
    }
