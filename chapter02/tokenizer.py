import nltk
from nltk import word_tokenize
nltk.download('punkt_tab')

def tokenize(input):
    word_list = []
    for word in word_tokenize(input):
        word_list.append(word)
    return word_list


input = "What's the best way to split a sentence into words?"
print(tokenize(input))
