SCAM_KEYWORDS = [
    "account blocked", "verify immediately",
    "upi", "bank account", "urgent",
    "click link", "otp"
]

def detect_scam(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in SCAM_KEYWORDS)
