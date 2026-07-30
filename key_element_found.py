n = int(input())
arr = list(map(int, input().split()))
key = int(input())

if key in arr:
    print("Element Found")
else:
    print("Element Not Found")



###################3333333333333333333333333333333333333333333


#in some cases
import sys

# 1. Read all numbers from the input stream at once
data = list(map(int, sys.stdin.read().split()))

# 2. Extract our variables using clear, basic indexing
n = data[0]
elements = data[1 : 1 + n]
key = data[-1]

# 3. Standard search and print logic
if key in elements:
    print("Element Found")
else:
    print("Element Not Found")
