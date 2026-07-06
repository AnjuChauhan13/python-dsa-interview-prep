"""
Problem:
Given an integer array and a window size k,
find the maximum sum of any contiguous subarray of size k.

Time Complexity: O(n)
Space Complexity: O(1)
"""

nums = [2, 1, 5, 1, 3, 2]
k = 3

# Calculate the sum of the first window
window_sum = 0
for i in range(k):
    window_sum += nums[i]

# Initialize max_sum with the first window sum
max_sum = window_sum

# Slide the window
for right in range(k, len(nums)):

    # Remove the element leaving the window
    window_sum -= nums[right - k]

    # Add the new element entering the window
    window_sum += nums[right]

    # Update the maximum sum
    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum Sum:", max_sum)