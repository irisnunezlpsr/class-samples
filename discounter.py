# find out price from user
print("What is the price?")
price = int(input())


# calculate discount price
disprice = price - (.10 * price)
xdip = str(disprice)

# if user gets dicount, tell them.
# if not, tell them.
if price > 1000:
	print("Your price is " + xdip)
else:
	print("Sorry, you don't get the discount.")
