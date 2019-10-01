import sys
import numpy as np

n = 3
num_list = []

mul = 1

for i in range(n):
    num = int(input())
    mul *= num

print(mul)

mul = list(str(mul))

for i in range(10):
    count = mul.count(str(i))
    print(count)

'''
예제 입력 1
150
266
427

124
321
909
'''

# n = 3
# num_list = []
#
# for i in range(n):
#     num = int(input())
#     num_list.append(num)
#
# mul = np.prod(num_list)
# print(mul)
# # mul_str = str(mul)
# mul_str = repr(mul)
#
# for i in range(10):
#     print(mul_str.count(repr(i)))
#
# # print(mul_str.count(str(i)) for i in range(10)) -> why error?
