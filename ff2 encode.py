version = "v. 0.1.0"

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
debuglog = ""

def logerror(errorNo):
	global errorlog
	errorlog += [[errorNo,datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")]]

def keygen():
	a = alphabet[random.randint(0,35)]+alphabet[random.randint(0,35)]
	return a

def FF2textinput():
	input = ""
	input = raw_input(">")
	input = input.lower()
	input = input.replace(" ","")
	input = str("" if input is None else input)
	for c in input
		if c in alphabet:	#
		input2 += c			#
	input = input2
	if not (input == ""):
		return input
	else:
		logerror("01")
		return False	

def keyinput():
	key = raw_input("\n\nIf you want to use a random key (recommended) press ENTER, else type the two characters. you wish to use as the key. Only type standard Letters or Numbers. Type help for more info.\n\n>")
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
		
def tonum(char):
	i=0
	for c in alphabet:
		if c == char:
			return i
		i += 1
	logerror("04")
	return False	
	
def NumCat(grid):
	output = 0
	for i in grid:
		output = output*36
		output += i
	return output
	
def debugadd(debugData):
	global debuglog
	debuglog += debugData
	debuglog += "\n"
		
##############################
#	REAL ENCODER STARTS HERE #
##############################

def obtainxy(char,grid):
	y = 0
	for r in grid:
		x=0
		for c in r:
			if c == char:
				return (x,y)
			x +=1
		y += 1

def encode3(char1,char2,gridItems):
	# print gridItems
	grid=[gridItems[0:6],gridItems[6:12],gridItems[12:18],gridItems[18:24],gridItems[24:30],gridItems[30: ]]
	# print 1,char1
	# print "g",grid
	y = 0
	char1x,char1y = obtainxy(char1,grid)
	char2x,char2y = obtainxy(char2,grid)
	if char1x == char2x:
		return alphabet[grid[(char1y+1)%6][(char2x+1)%6]] + alphabet[grid[(char2y+1)%6][(char1x+1)%6]]
	if char1y == char2y:
		return alphabet[grid[(char1y+1)%6][(char2x+1)%6]] + alphabet[grid[(char2y+1)%6][(char1x+1)%6]]
	# print char1x
	# print char1y
	# print char2x
	# print char2y
	# print grid
	# print grid[char2x][char1y]
	# print grid[char1x][char2y]
	# print alphabet[grid[char2x][char1y]]
	# print alphabet[grid[char1x][char2y]]
	return alphabet[grid[char1y][char2x]] + alphabet[grid[char2y][char1x]]
	

def encode2(char1,char2,key):
	grid = []
	diff = (tonum(key[1])-tonum(key[0]))%36
	letter = tonum(key[0])
	for i in range(0,36):
		if letter in grid:
			letter += 1 
		grid += [letter]
		letter = (letter+diff)%36
	if not alphabet[letter] == key[0]:
		logerror("05")
	debugadd(char1+key[0]+"."+str(tonum(char2))+","+str(tonum(char1))+"."+str(NumCat(grid))+"\\"+char2+key[1])
	return encode3(tonum(char1),tonum(char2),grid)
			

def encode(inputText,key): #TODO
	if not len(key) == 2:
		print "THIS SHOULD NOT HAPPEN. PYTHON IS BROKEN!"
	i = 0
	encoded = ""
	activekey = key
	output = ""
	while i < ((len(inputText)+1)/2):
		char1 = inputText[(2*i)]
		if ((len(inputText))%2) == 0 or len(inputText) > i*2+1:
			char2 = inputText[(2*i)+1]
		else:
			char2 = 'x'
		output += encode2(char1,char2,activekey)	
		activekey = output[-2:]
		i += 1
	output = output[0]+key[0]+output[1:]+key[1]
	return output
		
		
		
		

####################
# START OF PROGRAM #
####################

print("FF2 Cipher encoder: "+version+"\n\n\n     Type the text you wish to encode. Press enter when finished\n")
text = False
while text == False:
	text = FF2textinput()
key = False
while key == False: #loop if keyinput() returns False (if it encounters an error)
	key = keyinput()
output = encode(text,key)
print "\n\nEncoded message:\n   "+output+"\n\n\nPress enter to quit"
finalcommand=raw_input()
if finalcommand.lower() == "e":
	print errorlog
elif finalcommand.lower() == "d":
	print debuglog
elif finalcommand.lower() == "b":
	print str(errorlog)+"\n\n"+str(debuglog)
elif finalcommand.lower() == "r":
	restart()
elif finalcommand.lower() == "br":
	print errorlog