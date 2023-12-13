import caesar_cipher
import multiplicative_cipher
import affine_cipher
import columnar_transposition_cipher
import rail_fence_cipher
import playfair_cipher
import vigenere_cipher
import autokey_cipher
import atbash_cipher
import route_cipher
import beaufort_cipher

def print_cipher_list():
    """
    Print a list of available ciphers along with their descriptions.
    """
    print("Available Ciphers:")
    print("1. Caesar Cipher: Simple substitution with a fixed shift.")
    print("2. Multiplicative Cipher: A substitution cipher using multiplication.")
    print("3. Affine Cipher: Combines multiplication and addition in a substitution cipher.")
    print("4. Columnar Transposition Cipher: Rearranges text using a grid of columns.")
    print("5. Rail Fence Cipher: Encrypts text in a zigzag pattern.")
    print("6. Playfair Cipher: Uses a 5x5 grid of letters for encryption.")
    print("7. Vigenère Cipher: A polyalphabetic cipher using a keyword.")
    print("8. Autokey Cipher: Extends the Vigenère cipher using the plaintext as part of the key.")
    print("9. Atbash Cipher: Simple substitution with reverse alphabet mapping.")
    print("10. Route Cipher: Encrypts text by rearranging in a grid.")
    print("11. Beaufort Cipher: A reciprocal cipher based on the Vigenère cipher.")

def select_cipher(choice):
    """
    Select and return the cipher module based on the user's choice.
    """
    ciphers = {
        1: caesar_cipher,
        2: multiplicative_cipher,
        3: affine_cipher,
        4: columnar_transposition_cipher,
        5: rail_fence_cipher,
        6: playfair_cipher,
        7: vigenere_cipher,
        8: autokey_cipher,
        9: atbash_cipher,
        10: route_cipher,
        11: beaufort_cipher,
    }
    return ciphers.get(choice)

def get_cipher_operation():
    """
    Get the user's choice for encryption or decryption operation.
    """
    print("Choose an operation:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input("Enter the number of the operation: "))
    return choice

def get_key_description(cipher_choice):
    """
    Return the description of the key for the selected cipher.
    """
    key_descriptions = {
        1: "Shift value (0-25)",
        2: "Multiplication factor (must be coprime with 26)",
        3: "Two integers (a and b) for the formula E(x) = (ax + b) % 26",
        4: "A keyword to determine column order",
        5: "Number of rails (2 or more)",
        6: "A keyword (letters only)",
        7: "A keyword (letters only)",
        8: "A keyword (letters only)",
        9: "No key required",
        10: "Route directions (e.g., URDL for Up, Right, Down, Left)",
        11: "A keyword (letters only)",
    }
    return key_descriptions.get(cipher_choice, "Key description not available")

def perform_cipher_operation(cipher, operation, text, key, cipher_choice):
    """
    Perform the encryption or decryption operation based on the user's choice.
    """
    ciphers_requiring_int_key = [1, 2, 3, 5, 10]
    
    if operation == 1:
        if cipher_choice in ciphers_requiring_int_key:
            key = int(input("Enter the key (an integer): "))

        return cipher.encrypt(text, key)
    elif operation == 2:
        if cipher_choice in ciphers_requiring_int_key:
            key = int(input("Enter the key (an integer): "))

        return cipher.decrypt(text, key)

def get_cipher_input():
    """
    Main function to get user input and perform cipher operations.
    """
    while True:
        print_cipher_list()
        choice = int(input("Enter the number of the cipher: "))

        cipher_choice = choice
        cipher = select_cipher(choice)

        if cipher:
            operation = get_cipher_operation()
            key_description = get_key_description(cipher_choice)
            print(f"Key Description: {key_description}")

            key_input_prompt = f"Enter the key ({key_description}): "
            key = input(key_input_prompt)

            text = input("Enter the text: ")

            result = perform_cipher_operation(cipher, operation, text, key, cipher_choice)
            print("Result:")
            print(result)

        choice = input("Do you want to continue (yes/no)? ").strip().lower()
        if choice != "yes":
            break
