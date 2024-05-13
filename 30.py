# Project Euler problem 30: Find the sum of all the numbers that can be written as
# the sum of fifth powers of their digits.

def sumOfFifthPowers(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** 5
        num //= 10
    return total


# Because 7 * 9^5 = 413343 is a 6-digit number, this means that any 7-digit number
# will be larger than the sum of the fifth powers of its digits, so we only need to
# test numbers up to six digits in length.

fifthPowerSums = []
for n in range(10, 1000000):
    if n == sumOfFifthPowers(n):
        fifthPowerSums.append(n)

print(sum(fifthPowerSums))

