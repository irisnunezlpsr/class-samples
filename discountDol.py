print("Enter the amount of purchases, in dollars:")
number = int(input())
number = int(number)
x = number * .10
xx = str(x)
xxx = number - x
xxxx = str(xxx)
if number > 10:
        print("You spent over $10! Your final price is " + xxxx + "  dollars.")
else:
        print("Sorry, you don't get the discount.")
