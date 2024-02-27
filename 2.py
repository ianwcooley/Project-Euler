sum = 0
fib1 = 1
fib2 = 1
fib3 = 2
fibTemp = 0
while fib3 <= 4000000:
    if fib3 % 2 == 0:
        sum = sum + fib3
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2
print(sum)
    
