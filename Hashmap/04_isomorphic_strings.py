"""
Problem: Isomorphic Strings

Determine whether two strings are isomorphic.

Time Complexity: O(n)
Space Complexity: O(n)
"""

s = "paper"
t = "title"

# Different lengths can never be isomorphic
if len(s) != len(t):
    print(False)

else:

    s_to_t = {}
    t_to_s = {}

    is_isomorphic = True

    for i in range(len(s)):

        char_s = s[i]
        char_t = t[i]

        # Check mapping from s -> t
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                is_isomorphic = False
                break
        else:
            s_to_t[char_s] = char_t

        # Check mapping from t -> s
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                is_isomorphic = False
                break
        else:
            t_to_s[char_t] = char_s

    print(is_isomorphic)