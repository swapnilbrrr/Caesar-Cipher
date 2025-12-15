"""
utils.py
--------
Helper functions for text processing and normalization.
"""

import re

def normalize_text(text: str) -> str:
    """
    Prepares text for frequency analysis.

    - Converts to lowercase.
    - Removes all non-alphabetic characters.

    Args:
        text (str): The input string.

    Returns:
        str: The normalized string containing only lowercase letters.
    """
    return re.sub(r'[^a-z]', '', text.lower())
