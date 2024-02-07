from uzwords import words
import random as r

def get_word(x=0):
    n = r.randint(x,31994)
    r_word = list(words[n])
    return r_word

word = get_word()

def display(user, word):
    arr = []
    while True:
        user = input('Harf kiriting: ')
        for i in word:
            if user == i:
                print(i)
            else:
                print('-')
        return arr

