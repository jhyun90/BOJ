
n = int(input())

random_seq = []

for i in range(n):
    random_seq.append(int(input()))

# print(random_seq)

stack = []
operator = []

j = 0

for i in range(n):
    stack.append(i + 1)
    operator.append('+')

    while len(stack) != 0 and stack[-1] == random_seq[j]:
        stack.pop()
        operator.append('-')
        j += 1

# print(stack)

if len(stack) == 0:
    for x in operator:
        print(x)

if len(stack) != 0:
    print("NO")
