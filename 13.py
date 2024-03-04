# Project Euler problem 13: Find the first 10 digits of the sum 
# of the following 100 50-digit numbers (stored in 13.txt):

# get numbers from 13.txt and store as a list of strings:
textFile = open('./13.txt')
numbers = textFile.readlines()
for number in numbers:
    number = number.strip()
textFile.close()

# Add numbers using the addition algorithm from elementary school:
totalSum = [] # the sum of all numbers, one character per digit
columnSum = 0 # running sum from each column - (no worries about it getting too big because we only have 100 numbers to work with)
for i in range(49, -1, -1):
    for number in numbers:
        columnSum += int(number[i])
    columnSumString = str(columnSum)
    digit = columnSumString[len(columnSumString)-1]
    totalSum.insert(0,digit)
    #print(columnSum)
    columnSum //= 10 # chop off last digit of columnSum and continue

# columnSum will have some digits left at the end, so prepend them to the totalSum
columnSumString = str(columnSum)
totalSum = [*columnSumString] + totalSum

firstTenDigits = ''.join(totalSum[0:10])
print(firstTenDigits)

