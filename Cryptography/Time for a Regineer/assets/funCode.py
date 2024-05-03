import string
import random

def generate_key():
    all_chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    all_chars_list = list(all_chars)
    random.shuffle(all_chars_list)
    return dict(zip(all_chars, all_chars_list))

def encrypt(message, key):
    encrypted = []
    for char in message:
        if char in key:
            encrypted_char = key[char]
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

key = generate_key()
plaintext = "hello world!"
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)