# Search Insert Position
# Problem

# Return the index if the target exists. Otherwise, return the position where it should be inserted.

# Example
# nums = [1, 3, 5, 6]
# target = 2

# Output
# 1

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return left


nums = [1, 3, 5, 6]
target = 2

print(search_insert(nums, target))