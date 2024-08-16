import sys
from collections import deque
# deque(리스트)  < 디큐 만듦
# append(요소)  < 
# pop()  <  오른쪽 맨끝 삭제
# popleft()  < 왼쪽 끝 삭제

# 큐 구현

num = int(sys.stdin.readline())


list_que = deque([])
for i in range(num):

    doit = sys.stdin.readline().split()

    if doit[0] == 'push':

        list_que.append(doit[1])

    elif doit[0] == "pop":

        if len(list_que) > 0:
            print(list_que.popleft())

        else:
            print(-1)

    elif doit[0] == "size":

        print(str(len(list_que)))
    
    elif doit[0] == "empty":

        if len(list_que) == 0:
            print(1)
        else:
            print(0)
    
    elif doit[0] == "front":

        if len(list_que) == 0:
            print(-1)
            
        else:
            print(list_que[0])
    
    elif doit[0] == "back":

        if len(list_que) == 0:
            print(-1)
            
        else:
            print(list_que[-1])