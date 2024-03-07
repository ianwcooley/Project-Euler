# Project Euler problem 17: find the number of letters in the printed words for
# the numbers 1-1000, all together

numMap = { # maps the number to the number of letters in the number (only for necessary numbers)
    0: 0, # we aren't counting "zero" because it isn't used
    1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
    10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 
    20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6
}

def numLetters(n):
    num = 0 # number of letters in number-word
    onesPlace = n % 10
    tensPlace = (n // 10) % 10
    tensAndOnesPlace = n % 100
    hundredsPlace = (n // 100) % 10
    if n == 1000:
        return 11
    elif n < 20:
        return numMap[n]
    elif n < 100:
        return numMap[tensPlace * 10] + numMap[onesPlace]
    elif n >= 100 and n % 100 == 0: # exact hundred number ("hundred" has 7 letters)
        return numMap[hundredsPlace] + 7 
    elif n > 100: # inexact hundred number ("hundred and" has 10 letters)
        return numMap[hundredsPlace] + 10 + numLetters(tensAndOnesPlace)

# perform the final calculation
totalNumLetters = 0
for n in range(1, 1001):
    totalNumLetters += numLetters(n)

print(totalNumLetters)
    


