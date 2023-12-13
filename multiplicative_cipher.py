def encrypt(plain_text, key):
    """
    Encrypt the given plaintext using the Multiplicative cipher with the provided key.
    """
    if not isinstance(key, int) or key < 0 or key >= 26:
        return "Invalid key: Key must be an integer between 0 and 25."
    
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(((ord(char) - shift) * key % 26) + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    """
    Decrypt the given ciphertext using the Affine cipher with the provided key.
    """
    if not isinstance(key, int) or key < 0 or key >= 26:
        return "Invalid key: Key must be an integer between 0 and 25."
    
    # Find the modular multiplicative inverse of the key
    for i in range(1, 26):
        if (key * i) % 26 == 1:
            modular_inverse = i
            break
        else:
            return "Invalid key: Key and 26 must be coprime."

    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((ord(char) - shift) * modular_inverse % 26) + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
