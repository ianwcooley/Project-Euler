# Project Euler problem 26: Find the value of d < 1000 for which 1 / d
# contains the longest recurring cycle in its decimal fraction part.

# We use the standard long division algorithm from grade school to
# determine the longest cycle:

longestDivisor = 3 # (the divisor that creates the longest cycle)
longestCycle = 1

for divisor in range (4, 1000):
    # We keep track of all the dividends, because the first time we see the
    # same dividend again, we know the cycle will repeat. Furthermore, the 
    # length of the cycle will be the difference between the indices of the 
    # repeated dividends
    dividends = [10]
    # Check if same dividend occurs or decimal expansion terminates. 
    # If not, continue with long division algorithm:
    while dividends.index(dividends[-1]) == len(dividends) - 1 \
    and dividends[-1] != 0:
        # cycle.append(dividend // divisor)
        dividends.append((dividends[-1] % divisor) * 10)
    # If decimal terminates, don't consider it:
    if dividends[-1] == 0:
        continue
    # But if it cycles, find the cycle length:
    else:
        cycleLength = len(dividends) - 1 - dividends.index(dividends[-1])
        if cycleLength > longestCycle:
            longestCycle = cycleLength
            longestDivisor = divisor

print(longestDivisor)


        
    