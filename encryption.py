import string

def encrypt_text(text, shift):
    alphabet = string.ascii_letters

    encrypted_text = ''
    for char in text:
        if char not in alphabet:
            encrypted_text += char
            continue
        index = alphabet.find(char)
        encrypted_text += alphabet[(index + shift) % len(alphabet)]

    return encrypted_text