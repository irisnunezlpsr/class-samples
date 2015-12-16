print("I'm thinking of a number between 1 and 1000. Enter your guess!")

import random

mn = random.randint(1, 1000)
ui = "."
# what happens when user inputs number
while ui != mn:
	ui = input()
	if ui > mn:
		print("Too high! Guess again.")
	elif ui < mn:
		print("Too low! guess again!")
if ui == mn:
	print("You Win!")
