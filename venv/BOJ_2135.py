
# https://www.acmicpc.net/problem/2135

# string = 'aabbaccc'
# string = 'abcabcdede'
# string = 'letsgogogo'
# string = 'letsgogogoletsgogogo'
# string = 'nowletsgogogoletsgogogo' # now2(lets3(go))
# string = 'nowletsgogogoletsgogogoandrunrunrun' # now2(lets3(go))and3(run)

# string = input()
#
# n = len(string)
#
# result = ''
#
# for i in range(1, n // 2 + 1):
#
#     # if i == 1:
#     #     result = ''
#
#     # string[0:1] begin = 0
#     # string[1:2] begin = 1
#     # string[2:3] begin = 2
#     # string[3:4] begin = 3
#     # string[4:5] begin = 4
#     # string[5:6] begin = 5
#     # string[6:7] begin = 6
#     # string[7:8] begin = 7
#     # string[8:9] begin = 8
#     # string[9:10] begin = 9
#
#     # string = 'abccddd'
#     # stack = []
#     # stack.append(string[0])
#     # count = 1
#     # result = ''
#     #
#     # for i in range(1, len(string)):
#     #     stack.append(string[i])
#     #
#     #     print(stack[0], stack[-1])
#     #
#     #     if stack[0] == stack[-1]:
#     #         count += 1
#     #         del stack[0]
#     #
#     #     else:
#     #         if count > 1:
#     #             result += str(count)
#     #
#     #         result += stack[0]
#     #         del stack[0]
#     #         count = 1
#     #
#     # result += stack[0] + str(count)
#     #
#     # print(result)
#
#     # else:
#         # if i == 2:
#         # ab ca bc de de
#
#     # string[0:2] string[2:4] string[4:6] string[6:8] string[8:10]
#     # string[1:3] string[3:5] string[5:7] string[7:9] (string[9:10])
#
#     # string[0:3] string[3:6] string[6:9] (string[9:10])
#     # string[1:4] string[4:7] string[7:10]
#     # string[2:5] string[5:8] (string[8:10])
#
#     stack = []
#     begin = 0
#     end = begin + i
#     # string[0:2] begin = 0
#     stack.append(string[begin:end])
#     cnt = 1
#
#     for _ in range(1, n):
#         print(begin, end)
#         begin += i
#         end = begin + i
#         stack.append(string[begin:end])
#         print(stack)
#
#         # letter_list = [[string[i:i + j] for i in range(begin, len(string))[::j] if len(string[i:i+j]) == j] for j in range(2, n//2 + 1) for begin in range(j)]
#         # letter_stack = [[x for x in letter_list if len(x) == i] for i in range(2, len(string) // 2 + 1)]
#
#         # string[2:4] begin = 2
#         # string[4:6] begin = 4
#         # string[6:8] begin = 6
#         # string[8:10] begin = 8
#
#         if end <= n and stack[0] == stack[-1]:
#             cnt += 1
#             del stack[0]
#
#         else:
#             if cnt > 1:
#                 result += str(cnt) + '('
#
#             result += stack[0]
#
#             if cnt > 1:
#                 result += ')'
#
#             del stack[0]
#             cnt = 1
#
#     if cnt > 1:
#         result += str(cnt)
#
#     result += stack[0] + '\n'
#
# print(result)
#
# compress = [x for x in result.split('\n')]
# compress_len = [len(x) for x in result.split('\n')]
# # print(compress)
# # print(compress_len)
# del compress[-1]
# del compress_len[-1]
#
# print(compress)
# print(min(compress_len))


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


def solution(string):
    n = len(string)

    letter_list = [[string[i:i + j] for i in range(begin, len(string))[::j] if len(string[i:i+j]) == j] for j in range(2, n//2 + 1) for begin in range(j)]
    print(letter_list)

    compress = []

    for i in range(len(letter_list)):
        result = ''
        stack = []
        stack.append(letter_list[i][0])
        count = 1

        for j in range(1, len(letter_list[i])):
            stack.append(letter_list[i][j])

            if stack[-1] in '1234567890()':
                continue

            if stack[0] == stack[-1]:
                count += 1
                del stack[0]

            else:
                if count > 1:
                    result += str(count) + '('

                result += stack[0]

                if count > 1:
                    result += ')'

                del stack[0]
                count = 1

        if count > 1:
            result += str(count) + '('

        result += stack[0]

        if count > 1:
            result += ')'

        print(result)

        if '(' and ')' in result:
            compress.append(result)

    print(compress)

    # for i in range(len(compress)):
    #     stack = []
    #     count = 0
    #
    #     for j in range(len(compress[i])):
    #         stack.append(compress[i][j])
    #
    #         if stack[-1] in '()':
    #             count += 1
    #
    #     print(count)


string = 'letsgogogoletsgogogo'
# string = 'lets3(go)lets3(go)'
# string = '2(letsgogogo)'
# string = 'nowletsgogogoletsgogogoandrunrunrun'
# string = 'owlets3(go)lets3(go)andrunrunrun'
print(string)

solution(string)
print()
