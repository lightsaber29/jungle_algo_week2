import sys
from collections import deque 

# n, k= map(int,sys.stdin.readline().split())
n, k = 7, 3

peoplelist = deque([x for x in range(1,n+1)])

linepeople = []

for i in range(len(peoplelist)):
    
    for push in range(k-1):
        peoplelist.append(peoplelist.popleft())

    linepeople.append(peoplelist.popleft())

print("<" + ", ".join(map(str,linepeople)) +">")

# print("<" + ", ".join(map(str,linepeople)) +">") 이 방식 기억하자
