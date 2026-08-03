import sys

# 1. Read all input values safely
data = list(map(int, sys.stdin.read().split()))

if data:
    n = data[0]
    A = data[1:]
    
    # Base case: if array has 0 or 1 elements, no duplicates exist
    if n <= 1:
        print(-1)
    else:
        i = 0  # 'i' is the slow pointer tracking unique elements
        
        # 2. 'j' is the fast pointer scanning through the array
        for j in range(1, n):
            if A[j] != A[i]:
                i += 1
                A[i] = A[j]
        
        distinct_count = i + 1
        
        # 3. If distinct count equals original size, no duplicates were removed
        if distinct_count == n:
            print(-1)
        else:
            # Print the modified portion from index 0 to i
            result = A[:distinct_count]
            print(*result)
