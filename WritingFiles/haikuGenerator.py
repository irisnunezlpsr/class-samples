# welcomes user
print("Welcome to Haiku Generator!")

# Whatever the user types, will be added and saved to a file
print("Type first line for your haiku:")
fl = raw_input()

print("Type second line for your haiku:")
sl = raw_input()

print("Type third line for your haiku:")
tl = raw_input()

# saves lines in a file they make
print("What file would you like to write your haiku to?")
filename = raw_input()
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")

# actual file to save to
file = open((filename), "a")

# adds the raw inputs to the file they make
file.write(fl + '\n' + sl + '\n' + tl + '\n')

# close the file
file.close()
