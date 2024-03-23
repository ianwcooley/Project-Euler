# Project Euler problem 25: Find the index of the first term in the
# Fibonacci sequence to contain 1000 digits.


def numDigits(num):
    return len(str(num))


fibs = [1, 1]
i = 1
while numDigits(fibs[i]) < 1000:
    i += 1
    fibs.append(fibs[i-1] + fibs[i-2])

print(i + 1) # print the math index, not the compsci index
    