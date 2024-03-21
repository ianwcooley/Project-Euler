# Project Euler problem 24: Find the millionth lexicographic permutation
# of the digits 0,1,2,3,4,5,6,7,8,9

import math

digits = list(range(0,10))
number = []
place = 999999
for i in range(len(digits) - 1, -1, -1):
    print(place // math.factorial(i))
    digit = digits[place // math.factorial(i)]
    digits.remove(digit)
    number.append(digit)
    place = place % math.factorial(i)
    print(place)

print(number)
print(''.join(map(str, number)))