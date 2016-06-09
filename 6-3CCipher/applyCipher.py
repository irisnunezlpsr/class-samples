#apply
#a program to encrypt and decryot user text
#using CC

#author: Me

#arg: key 
#returns: book of mapped letters
import string

def book(key):
	# gets the Upper and Lowercase letter in the alphabet
	alpha = string.ascii_lowercase
	ALPHA = string.ascii_uppercase
	alphDict = {}
	c = 0
        for l in alpha:
		alphDict[l] = alpha[(key + c) % 26]
		c = c + 1
	for l in ALPHA:
		alphDict[l] = ALPHA[(key + c) % 26]
		c = c + 1
	dictionary[" "] = " "
	return alphDict


#gets msg from user
#arg: none
#returns: encoded msg
def getMsg(message):
	return message


#for each letter in the msg:
#decodes and records
#arg: encoded msg, book
#returns: decoded msg
def decode(msg, book):
	nmsg = ''
	for m in msg:
		nm = book[m]
		nmsg = nmsg + nm
	return nmsg


#outputs the msg to the terminal
#arg:
#returns: 
def printM(dMsg):
	print(dMsg)




#------execution starts here----------

try:
	#ask user for key
	print("What key would you like to use to decode?")

	key = input()

	# creating dictionary
	dict = book(key)

	print("Type message you would like the decode:")
	input = raw_input()
	#records the message
	enMsg = getMsg(input)
	#decodes the message
	decoded = decode(enMsg, dict)

	#prints the message
	printM(decoded)
except:
	print("Sorry, this code cannot be accepted.")
