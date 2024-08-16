import sys

# n = int(sys.stdin.readline())
# block = [int(sys.stdin.readline()) for _ in range(n)]
n = 6
block = [6, 9, 7, 6, 4, 6]
cansee = [0]
for i in block[::-1]:
    if i > cansee[-1]:
        cansee.append(i)
        block.pop()
print(len(cansee)-1)