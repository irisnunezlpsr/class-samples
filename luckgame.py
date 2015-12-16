print("Welcome to Vanessa's Quest!")
print("Enter the name of your character:")
name = (raw_input())

# ask for strength, health, and luck
print("Enter strength (1-10):")
s = (input())
s = str(s)

print("Enter health:")
h = (input())
h = str(h)

print("Enter luck (1-10)")
l = (input())
l = str(l)

# determine the numbers and their outcomes
if int(s) + int(h) + int(l) <= 15:
	print("Your values have been set: strength: " + s + " health: " + h + " luck: " + l)
else:
	print("Too many points! Your default values have been set to- strength: 5, health: 5, luck: 5.") 

# they have come to a fork in the road, make them choose
print("Hm, " + name + ", looks like you've come to a fork in the road. Do you want to go left or right?")
print(" Type 1 for left or 2 for right.")
dir = (input())

# what their direction and strength, health, and luck will get them
if dir == 1:
	print(name + ", you've met a dragon!")
	if int(h) <=5:
		print("Oh no, " + name + "! Your heatlh wasn't high enough to survive its fire breath. You lost the game!")
		print(":(")
	else:
		print("Yay! Your health was high enough to kill the dragon! You won the game!")
		print("*Gives Cookie*")
if dir == 2:
	print(name + ", there's a huge mountain in front of you!")
	
	import random
	n = random.randint(1,10)
	ltn = int(l) * int(n)
	
	if int(s) <=5 and int(ltn) <= 20:
		print(name + ",while you were climbing, there was a lighting storm and you got struck by lighting!")
		print("You weren't strong enough to survive and climb over the mountain. You lost the game!")
		print("Such bad luck! :(")
	else:
		print("While climbing, rocks started to fall from the top of the mountain.")
		print("You were lucky enough to dodge them and climb over the mountain." + name + ", you won the game!")
		print("*Gives Cookie*")
