# Check Palindrome using Stack

s = "madam"

stack = []

# Push every character
for ch in s:
    stack.append(ch)

result = ""

# Reverse using stack
while stack:
    result += stack.pop()

if result == s:
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is Not a Palindrome')