import ciphers

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
    while True:
        print("For text encryption/decryption choose 1")
        print("To exit choose 2")

        choice = input("Enter your choice: ")

        if choice == "1":
            ciphers.get_cipher_input()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
