import sys
data=list(map(int, sys.stdin.read().split()))
n=data[0]
arr=data[1:]
for num in arr:
    if arr.count(num) == 1:
        print(num)
        break
