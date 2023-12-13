def mod_inverse(a, m):
    """
    Calculate the modular inverse of 'a' modulo 'm'.
    """
    if m < 2:
        return None
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(plain_text, a, b):
    """
    Encrypt a given plaintext using the affine cipher.
    """
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(((a * (ord(char) - shift) + b) % 26) + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, a, b):
    """
    Decrypt a given ciphertext using the affine cipher.
    """
    # Calculate the modular inverse of 'a'
    modular_inverse = mod_inverse(a, 26)
    if modular_inverse is None:
        return "Invalid key 'a'"

    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            # Decrypt the character using the modular inverse
            decrypted_char = chr(((modular_inverse * (ord(char) - shift - b)) % 26) + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
