# Hangman

I developed the Hangman game in the CLI, hope you like it, you can play offline (obviously) and the words are only in english.

### Installing

Clone the repository to your machine

```
https://github.com/Nicolasopf/Hangman.git
```

Then just run the game!
```
python3 main.py
```

## Using

You will get a random word from the wordlist.txt file with +50000 words in english. You need to type letters trying to guess which letters left.
If you type a wrong letter, the Hangman will show how he is going to the death slowly.

## Example

Run the game and you will get into a prompt that you will see as below:

```
_ _ _ _ _ _ _ _ _
Letter:
```

Just type letters, trying to guess which is correct, if you get a correct answer, all the letters of the word will be shown.
If you type a wrong letter, you will drive this poor man to the death.

Example of the hangman when you have some wrong letters:
```

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

b a _ _ _ _ _ _ _
Letter:
```

## Authors

* **Nicolas Felipe U.R** - nico15935746@gmail.com
