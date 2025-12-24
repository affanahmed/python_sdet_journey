def count_errors(text: str) -> int:
    if text is None:
        raise ValueError("text cannot be None")
    return text.count("ERROR")
