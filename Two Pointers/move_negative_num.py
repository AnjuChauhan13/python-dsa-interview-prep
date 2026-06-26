"""
Question:
Move all negative numbers to the left side of the array using two pointers.

Approach:
1. Use two pointers:
   - left starts from the beginning.
   - right starts from the end.
2. If left is already negative, move left.
3. If right is already positive, move right.
4. Otherwise, swap the positive number on the left with the negative number on the right.
5. Continue until the pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

nums = [3, -2, 5, -1, 4, -6]

left = 0
right = len(nums) - 1

while left < right:

    # Left number is already negative
    if nums[left] < 0:
        left += 1

    # Right number is already positive
    elif nums[right] > 0:
        right -= 1

    # Left is positive and right is negative → swap
    else:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

print(nums)