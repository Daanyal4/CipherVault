import ciphers

def print_intro():
    """
    Print an introductory message.
    """
    print ("""
      _____ _       _            __      __         _ _   
     / ____(_)     | |           \ \    / /        | | |  
    | |     _ _ __ | |__   ___ _ _\ \  / /_ _ _   _| | |_ 
    | |    | | '_ \| '_ \ / _ \ '__\ \/ / _` | | | | | __|
    | |____| | |_) | | | |  __/ |   \  / (_| | |_| | | |_ 
     \_____|_| .__/|_| |_|\___|_|    \/ \__,_|\__,_|_|\__|
             | |                                          
             |_|                                          
    """)

def main():
    print_intro()

    while True:
        print("\nMenu:")
        print("E. Text Encryption/Decryption")
        print("X. Exit")

        choice = input("Enter your choice (E or X): ").upper()

        if choice == "E":
            ciphers.get_cipher_input()
        elif choice == "X":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
