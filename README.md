# Hangman
A game of Hangman where user needs to guess the word based on the blank spaces given. - Terminal Version.

*******************************************************************************************************************************

This is one of the old computer games of the time of our childhood. This mini project is a terminal version of the same game. 

Just type 'python Hangman.py' , to start the game.


*******************************************************************************************************************************


Problem Definition:

This game fetches a word from 'words.txt' at random using methods in python. This is our 'secret word' .The number of letters in the secret word is informed to the player. The program asks player for letters of guess. If the guessed letter is present in the secret word, the partial secret word is displayed with the correctly guessed letter at its place(or places, for multiple
occurence of same letter.) and rest of places are filled with underscore.

If the guess is wrong, the number of guesses the player can make decreases. The number of guesses the player gets in the game here is 8.

We can however change it in the code.

The code is present in 'Hangman.py' file.

The role of every function in the code is explained in the beginning of every function in 'Function significance'.


*******************************************************************************************************************************
