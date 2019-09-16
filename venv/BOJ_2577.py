import sys
import numpy as np

n = 3
num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)

mul = np.prod(num_list)
# print(mul)
# mul_str = str(mul)
mul_str = repr(mul)

for i in range(10):
    print(mul_str.count(repr(i)))

# print(mul_str.count(str(i)) for i in range(10)) -> why error?
