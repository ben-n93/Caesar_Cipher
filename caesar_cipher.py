import string

from colorama import init, Fore, Style

init(autoreset=True)
ALPHABET_LIST = list(string.ascii_lowercase)
ALPHABET_LIST += string.digits
ALPHABET_LIST += string.punctuation
ALPHABET_LIST_LENGTH = len(ALPHABET_LIST)
ALPHABET_LIST_LENGTH_NEGATIVE = ALPHABET_LIST_LENGTH - (ALPHABET_LIST_LENGTH
                                                        * 2)

def encrypt(encryption_key, plain_text):
    """Encrypt cipher text."""
    encrypted_message = ""
    for letter in plain_text:
        if letter not in ALPHABET_LIST:
            encrypted_message += letter
        elif letter in ALPHABET_LIST:
            plain_letter_index = ALPHABET_LIST.index(letter)
            encrypted_letter_index = plain_letter_index + encryption_key
            try:
                encrypted_message += ALPHABET_LIST[encrypted_letter_index]
            except IndexError:
                # How many characters left before end of alphabet.
                index_difference = ALPHABET_LIST_LENGTH - plain_letter_index
                # Check to see if encryption key extends beyond end of alphabet.
                index_check = index_difference - encryption_key
                # If index check is less than 0 then there are no more chars left
                # in current alphabet.
                while ALPHABET_LIST_LENGTH > index_check < 0:
                    if index_check < 0:
                        index_check = (index_check*-1)
                    if index_check > ALPHABET_LIST_LENGTH:
                        index_check = index_check - ALPHABET_LIST_LENGTH
                encrypted_message += ALPHABET_LIST[index_check]
    return encrypted_message


def decrypt(encryption_key, cipher_text):
    """Decrypting ciphertext."""
    decrypted_message = ""
    for letter in cipher_text:
        if letter == " ":
            decrypted_message += letter
        elif letter in ALPHABET_LIST:
            plain_letter_index = ALPHABET_LIST.index(letter)
            decrypted_letter_index = plain_letter_index - encryption_key
            # Check to make sure encryption key hasn't resulted in a negative
            # integer index (which will provide the incorrect plaintext).
            if decrypted_letter_index >= 0:
                decrypted_message += ALPHABET_LIST[decrypted_letter_index]
            # If index integer is less than 0.
            else:
                # Handles the negative integer problem - by adding the alphabet
                # list length, we get the correct index position/integer.
                try:
                    decrypted_letter_index += ALPHABET_LIST_LENGTH
                    decrypted_message += ALPHABET_LIST[decrypted_letter_index]
                # Handles a negative integer problem that can't be handled by
                # the above try block.
                except IndexError:
                    while decrypted_letter_index < ALPHABET_LIST_LENGTH_NEGATIVE:
                        decrypted_letter_index = decrypted_letter_index + ALPHABET_LIST_LENGTH
                    decrypted_message += ALPHABET_LIST[decrypted_letter_index]
        else:
            decrypted_message += letter
    return decrypted_message


def break_cipher(cipher_text, max_key_length=ALPHABET_LIST_LENGTH):
    """ Print all possible plaintext for the provided ciphertext."""
    for possible_key in range(0, max_key_length):
        possible_text = decrypt(possible_key, cipher_text)
        print(f"Encryption key: {possible_key} - Plain text: {Fore.GREEN + possible_text}")


while True:
    request_type = input("Do you want to encrypt, decrypt or break? ")
    if request_type in ("decrypt", "d"):
        try:
            encryption_key_input = int(input("Enter encryption key: "))
        except ValueError:
            print("Please only enter a number.")
            continue
        text_to_decrypt_input = input("Enter text to decipher: ")
        decrypted_text = decrypt(encryption_key_input, text_to_decrypt_input)
        print(f"Decrypted messaged: {Fore.GREEN + decrypted_text}")
    elif request_type in ("encrypt", "e"):
        try:
            key_input = int(input("What key do you want to use? "))
        except ValueError:
            print("Please only enter a number.")
            continue
        text_to_encrypt_input = input("Enter text to encrypt: ")
        encrypted_text = encrypt(key_input, text_to_encrypt_input)
        print(f"Encrypted text: {Fore.RED + encrypted_text}")
    elif request_type in ("break", "b"):
        cipher_text_to_break = input("What's the cipher text? ")
        break_cipher(cipher_text_to_break)
    elif request_type == "exit":
        break
    else:
        continue
