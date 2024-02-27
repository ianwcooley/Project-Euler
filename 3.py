num = 600851475143
#num = 13195
#limiter = 2

# Note: This function can be improved: loop through sqrt(n)

def isPrime(num):
    i = 2
    n = num
    while i < n:
        if num % i == 0:
            return False
        n = num / i
        i = i + 1
    return True

def largestPrime(num):
    i = 2
    n = num
    largestPrime = 2
    while (i < n):
        if isPrime(i) and n % i == 0:
            largestPrime = i
            n = n // i
        i = i + 1
    if isPrime(n):
        largestPrime = n
    return largestPrime

print(largestPrime(num))
