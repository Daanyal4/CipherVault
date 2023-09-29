def encrypt(plain_text):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord('Z') - (ord(char) - shift)) if char.isupper() else (ord('z') - (ord(char) - shift)))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text):
    return encrypt(cipher_text)  # Atbash encryption and decryption are the same
