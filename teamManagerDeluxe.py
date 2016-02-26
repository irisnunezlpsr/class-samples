# makes class called player
# like profiles for each player made
class Player(object):
	def __init__(self, name,  age, goals, jn, pos):
		self.name = name
		self.age = age
		self.goals = goals
		self.jn = jn
		self.pos = pos
# Print their information entered by the user, name  age  goals	
	def printStats(self):
		print(" ")
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.goals))
		print("Jersey Number: " + str(self.jn))
		print("Position: " + self.pos)
		print(" ")

# when player saves their current team to see later
def saveTeam(list, filename):
	# open file
	file = open((filename), "a")
	# write to the file
	for p in nlist:
		file.write(p.name + " " + str(p.age) + " " + str(p.goals) + " " + str(p.jn) + " " + p.pos + '\n')
	# close the file
	file.close()		

# to load the team, and add to the list or the check
def loadTeam(list, filename):
	# empty list
	list  = []
	# open
	file = open((filename), "r")
	ltr = file.readline()
	# makes the players into a list to be read
	while ltr != "":
		ltr.split()
		words = ltr.split()
		list.append(Player(words[0], words[1], words[2], words[3], words[4]))
		ltr = file.readline()
	file.close()
	return list
	

# to pause 
# asks to load file or make new one
import time 
print("Do you want to start with a new team or open an existing team?") 
print("(A) Start with a new team")
print("(B) Open a file for an existing team") 
user = raw_input() 

# either asks to load file or starts a new player list
if user == "B" or user == "b":
	print("What's the filename for your exsiting team? Enter name with .tmd extension:")
	filename = raw_input()
	list = loadTeam(list, filename)
	print("Done. Now what do you want to do?")
else:
	nlist = []
	list = []
# asks user to type in number For option
nlist = []
print("Enter the number of your choice.") 
time.sleep(.5) 
print("(1) Make Player") 
time.sleep(.2) 
print("(2) List Players") 
time.sleep(.2) 
print("(3) Save Players") 
time.sleep(.2) 
print("(0) Exit and delete players")
time.sleep(.2)
 
# ui = user input
ui = raw_input()

# what happens when they type 1, 2, or 3
while ui != "0":
	if ui == "1":
# user creates a player with name, age etc
		print("_____________________________________")
		print("Enter FIRST Name: ")
		name = raw_input()

		print("Enter Age: ")
		age = input()

		print("Enter Goals: ")
		goals = input()
		
		print("Enter Jersey Number: ")
		jn = input()
		
		print("Enter Position: ")
		pos = raw_input()

# saves name, age, and goals to their profile and adds to list
		nlist.append(Player(name, age, goals, jn, pos))

		time.sleep(.5)
		print(" ")
		print("Player Made.")
		print("_____________________________________")

# more options
		time.sleep(.6)
		print("Anything else?")
		time.sleep(1)
		print("(1) Make Player")
		time.sleep(.1)
		print("(2) List Players")
		time.sleep(.1)
		print("(3) Save Players")
		time.sleep(.1)
		print("(0) Exit and delete players")
		time.sleep(.1)
		ui = raw_input()

# if 2, will print the player's stats -- name, age etc
	elif ui == "2":
		time.sleep(1)
		print("-------------------------------------")
		print("Current List:")
		time.sleep(.5)
		for p in nlist:
			p.printStats()
			time.sleep(.5)
		for pl in list:
			pl.printStats()
			time.sleep(.5)
		print("-------------------------------------")

# more options
		time.sleep(.6)
		print("Anything else?")
		time.sleep(.1)
		print("(1) Make Player")
		time.sleep(.1)
		print("(2) List Players")
		time.sleep(.1)
		print("(3) Save Players")
		time.sleep(.1)
		print("(0) Exit and delete players")
		time.sleep(.1)
		ui = raw_input()

# if user input equals 3
# will add the new list to the loaded list and save to the same file to load later
	if ui == "3":
		print("What will your file be called? (include .tmd)")
		filename = raw_input()	
		saveTeam(list, filename)
		nlist.append(list)
		time.sleep(.3)
		print("Saved. Press (0) to exit. Restart the program to view your team.")
		ui = raw_input()
# if they enter 0
if ui == "0":
	time.sleep(.5)
	print("Bye Bye.")		
