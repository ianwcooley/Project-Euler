# Project Euler problem 4: Find the largest palindrome made from the product of two 3-digit numbers

def isPalindrome(num):
    num = str(num)
    i = 0
    j = len(num) - 1
    while (i < j):
        if (num[i] != num[j]):
            return False
        i += 1
        j -= 1
    return True

i = 999
j = 999
num = 999*999
largestPalindrome = 0

while (largestPalindrome == 0 and num >= 0):
    if (isPalindrome(num)):
        for n in range(999,99,-1):
            if (num % n == 0 and num // n > 99 and num // n < 1000):
                largestPalindrome = num
                print(n)
                print (num // n)
                break
    num -= 1

print(largestPalindrome)

    
'''
for i in range(999,0,-1)

while (i > 0 and j > 0):
    if isPalindrome(i*j) && i*j > largestPalindrome:
        largestPalindro
        break
    if (i < j):
        j -= 1
    else:
        i -= 1
   ''' 
        
        
        
