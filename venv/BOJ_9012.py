
T = int(input())

for i in range(T):
    line = list(input())

    stack = []

    for j in range(len(line)):
        if line[j] == '(':
            stack.append(line[j])

        if line[j] == ')':
            if len(stack) != 0:
                del stack[-1]
            else:
                stack.append(line[j])

        # print(stack)

    # print(stack)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
