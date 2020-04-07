word = input('Enter a word please')
word_dict = {}


def rahuvailo(word):
    count = 1
    for i in word:
        if i in word_dict:
            count = count + 1
            word_dict[i] = count
        else:
             count = 1
             word_dict[i] = count
    print(word_dict)


rahuvailo(word)
#hello test
assert word_dict == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
