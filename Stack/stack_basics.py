# Stack Basics in Python

stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Current Stack:", stack)

# Peek
print("Top Element:", stack[-1])

# Pop
removed = stack.pop()

print("Removed:", removed)

print("Current Stack:", stack)

# Check Empty
if not stack:
    print("Stack is Empty")
else:
    print("Stack is Not Empty")