def encrypt(plain_text, key):
    key = key.upper()
    encrypted_text = ""
    key_len = len(key)
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_len]
            key_shift = ord('A')
            encrypted_char = chr(((ord(char) - shift + ord(key_char) - key_shift) % 26) + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    key = key.upper()
    decrypted_text = ""
    key_len = len(key)
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_len]
            key_shift = ord('A')
            decrypted_char = chr(((ord(char) - shift - (ord(key_char) - key_shift)) % 26) + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
