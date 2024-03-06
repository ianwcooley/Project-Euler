# Project Euler problem 16: Find the sum of the digits in 2^1000

# (Just as we wrote an addition algorithm for very large integers in problem 13,
# representing those integers as strings, we do the same here for the operation
# of multiplying a very large integer by 2):

digits = [1] # the digits of the number, in reverse order

for n in range (0, 1000):
    # double all digits
    for i in range(0, len(digits)):
        digits[i] *= 2
    # adjust for double digit results by augmenting next digit by 1
    # and replacing given digit by itself mod 10:
    for i in range(0, len(digits)): 
        if (digits[i] > 9):
            if i + 1 == len(digits):
                digits.append(1)
            else:
                digits[i+1] += 1
            digits[i] %= 10

print(sum(digits))
        
