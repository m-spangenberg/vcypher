"""
vcypher - (MIT) Copyright (c) 2018 Marthinus Spangenberg
A script that encrypts and decrypts strings using poly-alphabetic substitution, written in Python!


# A variation of a Caesar cipher called a 'Vigenere cipher'

# | a  | b  | c  | d  | e  | f  | g  | h  | i  | j  |
# | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
# ---------------------------------------------------
# | k  | l  | m  | n  | o  | p  | q  | r  | s  | t  |
# | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
# ---------------------------------------------------
# | u  | v  | w  | x  | y  | z  |
# | 21 | 22 | 23 | 24 | 25 | 26 |
"""

import re
import itertools


alphabet = {
'a' : 1,'b' : 2,'c' : 3,'d' : 4,'e' : 5,'f' : 6,'g' : 7,
'h' : 8,'i' : 9,'j' : 10,'k' : 11,'l' : 12,'m' : 13,'n' : 14,
'o' : 15,'p' : 16,'q' : 17,'r' : 18,'s' : 19,'t' : 20,'u' : 21,
'v' : 22,'w' : 23,'x' : 24,'y' : 25,'z' : 26}

def secretMessage():
	"""
	take a user input and pass to 'userInput' as a string
	strip and make lower-case
	"""
	userInput = input(str('Enter your secret message: ')).lower()
	parsedInput = re.sub('[^A-Za-z]+', '', userInput)

	return parsedInput

def secretKey():
	"""
	take user input and pass to 'userInputKey' as a string
	strip and make lower-case
	"""
	userInputKey = input(str('Enter your secret key: ')).lower()
	parsedInputKey = re.sub('[^A-Za-z]+', '', userInputKey)

	return parsedInputKey

def cGen():
	"""
	Finds the dictionary value of each letter in the secret message
	"""
	cVal = []

	for c in secretMessage():
		for letter, number in alphabet.items():
			if c == letter:
				cVal.append(number)

	return cVal

def kGen():
	"""
	Finds the dictionary value of each letter in the secret key
	"""
	kVal = []

	for k in secretKey():
		for letter, number in alphabet.items():
			if k == letter:
				kVal.append(number)

	return kVal


def obfuscate():
	"""
	Commits the key to scramble the message
	"""
	xLetter = []

	for a,b in zip(cGen(), itertools.cycle(kGen())):
		cypherStep = (a + b)%26
		if cypherStep == 0:
			cypherStep = 26
		else:
			pass

		for letter, number in alphabet.items():
			if cypherStep == number:
				xLetter.append(letter)

	cypherShow = ''.join(str(cyp) for cyp in xLetter)
	return cypherShow

def deobfuscate():
	"""
	Unscrambles the hashed message using a key
	"""
	zLetter = []

	for a,b in zip(cGen(), itertools.cycle(kGen())):
		clearTextStep = (a - b)%26
		if clearTextStep == 0:
			clearTextStep = 26
		else:
			pass

		for letter, number in alphabet.items():
			if clearTextStep == number:
				zLetter.append(letter)

	clearText = ''.join(str(clear) for clear in zLetter)

	return clearText

def sanityCheck():
	"""
	Outputs debug information of program
	"""
	pass

def startEncoding():
	"""
	Runs the Encoder
	"""
	print('Your hashed string is: {}'.format(obfuscate()))

def startDecoding():
	"""
	Runs the Decoder
	"""
	print('Your clean string is: {}'.format(deobfuscate()))


def startCypher():
	"""
	Run main program and call either encode or decode functions
	"""
	print('Vigenere Cipher\n')
	userChoice = input('Select ||| Encode/Decode: ').lower()
	userChoicePolish = re.sub('[^A-Za-z]+', '', userChoice)

	if userChoicePolish == 'encode':
		startEncoding()
	else:
		startDecoding()

startCypher()