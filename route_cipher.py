def encrypt(plain_text, rows, cols):
    if rows * cols != len(plain_text):
        raise ValueError("Number of rows times number of columns must equal the text length")

    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
    idx = 0

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = plain_text[idx]
            idx += 1

    encrypted_text = ""
    for col in range(cols):
        for row in range(rows):
            encrypted_text += matrix[row][col]

    return encrypted_text

def decrypt(cipher_text, rows, cols):
    if rows * cols != len(cipher_text):
        raise ValueError("Number of rows times number of columns must equal the text length")

    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
    idx = 0

    for col in range(cols):
        for row in range(rows):
            matrix[row][col] = cipher_text[idx]
            idx += 1

    decrypted_text = ""
    for row in range(rows):
        for col in range(cols):
            decrypted_text += matrix[row][col]

    return decrypted_text
