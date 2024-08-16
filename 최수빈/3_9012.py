import sys

stack = []
# 결국에 괄호가 짝이 맞아야함
# 그래서 우괄호 체크하면 
def check_vps(str):
    stack = []
    for s in str:
        if s == '(':
            stack.append(1)
        elif s == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

t = int(sys.stdin.readline())
str_arr = [sys.stdin.readline().strip() for _ in range(t)]

for str in str_arr:
    print(check_vps(str))

# print(str_arr)