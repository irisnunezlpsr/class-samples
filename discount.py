print("Enter the amount of purchases, in cents:")
number = int(input())
number = int(number)
x = number * .10
xx = str(x)
xxx = number - x
xxxx = str(xxx)
if number > 1000:
        print("You spent over $10! Your final price is " + xxxx + "  cents.")
else:
        print("Sorry, you don't get the discount.")
