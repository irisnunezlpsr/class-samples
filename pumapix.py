print("Welcome to PumaPix!")

# will ask for 5 shows
print("Enter your 5 favorite shows:")

l = []
x = 0
while x != 5:
        print("Enter a show name:")
        a = raw_input()
        l.append(a)
        x = x + 1

# will print out what they put
print("Ok here's what you entered:")
print(l)

# remove shows if necessary and add important shows
if 'CSI' in l or 'NCIS' in l:
    print("We've removed some shows from your list and added a couple of important ones.")

# how it will remove
    if 'CSI' in l and 'NCIS' in l:
        l.remove('CSI')
        l.remove('NCIS')
    elif 'NCIS' in l:
        l.remove('NCIS')
    else:
        l.remove('CSI')
        
    
# add important shows 
    l.append('Breaking Bad')
    l.append('The Wire')
    for num, e in enumerate(l):
        print(str(num + 1) + " " + e)
        
# If there's no bad shows
else:
    print("We've added a couple of important shows to your list:")
    l.append('Breaking Bad')
    l.append('The Wire')
    for num, e in enumerate(l):
        print(str(num + 1) + " " + e)
