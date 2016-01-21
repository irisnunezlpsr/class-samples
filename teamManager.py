# to pause
import time

# asks user to type in number
# For option
print("Enter the number of your choice.")
time.sleep(1.3)
print("(1) Make Player")
time.sleep(.8)
print("(2) List Players")
time.sleep(.8)
print("(0) Exit and delete players")

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

# ui = user input
ui = raw_input()

# what happens when they type 1, 2, or 3
while ui != "0":
	if ui == "1":

# user creates a player with name, age etc
		print("_____________________________________")
		print("Enter Name: ")
		name = raw_input() 

		print("Enter Age: ")
		age = raw_input()
	
		print("Enter Goals: ")
		goals = raw_input()

# saves name, age, and goals to their profile and adds to list
		list.append(Player(name, age, goals))

		time.sleep(1)
		print("Player Made.")
		print("_____________________________________")

# more options
		time.sleep(1)
		print("Anything else?")
		print("(1) Make Player")
		print("(2) List Players")
		print("(0) Exit and delete players")
		ui = raw_input()

# if 2, will print the player's stats -- name, age etc
	elif ui == "2":
		time.sleep(1)
		print("-------------------------------------")
		print("Current List:")
		print(" ")
		for p in list:
			p.printStats()
		print("-------------------------------------")

# more options
		time.sleep(1)
		print("Anything else?")
		print("(1) Make Player")
		print("(2) List Players")
		print("(0) Exit and delete players")
		ui = raw_input()
