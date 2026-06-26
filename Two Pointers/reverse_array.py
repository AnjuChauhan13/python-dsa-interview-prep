"""
Question:
Reverse an array using the Two Pointer approach.

Approach:
1. Initialize two pointers:
   - left starts from the beginning.
   - right starts from the end.
2. Swap the elements at left and right.
3. Move left one step forward and right one step backward.
4. Repeat until the pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

nums = [1, 2, 3, 4, 5]

# Left pointer starts from the first element
left = 0

# Right pointer starts from the last element
right = len(nums) - 1

# Continue until both pointers meet
while left < right:

    # Swap the elements at left and right
    nums[left], nums[right] = nums[right], nums[left]

    # Move left pointer forward
    left += 1

    # Move right pointer backward
    right -= 1

# Print the reversed array
print(nums)