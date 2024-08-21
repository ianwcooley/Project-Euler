# Project Euler problem 33: Find the four non-trivial examples of
# digit-cancelling proper fractions whose numerators and denominators are
# two-digit numbers, find their product in lowest terms, and return
# the denominator of this product.

# This list will hold the four non-trivial examples:
examples = []

def digits(number):
    """Input: int
    Output: list of its digits"""
    digits = []
    while number > 0:
        digit = number % 10
        digits.insert(0, digit)
        number //= 10
    return digits

def number(digits):
    """Input: list of digits
    Output: int represented by the digits"""
    for i, digit in enumerate(digits):
        digit *= 10
        for j in range(0,i):
            digits[j] *= 10
    return sum(digits)

def lowest_terms(numerator, denominator):
    """Input: two ints representing a fraction: numerator, denominator
    Output: tuple representing the fraction in lowest terms: 
        (reduced_numerator, reduced_denominator)"""
    potential_factor = 2
    while potential_factor <= numerator:
        # if potential_factor is a common factor:
        while numerator % potential_factor == 0 and denominator % potential_factor == 0:
            numerator //= potential_factor
            denominator //= potential_factor
        potential_factor += 1
    return((numerator, denominator))

# Go through all proper fractions with two-digit numerators and denominators
# and check if they are non-trivial "digit-cancelling":
for numerator in range(10, 100):
    for denominator in range(numerator+1, 100):
        # ignore "trivial" examples:
        if numerator % 10 == 0 and denominator % 10 == 0:
            continue
        # Remove common digits:
        numerator_digits = digits(numerator)
        denominator_digits = digits(denominator)
        for digit in numerator_digits:
            if digit in denominator_digits:
                numerator_digits.remove(digit)
                denominator_digits.remove(digit)
        # If both digits are common then ignore, as reduced fraction == 1:
        if (len(numerator_digits)== 0 or len(denominator_digits) == 0):
            continue
        # If one digit is common, check to see if "reduced form" == original fraction,
        # and if so, append fraction in lowest terms to list of examples:
        elif (len(numerator_digits) == 1 and len(denominator_digits) == 1):
            if (lowest_terms(numerator, denominator) == lowest_terms(numerator_digits[0], denominator_digits[0])):
                examples.append(lowest_terms(numerator, denominator))

# Get product of examples in lowest terms:
numerator = 1
denominator = 1
for example in examples:
    numerator *= example[0]
    denominator *= example[1]
product = lowest_terms(numerator, denominator)

# Print denominator of said product:
print(product[1])