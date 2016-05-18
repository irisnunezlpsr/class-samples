#apply
#a program to encrypt and decryot user text
#using CC

#author: me

#arg: key 
#returns: book of mapped letters


def book(key):

	#placeholder
	return {}


#gets msg from user
#arg: none
#returns: encoded msg
def getMsg():
	
	pass


#for each letter in the msg:
#decodes and records
#arg: encoded msg, book
#returns: decoded msg
def decode(msg, book):
	pass



#outputs the msg to the terminal
#arg: 
#returns: 
def printM():
	pass




#------execution starts here----------

#ask user for key
print("What key would you like to use to decode?")

key = input()

# creating dictionary
dict = book(key)

#records the message
enMsg = getMsg()

#decodes the message
decoded = decode(enMsg, dict)

#prints the message
printM(decoded)
