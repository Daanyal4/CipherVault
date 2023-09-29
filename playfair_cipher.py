def build_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: 'J' is omitted in the Playfair cipher

    # Initialize a 5x5 matrix with empty strings
    matrix = [['' for _ in range(5)] for _ in range(5)]

    # Fill the matrix with the unique letters from the key and remaining alphabet
    used_letters = set()
    row, col = 0, 0

    for char in key + alphabet:
        char = char.upper()
        if char not in used_letters:
            matrix[row][col] = char
            used_letters.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix

def find_char_positions(matrix, char):
    positions = []
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                positions.append((row, col))
    return positions

def encrypt(plain_text, key):
    key_matrix = build_playfair_matrix(key)
    plain_text = plain_text.replace(" ", "").upper()
    encrypted_text = ""
    i = 0

    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
        
        if char1 == char2:
            char2 = 'X'
            i -= 1
        
        row1, col1 = find_char_positions(key_matrix, char1)[0]
        row2, col2 = find_char_positions(key_matrix, char2)[0]

        if row1 == row2:  # Same row
            encrypted_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:  # Forming a rectangle
            encrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
        
        i += 2

    return encrypted_text

def decrypt(cipher_text, key):
    key_matrix = build_playfair_matrix(key)
    decrypted_text = ""
    i = 0

    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]

        row1, col1 = find_char_positions(key_matrix, char1)[0]
        row2, col2 = find_char_positions(key_matrix, char2)[0]

        if row1 == row2:  # Same row
            decrypted_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:  # Forming a rectangle
            decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]

        i += 2

    return decrypted_text
