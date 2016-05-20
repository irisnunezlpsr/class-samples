# empty dictionary
contacts = {}


choice = 1
while choice != 0:
	print("Welcome to contacts!")
# 1 to add a contact, 2 to show contact list and 3 to show a specific person's number
	print("What would you like to do?")
	print("(1)Add a phone number.")
	print("(2)Print the full list of contacts.")
	print("(3)Retrieve a phone number.")

	print("(0)Exit.")

# wil add the name and number to dictionary
	choice = input()

	if choice == 1:
		print("Name of Contact:")
		name = raw_input()
		print("Number:")
		number = raw_input()
		contacts[name] = number
# will print out the dictionary
	if choice == 2:
		print(contacts)

# will print out the name's number
	if choice == 3:
		print("Whos number do you want?")
		name = raw_input()
		print("Here you go:")
		print(contacts[name])

