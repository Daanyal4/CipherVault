def encrypt(plain_text, rails):
    """
    Encrypt the given plaintext using the Rail Fence cipher with the specified number of rails.
    """
    if not isinstance(rails, int) or rails <= 0:
        return "Invalid number of rails. Please provide a positive integer."

    fence = [[' ' for _ in range(len(plain_text))] for _ in range(rails)]
    direction = -1  # Start moving upwards
    row, col = 0, 0

    for char in plain_text:
        fence[row][col] = char
        if row == 0 or row == rails - 1:
            direction *= -1  # Change direction at the top and bottom rails
        row += direction
        col += 1

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text.replace(' ', '')


def decrypt(cipher_text, rails):
    """
    Decrypt the given ciphertext using the Rail Fence cipher with the specified number of rails.
    """
    if not isinstance(rails, int) or rails <= 0:
        return "Invalid number of rails. Please provide a positive integer."

    fence = [[' ' for _ in range(len(cipher_text))] for _ in range(rails)]
    direction = -1  # Start moving upwards
    row, col = 0, 0

    for _ in range(len(cipher_text)):
        fence[row][col] = '*'
        if row == 0 or row == rails - 1:
            direction *= -1  # Change direction at the top and bottom rails
        row += direction
        col += 1

    idx = 0
    for row in range(rails):
        for col in range(len(cipher_text)):
            if fence[row][col] == '*':
                fence[row][col] = cipher_text[idx]
                idx += 1

    direction = -1  # Start moving upwards
    row, col = 0, 0
    decrypted_text = ""
    for _ in range(len(cipher_text)):
        if fence[row][col] != '*' and (row, col) != (row := row + direction, col):
            decrypted_text += fence[row][col]
    
    return decrypted_text
