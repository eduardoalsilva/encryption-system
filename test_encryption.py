from encryption import encrypt_text

first_text = encrypt_text("Why so Serious?", 16)
print(first_text)

second_text = encrypt_text("Are you hungry?", -12)
print(second_text)