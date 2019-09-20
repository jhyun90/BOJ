import sys

n = int(sys.stdin.readline())
n_arr = list(input().split())

# result = [-1 for _ in range(n)]

# n_arr[0] < n_arr[1], n_arr[2], n_arr[3] -> 큰 수 나오면 바로 멈춤 break
# n_arr[1] < n_arr[2], n_arr[3] -> 큰 수 나오면 바로 멈춤 break
# n_arr[2] < n_arr[3] -> 큰 수 나오면 바로 멈춤 break
# n_arr[3] -> -1 추
# 큰 수 없으면 -1로 채우기

stack = []
result = []

i = 0
# for i in range(n):
while i < n:
    print("i:", i)
    stack.append(n_arr[i])

    while stack[0] < stack[-1]:
        print("stack before pop:", stack)
        result.append(stack[-1])
        print("result:", result)
        del stack[0]
        print("stack:", stack)


    if i == n - 1:
        if len(stack) == 1:
            result.append(-1)

        if len(stack) == n:
            result.append(-1)
            del stack[0]

    i += 1
    print()

print("final:", result)


'''
예제 입력 1
4
3 5 2 7

예제 입력 2
4
9 5 4 8
'''

# import sys
#
# n = int(sys.stdin.readline())
#
# n_arr = list(map(int, sys.stdin.readline().split()))
# print(n_arr)
#
# idx = []
# result = [-1 for _ in range(n)]
#
# idx.append(0)
#
# i = 1
#
# while idx and i < n:
#     print("i:", i)
#     print("idx[-1]:", idx[-1])
#
#     while idx and n_arr[idx[-1]] < n_arr[i]:
#         print("n_arr[", i, "]:", n_arr[i])
#         result[idx[-1]] = n_arr[i]
#         print("result[", idx[-1], "]:", result[idx[-1]])
#         idx.pop()
#         print("idx after pop:", idx)
#
#     idx.append(i)
#     print("idx:", idx)
#     i += 1
#     print()
#
# for i in range(n):
#     print(result[i], end=' ')
