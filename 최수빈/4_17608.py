import sys


n = int(sys.stdin.readline())
sticks = [int(sys.stdin.readline()) for _ in range(n)]
count = 1
max_len = sticks[len(sticks)-1]


for stick in sticks[::-1]:
    if stick > max_len:
        max_len = stick
        count += 1

print(count)