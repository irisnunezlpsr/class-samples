print("How many miles away do you live from Richmond state?")
miles = int(input())

if miles <= 30:
    print("What is your GPA?")
    GPA = float(input())
    if GPA >= 2.0:
        print("Accepted")
        
else:
    print("What is your GPA?")
    GPA = float(input())
    print("What is your ACT score?")
    ACT = float(input())
    if GPA  >= 2.5  and ACT >= 18:
        print("Accepted")
    else:
     print("Not Accepted")
