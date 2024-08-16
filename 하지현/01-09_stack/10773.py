import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('10773.txt', 'r')
sys.stdout = open('10773_o.txt', 'w')


import sys
input = sys.stdin.readline

N = int(input())
stack = []
budget = 0
for _ in range(N):
    money = int(input().strip())
    if money > 0:
        stack.append(money)
        budget += money
    elif money == 0:
        pop_money = stack.pop() #stack에서 pop한 값을 pop_value에 저장
        budget -= pop_money

print(budget)