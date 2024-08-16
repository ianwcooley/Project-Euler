# Project Euler problem 31: Find the number of ways to make two pounds with the
# standard UK coins:

TWO_POUNDS = 200
ONE_POUND = 100
FIFTY_PENCE = 50
TWENTY_PENCE = 20
TEN_PENCE = 10
FIVE_PENCE = 5
TWO_PENCE = 2
ONE_PENCE = 1

coins = [TWO_POUNDS, ONE_POUND, FIFTY_PENCE, TWENTY_PENCE, 
         TEN_PENCE, FIVE_PENCE, TWO_PENCE, ONE_PENCE]

# We make combinations of coins by appending and popping them from a list 
# called "combination". When the combination adds up to 200, we increment 
# the number_of_combinations

number_of_combinations = 0

coin_index = 0
# the coin we are currently appending to our combination to try to get to 200:
coin = coins[coin_index]

# the combination of coins that we are currently examining and its sum
combination = []
combination_sum = 0

while True:

    # keep appending the current coin until we reach or excede 200:
    while combination_sum < 200:
        combination.append(coin)
        combination_sum += coin

    # if we reach 200, increment the number_of_combinations:
    if combination_sum == 200:   
        number_of_combinations += 1
        # our final combination will be all ONE_PENCE coins, at
        # which point we stop:
        if all(coins == ONE_PENCE for coins in combination):
            print(number_of_combinations)
            break

    # If our given coin is ONE_PENCE, we must remove the ONE_PENCE coins
    # we added to our combination until we get the next biggest coin we are using,
    # then we pop it and continue the process with the next smallest coin after it
    if coin == ONE_PENCE:
        while combination[-1] == ONE_PENCE:
            combination_sum -= combination[-1]
            combination.pop()
        coin_index = coins.index(combination[-1]) + 1
        coin = coins[coin_index]
    # Otherwise, we move on to the next smallest coin:
    else:
        coin_index += 1
        coin = coins[coin_index]

    # Whether we've exceeded or reached 200, we must pop off the last coin
    # and try to make our next combination:
    combination_sum -= combination[-1]
    combination.pop()

# test_file.close()
