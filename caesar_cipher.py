import string

from colorama import init, Fore, Style

init(autoreset=True)
alphabet_list = list(string.printable)


def encrypt(encryption_key, plain_text):
    """Encrypt cipher text"""
    encrypted_message = ""
    for letter in plain_text:
        if letter == " ":
            encrypted_message += letter
        else:
            plain_letter_index = alphabet_list.index(letter)
            encrypted_letter_index = plain_letter_index + encryption_key
            encrypted_message += alphabet_list[encrypted_letter_index]
    return encrypted_message


def decrypt(encryption_key, cipher_text):
    """Decrypting ciphertext"""
    decrypted_message = ""
    for letter in cipher_text:
        if letter == " ":
            decrypted_message += letter
        else:
            plain_letter_index = alphabet_list.index(letter)
            decrypted_letter_index = plain_letter_index - encryption_key
            decrypted_message += alphabet_list[decrypted_letter_index]
    return decrypted_message


while True:
    request_type = input("Do you want to encrypt or decrypt? ")
    if request_type == 'decrypt' or request_type == 'd':
        try:
            encryption_key_input = int(input("Enter encryption key: "))
        except ValueError:
            print("Please only enter a number.")
            continue
        text_to_decrypt_input = input("Enter text to decipher: ")
        decrypted_text = decrypt(encryption_key_input, text_to_decrypt_input)
        print(f"Decrypted messaged: {Fore.GREEN + decrypted_text}")
    elif request_type == "encrypt" or request_type == "e":
        try:
            key_input = int(input("What key do you want to use? "))
        except ValueError:
            print("Please only enter a number.")
            continue
        text_to_encrypt_input = input("Enter text to encrypt: ")
        encrypted_text = encrypt(key_input, text_to_encrypt_input)
        print(f"Encrypted text: {Fore.RED + encrypted_text}")
    elif request_type == "exit":
        break
    else:
        continue
