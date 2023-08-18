from typing import List

""""""

def add_nums(nums: List[int]) -> int:

    #Base Case: nums = [3]
    if len(nums) == 1:
        return nums[0]
    
    # Recursive Case (Divide and Conquer): nums = [1, 2, 3, 4]
    first = add_nums([nums[0]])
    second = add_nums(nums[1:0])

    return first + second


# add_nums([31, 45, 123, 312])



"""Reverse an array"""
def reverse(nums: List[int]) -> int:

    #Base Case: [4] => [4]
    if len(nums)==1:
        return nums
    
    #Recursive: [1] + [1, 2] || [2] + [1] => [2, 1]
    first = reverse([nums[0]])
    second = reverse(nums[1:])

    return second + first


# reverse([1, 2, 6, 7, 8 ])




"""Factorial of a number"""

def factorial(n):

    # Base Case
    if n == 1 or n == 0:
        return 1
    
    # Recursive 
    first = n
    second = factorial(n-1)

    return first * second



n = 1
print(factorial(n))