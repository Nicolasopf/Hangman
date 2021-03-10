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
        self.underscore = ['_'] * (len(self.word) - 1)
        self.tried = 0
        self.correct = 0
        self.tried_letters = ""

    def input_loop(self):
        """ Infinite loop to get the letters """
        while 1:
            try:
                if "_" not in self.underscore:
                    print("\n\nYOU WIN! CONGRATULATIONS! THE WORD\
 WAS: ", self.word)
                    input_for_play = input("Do you want to play again? (Y/y for\
 yes, other letter = no): ")
                    if input_for_play is "Y" or input_for_play is "y":
                        self.clean()
                        self.__init__()
                    else:
                        exit()
                for i in self.underscore:
                    print(i, end=" ")
                print()
                print("Tried: " + self.tried_letters)
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
            return
        elif letter in self.word:
            self.set_in(letter)
            self.clean()
        else:
            self.tried_letters += "{} ".format(letter)
            self.tried += 1
            print(self.hang_count())
            print()

    def set_in(self, letter):
        """ Set the letters where it should be in underscores """
        for i in range(len(self.word) - 1):
            if self.word[i] == letter:
                self.underscore[i] = self.word[i]
        return

    def clean(self):
        """ Clear the screen """
        system('clear')

    def get_word(self):
        """ Gets the word to play with """
        line = randint(0, 58108)
        with open("wordlist.txt", "r") as file:
            text_lines = file.readlines()
            word = text_lines[line]
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
                self.__init__()
            else:
                exit()


cuerpo = Hangman()
cuerpo.input_loop()
