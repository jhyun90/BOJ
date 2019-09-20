import sys

num_arr = [True for i in range(1000)]

for i in range(123, 1000):
    num = str(i)

    if (num[0] == '0' or num[1] == '0' or num[2] == '0') or (num[0] == num[1] or num[1] == num[2] or num[2] == num[0]):
        # print(num, "F")
        num_arr[i] = False

    # if num[0] == '0' or num[1] == '0' or num[2] == '0':
    #     print(num)
    #     num_arr[i] = False
    #
    # if num[0] == num[1] or num[1] == num[2] and num[2] == num[0]:
    #     print(num)
    #     num_arr[i] = False

    # if num_arr[i]:
    #     print(num, "T")
        # print(num_arr[i])

n = int(sys.stdin.readline())

answer = 0

for i in range(n):
    n_try = list(map(int, sys.stdin.readline().split()))
    # print(n_try)

    guess = str(n_try[0])
    strike = n_try[1]
    ball = n_try[2]

    for j in range(123, 1000):
        num = str(j)

        strike_cnt = 0
        ball_cnt = 0

        if num_arr[j]:
            for x in range(3):
                for y in range(3):
                    if guess[x] == num[y] and x == y:
                        strike_cnt += 1

                    if guess[x] == num[y] and x != y:
                        ball_cnt += 1

            # 입력 받은 스트라이크와 볼의 개수가 일치하지 않는 경우 제외
            if strike_cnt != strike or ball_cnt != ball:
                num_arr[j] = False

for i in range(123, 1000):
    if num_arr[i]:
        # print(num_arr[i])
        answer += 1

print(answer)

'''
예제 입력 1
4
123 1 1
356 1 0
327 2 0
489 0 1
'''

'''
    3 2 4
  4     B
  2   S
  9

    3 2 4
  2   B
  4     B
  1

    3 2 4
  9
  2   S
  4     S
'''

'''
    x x x
  1 S
  2 B
  3

    x x x
  3 S
  5
  6

    x x x
  3
  2   S
  7     S

    x x x
  4   B
  8
  9
'''