# Project Euler problem 9: Find the Pythagorean triplet for which a + b + c = 1000. Find the product of this triplet.

for a in range(1, 998):
    for b in range(a, 998):
        if a+b > 998:
            break
        if 1000 * (a+b) - a * b == 500000:
            print(a, b, 1000 - a - b)
            print(a*b*(1000-a-b))