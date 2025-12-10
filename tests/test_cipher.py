"""
Unit tests for the Caesar Cipher engine.
Validates encryption, decryption, and edge-case behavior.
"""

import unittest
from cipher_engine import encrypt, decrypt, TOTAL


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
        self.assertEqual(encrypt("A", TOTAL), "A")     # key == TOTAL → no shift
        self.assertEqual(decrypt("A", TOTAL), "A")

    def test_invalid_key_type(self):
        with self.assertRaises(TypeError):
           encrypt("test", "5")  # type: ignore

    def test_invalid_key_value(self):
        with self.assertRaises(ValueError):
            encrypt("test", -1)
        with self.assertRaises(ValueError):
            encrypt("test", TOTAL + 5)


if __name__ == "__main__":
    unittest.main()
