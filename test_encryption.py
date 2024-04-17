from encryption import EncryptionSystem

first_text = EncryptionSystem.encrypt_text("Why so Serious?", 16)
print(first_text)

second_text = EncryptionSystem.encrypt_text("Are you hungry?", -12)
print(second_text)