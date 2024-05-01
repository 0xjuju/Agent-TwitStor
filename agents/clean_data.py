import re


def start_text_at_word(text: str, start_word: str, stop_word=None):

    if not stop_word:
        pattern = f"({re.escape(stop_word)}.*)"
    else:
        pattern = f"({re.escape(start_word)}.*?)(?={re.escape(stop_word)})"

    matched_pattern = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if matched_pattern:
        return matched_pattern.group(1)
    else:
        return None


def split_clean_data(text, delimiter):
    split_data = text.split(delimiter)
    split_data = map(lambda s: s.strip(), split_data)
    return [i for i in split_data if i != ""]

















