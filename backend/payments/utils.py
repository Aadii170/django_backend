# 🔐 Import necessary modules for encryption and padding
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib


# ✨ Function to encrypt plain text using AES encryption
def encrypt(plainText, workingKey):
    # 🧊 Initialization vector (IV) - fixed 16-byte value
    iv = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"

    # 🧼 Padding the plaintext to match AES block size (128 bits)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plainText.encode()) + padder.finalize()

    # 🔑 Create AES key from MD5 hash of workingKey
    key = hashlib.md5(workingKey.encode()).digest()

    # 🛡️ Create AES cipher in CBC mode with key and IV
    cipher = ciphers.Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
    encryptor = cipher.encryptor()

    # 🔄 Perform encryption
    cipherText = encryptor.update(padded_data) + encryptor.finalize()

    # 🔁 Return hex representation of encrypted data
    return cipherText.hex()


# ✨ Function to decrypt cipher text using AES decryption
def decrypt(cipherText, workingKey):
    # 🧊 Same IV used during encryption
    iv = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"

    # 🔑 Recreate the AES key from MD5 of workingKey
    key = hashlib.md5(workingKey.encode()).digest()

    # 🛡️ Create AES cipher in CBC mode with key and IV
    cipher = ciphers.Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
    decryptor = cipher.decryptor()

    # 🔄 Convert hex back to bytes and decrypt
    encrypted_data = bytes.fromhex(cipherText)
    padded_plainText = decryptor.update(encrypted_data) + decryptor.finalize()

    # 🧼 Remove padding after decryption
    unpadder = padding.PKCS7(128).unpadder()
    plainText = unpadder.update(padded_plainText) + unpadder.finalize()

    # ✅ Return the original plain text
    return plainText.decode("utf-8")


# 🧪 Sample test for encryption and decryption (uncomment to test)
# workingKey = "ThisIsAKey123"
# plainText = "Hello, World!"

# cipherText = encrypt(plainText, workingKey)
# print(f"🔒 Encrypted: {cipherText}")

# decrypted_text = decrypt(cipherText, workingKey)
# print(f"🔓 Decrypted: {decrypted_text}")
