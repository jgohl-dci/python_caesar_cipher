text_input = input("Text to decrypt: ")
key_input = int(input("Key to decrypt: "))
cipher_text = ""
decrypt_text = ""

for letter in text_input:
    if letter == " ":
        cipher_text += " "
    elif letter.isupper():
        char_pos = ord(letter)
        new_pos = (char_pos - key_input - 65) % 26 + 65
        new_letter = chr(new_pos)
        cipher_text += new_letter
    else:
        char_pos = ord(letter)
        new_pos = (char_pos - key_input - 97) % 26 + 97
        new_letter = chr(new_pos)
        cipher_text += new_letter

print(cipher_text)