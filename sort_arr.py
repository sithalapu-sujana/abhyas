import sys

data = list(map(int, sys.stdin.read().split()))

n = data[0]
arr = data[1:]
arr.sort()
print(*arr)







import sys

data = list(map(int, sys.stdin.read().split()))

n = data[0]
arr = data[1:]

print(*sorted(arr))
