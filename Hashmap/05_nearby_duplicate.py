"""
Problem: Contains Nearby Duplicate

Return True if there are two equal numbers
whose indices differ by at most k.

Time Complexity: O(n)
Space Complexity: O(n)
"""

nums = [1, 2, 3, 1, 2, 3]
k = 2

seen = {}

for i in range(len(nums)):

    # If number already exists
    if nums[i] in seen:

        # Check the distance
        if i - seen[nums[i]] <= k:
            print(True)
            break

    # Store/update latest index
    seen[nums[i]] = i

else:
    print(False)