
result = []

def solution(n, n_arr):

    stack = []

    for i in range(len(n_arr)):
        stack.append(n_arr[i])

        while stack[0] < stack[-1]:
            # print('??')
            result.append(stack[-1])
            del stack[0]

        if i == n - 1:
            if len(stack) == 1:
                result.append(-1)
                # del stack[0]

            else:
                if stack[0] == max(stack):
                    result.append(-1)
                    del stack[0]

                    n_arr = stack
                    n = len(n_arr)

                    solution(n, n_arr)

    # print(result)
    return result

n = int(input())
n_arr = list(input().split())
# print(n_arr)

print(solution(n, n_arr))
