import sys
# 1. 처음 꺼낼때 "("  >  no
# 2. 마지막 꺼낼때 ")" > no

n = int(sys.stdin.readline())
checkstr = [sys.stdin.readline().strip() for _ in range(n)]
print(checkstr)
# n = 6
# checkstr = ["()()()()(()()())()"]
# count = 0

for i in range(n):
    count = 0
    for strcheck in checkstr[i]:
        if strcheck == ")":
            count += 1
        else:
            count -= 1
        
        if count > 0:
            print("NO")
            break

    if count == 0:
        print("YES")
    elif count < 0:
        print("NO")


