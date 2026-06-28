# Two Sum II (Input Array Is Sorted)

## Problem Statement

# Given a **sorted** array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

# You may assume that there is **exactly one solution**, and you may not use the same element twice.

# The solution must use the **Two Pointer** approach.




"""
Question:
Find the indices of two numbers in a sorted array
whose sum equals the target.

Approach:
1. Initialize two pointers:
   - left at the beginning.
   - right at the end.
2. Calculate the current sum.
3. If the sum equals the target, return the indices.
4. If the sum is smaller than the target, move the left pointer.
5. If the sum is greater than the target, move the right pointer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

nums = [2, 7, 11, 15]
target = 9

left = 0
right = len(nums) - 1

while left < right:

    current_sum = nums[left] + nums[right]

    if current_sum == target:
        print([left, right])
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1
