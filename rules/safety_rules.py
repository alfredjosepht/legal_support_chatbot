FORBIDDEN = ["guilty", "accused", "file fir"]

def sanitize(text: str) -> str:
    for word in FORBIDDEN:
        text = text.replace(word, "")
    return text
