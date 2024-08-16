import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('10828.txt', 'r')
sys.stdout = open('10828_o.txt', 'w')


class FixedStack:
    
    #Stack Pointer : 다음 빈 공간(다음 인덱스)을 가리키고 있는 요소 ptr
    
    #예외처리 비었을 때, 가득 찼을 때 함수를 실행하지 않고 pass 해 줌
    # class Empty(Exception):
    #     pass
    # class Full(Exception):
    #     pass
    
    #초기화 값 설정
    def __init__(self, c:int): #c는 capacity 최대크기 = len
        # self.items = [] # . 뒤에 속성을 동적으로 할당
        self.ptr = 0
        self.capacity = c
        self.stk = [None] * c #아무것도 없는 상태를 stk이라는 변수에 할당
    
    #길이
    def __len__(self) -> int:
        return self.ptr #다음 인덱스를 가리키고 있으므로 전체 길이와 같다. 길이 = 인덱스-1
    #비었니
    def empty(self):
        if self.ptr == 0: #0이거나 0보다 더 작은 값을 가리키려고 할 때
            print(1) #!
        else:
            print(0) #!
    #다찼니
    def full(self) -> bool:
        return self.ptr >= self.capacity #전체길이보다 같거나 커지려할 때

    def push(self, item):
        # self.items.append(item)
        if self.full():
            return -1
        else:
            self.stk[self.ptr] = item #다음 포인터 인덱스의 값은 현재의 item이 된다.
            self.ptr += 1 # 포인터인덱스를 1 증가시킨다.
            
        
    def pop(self):
        # self.items.pop(item)
        if self.ptr == 0:
            print(-1) #!
        else:
            self.ptr -= 1
            print(self.stk[self.ptr]) #!
        
    def size(self):
        print(self.ptr) #!!
        
    def top(self):
        # self.items[-1]
        if self.ptr == 0:
            print(-1) #!
        else:
            print(self.stk[self.ptr - 1]) #!
            
            
if __name__ == "__main__":
    n = int(input())
    stack = FixedStack(n)

#커맨드를 입력받을 리스트, 명령은 인덱스[0], 뒤의 숫자는 [1]을 읽는다.
    for _ in range(n):
        comm = sys.stdin.readline().split()
        if comm[0] == "push":
            stack.push(comm[1])
        elif comm[0] == "pop":
            stack.pop()
        elif comm[0] == "size":
            stack.size()
        elif comm[0] == "empty":
            stack.empty()
        elif comm[0] == "top":
            stack.top()
        