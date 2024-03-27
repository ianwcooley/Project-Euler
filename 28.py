# Project Euler problem 28: https://projecteuler.net/problem=28
# Find the sum of the numbers in the diagonals of a 1001 x 1001 spiral
# increasing consecutively by 1 as it goes around clockwise.

sumDiag = 1
num = 1
width = 1
while width < 1001:
    width += 2
    # i : index within level ~ i resets to 0 when we enter a new level of the
    #  spiral, so we can keep track of where we are in that level
    i = 0 
    while num < width ** 2:
        num += 1
        i += 1
        # We reach a diagonal every (width - 1) steps:
        if i % (width - 1) == 0:
            sumDiag += num

print(sumDiag)






