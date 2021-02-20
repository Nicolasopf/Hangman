#!/usr/bin/python3
from os import system
from random import randint


class Hangman:
    body = 0
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    word = ""

    def __init__(self, word=""):
        """ Constructor to set word to a random word of wordlist.txt """
        word = self.get_word()

    def input_loop(self):
        """ Infinite loop to get the letters """
        while 1:
            letter = input("Letter: ")
            try:
                self.check_letter(letter)
            except EOFError:
                pass

    def check_letter(self, letter):
        """ Check if the letter is a letter
        Also check if it is in the word.
        """
        if len(letter) != 1 or letter.isalpha() is False:
            print("It must be a letter!")

    def clean(self):
        """ Clear the screen """
        system('clear')

    def show_word(self, word):
        """ Show the word playing """
        print(word)

    def get_word(self):
        """ Gets the word to play with """
        line = randint(0, 50000)
        with open("wordlist.txt", "r") as file:
            text_lines = file.readlines()
            word = text_lines[line]
        self.show_word(word)
        return word

    def __str__(self):
        """ Prints the body and clean the screan """
        self.clean()
        return self.HANGMANPICS[self.body]


cuerpo = Hangman()
cuerpo.input_loop()
