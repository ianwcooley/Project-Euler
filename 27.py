# Project Euler problem 27: Find the product a * b where |a| < 1000 and 
# |b| <= 1000 such that n^2 + an + b produces the maximum number of primes
# for consecutive values of n, starting with n = 0.

from math import isqrt

# We'll use this speed-boosted isPrime function to check if
# a given number is prime:
def isPrime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

# b must be prime, otherwise we couldn't get a prime number for n = 0.
# Thus, we use Sieve of Eratosthenes to get all prime numbers under 1000 as
# potential values of b:
bOptions = list(range(2, 1000))
i = 0
while i < len(bOptions):
    num = bOptions[i]
    while num < 1000:
        num += bOptions[i]
        if num in bOptions:
            bOptions.remove(num)
    i += 1
# And just like that, we've narrowed our list of potential b
# values from 2001 down to 168 :)

# Now, the hard part:

product = 0 # the product of a * b that we're looking for
mostPrimes = 0 # the most primes found for consecutive values of n

aOptions = list(range(-999, 999))

for a in aOptions:
    for b in bOptions:
        n = 0
        numPrimes = 0
        while isPrime(n ** 2 + a * n + b):
            numPrimes += 1
            n += 1
        if numPrimes > mostPrimes:
            product = a * b 
            mostPrimes = numPrimes

print(product)
# And just like that, we have the answer. This was a surprisingly easy problem,
# considering the intimidating description of it on the website. 
