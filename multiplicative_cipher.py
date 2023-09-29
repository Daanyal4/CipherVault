def encrypt(plain_text, key):
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
    # Find the modular multiplicative inverse of the key
    for i in range(1, 26):
        if (key * i) % 26 == 1:
            modular_inverse = i
            break

    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((ord(char) - shift) * modular_inverse % 26) + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
