# Project Euler problem 21: Find the sum of all the amicable numbers under 10000.
# (Two distinct numbers are "amicable" if each is the sum of the other's proper divisors.)

amicableNumbers = []

# Test each number n under 10000 to see if it is amicable.
# If so, add it to the list of amicable numbers (if it has not already been found)
for n in range(1, 10000):
    if n in amicableNumbers:
        continue
    m = 0 # sum of n's proper divisors
    for i in range(1, n):
        if n % i == 0:
            m += i
    k = 0 # sum of m's proper divisors
    for i in range(1, m):
        if m % i == 0:
            k += i 
    if k == n and n != m:
        amicableNumbers += [n, m]

print(sum(amicableNumbers))
    
    


