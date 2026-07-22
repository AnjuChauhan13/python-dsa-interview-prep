# Reverse Words using Stack

s = "I love Python"

words = s.split()

stack = []

# Push every word
for word in words:
    stack.append(word)

result = []

# Pop every word
while stack:
    result.append(stack.pop())

print("Original Sentence:")
print(s)

print("\nReversed Sentence:")
print(" ".join(result))
