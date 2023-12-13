def encrypt(plain_text: str, key: str) -> str:
    """
    Encrypt the given plaintext using the Vigenere cipher with the provided key.
    """
    key = key.upper()
    key_len = len(key)
    encrypted_text = ""
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index]
            key_shift = ord('A')
            encrypted_char = chr(((ord(char) - shift + ord(key_char) - key_shift) % 26) + shift)
            encrypted_text += encrypted_char
            key_index = (key_index + 1) % key_len
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(cipher_text: str, key: str) -> str:
    """
    Decrypt the given ciphertext using the Vigenere cipher with the provided key.
    """
    key = key.upper()
    key_len = len(key)
    decrypted_text = ""
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index]
            key_shift = ord('A')
            decrypted_char = chr(((ord(char) - shift - (ord(key_char) - key_shift)) % 26) + shift)
            decrypted_text += decrypted_char
            key_index = (key_index + 1) % key_len
        else:
            decrypted_text += char

    return decrypted_text
