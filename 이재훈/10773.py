import sys

num = int(sys.stdin.readline())
list_stack = []

for count in range(num):
    number = int(sys.stdin.readline())
    if number == 0:
       list_stack.pop() 
    else:
        list_stack.append(number)

print(sum(list_stack))