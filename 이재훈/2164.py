import sys
from collections import deque

# n = int(sys.stdin.readline())
n = 6
cardnum = deque([x for x in range(1,n+1)])
for i in range(n-1):
    cardnum.popleft()
    cardnum.append(cardnum.popleft())

print(*cardnum)  

# 언팩킹 연산자 a = [1, 2, 3]라고 하면 print(*a)는 print(1, 2, 3)과 동일한 결과를 출력