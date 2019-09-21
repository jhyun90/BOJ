
class Queue:

    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, data):
        self.list.append(data)
        self.len += 1

    def pop(self):
        if self.len == 0:
            return -1

        pop_res = self.list[0]

        del self.list[0]
        self.len -= 1

        return pop_res

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def front(self):
        return self.list[0] if self.len != 0 else -1

    def back(self):
        return self.list[-1] if self.len != 0 else -1


n_lines = int(input())

queue = Queue()

for i in range(n_lines):
    line = input().split()

    cmd = line[0]

    if cmd == "push":
        queue.push(line[1])
    elif cmd == "pop":
        print(queue.pop())
    elif cmd == "size":
        print(queue.size())
    elif cmd == "empty":
        print(queue.empty())
    elif cmd == "front":
        print(queue.front())
    elif cmd == "back":
        print(queue.back())

'''
예제 입력 1
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
'''
