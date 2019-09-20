
# string = 'abccddd'
#
# stack = []
# stack.append(string[0])
# count = 1
# result = ''
#
# for i in range(1, len(string)):
#     stack.append(string[i])
#
#     print(stack[0], stack[-1])
#
#     if stack[0] == stack[-1]:
#         count += 1
#         del stack[0]
#
#     else:
#         if count > 1:
#             result += str(count)
#
#         result += stack[0]
#         del stack[0]
#         count = 1
#
# result += stack[0] + str(count)
#
# print(result)


# string = 'aabbaccc'
# string = 'abcabcdede'
# string = 'letsgogogo'

string = input()

n = len(string) # n = 10

result = ''

for i in range(1, n // 2 + 1): # range(1, 6): 1, 2, 3, 4, 5

    # if i == 1:
    #     result = ''

    # string[0:1] begin = 0
    # string[1:2] begin = 1
    # string[2:3] begin = 2
    # string[3:4] begin = 3
    # string[4:5] begin = 4
    # string[5:6] begin = 5
    # string[6:7] begin = 6
    # string[7:8] begin = 7
    # string[8:9] begin = 8
    # string[9:10] begin = 9

    # else:
        # if i == 2:
        # ab ca bc de de

    stack = []
    begin = 0
    end = begin + i
    # string[0:2] begin = 0
    stack.append(string[begin:end])
    cnt = 1

    for _ in range(1, n):
        print(begin, end)
        begin += i
        end = begin + i
        stack.append(string[begin:end])
        print(stack)

        # string[2:4] begin = 2
        # string[4:6] begin = 4
        # string[6:8] begin = 6
        # string[8:10] begin = 8

        if end <= n and stack[0] == stack[-1]:
            cnt += 1
            del stack[0]

        else:
            if cnt > 1:
                result += str(cnt)

            result += stack[0]
            del stack[0]
            cnt = 1

    if cnt > 1:
        result += str(cnt)

    result += stack[0] + '\n'

print(result)

compress = [x for x in result.split('\n')]
compress_len = [len(x) for x in result.split('\n')]
del compress[-1]
del compress_len[-1]

print(compress)
print(min(compress_len))


    # if i == 3:
    #     # abc abc ded e
    #     string[begin:begin + i]
    #
    #     string[0:3] begin = 0
    #     string[3:6] begin = 3
    #     string[6:9] begin = 6
    #
    #     string[9:10] # index out of range
    #
    # if i == 4:
    #     # abca bcde
    #     string[begin:begin + i]
    #
    #     string[0:4]
    #     string[4:8]
    #
    #     string[8:10] # # index out of range
    #
    # if i == 5:
    #     # abcab cdede
    #     string[begin:begin + i]
    #
    #     string[0:5]
    #     string[5:10]
