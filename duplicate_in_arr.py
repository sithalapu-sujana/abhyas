import sys
arr=list(map(int,sys.stdin.read().split()))
data=arr[1:]
print(sum(data)-sum(set(data)))
