# will write the prime numbers on a file
def isPrime(n):
    if n > 1:
        x = n // 2
# if the number divided by the number in the list (2-10000) comes out with factors of 1 and itself, then its 
# prime
        for i in range(2, x + 1):
            if n % i == 0:
# if not, nothing will return
                return False
        return True
    else:
        return False
 

# if the number is prime, it will add to the file
# if not, it will skip the number
file = open("primes.txt", "w")
for num in range(2,10001):
        if isPrime(int(num)):   
		file.write(str(num) + '\n')
		print(str(num))
