"""
main.py
--------
Command-line interface for the adaptive Caesar cipher engine.

Connects:
    • cipher_engine.encrypt()
    • cipher_engine.decrypt()
    • analyzer.calculate_frequencies()
    • analyzer.score_text_by_frequency()
    • utils.normalize_text()

Provides:
    - Caesar encryption
    - Caesar decryption
    - Frequency analysis
"""

from cipher_engine import encrypt, decrypt
from analyzer import calculate_frequencies, score_text_by_frequency
from breaker import break_cipher
from utils import normalize_text


def show_menu():
    """Display available commands."""
    print("\n=== CAESAR CIPHER TOOL ===")
    print("1) Encrypt text")
    print("2) Decrypt text")
    print("3) Break cipher")
    print("4) Frequency analysis")
    print("0) Exit")
    print("===========================")


def run():
    """Main application loop."""
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        # Exit
        if choice == "0":
            print("Exiting...")
            break

        # Encrypt
        elif choice == "1":
            text = input("Enter plaintext: ")
            key = int(input("Enter numeric key (0–94): "))
            result = encrypt(text, key)
            print(f"\nEncrypted Output:\n{result}")

        # Decrypt
        elif choice == "2":
            text = input("Enter ciphertext: ")
            key = int(input("Enter numeric key (0–94): "))
            result = decrypt(text, key)
            print(f"\nDecrypted Output:\n{result}")

        # Break Cipher
        elif choice == "3":
            text = input("Enter ciphertext to break: ")
            result = break_cipher(text)
            print("\n--- Cipher Broken ---")
            print(f"Best Key Found: {result['key']}")
            print(f"Recovered Plaintext: {result['plaintext']}")
            print(f"Confidence Score: {result['score']:.2f} (lower is better)")

        # Frequency Analysis
        elif choice == "4":
            text = input("Enter text to analyze: ")
            cleaned = normalize_text(text)
            freqs = calculate_frequencies(cleaned)
            score = score_text_by_frequency(cleaned)

            print("\n--- Frequency Analysis ---")
            print("Letter % frequencies (sorted):")
            for letter, pct in sorted(freqs.items(), key=lambda x: x[1], reverse=True):
                print(f"  {letter}: {pct:.2f}")

            print(f"\nEnglish similarity score: {score:.2f} (lower = more like English)")

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run()
