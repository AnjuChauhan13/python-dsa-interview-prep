"""
Problem: Bubble Sort

Given an array of integers, sort the array in ascending order
using the Bubble Sort algorithm.

Time Complexity:
Worst Case: O(n²)
Average Case: O(n²)
Best Case: O(n) (with optimization)

Space Complexity:
O(1)
"""

arr = [7, 4, 5, 2]

n = len(arr)

for i in range(n):

    # Flag to check if any swap happened
    swapped = False

    for j in range(n - i - 1):

        if arr[j] > arr[j + 1]:

            # Swap adjacent elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            swapped = True

    # If no swaps happened, array is already sorted
    if not swapped:
        break

print("Sorted Array:", arr)