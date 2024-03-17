# Project Euler problem 23: Find the sum of all positive integers which cannot be written 
# as the sum of two abundant numbers.

import math

lowerLimit = 12
upperLimit = 28123

# get all abundant numbers lower than 28123, which is the number past which
# all numbers can be written as the sum of two abundant numbers
abundantNumbers = []
for i in range(lowerLimit, upperLimit - 12):
    factorSum = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if (i % j == 0):
            if (j == i // j):
                factorSum += j
            else:
                factorSum += j + i // j
    if factorSum > i:
        abundantNumbers.append(i)

# put all sums of two abundant numbers in a list, and remove duplicates
abundantSums = []
for abunNum1 in abundantNumbers:
    for abunNum2 in abundantNumbers:
        abundantSums.append(abunNum1 + abunNum2)
abundantSums = list(dict.fromkeys(abundantSums))

# find the sum of the numbers that cannot be written as
# a sum of two abundant numbers:
finalSum = 0 
for num in range(1, upperLimit):
    if num not in abundantSums:
        finalSum += num
        
print(finalSum)


