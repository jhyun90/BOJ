
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

'''
예제 입력 1
4
3
0
4
0

예제 입력 2
10
1
3
5
4
0
0
7
0
0
6
'''
