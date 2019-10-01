
def count_fibonacci(n):
    count_zero = [1, 0]
    count_one = [0, 1]

    if n <= 1:
        return

    for i in range(2, n + 1):
        count_zero.append(count_zero[i - 1] + count_zero[i - 2])
        count_one.append(count_one[i - 1] + count_one[i - 2])

    return count_zero, count_one


n = int(input())
count_zero, count_one = count_fibonacci(40)

for _ in range(n):
    m = int(input())
    print("{} {}".format(count_zero[m], count_one[m]))

'''
예제
3
0
1
3
출력
1 0
0 1
1 2
'''
