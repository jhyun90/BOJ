
n_lines = int(input())
stack = []

for i in range(n_lines):
    x = int(input())

    if x != 0:
        stack.append(x)

    if x == 0:
        del stack[-1]

# print(stack)

sum = 0

for i in stack:
    sum += i

print(sum)
