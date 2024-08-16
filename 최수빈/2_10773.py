# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
import sys

k = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(k)]
stack = []

for a in arr:
    if a == 0:
        # 최근에 쓴 수를 지우기
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))