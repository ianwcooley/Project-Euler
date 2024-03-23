# Project Euler problem 24: Find the millionth lexicographic permutation
# of the digits 0,1,2,3,4,5,6,7,8,9

import math

digits = list(range(0,10))
number = []
# Since computer counting starts at 0, we look for the "999999th"
# permutation, which is really the 1000000th permutation. TBH still not
# sure why 999999 works and not 1000000 here, but that's my best explanation.
place = 999999
for i in range(len(digits) - 1, -1, -1):
    # Each first digit appears 9! times in the list of all permutations,
    # each second digit 8! times, etc.
    digit = digits[place // math.factorial(i)]
    # Each digit only appears once in the 1000000th permutation,
    # so remove it from the list of digits we're looking for next
    digits.remove(digit)
    number.append(digit)
    # We've found the 1000000th permutation, now search for the
    # next digit within the permutations starting with the first
    # digit, etc.
    place = place % math.factorial(i)

print(''.join(map(str, number)))