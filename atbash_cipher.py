def encrypt(plain_text):
    """
    Encrypt the given plaintext using the Atbash cipher.
    """
    encrypted_text = []
    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            # Calculate the mirror image of the character in the alphabet
            encrypted_char = chr((ord('Z') - (ord(char) - shift)) if char.isupper() else (ord('z') - (ord(char) - shift)))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(cipher_text):
    """
    Decrypt the given ciphertext using the Atbash cipher.
    """
    # Atbash encryption and decryption are the same
    return encrypt(cipher_text) 