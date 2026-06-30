# Valid Anagram

## Problem Statement

# Given two strings `s1` and `s2`, determine whether they are anagrams of each other.

# Two strings are anagrams if they contain the same characters with the same frequency, but the characters can appear in a different order.

# Return True if the strings are anagrams; otherwise, return False.



## Example 1
# s1 = "listen"
# s2 = "silent"
# Output
# True


## Example 2
# s1 = "rat"
# s2 = "car"
# Output
# False






# Approach (Hash Map)

# 1. If the lengths of both strings are different, return `False`.
# 2. Create a dictionary to store the frequency of each character in the first string.
# 3. Traverse the second string and decrease the frequency of each character.
# 4. If every frequency becomes `0`, the strings are anagrams.
# 5. Otherwise, return `False`.



# Python Solution


# Question:
# Check whether two strings are valid anagrams.

# Approach:
# 1. Compare the lengths.
# 2. Count the frequency of characters in the first string.
# 3. Decrease the frequency using the second string.
# 4. If every frequency is zero, return True.

# Time Complexity: O(n)
# Space Complexity: O(n)


def valid_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    count = {}

    # Count characters from the first string
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    # Decrease count using the second string
    for ch in s2:
        count[ch] = count.get(ch, 0) - 1

    # Check whether all frequencies are zero
    for value in count.values():
        if value != 0:
            return False

    return True


print(valid_anagram("listen", "silent"))
print(valid_anagram("rat", "car"))
print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("hello", "world"))


