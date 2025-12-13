"""
cipher_engine.py
----------------
Adaptive Caesar Cipher engine for all printable ASCII characters.
Provides encryption and decryption functions with key validation.
"""

START = 32    # ASCII code for space character
END = 126     # ASCII code for '~' character
TOTAL = END - START + 1  # Total printable characters (95)


def encrypt(text: str, key: int) -> str:
    """Encrypt text using adaptive Caesar cipher with a numeric key."""
    if not isinstance(key, int):
        raise TypeError("Key must be an integer")
    if key < 0:
        raise ValueError(f"Key must be a positive integer")
    
    # Allow keys larger than TOTAL, wrap them around
    key = key % TOTAL

    result = ""
    for char in text:
        if START <= ord(char) <= END:
            # Shift character forward within printable ASCII range
            shifted = (ord(char) - START + key) % TOTAL + START
            result += chr(shifted)
        else:
            # Non-printable chars remain unchanged
            result += char
    return result


def decrypt(text: str, key: int) -> str:
    """Decrypt text encrypted with adaptive Caesar cipher using the same key."""
    if not isinstance(key, int):
        raise TypeError("Key must be an integer")
    if key < 0:
        raise ValueError(f"Key must be a positive integer")

    # Allow keys larger than TOTAL, wrap them around
    key = key % TOTAL

    result = ""
    for char in text:
        if START <= ord(char) <= END:
            # Shift character backward within printable ASCII range
            shifted = (ord(char) - START - key) % TOTAL + START
            result += chr(shifted)
        else:
            result += char
    return result


if __name__ == "__main__":
    # Simple self-test to verify encryption/decryption
    sample_text = "Hello, Swapnil!"
    key = 10

    cipher = encrypt(sample_text, key)
    print(f"Encrypted: {cipher}")

    decrypted = decrypt(cipher, key)
    print(f"Decrypted: {decrypted}")
