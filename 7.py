from math import isqrt
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

numPrime = 0
prime = 0
num = 0
while (numPrime < 10001):
    num += 1
    if (is_prime(num)):
        prime = num
        numPrime += 1

print(prime)
        
    
