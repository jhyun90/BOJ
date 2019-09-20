
n_lines = int(input())

for i in range(n_lines):
    string = list(input())
    # print(string)
    stack = []

    for j in range(len(string)):
        if string[j] == '(':
            stack.append(string[j])

        if string[j] == ')':
            if len(stack) != 0:
                del stack[-1]
            else:
                stack.append(string[j])

        # print(stack)

    # print(stack)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

'''
예제 입력 1
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
'''
