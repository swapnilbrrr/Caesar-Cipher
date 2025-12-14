"""
breaker.py
----------
Attempts to automatically break a Caesar cipher by testing all possible shifts
and scoring each candidate using frequency analysis.
"""

from cipher_engine import decrypt
from analyzer import score_text_by_frequency


def break_cipher(ciphertext: str) -> dict:
    """
    Attempts to determine the most likely decryption key for the given ciphertext.
    Tests all possible shifts (0-94) and selects the one with the lowest frequency score.
    
    Returns a dictionary:
        {
            "key": best_key,
            "plaintext": best_plaintext,
            "score": best_score
        }
    """
    best_key = None
    best_score = float("inf")
    best_plaintext = ""

    for key in range(95):  # Full ASCII printable range used by cipher_engine
        candidate = decrypt(ciphertext, key)
        score = score_text_by_frequency(candidate)

        if score < best_score:
            best_key = key
            best_score = score
            best_plaintext = candidate

    return {
        "key": best_key,
        "plaintext": best_plaintext,
        "score": best_score
    }


if __name__ == "__main__":
    # Demo run
    encrypted = "Lipps${svph"  # 'Hello World' shifted by key 4
    result = break_cipher(encrypted)

    print("--- Cipher Breaker Demo ---")
    print(f"Ciphertext: {encrypted}")
    print(f"Best Key: {result['key']}")
    print(f"Recovered Plaintext: {result['plaintext']}")
    print(f"Score: {result['score']:.2f}")
