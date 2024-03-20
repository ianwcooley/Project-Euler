# Project Euler problem 24: Find the millionth lexicographic permutation
# of the digits 0,1,2,3,4,5,6,7,8,9

import math




# This almost works - keep it

# def printPermutations(arr):
#     if len(arr) == 0:
#         print('') # print a new line and move on
#     else:
#         for i in range(0, len(arr)):
#             digit = arr[i]
#             arr.remove(digit)
#             print(digit, end='')
#             printPermutations(arr)
#             arr.insert(i, digit)
  
# printPermutations([0,1,2])