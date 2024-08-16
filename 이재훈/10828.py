# 스택 구현
import sys
num = int(sys.stdin.readline())


list_stack = []
for i in range(num):

    doit = sys.stdin.readline().split()

    if doit[0] == 'push':
        list_stack.append(doit[1])

    elif doit[0] == "top":
        if len(list_stack) == 0:
            print(-1)
            
        else:
            print(list_stack[-1])

    elif doit[0] == "pop":
        if len(list_stack) == 0:
            print(-1)

        else:
            print(list_stack[-1])
            list_stack.pop()
    
    elif doit[0] == "size":
        print(len(list_stack))
    
    elif doit[0] == "empty":
        if len(list_stack) == 0:
            print(1)

        else:
            print(0)