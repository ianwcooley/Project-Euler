# Project Euler problem 35: find the number of circular primes below 1 million

# This Sieve of Eratosthenes returns a list of 1,000,001 Booleans saying
# whether or not the index is prime
def sieve_of_eratosthenes(limit):
    # Create a boolean array "is_prime[0..limit]" and initialize all entries as True.
    # A value in is_prime[i] will be False if i is not a prime.
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # We only need to iterate up to the square root of the limit because 
    # any composite number n will have at least one factor less than or equal 
    # to sqrt(n).
    for i in range(2, int(limit**0.5) + 1): 
        if is_prime[i]:  # If is_prime[i] is still True, i is a prime
            # we iterate starting at i^2, because any smaller multiple of i, like i*k,
            # will have already been found when iterating through k
            for j in range(i * i, limit, i):  # Mark all multiples of i as False
                is_prime[j] = False

    return is_prime

    # # Leaving this code here, if we wanted to us sieve of eratosthenes normally
    # # to return all primes below the limit
    # # Collect all numbers marked as True in is_prime, which are prime numbers
    # primes = [i for i, prime in enumerate(is_prime) if prime]
    # return primes


def get_digits(number):
    """Input: int
    Output: list of its digits"""
    digits = []
    while number > 0:
        digit = number % 10
        digits.insert(0, digit)
        number //= 10
    return digits

def get_number(digits):
    """Input: list of digits
    Output: int represented by the digits"""
    for i, digit in enumerate(digits):
        digit *= 10
        for j in range(0,i):
            digits[j] *= 10
    return sum(digits)

def get_cycles(number):
    """ Input: int
    Output: list of all ints that are its circular permutations"""
    digits = get_digits(number)
    circular_permutations = [digits[i:] + digits[:i] for i in range(len(digits))]
    cycles = [get_number(permutation) for permutation in circular_permutations]
    return cycles



is_prime = sieve_of_eratosthenes(1000000)
is_circular_prime = is_prime.copy()

for number in range(len(is_prime)):
    if is_prime[number]:
        cycles = get_cycles(number)
        for cycle in cycles:
            if not is_prime[cycle]:
                is_circular_prime[number] = False
                break

number_of_circular_primes = 0
for number, circular_prime in enumerate(is_circular_prime):
    if circular_prime:
        print(number)
        number_of_circular_primes += 1

print(number_of_circular_primes)

# Find all primes below 1,000,000
# primes_below_million = sieve_of_eratosthenes(1000000)
# print(len(primes_below_million))
