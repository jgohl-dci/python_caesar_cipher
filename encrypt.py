text_input = input("Text to encrypt: ")
key_input = int(input("Key to encrypt: "))
cipher_text = ""
decrypt_text = ""
punctuation = ".,!?;:"
german_problems = ["ä", "ü", "ö", "ß"]
german_problems2 = ["ae", "ue", "oe", "ss"]


for letter in text_input:
    if letter == " ":
        cipher_text += " "
    elif letter in punctuation:
        cipher_text += "."
    elif not letter.isalpha():
        cipher_text += ""
    elif letter in german_problems:
        j = 0
        for i in german_problems:
            if letter == i:
                cipher_text += german_problems2[j]
            else:
                j += 1
                
    elif letter.isupper():
        char_pos = ord(letter)
        new_pos = (char_pos + key_input - 65) % 26 + 65
        new_letter = chr(new_pos)
        cipher_text += new_letter
    else:
        char_pos = ord(letter)
        new_pos = (char_pos + key_input - 97) % 26 + 97
        new_letter = chr(new_pos)
        cipher_text += new_letter

print(cipher_text)