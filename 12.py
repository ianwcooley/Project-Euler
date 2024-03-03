# Project Euler Problem 12: Find the first triangular number with over 500 divisors

from math import isqrt

numDivisors = 0
triangNum = 0
i = 0
while numDivisors <= 500:
    numDivisors = 0
    i += 1
    triangNum += i
    for j in range(1, isqrt(triangNum)+1):
        if triangNum % j == 0:
            numDivisors += 1
    numDivisors *= 2

print(triangNum)
