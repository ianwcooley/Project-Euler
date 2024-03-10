# Project Euler problem 20: Find the sum of the digits of 100!

# Here we build on the idea behind our function in problem 16. That is, we store
# the digits of the factorial we are calculating as ints in a list by place value
# in reverse order. 

# Then, we multiply each digit in the list by n, and if the result 
# is greater than 9, we add its remaining digits to the corresponding digits
# in our list, and continue.

digits = [1] # the digits of the number, in reverse order

for n in range(2, 101):
    # multiply all digits by n
    for i in range(0, len(digits)):
        digits[i] *= n
    # adjust for multiple digit results by adding those digits to the next
    # digits in our number, and replacing given digit by itself mod 10:
    for i in range(0, len(digits)): 
        if (digits[i] > 9):
            tooLargeDigit = digits[i]
            digits[i] = tooLargeDigit % 10
            j = 1
            tooLargeDigit //= 10
            while tooLargeDigit > 0:
                if i + j == len(digits):
                    digits.append(tooLargeDigit % 10)
                else:
                    digits[i+j] += tooLargeDigit % 10
                tooLargeDigit //= 10
                j += 1
print(sum(digits))
