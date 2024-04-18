import string

def vigenere(message, key, direction=1):
    alphabet = string.ascii_letters
    key_index = 0

    final_message = ''
    for char in message:
        if not char.isalpha():
            final_message += char
            continue

        key_char = key[key_index % len(key)]
        key_index += 1
        offset = alphabet.find(key_char)
        index = alphabet.find(char)
        final_message += alphabet[(index + offset * direction) % len(alphabet)]

    return final_message

def encrypt_message(message, key):
    return vigenere(message, key)

def decrypt_message(message, key):
    return vigenere(message, key, -1)