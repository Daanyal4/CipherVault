def encrypt(plain_text, key):
    """
    Encrypt the given plaintext using the Caesar cipher with the provided key.
    """
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar cipher encryption formula
            encrypted_char = chr(((ord(char) - shift + key) % 26) + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    """
    Decrypt the given ciphertext using the Caesar cipher with the provided key.
    """
    # To decrypt, use the negative of the key in the encryption function
    return encrypt(cipher_text, -key)
