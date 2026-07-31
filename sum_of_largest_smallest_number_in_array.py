import sys
data=list(map(int,sys.stdin.read().split()))
arr=data[1:]
print(max(arr)+min(arr))
