# Project Euler problem 34: Find the sum of all numbers which are equal to
# the sum of the factorial of their digits

import math

# we set 9,999,999 as our highest number to check, as the sum of its digits'
# factorials is less than itself, and this will be the case for all numbers greater
# than it.
MAX_NUMBER = 9999999

def get_digits(number):
    """Input: int
    Output: list of its digits"""
    digits = []
    while number > 0:
        digit = number % 10
        digits.insert(0, digit)
        number //= 10
    return digits

final_sum = 0
for number in range(10, MAX_NUMBER):
    digits = get_digits(number)
    if number == sum(math.factorial(digit) for digit in digits):
        final_sum += number

print(final_sum)



    