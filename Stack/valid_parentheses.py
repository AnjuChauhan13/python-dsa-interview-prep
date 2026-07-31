def valid_parentheses(s):

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        # Opening brackets
        if ch in "([{":
            stack.append(ch)

        # Closing brackets
        else:

            # Stack is empty
            if not stack:
                return False

            # Top does not match
            if stack[-1] != pairs[ch]:
                return False

            # Remove matching opening bracket
            stack.pop()

    return len(stack) == 0


print(valid_parentheses("()"))
print(valid_parentheses("()[]{}"))
print(valid_parentheses("(]"))
print(valid_parentheses("([)]"))
print(valid_parentheses("{[]}"))