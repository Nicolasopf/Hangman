#!/usr/bin/python3
from random_word import RandomWords


class Hangman:
    r = RandomWords()
    word = r.get_random_word()
    print(word)
#    def __init__(self):
