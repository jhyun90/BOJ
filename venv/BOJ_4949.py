
# lines = [x for x in input().split('\n')]

while 1:
    string = input()

    if string[0] == '.':
        break

    # print(len(string))

    stack = []

    for char in string:

        # print(char)

        if char == '.':
            break

        if char == '(' or char == '[':
            stack.append(char)

        if char == ')':
            if len(stack) != 0 and stack[-1] == '(':
                del stack[-1]
            else:
                stack.append(char)

        if char == ']':
            if len(stack) != 0 and stack[-1] == '[':
                del stack[-1]
            else:
                stack.append(char)

    # print(stack)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")

'''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
'''
