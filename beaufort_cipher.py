def encrypt(plain_text, key):
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
    return encrypt(cipher_text, key)  # Beaufort encryption and decryption are the same
