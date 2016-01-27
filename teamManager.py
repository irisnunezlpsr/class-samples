# to pause
import time

# asks user to type in number
# For option
print("Enter the number of your choice.")
time.sleep(.7)
print("(1) Make Player")
time.sleep(.5)
print("(2) List Players")
time.sleep(.5)
print("(3) List Average Age and Goals")
time.sleep(.5)
print("(0) Exit and delete players")
time.sleep(.5)

# makes class called player
# like profiles for each player made
class Player(object):
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals

# Print their information entered by the user, name  age  goals	
	def printStats(self):
		print(" ")
		print("Name: " + self.name)
		print("Age: " + self.age)
		print("Goals: " + self.goals)
		print(" ")


# empty list to add player proflies
list = []

# counts number of players entered
counter = 0

# adds goals entered by the user
goalsc = 0

# adds ages entered by the user
agec = 0

# ui = user input
ui = raw_input()

# what happens when they type 1, 2, or 3
while ui != "0":
	if ui == "1":
		counter = counter + 1
# user creates a player with name, age etc
		print("_____________________________________")
		print("Enter Name: ")
		name = raw_input() 

		print("Enter Age: ")
		age = input()
		agec = agec + age
		print("Enter Goals: ")
		goals = input()
		goalsc = goalsc + goals
# saves name, age, and goals to their profile and adds to list
		list.append(Player(name, age, goals))

		time.sleep(.5)
		print("Player Made.")
		print("_____________________________________")

# more options
		time.sleep(.6)
		print("Anything else?")
		time.sleep(1)
		print("(1) Make Player")
		time.sleep(.3)
		print("(2) List Players")
		time.sleep(.3)
		print("(3) List Average Age and Goals")
		time.sleep(.3)
		print("(0) Exit and delete players")
		time.sleep(.2)
		ui = raw_input()

# if 2, will print the player's stats -- name, age etc
	elif ui == "2":
		time.sleep(1)
		print("-------------------------------------")
		print("Current List:")
		time.sleep(.5)
		for p in list:
			p.printStats()
			time.sleep(.5)
		print("-------------------------------------")

# more options
		time.sleep(.6)
		print("Anything else?")
		time.sleep(.3)
		print("(1) Make Player")
		time.sleep(.3)
		print("(2) List Players")
		time.sleep(.3)
		print("(3) List Average Age and Goals")
		time.sleep(.3)
		print("(0) Exit and delete players")
		time.sleep(.2)
		ui = raw_input()

# if user input equals 3
# will find the average age and goals for all players
	if ui == "3":
		time.sleep(1)
		print("Ok, here is the average age and goals.")

# takes the number of goals and number of players and divides
		avg = goalsc / counter

# takes # of age and # of players and divides
		avgA = agec / counter

# Prints the avg goals and avg age
		print("Goals: " + str(avg))
		print("Age: " + str(avgA))
		time.sleep(.6)
                print("Anything else?")
                time.sleep(.3)
                print("(1) Make Player")
                time.sleep(.3)
                print("(2) List Players")
                time.sleep(.3)
                print("(3) List Average Age and Goals")
                time.sleep(.3)
                print("(0) Exit and delete players")
                time.sleep(.2)
		ui = raw_input()

# if they enter 0
if ui == "0":
	time.sleep(.5)
	print("Bye Bye.")		
