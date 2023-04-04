import emoji

#ask the user to input the encrypted string with bold text
encrypted_txt = input("\033[1mEnter a string to decrypt: \033[0m")
#replace the encrypted characters in the string to their corresponding letters:
# replace '*' with '*'
# replace '&' with 'e'
# replace '#' with 'i'
# replace '+' with 'o'
# replace '!' with 'u'

decrypted_string = encrypted_txt.replace('*', '*') \
                                .replace('&','e') \
                                .replace('#','i') \
                                .replace('+','o') \
                                .replace('!','u')
                                          
#find the word 'brown' in the decrypted string
brown_word = decrypted_string.find("brown")

#and highlight the word 'brown' with brown color then add emoji at the end of the string
highlighted_word = decrypted_string[:brown_word] + \
"\033[38;2;165;42;42m" + "brown" + "\033[0m" + \
decrypted_string[brown_word + 5:] + \
emoji.emojize(":fox:" + ":person_cartwheeling:" + ":dog_face:")

#print the output
print(" \n\033[1mThe Plain Text: \033[0m" + highlighted_word)