import string

from colorama import init, Fore, Style

init(autoreset=True)

ALPHABET = string.ascii_lowercase
ALPHABET_LENGTH = len(ALPHABET)
ALPHABET_LENGTH_NEGATIVE = - ALPHABET_LENGTH


def encrypt(plaintext, encryption_key):
    """Encrypt cipher text."""
    encrypted_letters = []
    for letter in plaintext:
        if letter not in ALPHABET:
            encrypted_letters.append(letter)
        elif letter in ALPHABET:
            plain_letter_index = ALPHABET.index(letter)
            encrypted_letter_index = plain_letter_index + encryption_key
            try:
                encrypted_letters.append(ALPHABET[encrypted_letter_index])
            except IndexError:
                index_difference = ALPHABET_LENGTH - plain_letter_index
                index_check = index_difference - encryption_key
                while ALPHABET_LENGTH <= index_check or index_check < 0:
                    if index_check < 0:
                        index_check = index_check * -1
                    if index_check >= ALPHABET_LENGTH:
                        index_check = index_check - ALPHABET_LENGTH
                    if index_check == ALPHABET_LENGTH:
                        index_check = 0
                encrypted_letters.append(ALPHABET[index_check])
    encrypted_message = "".join(encrypted_letters)
    return encrypted_message


def decrypt(ciphertext, encryption_key):
    """Decrypt ciphertext."""
    decrypted_letters = []
    for letter in ciphertext:
        if letter not in ALPHABET:
            decrypted_letters.append(letter)
        elif letter in ALPHABET:
            plain_letter_index = ALPHABET.index(letter)
            decrypted_letter_index = plain_letter_index - encryption_key
            if decrypted_letter_index >= 0:
                decrypted_letters.append(ALPHABET[decrypted_letter_index])
            else:
                try:
                    decrypted_letter_index += ALPHABET_LENGTH
                    decrypted_letters.append(ALPHABET[decrypted_letter_index])
                except IndexError:
                    while decrypted_letter_index <= ALPHABET_LENGTH_NEGATIVE:
                        decrypted_letter_index = (
                            decrypted_letter_index + ALPHABET_LENGTH
                        )
                    decrypted_letters.append(ALPHABET[decrypted_letter_index])
    decrypted_message = "".join(decrypted_letters)
    return decrypted_message


def brute_force(ciphertext, possible_keys=ALPHABET_LENGTH):
    """Print possible plaintext for the provided ciphertext."""

    for possible_key in range(1, possible_keys):
        possible_text = decrypt(ciphertext, possible_key)
        print(
            f"Encryption key: {possible_key} - Plain text: {Fore.GREEN + possible_text}"
        )


while True:
    request_type = input("Do you want to encrypt, decrypt or break? ")
    if request_type in ("decrypt", "d"):
        try:
            encryption_key_input = int(input("Enter encryption key: "))
        except ValueError:
            print("Please only enter a number.")
            continue
        text_to_decrypt_input = input("Enter text to decipher: ")
        decrypted_text = decrypt(text_to_decrypt_input, encryption_key_input)
        print(f"Decrypted messaged: {Fore.GREEN + decrypted_text}")
    elif request_type in ("encrypt", "e"):
        try:
            key_input = int(input("What key do you want to use? "))
        except ValueError:
            print("Please only enter a number.")
            continue
        text_to_encrypt_input = input("Enter text to encrypt: ")
        encrypted_text = encrypt(text_to_encrypt_input, key_input)
        print(f"Encrypted text: {Fore.RED + encrypted_text}")
    elif request_type in ("break", "b"):
        cipher_text_to_break = input("What's the cipher text? ")
        brute_force(cipher_text_to_break)
    elif request_type == "exit":
        break
    else:
        continue
