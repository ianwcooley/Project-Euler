# Project Euler problem 10: Find the sum of all the primes below two million.

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

def sumPrimesLessThan(num):
    sum = 0
    for i in range(2, num):
        if is_prime(i):
            sum += i
    return sum

print(sumPrimesLessThan(2000000))
