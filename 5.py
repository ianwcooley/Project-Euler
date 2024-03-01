# Project Euler problem 5: what is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import copy
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

def smallestMultiple(rng):
    primes = list(rng)
    i = len(primes)-1
    while (i >=  0):
        if not is_prime(primes[i]):
            del primes[i]
        i -= 1
    print(primes)
    for i in range(len(primes)):
        while (primes[i]*primes[i] < len(rng)):
            primes[i] *= primes[i]   
    print(primes)
    lcm = 1
    for prime in primes:
        lcm *= prime
    print(lcm)
    
smallestMultiple(range(20))
    
    
        
        
    
    
    
        
        
