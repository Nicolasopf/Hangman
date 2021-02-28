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

    def __init__(self, word=""):
        """ Constructor to set word to a random word of wordlist.txt """
        self.word = self.get_word()
        self.underscore = "_ " * (len(self.word) - 1)
        self.tried = 0
        self.correct = 0

    def input_loop(self):
        """ Infinite loop to get the letters """
        while 1:
            try:
                letter = input("Letter: ")
                self.check_letter(letter)
            except EOFError:
                print()
                return

    def check_letter(self, letter):
        """ Check if the letter is a letter
        Also check if it is in the word.
        """
        if letter == "exit":
            exit()
        elif len(letter) != 1 or letter.isalpha() is False:
            self.clean()
            print("It must be a letter!")
            print(self.underscore)
            return
        elif letter in self.word:
            print("i am")
        else:
            self.tried += 1
            print(self.hang_count())

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

    def hang_count(self):
        """ Prints the body and clean the screan """
        self.clean()
        try:
            return self.HANGMANPICS[self.tried]
        except IndexError:
            print("\n\n\n YOU LOST! THE WORD WAS: {}\n\n\n" .format(self.word))
            input_for_play = input("Do you want to play again? (Y/y for yes,\
            other letter = no): ")
            if input_for_play is "Y" or input_for_play is "y":
                self.clean()
                return(self.__init__())
            else:
                exit()


cuerpo = Hangman()
cuerpo.input_loop()
