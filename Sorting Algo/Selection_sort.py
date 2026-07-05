"""
Problem: Selection Sort

Given an array of integers, sort the array in ascending order
using the Selection Sort algorithm.

Time Complexity:
Worst Case: O(n²)
Average Case: O(n²)
Best Case: O(n²)

Space Complexity:
O(1)
"""

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):

    # Assume the current element is the minimum
    min_index = i

    # Find the index of the smallest element
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the smallest element with the current position
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:", arr)