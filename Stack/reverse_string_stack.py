# Reverse a String using Stack

s = "ChatGPT"

stack = []

# Push every character
for ch in s:
    stack.append(ch)

result = ""

# Pop every character
while stack:
    result += stack.pop()

print("Original String :", s)
print("Reversed String:", result)