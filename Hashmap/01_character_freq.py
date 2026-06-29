



"""
Question:
Find the first non-repeating character in a string.

Approach:
1. Count the frequency of each character.
2. Traverse the string again.
3. Print the first character whose frequency is 1.

Time Complexity: O(n)
Space Complexity: O(n)
"""

s = "aabbccddef"

count = {}

# Count frequency of each character
for ch in s:
    count[ch] = count.get(ch, 0) + 1

# Find the first non-repeating character
found = False

for ch in s:
    if count[ch] == 1:
        print("First Non-Repeating Character:", ch)
        found = True
        break

if not found:
    print("No unique character found")
