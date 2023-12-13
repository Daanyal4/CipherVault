def encrypt(plain_text, rows, cols):
    """
    Encrypt the given plaintext using a basic transposition cipher with the specified number of rows and columns.
    """
    # Check if the product of rows and columns is equal to the length of the plaintext
    if rows * cols != len(plain_text):
        raise ValueError("Number of rows times number of columns must equal the text length")

    # Create a matrix by arranging characters from the plaintext
    matrix = [[plain_text[idx] for idx in range(i, len(plain_text), cols)] for i in range(cols)]
    
    # Flatten the matrix into a string and return the result
    encrypted_text = ''.join(''.join(row) for row in matrix)
    return encrypted_text

def decrypt(cipher_text, rows, cols):
    """
    Decrypt the given ciphertext using a basic transposition cipher with the specified number of rows and columns.
    """
    # Check if the product of rows and columns is equal to the length of the ciphertext
    if rows * cols != len(cipher_text):
        raise ValueError("Number of rows times number of columns must equal the text length")

    # Create a matrix by arranging characters from the ciphertext
    matrix = [[cipher_text[idx] for idx in range(i, len(cipher_text), rows)] for i in range(rows)]

    # Flatten the matrix into a string and return the result
    decrypted_text = ''.join(''.join(row) for row in matrix)
    return decrypted_text
