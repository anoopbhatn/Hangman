import random	
import string

WORDLIST_FILENAME = "words.txt"			 # Extracts the contents of 'words.txt' and stores it in the variable 'WORDLIST_FILENAME'.
						 # 'words.txt' contains a big number of words that are to be guessed in the game.


def loadWords():
	"""
	Function significance :
	Returns a list of valid words. Words are strings of lowercase letters.
    
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print "Loading word list from file..."   # This prints the message telling that loading may take some time.
						 # inFile: file
	inFile = open(WORDLIST_FILENAME, 'r', 0) # opens the file in read mode and returns file handle to the variable 'inFile'
						 # line: string
	line = inFile.readline() 		 # A string of the contents of the file is returned and stored in variable 'line'
						 # wordlist: list of strings
	wordlist = string.split(line) 		 # a list of words is formed using split() method of string class
	print len(wordlist), "words loaded." 	 # Number of words is printed in the screen
	return wordlist 			 # The list of words is returned


def chooseWord(wordlist):
	"""
	Function significance: 
	wordlist (list): list of words (strings)

	Returns a word from wordlist at random
	"""
	# a word at random is chosen from the wordlist using choice() method of random class
	return random.choice(wordlist)


def getAvailableLetters(lettersGuessed):
	"""
	Function significance :
	Takes in one parameter - a list of letters, lettersGuessed. 

	This function returns a string that is comprised of lowercase English letters 
	- all lowercase English letters that are not in lettersGuessed.
	"""	
	alp='abcdefghijklmnopqrstuvwxyz' # 'alp' is a string of letters of English alphabet
	a=''				 # an empty string is created
	for i in alp:			 # Iterates through all letters of alp
		if i not in lettersGuessed:
			a+=i 		 # The string is appended with letters that are not guessed by player 
			    		 # i.e. 'a' is a string of letters available to the player
	return a


def getGuessedWord(secretWord, lettersGuessed):
	"""
	Function significance :
	Takes in two parameters - a string, secretWord, 
	and a list of letters, lettersGuessed. 
	
	This function returns a string that is comprised of letters and underscores, 
	based on what letters in lettersGuessed are in secretWord. 
	"""
	a=' ' 				 # an empty string is created
	for i in secretWord: 		 # Iterates through the secret word generated in chooseWord
		n=0 	     		 # set n=0 for every iteration 
		for j in lettersGuessed: # Iterates through 'lettersGuessed'
			if j==i:         # if letter guessed is in the secretWord, 
				n+=1	 # increment the variable n 
				break	 # breaks on finding letter guessed in secretWord
		if n!=0:
			a+=i		 # The letter found in secret word is filled in Guessed Word 'a'
			a+=' '
		else:
			a+='_'		 # an underscore is filled in Guessed word 'a' if letter is not guessed
			a+=' '
	return a			 # the (partial) Guessed word 'a' is returned 


def isWordGuessed(secretWord, lettersGuessed):
	"""
	Function significance :
	Takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. 

	This function returns a boolean - True if secretWord has been guessed 
	(ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
	"""
	n=0
	for i in secretWord:		 # Iterates through the secret word 
		if i in lettersGuessed:  # if the letter in the iteration is in the list of guessed letters,
			n+=1		 # increment a variable 'n'
	if n==len(secretWord):		 # if the value n is equal to length of secret word,
		return True		 # Returns True as the player has guessed the word
	else:
		return False		 # else returns False as the player has failed in guessing


def hangman(secretWord):
	"""
	Function significance :
	Takes a parameter -  a string secret word

	This is the method that starts the game and calls the above functions 
	"""
	print 'Welcome to the game, Hangman!'
	print 'I am thinking of a word that is',len(secretWord),'letters long.'
					 # Welcomes the player and tells him the number of letters in the word he has to guess
	print '-------------'
	lettersGuessed=list()		 # creates an empty list on a new game to fill the letters, the player has guessed
	g=9				 # 'g' is the variable to keep track of number of guesses player has used
	while g!=0:			 # checks if player has run out of the number of guesses
		g-=1			 # decrements number of guesses on a guess
		if g==0: 
			break	
		print 'You have',g,'guesses left.'
		a=getAvailableLetters(lettersGuessed) 	    # 'a' is a variable that has the letters available for player to guess
		print 'Available letters:',a
		b=raw_input('Please guess a letter:')
		b=b.lower()				    # a guess is taken from player and it is converted to lowercase
		lettersGuessed.append(b)		    # guessed letter is appended to list of guessed letters
		c=getGuessedWord(secretWord,lettersGuessed) # 'c' is the guessed word (partial)
		if b not in a:				    # checks if player tried to guess a letter he/she has already guessed
			print 'Oops! You\'ve already guessed that letter:',c
			g+=1
			print '------------'
			continue
		if b not in secretWord:			    # checks if guessed letter is in secret word
			print 'Oops! That letter is not in my word:',c
		if b in secretWord:			    # if letter guessed is in secret word (an else can also be used here)
			print 'Good guess:',c
			g+=1				    # the number of remaining guesses is incremented,
							    # giving a bonus to player on correct guess
		n=isWordGuessed(secretWord,lettersGuessed)  # 'n' is a boolean variable returned by isWordGuessed,
							    # to tell whether player is successful in guessing the secret word
		print '------------'
		if n==True:					
			break
	if n==True:					    # Player has guessed the correct word
		print 'Congratulations, you won!'
	else:						    # Player failed in guessing the secret word
		print 'Sorry, you ran out of guesses. The word was',secretWord


wordlist=loadWords()					    # a list of words is generated 
secretWord = chooseWord(wordlist).lower()		    # a secret word is chosen at random
hangman(secretWord)					    # The game begins calling this function
