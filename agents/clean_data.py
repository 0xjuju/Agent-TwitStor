import re


def start_text_at_word(text: str, word: str):

    pattern = f"({re.escape(word)}.*)"

    matched_pattern = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if matched_pattern:
        return matched_pattern.group(1)
    else:
        return None



















