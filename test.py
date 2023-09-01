char_pos = 75
key_input = 15



print(char_pos + key_input - 65)
print((char_pos + key_input - 65) % 26)
print((char_pos + key_input - 65) % 26 + 65)



'''
74 + 15 = 89 - 65 = 24 / 26 = 24 + 65 = 89
75 + 15 = 90 - 65 = 25 / 26 = 25 + 65 = 90
76 + 15 = 91 - 65 = 26 / 26 = 0 + 65 = 65
77 + 15 = 92 - 65 = 27 / 26 = 1 + 65 = 66

'''