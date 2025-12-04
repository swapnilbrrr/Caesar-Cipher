"""
Utility helpers used across the Caesar Cipher project.
"""

def normalize_text(text: str) -> str:
    """Return text converted to lowercase for uniform analysis."""
    return text.lower()


def count_characters(text: str) -> dict:
    """Return a frequency dictionary of characters in the given text."""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


def percentage(part: int, whole: int) -> float:
    """Return percentage value with safe zero-division handling."""
    if whole == 0:
        return 0.0
    return (part / whole) * 100
