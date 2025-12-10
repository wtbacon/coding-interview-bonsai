import re


def remove_non_alphanumeric(s: str):
    """Remove non-alphanumeric characters from a string"""
    return re.sub(r"[^a-zA-Z0-9]", "", s)
