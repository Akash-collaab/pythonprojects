def replace_word():

    str = "yo bro, who got you smile like that"
    word_to_be_replace = input("Enter the word to which you want to replace")
    word_replacement = input("Enter the word which you want to put on the relaceable word")
    print(str.replace(word_to_be_replace, word_replacement))

print(str)
replace_word()