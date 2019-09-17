
class Stack:

    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, data):
        self.list.append(data)
        self.len += 1

    def pop(self):
        if self.len == 0:
            return -1

        pop_res = self.list[self.len - 1]

        del self.list[self.len - 1]
        self.len -= 1

        return pop_res

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def top(self):
        return self.list[-1] if self.len != 0 else -1


n_lines = int(input())

stack = Stack()

for i in range(n_lines):
    line = input().split()

    cmd = line[0]

    if cmd == "push":
        stack.push(line[1])
    elif cmd == "pop":
        print(stack.pop())
    elif cmd == "size":
        print(stack.size())
    elif cmd == "empty":
        print(stack.empty())
    elif cmd == "top":
        print(stack.top())
