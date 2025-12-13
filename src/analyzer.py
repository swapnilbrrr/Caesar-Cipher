"""
analyzer.py
-----------
Frequency analysis tools to measure character distribution in text.
Compares text frequencies against standard English letter frequencies
to assist in cryptanalysis.
"""

def normalize_text(text: str) -> str:
    """Return text converted to lowercase for uniform analysis."""
    return text.lower()

# Standard English letter frequencies (source: Wikipedia/common sources)
ENGLISH_FREQUENCIES = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0,
    'h': 6.1, 'i': 7.0, 'j': 0.15, 'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7,
    'o': 7.5, 'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8,
    'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0, 'z': 0.074
}


def calculate_frequencies(text: str) -> dict:
    """
    Calculates the percentage frequency of each alphabetic character in the text.
    Ignores non-alphabetic characters.
    """
    text = normalize_text(text)
    
    # Count only alphabetic characters
    letter_counts = {}
    total_letters = 0
    for char in text:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
            total_letters += 1

    if total_letters == 0:
        return {}

    # Calculate frequency percentage for each letter
    frequencies = {char: (count / total_letters) * 100 for char, count in letter_counts.items()}
    return frequencies


def score_text_by_frequency(text: str) -> float:
    """
    Scores a text based on its deviation from standard English letter frequencies.
    A lower score indicates a closer match to English.
    """
    text_frequencies = calculate_frequencies(text)
    
    # If no alphabetic characters, deviation is high (bad score)
    if not text_frequencies:
        return 1000.0

    deviation = 0.0
    # Sum the absolute differences between text frequencies and English frequencies
    for letter, freq in ENGLISH_FREQUENCIES.items():
        deviation += abs(text_frequencies.get(letter, 0.0) - freq)
        
    return deviation


if __name__ == "__main__":
    # Example usage to demonstrate the analyzer's capabilities
    
    # 1. A normal English sentence
    english_text = "This is a sample sentence to demonstrate frequency analysis."
    english_score = score_text_by_frequency(english_text)
    english_freqs = calculate_frequencies(english_text)
    
    print("--- Analysis of a standard English sentence ---")
    print(f"Text: '{english_text}'")
    print(f"Frequency Score: {english_score:.2f} (Lower is better)")
    print("Top 5 letter frequencies:")
    for letter, freq in sorted(english_freqs.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"  '{letter}': {freq:.2f}%")
    print("-" * 20)

    # 2. A Caesar-cipher encrypted sentence (should have a high score)
    encrypted_text = "Lipps${svph" # "hello world" with key 4
    encrypted_score = score_text_by_frequency(encrypted_text)
    encrypted_freqs = calculate_frequencies(encrypted_text)

    print("\n--- Analysis of an encrypted sentence ---")
    print(f"Text: '{encrypted_text}'")
    print(f"Frequency Score: {encrypted_score:.2f} (Higher score suggests non-English or encrypted text)")
    print("Top 5 letter frequencies:")
    if encrypted_freqs:
        for letter, freq in sorted(encrypted_freqs.items(), key=lambda item: item[1], reverse=True)[:5]:
            print(f"  '{letter}': {freq:.2f}%")
    else:
        print("  No alphabetic characters found.")
    print("-" * 20)
