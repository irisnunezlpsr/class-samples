print("How many miles do you live from Richmond State?")
miles = (input())
miles = int(miles)

print("What is your GPA?")
GPA = float(input())
GPA = int(GPA)

if miles <= 30 and GPA >= 2.0:
    print("Accepted")
else:
        print("What is your ACT score?")
	ACT = (input())
	ACT = int(ACT)
if miles > 30 and GPA >=2.5 and ACT >= 18:
	print("Accepted")
else:
	print("Not Accepted")
