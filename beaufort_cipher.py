def encrypt(plain_text: str, key: str) -> str:
    """
    Encrypt the given plaintext using the Beaufort cipher with the provided key.
    """
    key = key.upper()
    encrypted_text = ""

    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[i % len(key)]
            key_shift = ord('A')
            encrypted_char = chr(((ord(key_char) - key_shift) - (ord(char) - shift)) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(cipher_text, key):
    """
    Decrypt the given ciphertext using the Beaufort cipher with the provided key.
    """
    # Beaufort encryption and decryption are the same
    return encrypt(cipher_text, key)  