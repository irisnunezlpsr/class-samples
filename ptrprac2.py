# Asking how old you are
print("How old are you in years?")
age = int(input())

# will multiply inputAge by 7
print("Today, you are " + str(7 * age) + " years old in dog years.")

# Will add a number between 1 and 5 to your age and times it by 7
for i in range(1, 5):
	new_age = age + i
	print("In another year, you'll be " + str(7 * new_age) + " years old in dog years.")

