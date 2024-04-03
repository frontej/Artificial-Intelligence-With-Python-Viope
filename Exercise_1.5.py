#In this exercise create two functions

#my_split : which splits sentence given as first argument using second argument as a separator character to separate list items. Function returns a list of items.
#my_join : which joins list given as first argument to a string separated with character given as second argument. Function returns a string.
#In this exercise you are not allowed to use Python split and join functions.

def my_split(sentence, separator):
    word = ''
    words = []
    for char in sentence:
        if char != separator:
            word += char
        else:
            words.append(word)
            word = ''
    words.append(word)
    return words

def my_join(words, separator):
    sentence = ''
    for i in range(len(words)):
        if i != 0:
            sentence += separator
        sentence += words[i]
    return sentence

sentence =str(input("Please enter sentence:"))
print(my_join(my_split(sentence, ' '),','))
print(my_join(my_split(sentence, ' '),'\n'))
