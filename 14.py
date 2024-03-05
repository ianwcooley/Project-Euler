# Project Euler problem 14: Find the number under one million that produces
# the longest Collatz sequence

def numCollatzTerms(number):
    numTerms = 1
    while (number != 1):
        if (number % 2 == 0):
            number = number // 2
        else:
            number = number * 3 + 1
        numTerms += 1
    return numTerms

longestCollatz = 1
mostCollatzTerms = 1
for n in range(1, 1000000):
    numTerms = numCollatzTerms(n)
    if numTerms > mostCollatzTerms:
        mostCollatzTerms = numTerms
        longestCollatz = n

print(longestCollatz)
print(mostCollatzTerms) 

