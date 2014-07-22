version = "v. 0.0.1"

#Error #01 textinput() - Invalid Input (empty)
#Error #02 keyinput() - Invalid input (02.1: Invalid Length   ;02.2: Char1 Bad   ;02.3: Char2 Bad) 
#Error #03 keygen() - Unspecified Error

import string
import time
import random
from datetime import datetime
alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
alphabet = alphabet + ['0','1','2','3','4','5','6','7','8','9']
errorlog = []

def logerror(errorNo):
	global errorlog
	errorlog += [[errorNo,datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")]]

def keygen():
	a = alphabet[random.randint(0,35)]+alphabet[random.randint(0,35)]
	return a

def FF2textinput():
	input = ""
	input = raw_input(">")
	input = str("" if input is None else input)
	if not (input == ""):
		return input
	else:
		logerror("01")
		return False	

def keyinput():
	key = raw_input("If you want to use a random key (recommended) press ENTER, else type the two characters. you wish to use as the key. Only type standard Letters or Numbers. Type help for more info.\n")
	key = str("" if key is None else key)
	key = key.lower()
	if (key == "help" or key == "h" or key == "?"):
		FF2help(keyinput)
	elif key == "":
		key = keygen()
		if ((len(key) == 2) and (key[0] in alphabet) and (key[1] in alphabet)):
			return key
		else:
			print("Sorry, something went wrong with the random key generator. Please enter a key manually:")
			logerror("03")
			return False
	elif ((len(key) == 2) and (key[0] in alphabet) and (key[1] in alphabet)):
		print("A Custom key of \""+key+"\" will be used to encode your message")
		return key
	else:
		if not (len(key) == 2):
			print("Sorry, your input was not a valid key. Your input should be two characters long. (#02.1)\n")
			logerror("02.1")
		elif not (key[0] in alphabet):
			print("Sorry, your input was not a valid key. Please type two standard letters or numbers. The first character is not a legal character. (#02.2)\n")
			logerror("02.2")
		elif not (key[0] in alphabet):
			print("Sorry, your input was not a valid key. Please type two standard letters or numbers. The second character is not a legal character. (#02.3)\n")
			logerror("02.3")
		else:
			print("Sorry, your input was not a valid key. Please type two standard letters or numbers. Symbols are not supported. (#02)\n")
			logerror("02")
		return False

def encode(inputText,key): #TODO
	i = 0
	encoded = ""
	activekey = key
	output = ""
	while i < ((len(inputText)/2)+1):
		char1 = inputText[(2*i)]
		if ((len(inputText))%2) == 0 or len(inputText) < i*2+1:
			char2 = inputText[(2*i)+1]
		else:
			char2 = 'X'
		output += encode2(char1,char2,activekey)
		activekey = output[-2:-1]
		i += 1
	output = output[0]+key[0]+output[1:]+key[1]
	return output
		
		
	
		

####################
# START OF PROGRAM #
####################

print("FF2 Cipher encoder: "+version+"\n     Type the text you wish to encode. Press enter when finished\n")
text = False
while text == False:
	text = FF2textinput()
key = False
while key == False: #loop if keyinput() returns False (if it encounters an error)
	key = keyinput()
encode(text,key)