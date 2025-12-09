import re

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^а-яa-z0-9\s]", "", text)
    return text.strip()