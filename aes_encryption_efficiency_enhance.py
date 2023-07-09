from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def aes_encrypt(key, plaintext):
    # Generate a secure random initialization vector (IV)
    iv = default_backend().random_bytes(16)

    # Create a cipher object with AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create an encryptor object
    encryptor = cipher.encryptor()

    # Apply padding and encrypt the plaintext
    padded_plaintext = encryptor.update(plaintext) + encryptor.finalize()

    return iv + padded_plaintext

def aes_decrypt(key, ciphertext):
    # Extract the IV from the ciphertext
    iv = ciphertext[:16]

    # Create a cipher object with AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create a decryptor object
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext and remove padding
    plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()

    return plaintext

# Example usage
key = b'my_secret_key_32bytes'  # 256-bit key
plaintext = b'Hello, AES encryption!'

# Encrypt
ciphertext = aes_encrypt(key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt
decrypted_plaintext = aes_decrypt(key, ciphertext)
print("Decrypted Plaintext:", decrypted_plaintext.decode())
