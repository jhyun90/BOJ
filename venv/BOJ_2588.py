
a = int(input())
b = int(input())

print("%d\n%d\n%d\n%d" % ((a * (b % 10)), (a * ((b % 100) // 10)), (a * (b // 100)), (a * b)))

'''
472
385

20
 35
  10
2360

  2360
 3776
1416
181720
'''
'''
# i_list = ""
ini_list = []
n_lines = 2

for i in range(n_lines):
    # ini_list += input() + '\n'
    ini_list.append(input())
    # ini_list.append(int(input()))
    # ini_list.append(input().splitlines())

# print(ini_list)

# print(ini_list[0])
# print(ini_list[1])
#
# print(ini_list[0][0], ini_list[0][1], ini_list[0][2], sep=' ')
# print(ini_list[1][0], ini_list[1][1], ini_list[1][2], sep=' ')

# a_list = [int(i) for i in ini_list][:1]
# b_list = [int(i) for i in ini_list][1:2]

# second_list = [int(i) * int(j) for i in reversed(ini_list[1]) for j in ini_list[0]]
a_list = [int(i) * int(j) for i in reversed(ini_list[1]) for j in ini_list[0]][:3]
b_list = [int(i) * int(j) for i in reversed(ini_list[1]) for j in ini_list[0]][3:6]
c_list = [int(i) * int(j) for i in reversed(ini_list[1]) for j in ini_list[0]][6:9]

# print(second_list)
# print(a_list)
# print(b_list)
# print(c_list)

# print(a_list[0] // 10,
#       a_list[0] % 10 + a_list[1] // 10,
#       a_list[1] % 10 + a_list[2] // 10,
#       a_list[2] % 10, sep='')
#
# print(b_list[0] // 10,
#       b_list[0] % 10 + b_list[1] // 10,
#       b_list[1] % 10 + b_list[2] // 10,
#       b_list[2] % 10, sep='')
#
# print(c_list[0] // 10,
#       c_list[0] % 10 + c_list[1] // 10,
#       c_list[1] % 10 + c_list[2] // 10,
#       c_list[2] % 10, sep='')

# d = [(a_list[i] % 10) + (a_list[i + 1] // 10) for i in range(len(a_list) - 1)]
# print(int(''.join(map(str, d))))

a = str(a_list[0] // 10) + str(a_list[0] % 10 + a_list[1] // 10) + str(a_list[1] % 10 + a_list[2] // 10) + str(a_list[2] % 10)
b = str(b_list[0] // 10) + str(b_list[0] % 10 + b_list[1] // 10) + str(b_list[1] % 10 + b_list[2] // 10) + str(b_list[2] % 10)
c = str(c_list[0] // 10) + str(c_list[0] % 10 + c_list[1] // 10) + str(c_list[1] % 10 + c_list[2] // 10) + str(c_list[2] % 10)

print(int(a))
print(int(b))
print(int(c))

# print(a, b, c, sep=' ')
#
# print(int(c) // 1000)
#
# print((((int(c) % 1000) // 100) + (int(b) // 1000)) +
#       ((((int(c) % 100) // 10) + ((int(b) % 1000) // 100) + (int(a) // 1000)) // 10))
#
# print(((((int(c) % 100) // 10) + ((int(b) % 1000) // 100) + (int(a) // 1000)) % 10) +
#       (((int(c) % 6) + ((int(b) % 100) // 10) + ((int(a) % 1000) // 100)) // 10))
#
# print((((int(c) % 6) + ((int(b) % 100) // 10) + ((int(a) % 1000) // 100)) // 10) +
#       ((int(b) % 10) + ((int(a) % 100) // 10) // 10))
#
# print(((int(b) % 10) + ((int(a) % 100) // 10)) % 10)
#
# print(int(a) % 10)

res = str(int(c) // 1000) + \
      str((((int(c) % 1000) // 100) + (int(b) // 1000)) +
          ((((int(c) % 100) // 10) + ((int(b) % 1000) // 100) + (int(a) // 1000)) // 10)) + \
      str((((((int(c) % 100) // 10) + ((int(b) % 1000) // 100) + (int(a) // 1000)) % 10) +
           (((int(c) % 6) + ((int(b) % 100) // 10) + ((int(a) % 1000) // 100)) // 10))) + \
      str((((int(c) % 6) + ((int(b) % 100) // 10) + ((int(a) % 1000) // 100)) // 10) +
          ((int(b) % 10) + ((int(a) % 100) // 10) // 10)) + \
      str(((int(b) % 10) + ((int(a) % 100) // 10)) % 10) + \
      str(int(a) % 10)

print(int(res))
'''
