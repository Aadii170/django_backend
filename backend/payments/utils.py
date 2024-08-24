from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib


def encrypt(plainText, workingKey):
    iv = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plainText.encode()) + padder.finalize()

    key = hashlib.md5(workingKey.encode()).digest()
    cipher = ciphers.Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
    encryptor = cipher.encryptor()

    cipherText = encryptor.update(padded_data) + encryptor.finalize()
    return cipherText.hex()


def decrypt(cipherText, workingKey):
    iv = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
    key = hashlib.md5(workingKey.encode()).digest()

    cipher = ciphers.Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
    decryptor = cipher.decryptor()

    encrypted_data = bytes.fromhex(cipherText)
    padded_plainText = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plainText = unpadder.update(padded_plainText) + unpadder.finalize()

    return plainText.decode("utf-8")


# Testing
# workingKey = "ThisIsAKey123"
# plainText = "Hello, World!"

# cipherText = encrypt(plainText, workingKey)
# print(f"Encrypted: {cipherText}")

# decrypted_text = decrypt(cipherText, workingKey)
# print(f"Decrypted: {decrypted_text}")
