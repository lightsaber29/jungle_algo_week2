import sys

instr = sys.stdin.readline().strip()
stack = []
cal_val = 1
result = 0

# 괄호가 다음거에서 안 닫히고 들어가면 곱하기네
# 곱과 합을 결정하는 기준?
# 우괄호([ 다음에 우괄호([ 가 오면 곱하기
# 우괄호 들어갈 때 곱하기
# 

# 일단 곱셈부터만 구현해보자
# [[]()] 이거부터 해보자
for idx, s in enumerate(instr):
    print(f's: {s} stack: {stack} cal_val: {cal_val}')
    # 우괄호 들어올 때
    if s == '(':
        stack.append(s)
        cal_val *= 2
    elif s == '[':
        stack.append(s)
        cal_val *= 3
    # 좌괄호 들어올 때 -> 계산해야함
    elif s == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if instr[idx-1] == '(':
            result += cal_val
        cal_val //= 2
        stack.pop()
    elif s == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if instr[idx-1] == '[':
            result += cal_val
        cal_val //= 3
        stack.pop()

if stack:
    result = 0

print(result)