def encrypt(plain_text, key):
    """
    Encrypt the given plaintext using the columnar transposition cipher with the provided key.
    """
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = ""

    for col in key_order:
        for row in range(0, len(plain_text), len(key)):
            if row + col < len(plain_text):
                encrypted_text += plain_text[row + col]

    return encrypted_text

def decrypt(cipher_text, key):
    """
    Decrypt the given ciphertext using the columnar transposition cipher with the provided key.
    """
    if not key or len(set(key)) != len(key):
        return "Invalid key: Key must be non-empty and contain unique characters."
    
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cols = len(key)
    rows = -(-len(cipher_text) // cols)  # Ceiling division

    # Calculate the number of characters in the last column
    last_col_chars = len(cipher_text) % cols

    # Create a list of lists to represent the grid
    grid = [['' for _ in range(rows)] for _ in range(cols)]

    idx = 0
    for col in key_order:
        num_chars = rows if col < last_col_chars else rows - 1
        for row in range(num_chars):
            grid[col][row] = cipher_text[idx]
            idx += 1

    decrypted_text = ""
    for row in range(rows):
        for col in key_order:
            decrypted_text += grid[col][row]

    return decrypted_text
