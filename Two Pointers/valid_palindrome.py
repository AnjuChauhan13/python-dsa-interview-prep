"""
Problem:
Given a string, determine whether it is a palindrome after
removing all non-alphanumeric characters and ignoring cases.

Time Complexity: O(n)
Space Complexity: O(1)
"""

s = "A man, a plan, a canal: Panama"

left = 0
right = len(s) - 1

while left < right:

    # Skip non-alphanumeric characters from the left
    while left < right and not s[left].isalnum():
        left += 1

    # Skip non-alphanumeric characters from the right
    while left < right and not s[right].isalnum():
        right -= 1

    # Compare characters (ignore uppercase/lowercase)
    if s[left].lower() != s[right].lower():
        print(False)
        break

    # Move both pointers inward
    left += 1
    right -= 1

else:
    # Executed only if the while loop completes without break
    print(True)