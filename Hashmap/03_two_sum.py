"""
Problem: Two Sum Using Hash Map

Given an array of integers and a target,
return the indices of two numbers whose sum equals the target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):

    complement = target - nums[i]

    if complement in seen:
        print([seen[complement], i])
        break

    seen[nums[i]] = i