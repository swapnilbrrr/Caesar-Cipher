"""
Unit tests for the Caesar Cipher engine.
Validates encryption, decryption, and edge-case behavior.
"""

import unittest
from src.cipher_engine import encrypt, decrypt, TOTAL


class TestCipherEngine(unittest.TestCase):

    def test_basic_encryption(self):
        self.assertEqual(encrypt("abc", 1), "bcd")
        self.assertEqual(encrypt("Hello", 5), "Mjqqt")

    def test_basic_decryption(self):
        encrypted = encrypt("Swapnil", 10)
        self.assertEqual(decrypt(encrypted, 10), "Swapnil")

    def test_full_ascii_range(self):
        sample = "".join(chr(i) for i in range(32, 127))
        encrypted = encrypt(sample, 20)
        decrypted = decrypt(encrypted, 20)
        self.assertEqual(sample, decrypted)

    def test_key_wrapping(self):
        # A key of 0 should produce no change
        self.assertEqual(encrypt("A", 0), "A")
        # A key equal to the total number of characters should wrap around to 0
        self.assertEqual(encrypt("A", TOTAL), "A")

    def test_invalid_key_type(self):
        with self.assertRaises(TypeError):
           encrypt("test", "5")  # type: ignore

    def test_invalid_key_value(self):
        with self.assertRaises(ValueError):
            encrypt("test", -1)
        # No longer raises ValueError for key > TOTAL, as it now wraps
        # with self.assertRaises(ValueError):
        #     encrypt("test", TOTAL + 5)


if __name__ == "__main__":
    unittest.main()
