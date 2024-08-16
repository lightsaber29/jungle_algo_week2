import sys

innum = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip().split() for _ in range(innum)]

stack = []

for a in arr:
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())