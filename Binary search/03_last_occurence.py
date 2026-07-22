# Find Last Occurrence
# Problem

# Return the last occurrence of the target.

# Example
# nums = [1, 2, 2, 2, 3, 4]
# target = 2

# Output

# 3

def last_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            answer = mid
            left = mid + 1

        elif target > nums[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return answer


nums = [1, 2, 2, 2, 3, 4]
target = 2

print(last_occurrence(nums, target))