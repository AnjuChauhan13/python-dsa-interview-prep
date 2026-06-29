# Remove Duplicates from Sorted Array

## Problem Statement

# Given a **sorted** array `nums`, remove the duplicates **in-place** such that each unique element appears only once.

# Return the number of unique elements.

# **Do not create another array.** Modify the input array using **O(1)** extra space.


# Approach (Two Pointers)

# We use two pointers:

# * **write** → Points to the last unique element.
# * **read** → Traverses the array to find new unique elements.

### Algorithm

# 1. Initialize `write = 0`.
# 2. Traverse the array using `read`.
# 3. If `nums[read]` is different from `nums[write]`, a new unique element is found.
# 4. Move the `write` pointer forward.
# 5. Copy the unique element to the `write` position.
# 6. After the loop, the first `write + 1` elements are the unique elements.



# Python Solution

"""
# Question:
# Remove duplicates from a sorted array in-place.

# Approach:
# 1. Use two pointers:
#    - write: stores the position of the last unique element.
#    - read: scans the array.
# 2. When a new unique element is found,
#    move the write pointer and copy the element.
# 3. Return the unique elements and their count.

# Time Complexity: O(n)
# Space Complexity: O(1)
"""

nums = [0,0,1,1,1,2,2,3,3,4]

write = 0

for read in range(1, len(nums)):

    # Found a new unique element
    if nums[write] != nums[read]:

        # Move write pointer
        write += 1

        # Copy unique element
        nums[write] = nums[read]

print("Unique Elements:", nums[:write + 1])
print("Count:", write + 1)


# Dry Run

# Input:

# ```python
# nums = [0,0,1,1,1,2,2,3,3,4]
# ```

# Initially

# ```text
# Write
#   ↓
# 0 0 1 1 1 2 2 3 3 4
#   ↑
# Read
# ```

# * Duplicate `0` → Move `read`
# * New element `1` → Move `write`, copy `1`
# * Duplicate `1` → Move `read`
# * New element `2` → Move `write`, copy `2`
# * Duplicate `2` → Move `read`
# * New element `3` → Move `write`, copy `3`
# * Duplicate `3` → Move `read`
# * New element `4` → Move `write`, copy `4`

# Final array:

# ```python
# [0,1,2,3,4,2,2,3,3,4]
# ```

# Only the first **5** elements are valid:

# ```python
# [0,1,2,3,4]
# ```

# Return:

# ```python
# Count = 5
# ```

# ---

# # Time Complexity

# ```text
# O(n)
# ```

# Each element is visited once.

# ---

# # Space Complexity

# ```text
# O(1)
# ```

# No extra array is used.

# ---

# Key Learning

# * This problem works because the array is **already sorted**.
# * The **read** pointer checks every element.
# * The **write** pointer keeps track of where to place the next unique element.
# * Duplicate values are **overwritten**, not deleted.
# * Only the first `write + 1` elements are considered part of the final answer.
