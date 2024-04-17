import string

class EncryptionSystem:
    def __init__(self):
        pass

    def encrypt_text(text, shift):
        alphabet = string.ascii_letters

        encrypted_text = ''
        for char in text:
            if not char.isalpha():
                encrypted_text += char
                continue
            index = alphabet.find(char)
            encrypted_text += alphabet[(index + shift) % len(alphabet)]

        return encrypted_text
    
    def decrypt_text(encrypted_text, original_shift):
        alphabet = string.ascii_letters

        decrypted_text = ''
        for char in encrypted_text:
            if not char.isalpha():
                decrypted_text += char
                continue

            index = alphabet.find(char)
            decrypted_text += alphabet[(index - original_shift) % len(alphabet)]

        return decrypted_text