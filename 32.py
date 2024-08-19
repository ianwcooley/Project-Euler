# Project Euler problem 32: Find the sum of all products whose 
# multiplicand/multiplier/product identity can be written as a 
# 1 through 9 pandigital.

products = []
product_sum = 0

def nine_pandigital(multiplicand, multiplier, product):
    digits = []
    for number in [multiplicand, multiplier, product]:
        while number > 0:
            digit = number % 10
            if digit in digits or digit == 0:
                return False
            digits.append(digit)
            number //= 10
    if len(digits) == 9:
        return True
    else:
        return False
    
# Note that the only possibilities for multiplicand/multiplier are
# 2-digit * 3-digit or 1-digit * 4-digit, 
# because 3-digit * 3-digit results in at least a 5-digit number,
# which would give us 11 total digits (too many), and 2-digit * 2-digit
# results in at most a 4-digit number, which would give us 8 total digits
# (too few)
        
# start with the 1-digit * 4-digit products:
for multiplicand in range(1, 10):
    for multiplier in range(1000, 10000 // multiplicand):
        product = multiplicand * multiplier
        if nine_pandigital(multiplicand, multiplier, product):
            if product not in products:
                products.append(product)

# now do 2-digit * 3-digit products:
for multiplicand in range(12, 99):
    for multiplier in range(102, 988):
        product = multiplicand * multiplier
        if nine_pandigital(multiplicand, multiplier, product):
            if product not in products:
                products.append(product)

# we've appended all valid products to our list with no repeats,
# so now we sum them to get our final result:
print(sum(products))

    