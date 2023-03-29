from typing import List

def add_nums(nums: List[int]) -> int:

    #Base Case: nums = [3]
    if len(nums) == 1:
        return nums[0]
    
    # Recursive Case (Divide and Conquer): nums = [1, 2, 3, 4]
    first = add_nums([nums[0]])
    second = add_nums(nums[1:0])

    return first + second


add_nums([31, 45, 123, 312])
    